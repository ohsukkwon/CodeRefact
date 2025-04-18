# -*- coding: utf-8 -*-
import traceback

import pandas as pd
from openai import RateLimitError, BadRequestError, APITimeoutError
from tabulate import tabulate

from GlobalUtil import *
from MyKeyStore import *
from apievaluation.engines.query_table import *
from apievaluation.engines.token_record import TokenRecord
from config.engine_config import *
from engines.abstract_api_engine import AbstractApiEngine
from libutils.generalutils import ClsAbsGeneralLib, ClsAbsGenerateOutput

# basename of directory / directory of parent / abs path of current file
_MY_PROMPT:str = os.path.basename(os.path.dirname(os.path.abspath(__file__)))

def MyPrint(msg : str):
    print(f'{_MY_PROMPT}:{msg}')

class ClsGeneralLibImpl(ClsAbsGeneralLib):
    mMyName: str = None

    def __init__(self, argname='None'):
        self.mMyName = f'(impl:{self.__class__.__name__}):{argname}'
        pass

    def do_print(self, argmsg: str):
        current_func_name = sys._getframe().f_code.co_name
        MyPrint(f"[{self.mMyName}]:{current_func_name}:{argmsg}")
        pass

    def __str__(self):
        global _MY_PROMPT
        retstr = f'str[{self.mMyName}]:[{_MY_PROMPT}]'

        return retstr

class ClsGenerateOutputImpl(ClsAbsGenerateOutput):
    def __init__(self, arg_args, arg_my_log):
        super().__init__(arg_args=arg_args, arg_my_log=arg_my_log)
        self.mMyName = f'(impl:{self.__class__.__name__}:{arg_args.getValInGlobalArg(argKey=ARG_KEY_NAME_PROMPTTYPE)})'
        self.mArgs = arg_args
        self.mLog = arg_my_log
        pass

    def do_generate(self, arg_datas):
        current_func_name = sys._getframe().f_code.co_name
        self.mLog.d(f'[{self.mMyName}]■ {current_func_name}:{arg_datas}')
        self.mLog.d()

        # GET g_sys_my_pmt in main.py
        main_module = sys.modules.get("__main__")
        if main_module:
            sys_my_pmt = getattr(main_module, "g_sys_my_pmt", "NOT FOUND")
        else:
            sys_my_pmt = "NOT FOUND"

        print(f'# sys_my_pmt: {sys_my_pmt}')

        for _idx, _ in enumerate(arg_datas):
            input_sentences_csv_name = main_module.g_sys_targetPrompt.get_my_csvname()
            inner_file_name = (f'result'
                               f'_{self.mArgs.getValInGlobalArg(ARG_KEY_NAME_PROMPTTYPE)}'
                               f'_{os.path.splitext(input_sentences_csv_name)[0]}'
                               f'_{self.mArgs.getValInGlobalArg(ARG_KEY_NAME_ENGINETYPE)}'
                               f'_{self.mArgs.getValInGlobalArg(ARG_KEY_NAME_ENGINEMODEL)}'
                               f'_{self.mArgs.getValInGlobalArg(ARG_KEY_NAME_ENGINEDEPLOYNAME)}'
                               f'_{self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_CFGMOTHERLANGUAGE)}'
                               f'_{self.mArgs.getValInGlobalArg(ARG_KEY_NAME_UNIQUE_TESTID)}'
                               )
            inner_file_name = inner_file_name.replace(' ', '')  # remove space char in filename.

            if _idx > 0:  # for multiple responses.
                inner_file_name = f'{inner_file_name}_{_idx}'

            try:
                result_full_path = main_module.g_config_dirpath_output
                if not os.path.exists(result_full_path):
                    os.makedirs(result_full_path)
            except OSError:
                self.mLog.e("OMG!! Error: Failed to create the directory.")

            result_excel_full_path = f"{main_module.g_config_dirpath_output}/" + f"{inner_file_name}.{FILE_EXTENSION_WITHOUT_DOT_XLSX}"
            result_excel_img_full_path = f"{main_module.g_config_dirpath_output}/" + f"{inner_file_name}_img.{FILE_EXTENSION_WITHOUT_DOT_XLSX}"
            result_csv_full_path = f"{main_module.g_config_dirpath_output}/" + f"{inner_file_name}.{FILE_EXTENSION_WITHOUT_DOT_CSV}"

            pd.set_option('display.width', 1000)
            pd.set_option('display.max_columns', None)
            df_total_results = pd.DataFrame.from_records([resultItem.to_dict() for resultItem in arg_datas[0].mResultRecords])
            df_total_results.columns = TBL_HEADER_COLUMNS_EVALIMG

            # for debugging
            # argMylog.d(df_total_results)
            df_total_results.index = df_total_results.index + 1  # change index from 0 to 1

            # for debugging
            self.mLog.d(tabulate(df_total_results, headers='keys', tablefmt='psql', showindex=False))

            with pd.ExcelWriter(result_excel_full_path, engine='xlsxwriter') as excel_writer:
                df_total_results.to_excel(excel_writer, sheet_name=NAME_EXCEL_SHEET_RAW, na_rep='EMPTY', index=False)

            df_total_results.to_csv(result_csv_full_path, sep='|', na_rep='EMPTY', encoding='utf-8-sig', header=False, index=False)

            # Attach Image files in the Excels
            out_image_dir = os.path.join(DIR_NAME_RES, DIR_NAME_RES_OutImage)
            in_image_dir = os.path.join(DIR_NAME_RES, DIR_NAME_RES_InImage)
            attach_img_to_excel(result_excel_full_path, arg_datas[0].mResultRecords, out_image_dir, in_image_dir, self.mArgs.getValInnerArg(ARG_KEY_NAME_HAS_INPUT_IMAGE, False))

            self.mLog.d()
            self.mLog.d(self.mLog)
            self.mLog.d()
            self.mLog.d(f'[__CheckSTEP__]■ Result_out_DIR : result_out_DIR -> {main_module.g_config_dirpath_output}')
            self.mLog.d()
            self.mLog.d(f'[__CheckSTEP__]■ Result_excel : result_excel_full_path -> {result_excel_full_path}')
            self.mLog.d()

        pass

    def __str__(self):
        return f'[{self.mMyName}]'

