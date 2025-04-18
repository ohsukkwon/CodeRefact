# -*- coding: utf-8 -*-
import copy
import csv
import io
import math
import os
import sys
import threading
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

sys.stdout.reconfigure(line_buffering=True)

# For adding AILIB_PATH
m_ailib_path = os.environ["AI_LIB_PATH"]
add_path = os.path.abspath(m_ailib_path)
if not add_path in sys.path:
    sys.path.append(add_path)

# For adding all import pathes to sys.path.
# ===== AILIB =====
add_path = os.path.join(m_ailib_path, 'apievaluation')
if not add_path in sys.path:
    sys.path.append(add_path)

add_path = os.path.join(m_ailib_path, 'libutils')
if not add_path in sys.path:
    sys.path.append(add_path)

add_path = os.path.join(m_ailib_path, 'utils')
if not add_path in sys.path:
    sys.path.append(add_path)

# ===== MY_PROJECT =====
add_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'dynamic_src')
if not add_path in sys.path:
    sys.path.append(add_path)

# # # # # for debugging
# for ___path in enumerate(sys.path):
#     print(f'____{___path}')
# sys.exit(0)

# DO *NOT* move the block below to the top. Because it causes issues with finding files in the sys.path.
import ValidationChecker
from ArgsGenerator import ArgsGenerator
from GlobalUtil import *
from MyLog import MyLog
from VoiceSelector import *
from engines.abstract_api_engine import AbstractApiEngine
from engines.token_record import TokenRecord
from prompts.ScorePromptFactory import ScorePromptFactory

from ResultTotalTestInfo import ResultTotalTestInfo
from env.env_vars import get_my_proj_result_file_prefix

from libutils.generalutils import load_class_impl__, ClsAbsGenerateOutput

##################### Input data ###########################
g_config_unique_testid  : str = ""
g_config_dirpath_input  : str = ""
g_config_dirpath_output : str = ""

g_sys_my_log = None
g_sys_args = None
g_sys_aivoices_obj = None
g_sys_targetPrompt = None
g_total_test_result = None

class EngineThread(threading.Thread):
    def __init__(self, argThreadName, argIdxThread, argEngine, argSentences, argArgs, argNewLog):
        super().__init__()
        self.mName = argThreadName
        self.mIdxThread = argIdxThread
        self.mEngine = argEngine
        self.mSentences = argSentences
        self.mArgs = argArgs
        # In the case of multi thread, if arg's ARG_KEY_NAME_SENTENCESCOUNT < count_all_sentences, You SHOULD change arg's ARG_KEY_NAME_SENTENCESCOUNT to count_all_sentences count again. Here!!.
        _count_all_sentences = len(self.mSentences)
        if self.mArgs.getValInGlobalArg(ARG_KEY_NAME_SENTENCESCOUNT) and int(self.mArgs.getValInGlobalArg(ARG_KEY_NAME_SENTENCESCOUNT)) > _count_all_sentences:
            self.mArgs.update_BothArgs(ARG_KEY_NAME_SENTENCESCOUNT, _count_all_sentences)  # Adjust SentencesCount
            argNewLog.e(f"[Update(EngineThread.__init__) ####### [{argThreadName}] Update PROMPT_ARG_KEY_NAME_SENTENCES_COUNT]")

        self.mArr_total_results = []
        self.mTokenRecord = TokenRecord(0,0,0,0,0)
        self.mLog = argNewLog
        self.mDuration = 0

    def run(self):
        self.mLog.d()
        time.sleep(0.5)
        self.mLog.d(f"■ Thread START[{self.mName}]")
        self.mLog.d()

        onestep_start_time = time.time()

        count_all_sentences = len(self.mSentences)
        s_idx = 0
        e_idx = 0
        try:
            while e_idx < count_all_sentences:
                s_idx = e_idx
                e_idx = count_all_sentences if s_idx + int(self.mArgs.getValInGlobalArg(ARG_KEY_NAME_SENTENCESCOUNT)) > count_all_sentences else s_idx + int(self.mArgs.getValInGlobalArg(ARG_KEY_NAME_SENTENCESCOUNT))

                self.mLog.e(f'================== EngineThread[{self.mName}].do_eval_main[{s_idx}:{e_idx}] ==================')

                # Generate api Engine
                _retCode, _retList, _token_record = self.mEngine.do_eval(self.mSentences[s_idx:e_idx])

                if _retCode != ERR_CODE_NONE:
                    # add fake datas
                    self.mLog.e(f'ERR_CODE:{_retCode}')

                if s_idx == 0:
                    self.mArr_total_results = _retList
                else:
                    for ___idx, _item in enumerate(_retList):
                        try:
                            self.mArr_total_results[___idx].mResultRecords = self.mArr_total_results[___idx].mResultRecords + _retList[___idx].mResultRecords
                        except IndexError:
                            self.mLog.e(f"mArr_total_results exception.{traceback.format_exc()}")
                            pass

                # Add TokenRecord
                self.mTokenRecord.add_record(_token_record)
                pass

            oneStepElaspedTime = time.time() - onestep_start_time
            self.mDuration = oneStepElaspedTime
        except:
            self.mLog.e(f"Thread start exception.{traceback.format_exc()}")
        finally:
            self.mLog.e(f'\t\t---> [{self.mName}] mDuration: {self.mDuration:0.9f} second(s)')  # display during time when response none
            self.mLog.e()
            self.mLog.e(f"■ Thread E N D[{self.mName}]")
            self.mLog.close()

class MainJob:
    def __init__(self):
        pass

    @staticmethod
    def check_validation(argMylog, argInnerArgArgs, argEngineVars):
        argMylog.d(msg=f'###')
        # 1. check api key.
        inner_gpt_api_key = None
        inner_azure_api_key = None

        try:
            inner_gpt_api_key = keystore_get_key_type(argType=KEYTYPE_IDX_GPTScenario_OpenAI_NONE_NONE)
        except KeyError:
            argMylog.e(msg=f'### OMG(inner_gpt_api_key)!!! exception.{traceback.format_exc()}', argGoExit=True)
        finally:
            pass

        try:
            inner_azure_api_key = keystore_get_key_type(argType=KEYTYPE_IDX_GPTScenario_Azure_OpenAI_GPT4o_mini)
        except KeyError:
            argMylog.e(msg=f'### OMG(inner_azure_api_key)!!! exception.{traceback.format_exc()}', argGoExit=True)
        finally:
            pass

        if(inner_gpt_api_key is None or len(inner_gpt_api_key) < 5) and (inner_azure_api_key is None or len(inner_azure_api_key) < 5):
            argMylog.e(f"# ERROR___inner_gpt_api_key:{inner_gpt_api_key}/inner_azure_api_key:{inner_azure_api_key}", argGoExit=True)

        pass

    @staticmethod
    def do_main(argMylog, innerArgArgs, argPromptFactory, argEngineVars):
        global g_config_dirpath_output, g_config_dirpath_input, g_sys_targetPrompt, g_total_test_result

        # override config variables
        if innerArgArgs.getValInGlobalArg(ARG_KEY_NAME_INPUTDIR):
            g_config_dirpath_input = innerArgArgs.getValInGlobalArg(ARG_KEY_NAME_INPUTDIR)

        # Check root of Input_dir
        if not os.path.exists(g_config_dirpath_input):
            argMylog.e(f'Error: g_config_dirpath_input is NOT exist. {g_config_dirpath_input}', argGoExit=True)

        try:
            if not os.path.exists(g_config_dirpath_output):
                os.makedirs(g_config_dirpath_output)
        except OSError:
            argMylog.e('Error: Creating directory. ' + g_config_dirpath_output, argGoExit=True)

        # for debugging
        argMylog.inner(idx=1, msg=f'[__CheckSTEP__]{innerArgArgs.getValInGlobalArg(ARG_KEY_NAME_PROMPTTYPE)}')

        try:
            g_sys_targetPrompt = argPromptFactory.getTargetPrompt(innerArgArgs.getValInGlobalArg(ARG_KEY_NAME_PROMPTTYPE), argArgs=innerArgArgs)
        except:
            mylog.e(msg=f"# No prompt with key[{innerArgArgs.getValInGlobalArg(ARG_KEY_NAME_PROMPTTYPE)}]", argGoExit=True)

        if g_sys_targetPrompt is None:
            mylog.e(msg='# No g_sys_targetPrompt!', argGoExit=True)

        # validation check here(for azure/gpt api key)
        MainJob.check_validation(argMylog=argMylog, argInnerArgArgs=innerArgArgs, argEngineVars=argEngineVars)

        # read all input items
        g_loop_idx_realCnt = 0
        g_arr_all_sentences = []
        g_all_sentences_column_count = 0

        # file open
        csvFile = open(os.path.join(innerArgArgs.getValInGlobalArg(ARG_KEY_NAME_INPUTDIR), g_sys_targetPrompt.get_my_csvname()), "r", encoding='utf-8-sig')
        readlines = csv.reader(csvFile, delimiter=r'|')  # readlines has list that it's splitted by '|'.

        for g_loop_idx, arr_row_splitted_str in enumerate(readlines):
            if len(arr_row_splitted_str) < LIMIT_MIN_INPUT_COLUMN_COUNT:  # check MIN_LENGTH
                argMylog.e(f'(OMG!!!) Critial err. len(arr_row_splitted_str) is too short.({len(arr_row_splitted_str)})', argGoExit=True)
                continue

            if g_loop_idx_realCnt == 0:
                g_all_sentences_column_count = len(arr_row_splitted_str)

                # 4:No InImage , 5: Has InImage, else : Error
                innerArgArgs.setValInnerArg(ARG_KEY_NAME_HAS_INPUT_IMAGE, g_all_sentences_column_count == 5)
            else:
                if g_all_sentences_column_count != len(arr_row_splitted_str):   # check validation of g_all_sentences_column_count about overall whole lines.
                    sys.exit(f'Critial err. {g_loop_idx}:{g_all_sentences_column_count}:{len(arr_row_splitted_str)}')

            g_arr_all_sentences.append(arr_row_splitted_str)
            g_loop_idx_realCnt += 1

        count_all_senetences = len(g_arr_all_sentences)
        argMylog.e(f'len(g_arr_all_sentences):{count_all_senetences}')
        argMylog.e()

        if count_all_senetences > SENTENCES_MAX_COUNT:
            argMylog.e(f'Too many sentences:{count_all_senetences}. Unsupport it.!!', argGoExit=True)

        g_token_record = TokenRecord(0, 0, 0, 0, 0)
        apiEngine = None

        total_start_time = time.time()

        argThreadNum = int(g_sys_args.getValInGlobalArg(ARG_KEY_NAME_THREADNUM))
        if argThreadNum <= 0:  # automatic
            if count_all_senetences > THRESHOLD_SENTENCES_COUNT_FOR_M_THREAD:
                if count_all_senetences <= 100:
                    argThreadNum = max(math.floor(GPT_PARALLEL_MAX_THREAD_LIMIT/4),1)
                elif count_all_senetences <= 500:
                    argThreadNum = max(math.floor(GPT_PARALLEL_MAX_THREAD_LIMIT/3),1)
                elif count_all_senetences <= 1000:
                    argThreadNum = max(math.floor(GPT_PARALLEL_MAX_THREAD_LIMIT/2),1)
                else:
                    argThreadNum = max(math.floor(GPT_PARALLEL_MAX_THREAD_LIMIT/1),1)
            else:
                argThreadNum = 1

        sentences_totalcount_Per1Thread = int(count_all_senetences / argThreadNum)
        remainder = count_all_senetences % argThreadNum

        argMylog.e(f"[### thread count: {argThreadNum} unit(s). sentences_totalcount_Per1Thread: {sentences_totalcount_Per1Thread} (+{remainder})sentense(s). ###]")

        # if arg's ARG_KEY_NAME_SENTENCESCOUNT < sentences_totalcount_Per1Thread, You SHOULD change arg's ARG_KEY_NAME_SENTENCESCOUNT to sentences_totalcount_Per1Thread count. Here!!.
        if innerArgArgs.getValInGlobalArg(ARG_KEY_NAME_SENTENCESCOUNT) and int(innerArgArgs.getValInGlobalArg(ARG_KEY_NAME_SENTENCESCOUNT)) > sentences_totalcount_Per1Thread:
            innerArgArgs.update_BothArgs(ARG_KEY_NAME_SENTENCESCOUNT, sentences_totalcount_Per1Thread)  # Adjust SentencesCount
            argMylog.e(f"[Adjust(do_main) ####### Need to Update PROMPT_ARG_KEY_NAME_SENTENCES_COUNT]")

        mAllThreadList = []
        s_idx = 0
        e_idx = 0
        _thread_idx = 0
        while _thread_idx < argThreadNum:
            s_idx = e_idx
            e_idx = count_all_senetences if _thread_idx == (argThreadNum-1) else s_idx + sentences_totalcount_Per1Thread

            argMylog.d(f'================== _thread_idx -> {_thread_idx} split{_thread_idx}: [{s_idx}:{e_idx}]==================')

            fname = os.path.basename(argMylog.get_my_path())
            fname_only = f'{os.path.splitext(fname)[0]}_{_thread_idx}.{FILE_EXTENSION_WITHOUT_DOT_LOG}'

            threadNewLog = MyLog(log_dir_path=f'{Path(argMylog.get_my_path()).parent}', argFname=f'{fname_only}', log_buf_max_length=LOG_BUFFER_SIZE_NO_FLUSH)
            threadNewArgs = copy.deepcopy(innerArgArgs)
            threadNewArgs.setMyName(f'T_{_thread_idx}')
            mylog.d(f'deepcopy(threadNewArgs)')
            mylog.d(msg=threadNewArgs)

            newTargetPrompt = argPromptFactory.getTargetPrompt(g_sys_targetPrompt.get_my_keyname(), argArgs=threadNewArgs)
            # apiEngine = GptApiEngine(argThreadId=_thread_idx, argArgs=threadNewArgs, argEngineVars=argEngineVars, argTargetPrompt=newTargetPrompt,
            #                          argMyLog=threadNewLog, argSentencesList=None)

            # # # For Code Refactoring # # #
            dl_ptr_ClsCustomEngineImpl = load_class_impl__(folder_name=g_sys_args.getValInGlobalArg(argKey=ARG_KEY_NAME_PROMPTTYPE), module_name='custom_func', cls_name='CustomEngineImpl', sup_name=AbstractApiEngine)
            instance_CustomEngineImpl = dl_ptr_ClsCustomEngineImpl(argThreadId=_thread_idx, argArgs=threadNewArgs, argEngineVars=argEngineVars, argTargetPrompt=newTargetPrompt, argMyLog=threadNewLog, argSentencesList=None)
            print(f'instance_CustomEngineImpl:{instance_CustomEngineImpl}')

            # apiEngine = EvalImgEngineImpl(argThreadId=_thread_idx, argArgs=threadNewArgs, argEngineVars=argEngineVars, argTargetPrompt=newTargetPrompt,
            #                          argMyLog=threadNewLog, argSentencesList=None)

            # Run thread
            mAllThreadList.append(EngineThread(argThreadName=f'engine_T{_thread_idx}', argIdxThread=_thread_idx, argEngine=instance_CustomEngineImpl , argSentences=g_arr_all_sentences[s_idx:e_idx],
                                               argArgs=threadNewArgs, argNewLog=threadNewLog))
            mAllThreadList[_thread_idx].start()
            _thread_idx = _thread_idx + 1

        argMylog.d(f'<<<<<<<<<<<< E N D :{argThreadNum} thread(s)')
        pass

        for ___idx in range(_thread_idx):
            mAllThreadList[___idx].join()

        scenario_end_time = time.time()
        total_elasped_time = scenario_end_time - total_start_time
        argMylog.d(f'<<<<<<<<<<<< E N D(EvalImg) : [{total_elasped_time:0.9f} second(s)]')
        argMylog.d()

        g_arr_total_results = []
        for _idx, _itemThread in enumerate(mAllThreadList):
            # Add TokenRecord
            g_token_record.add_record(_itemThread.mTokenRecord)
            if _idx == 0:
                g_arr_total_results = _itemThread.mArr_total_results
                argMylog.d(f'[{_idx}] Duration: {_itemThread.mDuration:0.9f} second(s)')
            else:
                for _inner_idx, _item in enumerate(_itemThread.mArr_total_results):
                    g_arr_total_results[_inner_idx].mResultRecords = g_arr_total_results[_inner_idx].mResultRecords + _itemThread.mArr_total_results[_inner_idx].mResultRecords

        if len(g_arr_total_results) > 1:
            argMylog.e(f'Too many threads. It should be only one. But it is {len(g_arr_total_results)}.', argGoExit=True)

        argMylog.d(f'g_arr_total_results(len:{len(g_arr_total_results)}) =>')
        for ___idx, _ in enumerate(g_arr_total_results):
            argMylog.d(f'g_arr_total_results[{___idx}].mResultRecords(count):{len(g_arr_total_results[___idx].mResultRecords)}')

        argMylog.d()

         # First of all, whether mResultRecords has FAKE data or not.
        b_has_wrong_data = False
        if len(g_arr_total_results) < 1:
            b_has_wrong_data = True
            pass
        else:
            if len(g_arr_total_results[0].mResultRecords) < 1:
                b_has_wrong_data = True
            else:
                peek_first_item = g_arr_total_results[0].mResultRecords[0]
                if peek_first_item:
                   if peek_first_item.getScore().lower() == 'FAKE'.lower():
                        b_has_wrong_data = True
                   else:
                       pass
                else:
                    b_has_wrong_data = True

        if b_has_wrong_data:
            argMylog.d(f"# # # # # # # # # # # # HAS WRONG result DATAs. so skip this.")
            pass
        else:
            pass

        argMylog.d()

        result_start_time = time.time()

        # 데이터 취합 세션
        if b_has_wrong_data:
            # Don't make sheet data here. skip this.
            argMylog.d(f"# # # # # # # # # # # # HAS WRONG result DATAs. so Don't make sheet data here. skip this.")
            argMylog.d(f"# # # # # # # # # # # # {g_sys_args.getValInGlobalArg(ARG_KEY_NAME_INPUTDIR)}")
        else:
            # # # For Code Refactoring # # #
            dl_ptr_ClsGenerateOutputImpl = load_class_impl__(folder_name='evalimg', module_name='custom_func', cls_name='ClsGenerateOutputImpl', sup_name=ClsAbsGenerateOutput)
            instance_GenerateOutput = dl_ptr_ClsGenerateOutputImpl(innerArgArgs, argMylog)
            instance_GenerateOutput.do_generate(arg_datas=g_arr_total_results)

        result_end_time = time.time()
        result_elasped_time = result_end_time - result_start_time
        argMylog.d(f'<<<<<<<<<<<< E N D(Result) : Th_{_thread_idx} thread(s). [{result_elasped_time:0.9f} second(s)]')
        argMylog.d()

        argMylog.d(f'■ TokenRecord:')
        argMylog.d()

        argMylog.d(g_token_record)
        tik_money, sys_monkey = g_token_record.calc_money(argEngineVars.config_GPT_TOKEN_MONEY_QUERY_PER_1token, argEngineVars.config_GPT_TOKEN_MONEY_QUERY_CACHE_PER_1token, argEngineVars.config_GPT_TOKEN_MONEY_RESPONSE_PER_1token)
        argMylog.d(f'TokenMoney(USD): tik:{tik_money},sys:{sys_monkey}')

        total_end_time = time.time()
        total_elasped_time = total_end_time - total_start_time

        argMylog.d(f'■■■■■ Result Duration : [{result_elasped_time:0.9f} second(s)]')
        argMylog.d(f'■■■■■ Total Duration : [{total_elasped_time:0.9f} second(s)]')
        argMylog.d()

        try:
            result_full_path = g_config_dirpath_output
            if not os.path.exists(result_full_path):
                os.makedirs(result_full_path)
        except OSError:
            mylog.e("OMG!! Error: Failed to create the directory.")

        argMylog.d(f'■ ■ ■ ■ ■ g_total_test_result : \n{g_total_test_result}')
        asr_gen_result_file_name = f'{get_my_proj_result_file_prefix()}{g_config_unique_testid}.txt'
        with open(os.path.join(g_config_dirpath_output, asr_gen_result_file_name), 'w', encoding='utf-8-sig') as r:
            r.write(f'{g_total_test_result}')

        argMylog.d(f'■ ■ ■ ■ ■ apiEngine.my_retry_count : {instance_CustomEngineImpl.my_retry_count} : {"OMG!Fail!!" if instance_CustomEngineImpl.my_retry_count > ASR_MAX_RETRY_COUNT else "Pass"}')
        pass