class CustomEngineImpl(AbstractApiEngine):
    def __init__(self, argThreadId, argArgs, argEngineVars, argTargetPrompt, argMyLog, argSentencesList):
        self.mMyName = f'(impl:{self.__class__.__name__}:{argArgs.getValInGlobalArg(argKey=ARG_KEY_NAME_PROMPTTYPE)})'
        self.mArgs = argArgs
        self.mLog = argMyLog
        super().__init__(argThreadId, argArgs, argEngineVars, argTargetPrompt, argMyLog, argSentencesList)

    # ===================================================================================
    def do_eval(self, slicedArrSentences):
        num_tiktokens_total = 0
        num_systemtokens_total = 0

        num_tiktokens_query = 0
        num_tiktokens_response = 0
        num_systemtokens_query = 0
        num_systemtokens_query_cached = 0
        num_systemtokens_response = 0

        measureStartTime = time.time()

        mArrQueryResultAllTables = []


        out_image_dir = os.path.join(DIR_NAME_RES, DIR_NAME_RES_OutImage)
        in_image_dir = os.path.join(DIR_NAME_RES, DIR_NAME_RES_InImage)

        __MAX_IMG_SIZE_IN_KB: int = 1024
        __DETAIL_MODE_IMG_THRESHOLD: int = 512

        ___l_has_in_img = self.mArgs.getValInnerArg(ARG_KEY_NAME_HAS_INPUT_IMAGE, False)

        if int(self.mArgs.getValInGlobalArg(ARG_KEY_NAME_SENTENCESCOUNT)) != len(slicedArrSentences):
            self.mArgs.update_BothArgs(ARG_KEY_NAME_SENTENCESCOUNT, len(slicedArrSentences))            # Adjust prompt's args.
            self.mMyLog.i(f"[Adjust({self.mMyThreadId}):{len(slicedArrSentences)}] ####### Need to Update PROMPT_ARG_KEY_NAME_SENTENCES_COUNT")

        real_count_eval_size_per_1cycle = len(slicedArrSentences)

        promptStr = self.mTargetPrompt.get_prompt(PROMPT_COMMAND_KEY_NAME_NOTIROLE)

        ___idx_per_1cycle = 0
        ___result_system_content_arr = []
        ___result_user_content_arr = []
        for ___idx in range(real_count_eval_size_per_1cycle):
            ___item = slicedArrSentences[___idx]

            ___inner_prompt_extra_imginfo_str = PROMPT_EXTRA_IMG_ITEM.format(
                inner_no=___item[0],                                                                            # No
                innerPrompt=___item[1],                                                                         # Prompt
                innerStyle=___item[2],                                                                          # Style
                innerStyleExtra='' if (___item[2] is None or ___item[2] == '') else f'+{___item[2]} Style',     # StyleExtra
                inner_out_img=___item[3],                                                                       # OutImage
                # inner_in_img = ___item[4],                                                                    # InImage
                inner_in_img_extra='' if ___l_has_in_img == False else f'Original image:{___item[4]}',             # InImageExtra
            )
            promptStr = promptStr + ___inner_prompt_extra_imginfo_str

            out_image_full_path = os.path.join(out_image_dir, ___item[3])
            ___inner_out_base64_image, ___out_max_dim, ___out_img_dim = process_image(out_image_full_path, __MAX_IMG_SIZE_IN_KB)
            print(f'({___idx})out_base64_image({out_image_full_path}):{___out_max_dim , ___out_img_dim}')
            ___result_user_content_arr.append(create_image_content(___inner_out_base64_image, ___out_max_dim, __DETAIL_MODE_IMG_THRESHOLD))

            if ___l_has_in_img:
                in_image_full_path = os.path.join(in_image_dir, ___item[4])
                ___inner_in_base64_image, ___in_max_dim, ___in_img_dim = process_image(in_image_full_path, __MAX_IMG_SIZE_IN_KB)
                print(f'({___idx})in_base64_image({in_image_full_path}):{___in_max_dim, ___in_img_dim}')
                ___result_user_content_arr.append(create_image_content(___inner_in_base64_image, ___in_max_dim, __DETAIL_MODE_IMG_THRESHOLD))

        ___result_user_content_arr.insert(0,{  # 1st
            "type": "text",
            "text": promptStr
        })

        self.mMyLog.e(f"{self.mMyThreadId} --->>>:■ prompt1 :")
        self.mMyLog.e(promptStr)
        self.mMyLog.e(f"{self.mMyThreadId} <<<---")

        #self.mMyLog.e(f"■ prompt(+ images) :")
        #self.mMyLog.e(___result_user_content_arr)
        #self.mMyLog.e()

        # For measure time
        num_tiktokens_query = self.mEngineVars.config_GPT_TOKEN_QUERY_ADJ  # Adjust count(+7)

        # ############ Block avoid connection error ####################
        # num_tiktokens_query += self._token_counter(prompt, self.mEngineVars.config_GPT_TIKTOKEN_ENGINE_NAME)
        # ############ Block avoid connection error ####################

        num_systemtokens_query = 0
        num_systemtokens_query_cached = 0
        num_systemtokens_response = 0

        measureStartTime = time.time()
        totalCountOfSentences = len(slicedArrSentences)

        if True:
            g_client = None
            g_assistant_id = None
            g_thread_id = None
            g_thread = None
            g_assistant_role = "assistant"
            g_message = None
            g_run = None
            response = None

            quotient = int(totalCountOfSentences / ASR_RESPONSE_COUNT_PER_RESPONSE)
            remainder = totalCountOfSentences % ASR_RESPONSE_COUNT_PER_RESPONSE
            if remainder > 0:
                quotient = quotient + 1

            text_prompt_mode = TEXT_PROMPT_MODE_COMPLETION

            if text_prompt_mode == TEXT_PROMPT_MODE_COMPLETION:
                response = None

                # For retry when token limit. Retry max 2
                retry_state = True
                retry_count = 0
                retry_max_count = 3
                fail_reason = None

                while retry_state and retry_count < retry_max_count:
                    self.mMyLog.e(f'{self.mMyThreadId}:Retry Count : {retry_count}\n')
                    retry_count = retry_count + 1
                    retry_state = False
                    if retry_count > retry_max_count:
                        raise RuntimeError(f'{retry_count} times run for RateLimitError. But still RateLimitError occurred.\n')

                    try:
                        query_time = time.time()
                        self.mMyLog.e("{self.mMyThreadId}:send query")
                        response = super()._get_completion_response_from(self.mEngineVars.config_GPT_ENGINE_TYPE_IDX, argUserPromptContent=___result_user_content_arr, argSystemPromptContent=___result_system_content_arr, usedTokenCount=num_tiktokens_query)

                        resopse_time = time.time()
                        self.mMyLog.e("{self.mMyThreadId}:for eval_query time : " + str(resopse_time - query_time))
                    except RateLimitError as rateErr:
                        # RateLimitError. 429 error token limit
                        fail_reason = "[EvalFail] RateLimitError"
                        self.mMyLog.e(f'RateLimitError occurred.\n')
                        retry_state = True
                        time.sleep(3)
                    except BadRequestError as e:
                        fail_reason = "[EvalFail] BadRequestError"
                        self.mMyLog.e(f'!!OMG. BadRequestError occurred.{e}')
                        self.mMyLog.e(f'!!OMG. BadRequestError occurred.{traceback.format_exc()}')
                    except APITimeoutError:
                        fail_reason = "[EvalFail] APITimeoutError"
                        self.mMyLog.e(f'!!OMG. APITimeoutError occurred.')
                        retry_state = True
                    finally:
                        # DON'T remove this, because it's raw response
                        self.mMyLog.e(f'{self.mMyThreadId}:response:{response}')
                        self.mMyLog.e()
                        # --------------------------------------------

                    if response is None:
                        self.mMyLog.e(f'{self.mMyThreadId}:response == NULL.')
                        if retry_state is True and retry_count < retry_max_count:
                            continue
                        return ERR_CODE_OUTPUT_NULL, self._make_dummy_table(slicedArrSentences), TokenRecord(0, 0, 0, 0,0)
                    else:
                        self.mMyLog.e(f'{self.mMyThreadId}:response is Not NULL.')

                    num_systemtokens_query = response.usage.prompt_tokens
                    num_systemtokens_query_cached = response.usage.prompt_tokens_details.cached_tokens
                    num_systemtokens_query -= num_systemtokens_query_cached
                    num_systemtokens_response = response.usage.completion_tokens

                    for outer_idx in range(0,len(response.choices)):
                        trimedResponseStr = response.choices[0].message.content.strip()

                        queryResultOneTable = QueryOneTableEvalImg(self.mArgs)
                        mArrQueryResultAllTables.append(queryResultOneTable)

                        p = re.compile('^\\|.*$', re.MULTILINE)

                        arrSplitedJustOneLine = p.findall(trimedResponseStr)

                        if len(arrSplitedJustOneLine) != (len(slicedArrSentences) + 2):
                            # if response has something wrong, retry it 3 times.
                            if retry_count < retry_max_count:
                                self.mMyLog.e(f'{self.mMyThreadId}:len(arrSplitedJustOneLine):[{len(arrSplitedJustOneLine)}] , (len(slicedArrSentences) + 2):[{(len(slicedArrSentences) + 2)}]')
                                retry_state = True
                                mArrQueryResultAllTables.remove(mArrQueryResultAllTables[-1])
                                continue
                            self.mMyLog.e(f'{self.mMyThreadId}:Critial Error_OMG{len(arrSplitedJustOneLine)}:{(len(slicedArrSentences) + 2)}')
                            fail_reason = "[EvalFail]Not same count of sentences"
                            return ERR_CODE_NOT_EQU_COUNT_BETWEEN_INPUT_AND_OUTPUT, self._make_dummy_table(slicedArrSentences), TokenRecord(0,0,0,0,0)

                        for inner_idx, oneLineItem in enumerate(arrSplitedJustOneLine[2:]):
                            itemArr = (oneLineItem.strip()[1:-1].split('|'))    # remove '|' in the one line
                            slicedArritem = slicedArrSentences[inner_idx]

                            try:
                                queryResultOneTable.add_record(argNo=f'{slicedArritem[IDX_EVALIMG_OUTPUT_NO]}',
                                                               argPrompt=f'{slicedArritem[IDX_EVALIMG_OUTPUT_PROMPT]}',
                                                               argStyle=f'{slicedArritem[IDX_EVALIMG_OUTPUT_STYLE]}',
                                                               argOutImg=f'{slicedArritem[IDX_EVALIMG_OUTPUT_OUTIMAGE]}',
                                                               argInImg='FAKE' if ___l_has_in_img == False else f'{slicedArritem[IDX_EVALIMG_OUTPUT_INIMAGE]}',
                                                               argScore=f'{itemArr[IDX_EVALIMG_OUTPUT_SCORE]}',
                                                               argReason=f'{itemArr[IDX_EVALIMG_OUTPUT_REASON]}',
                                                               argCaption=f'{itemArr[IDX_EVALIMG_OUTPUT_CAPTION]}')
                            except KeyError:
                                self.mMyLog.e(f'{self.mMyThreadId}:OMG!!! tid:{self.mMyThreadId} , itemArr[IDX_EVALIMG_OUTPUT_SCORE]:{itemArr[IDX_EVALIMG_OUTPUT_SCORE]}', argGoExit=True)
                            pass
            else:
                self.mMyLog.e(f'{self.mMyThreadId}:!!OMG. Text prompt mode not supported.{text_prompt_mode}', argGoExit = True)
                pass
        else:
            for _idx_loop in range(0,self.mEngineVars.config_GPT_PARAMETER_N):
                queryResultOneTable = QueryOneTableEvalImg(self.mArgs)
                mArrQueryResultAllTables.append(queryResultOneTable)
                for _idx, itemArr in enumerate(slicedArrSentences):
                    queryResultOneTable.add_record(
                        argNo=f'no:::{slicedArritem[IDX_EVALIMG_OUTPUT_NO]}',
                        argPrompt=f'prompt:::{slicedArritem[IDX_EVALIMG_OUTPUT_PROMPT]}',
                        argStyle=f'style:::{slicedArritem[IDX_EVALIMG_OUTPUT_STYLE]}',
                        argOutImg=f'outimg:::{slicedArritem[IDX_EVALIMG_OUTPUT_OUTIMAGE]}',
                        argInImg=f'inimg:::{slicedArritem[IDX_EVALIMG_OUTPUT_INIMAGE]}',
                        argScore=f'score:::{itemArr[IDX_EVALIMG_OUTPUT_SCORE]}',
                        argReason=f'reason:::{itemArr[IDX_EVALIMG_OUTPUT_REASON]}',
                        argCaption=f'caption:::{itemArr[IDX_EVALIMG_OUTPUT_CAPTION]}',
                    )

            sleep_time = 1
            print(f"Sleep {sleep_time} seconds from now on...")
            time.sleep(sleep_time)
            response = None

        responseMatrixCount = len(mArrQueryResultAllTables)
        self.mMyLog.e(f'{self.mMyThreadId}:● responseMatrixCount({responseMatrixCount}):')

        if responseMatrixCount < 1:
            self.mMyLog.e(f'{self.mMyThreadId}:responseMatrixCount is *too* short.')
            fail_reason = "responseMatrixCount is *too* short."
            return ERR_CODE_RESPONSE_IS_TOO_SHORT, self._make_dummy_table(slicedArrSentences), TokenRecord(0,0,0,0,0)

        for _idx in range(0, responseMatrixCount):
            self.mMyLog.e(f'{self.mMyThreadId}:responseMatrixCount[{_idx}] : \n{mArrQueryResultAllTables[_idx]}')
            self.mMyLog.e()

        if not response:    # Dummy case.
            return ERR_CODE_NONE, mArrQueryResultAllTables, TokenRecord(0,0,0,0,0)

        # For measure time
        measureEndTime = time.time()
        self.mMyLog.e(f"{self.mMyThreadId}:# Measure time : {measureEndTime - measureStartTime:.5f} second(s).")

        num_tiktokens_response = self.mEngineVars.config_GPT_TOKEN_RESPONSE_ADJ

        # ############ Block avoid connection error ####################
        # for _idx in range(0, responseMatrixCount):
        #     num_tiktokens_response += self._token_counter(response.choices[_idx].message.content, self.mEngineVars.config_GPT_TIKTOKEN_ENGINE_NAME)
        # ############ Block avoid connection error ####################

        self.mMyLog.e(f"{self.mMyThreadId}:# num_tiktokens_query: {num_tiktokens_query} , num_tiktokens_response: {num_tiktokens_response}")

        return ERR_CODE_NONE, mArrQueryResultAllTables, TokenRecord(num_tiktokens_query, num_tiktokens_response, num_systemtokens_query, num_systemtokens_query_cached, num_systemtokens_response)