if __name__ == '__main__':
    if len(sys.argv) > 1:
        # ================================================
        import argparse     # 1. import argparse

        __peek_parser = argparse.ArgumentParser(description='Peek parser')  # 2. make parser for prompt

        # 3. parser.add_argument로 받아들일 인수를 추가해나간다.
        # for peeking prompt.
        __peek_parser.add_argument('-Pmt', f'--{ARG_KEY_NAME_PROMPTTYPE}', type=str, help='Type of prompt.')

        _args, unknown = __peek_parser.parse_known_args(sys.argv)  # 4. 인수를 분석

        if _args.prompttype:
            from GlobalVars import g_sys_my_pmt

            g_sys_my_pmt = _args.prompttype
            print(f'# g_sys_my_pmt={g_sys_my_pmt}')
        else:
            print(f'### OMG!!! STOP no g_sys_my_pmt!!')
            sys.exit(0)

    else:
        print(f'### OMG!!! STOP no args.[{len(sys.argv)}]:{sys.argv}!!')
        sys.exit(0)

    g_config_unique_testid = get_date_file_name()
    print(f'# # # # # (BEFORE)g_config_unique_testid:{g_config_unique_testid}')

    print("---------------------------------------------")
    print("__________ LOCAL Variables")
    print(locals())
    print("========== GLOBAL Variables")
    print(globals())
    print("---------------------------------------------")

    # Generate Args
    m_default_log = MyLog(log_dir_path=get_dir_res('deflog'))
    g_sys_args = ArgsGenerator(sys.argv, m_default_log, argUniqueTestId=g_config_unique_testid, argMyName='g_sys_args')

    # Now, UNIQUE_TESTID is real! so use it with g_sys_args.getValInGlobalArg(ARG_KEY_NAME_UNIQUE_TESTID).
    g_config_unique_testid = g_sys_args.getValInGlobalArg(argKey=ARG_KEY_NAME_UNIQUE_TESTID, argDefValIfNone=g_config_unique_testid)
    print(f'# # # # # (AFTER)g_config_unique_testid:{g_config_unique_testid}')

    # Now, Log is real! so use it with g_sys_my_log.
    g_sys_my_log = m_default_log
    g_sys_my_log.inner(idx=0, msg=f'# # # # # # # # # # \t START_____PROGRAM \t # # # # # # # # # #')

    # Generate MyLog
    mylog = g_sys_my_log
    mylog.inner(idx=1, msg=f'# # # START_____LOG # # #')

    mylog.d(f'deepcopy(g_sys_args)')
    mylog.d(msg=g_sys_args)

    g_config_dirpath_input = os.path.join(get_dir_res(), 'config')
    if is_skip_unique_testid(g_sys_args):
        g_config_dirpath_output = get_dir_result(argSysArgs=g_sys_args, argLog=mylog, argExtPath=None)
    else:
        g_config_dirpath_output = os.path.join(get_dir_result(argSysArgs=g_sys_args, argLog=mylog, argExtPath=None),
                                               g_config_unique_testid)

    mylog.d('-----------------')
    for _idx, ___item in enumerate(sys.path):
        mylog.d(f'[{_idx}] : {___item}')
        pass
    mylog.d('=================')

    # Validation checker
    ValidationChecker.valid_check(mylog, 'evalimg')

    # =====   Generate IPromptFactory   =====
    mylog.inner(idx=0, msg='Create ScorePromptFactory')
    gPromptFactory = ScorePromptFactory()

    # Generate Engine variables
    print(f'[__CheckSTEP__]CURRENT_TARGET_PROGRAM_PROXY_MODE:{current_GPT_PROGRAM_PROXY_MODE}')
    g_engineVars = EngineVars(argProgramMode=current_GPT_PROGRAM_PROXY_MODE,
                              argGptType=g_sys_args.getValInGlobalArg(ARG_KEY_NAME_ENGINETYPE),
                              argGptModel=g_sys_args.getValInGlobalArg(ARG_KEY_NAME_ENGINEMODEL),
                              argDeployName=g_sys_args.getValInGlobalArg(ARG_KEY_NAME_ENGINEDEPLOYNAME))
    mylog.d(msg=g_engineVars)

    # Generate ASRGenResult
    g_total_test_result = ResultTotalTestInfo(g_config_unique_testid)

    try:
        MainJob.do_main(mylog, g_sys_args, gPromptFactory, g_engineVars)
    except Exception as err:
        mylog.inner(idx=1, msg=f'### OMG!!! exception_{err}.{traceback.format_exc()}')
        pass
    finally:
        mylog.inner(idx=1, msg=f'# # # # # # # # # # \t E N D_____PROGRAM \t # # # # # # # # # #')
        mylog.close()  # save to file
