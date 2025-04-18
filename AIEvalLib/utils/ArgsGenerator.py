# -*- coding: utf-8 -*-
import json
import os

from config.engine_config import *


class ArgsGenerator:
    def __init__(self, arg, argLog, argUniqueTestId, argMyName=None):
        self.mArgsV = arg
        self.mMyLog = argLog
        self.__doGenerate(argUniqueTestId)
        if argMyName:
            self.mMyName = argMyName
        else:
            self.mMyName = 'DEF_NAME'

    def setMyName(self, argName):
        self.mMyName = argName

    def __doGenerate(self, argUniqueTestId):
        self.mAllArgDicts = {}
        self.mInnerArgs = {}

        self.mAllArgDicts[ARG_KEY_NAME_UNIQUE_TESTID] = argUniqueTestId
        
        if len(self.mArgsV) > 1:
            # ================================================
            import argparse  # 1. import argparse
    
            parser = argparse.ArgumentParser(description='Run STP with option(s):')  # 2. make parser
    
            # 3. parser.add_argument로 받아들일 인수를 추가해나간다.
            # for AI Auto Evaluation
            parser.add_argument('-Uniquetid', f'--{ARG_KEY_NAME_UNIQUE_TESTID}', type=str, help='ID for unique test.(241127_012233)')  # ID for unique test.
            parser.add_argument('-Etype', f'--{ARG_KEY_NAME_ENGINETYPE}', type=str, help='Type of Engine.(gpt/azure)')  # Type of Engine.
            parser.add_argument('-Emodel', f'--{ARG_KEY_NAME_ENGINEMODEL}', type=str, help='Model of Engine.(gpt-4/gpt-4o/gpt-4o-mini/)')  # Type of Engine.
            parser.add_argument('-Pmt', f'--{ARG_KEY_NAME_PROMPTTYPE}', type=str, help='Type of prompt.(ex.trans/correct/emoji/toneprofessional/tonecasual/tonesocial/tonepolite/genasrlisten/genasrconversation)')  # Type of prompt.
            parser.add_argument('-Mlang', f'--{ARG_KEY_NAME_MOTHERLANGUAGE}', type=str, help='Type of Mother Language.')  # Mother Language.
            parser.add_argument('-Slang', f'--{ARG_KEY_NAME_SOURCELANGUAGE}', type=str, help='Type of Source Language.')  # Source Language.
            parser.add_argument('-Tlang', f'--{ARG_KEY_NAME_TARGETLANGUAGE}', type=str, help='Type of Target Language.')  # Target Language.
            parser.add_argument('-SCount', f'--{ARG_KEY_NAME_SENTENCESCOUNT}', type=str, help='Count of Split Sentences.')  # Split Sentences count
            parser.add_argument('-SLength', f'--{ARG_KEY_NAME_SENTENCESLENGTH}', type=str, help='Length of Sentences.')  # Sentences Length
            parser.add_argument('-SCategory', f'--{ARG_KEY_NAME_SENTENCESCATEGORY}', type=str, help='Category of Sentences')  # Sentencecs Category
            parser.add_argument('-TCount', f'--{ARG_KEY_NAME_TOTALSENTENCESCNT}', type=str, help='Total count of Sentences.')  # Sentences total count for sentence generation.
            parser.add_argument('-MCount', f'--{ARG_KEY_NAME_MAKESENTENCESCNT}', type=str, help='Make count of Sentences.')  # Sentences make count for sentence generation.
            parser.add_argument('-Icsv', f'--{ARG_KEY_NAME_INPUTCSVNAME}', type=str, help='Name of Csv.')  # Input Csv Name
            parser.add_argument('-Icfg', f'--{ARG_KEY_NAME_INPUTCONFIGNAME}', type=str, help='Name of Config.')  # Input Config Name
            parser.add_argument('-IDir', f'--{ARG_KEY_NAME_INPUTDIR}', type=str, help='Path of dir which are input')  # Input Dir
            #parser.add_argument('-ICsvDir', f'--{ARG_KEY_NAME_ICSVDIR}', type=str, help='Path of dir which are in-csv dir')  # ICsv Dir
            parser.add_argument('-IInImgDir', f'--{ARG_KEY_NAME_IINIMGDIR}', type=str, help='Path of dir which are in-img dir')  # IInImg Dir
            parser.add_argument('-IOutImgDir', f'--{ARG_KEY_NAME_IOUTIMGDIR}', type=str, help='Path of dir which are out-img dir')  # IOutImg Dir
            parser.add_argument('-ODir', f'--{ARG_KEY_NAME_OUTPUTDIR}', type=str, help='Path of dir which are output csv(s)')  # Output Dir
            parser.add_argument('-TNum', f'--{ARG_KEY_NAME_THREADNUM}', type=str, help='Number of thread.')  # Thread Number
            parser.add_argument('-SKipGptScenInFile', f'--{ARG_KEY_NAME_SKIPGENSCENINFILE}', type=str, help='Skip generate GPTScenario and Path of input file for scenario pre-made.')  # Skip gen scen & Input File Name
            parser.add_argument('-Voiceid', f'--{ARG_KEY_NAME_VOICEID}', type=str, help='Custom voice ids.')  # Input custom voice ids
            parser.add_argument(f'--{ARG_KEY_NAME_NORESPONSEINOUT}', action='store_true')
            parser.add_argument(f'--{ARG_KEY_NAME_SKIPGENAITTS}', action='store_true')

            args, unknown = parser.parse_known_args(self.mArgsV)  # 4. 인수를 분석

            # !!!!! Do it first
            if args.unique_testid:
                if ':skip' in args.unique_testid:
                    temp_unique_testid = str(args.unique_testid).split(':')
                    self.mAllArgDicts[ARG_KEY_NAME_UNIQUE_TESTID] = temp_unique_testid[0]
                    self.mAllArgDicts[ARG_KEY_NAME_SKIPUNIQUETID] = "skip"
                    self.mMyLog.d(f'{ARG_KEY_NAME_UNIQUE_TESTID}={temp_unique_testid[0]}')
                else:
                    self.mAllArgDicts[ARG_KEY_NAME_UNIQUE_TESTID] = args.unique_testid
                    self.mMyLog.d(f'{ARG_KEY_NAME_UNIQUE_TESTID}={args.unique_testid}')
            else:
                self.mMyLog.d(f'No {ARG_KEY_NAME_UNIQUE_TESTID}.')

            self.mMyLog.append_to_my_path(argPath=self.mAllArgDicts[ARG_KEY_NAME_UNIQUE_TESTID])  # update path of Log
    
            # 5. process overlay vars.
            self.mMyLog.d();self.mMyLog.d(f"■ Args :")

            # for AI Auto Evaluation
            if args.enginetype:
                # Change gpt to openai
                if args.enginetype.lower() == GPT_ENGINE_TYPE_OPENAI:
                    pass
                elif args.enginetype.lower() == GPT_ENGINE_TYPE_AZURE:
                    pass
                elif args.enginetype.lower() == GPT_ENGINE_TYPE_GPT:
                    args.enginetype = GPT_ENGINE_TYPE_OPENAI
                    pass
                else:
                    self.mMyLog.e(msg=f"Critical error args.enginetype:{args.enginetype}.", argGoExit=True)

                self.mAllArgDicts[ARG_KEY_NAME_ENGINETYPE] = args.enginetype.lower()
                self.mMyLog.d(f'{ARG_KEY_NAME_ENGINETYPE}={args.enginetype}')
            else:
                self.mMyLog.d(f'No {ARG_KEY_NAME_ENGINETYPE}.')

            if args.enginemodel:
                if args.enginetype is None:
                    self.mMyLog.e(msg=f"Critical error args.enginemodel is NOT None. but args.enginetype is none.", argGoExit=True)
                    pass
                else:
                    split_arr_model = args.enginemodel.strip().split(r':')
                    if len(split_arr_model) == 1:
                        self.mAllArgDicts[ARG_KEY_NAME_ENGINEMODEL] = split_arr_model[0].strip()
                        pass
                    elif len(split_arr_model) == 2:
                        self.mAllArgDicts[ARG_KEY_NAME_ENGINEMODEL] = split_arr_model[0].strip()
                        self.mAllArgDicts[ARG_KEY_NAME_ENGINEDEPLOYNAME] = split_arr_model[1].strip()
                        pass
                    else:
                        self.mMyLog.e(msg=f"Critical error len(split_arr_model):{len(split_arr_model)} is abnormal.", argGoExit=True)

                    self.mMyLog.d(f'{ARG_KEY_NAME_ENGINEMODEL}={args.enginemodel}')
            else:
                if args.enginetype is not None:    # This case is GPT-4-o only.
                    self.mMyLog.e(msg=f"Critical error args.enginemodel is None. but args.enginetype is not None.", argGoExit=True)

                self.mMyLog.d(f'No {ARG_KEY_NAME_ENGINEMODEL}.')

            if args.prompttype:
                self.mAllArgDicts[ARG_KEY_NAME_PROMPTTYPE] = args.prompttype
                self.mInnerArgs[ARG_KEY_NAME_PROMPTTYPE] = args.prompttype
                self.mMyLog.d(f'{ARG_KEY_NAME_PROMPTTYPE}={args.prompttype}')
            else:
                self.mMyLog.d(f'No {ARG_KEY_NAME_PROMPTTYPE}.')

            if args.motherlanguage:
                self.mAllArgDicts[ARG_KEY_NAME_MOTHERLANGUAGE] = args.motherlanguage
                self.mInnerArgs[ARG_KEY_NAME_MOTHERLANGUAGE] = args.motherlanguage
                self.mMyLog.d(f'{ARG_KEY_NAME_MOTHERLANGUAGE}={args.motherlanguage}')
            else:
                self.mMyLog.d(f'No {ARG_KEY_NAME_MOTHERLANGUAGE}.')

            if args.sourcelanguage:
                self.mAllArgDicts[ARG_KEY_NAME_SOURCELANGUAGE] = args.sourcelanguage
                self.mInnerArgs[ARG_KEY_NAME_SOURCELANGUAGE] = args.sourcelanguage
                self.mMyLog.d(f'{ARG_KEY_NAME_SOURCELANGUAGE}={args.sourcelanguage}')
            else:
                self.mMyLog.d(f'No {ARG_KEY_NAME_SOURCELANGUAGE}.')

            if args.targetlanguage:
                self.mAllArgDicts[ARG_KEY_NAME_TARGETLANGUAGE] = args.targetlanguage
                self.mInnerArgs[ARG_KEY_NAME_TARGETLANGUAGE] = args.targetlanguage
                self.mMyLog.d(f'{ARG_KEY_NAME_TARGETLANGUAGE}={args.targetlanguage}')
            else:
                self.mMyLog.d(f'No {ARG_KEY_NAME_TARGETLANGUAGE}.')

            if args.sentencescount:
                self.mAllArgDicts[ARG_KEY_NAME_SENTENCESCOUNT] = args.sentencescount
                self.mInnerArgs[ARG_KEY_NAME_SENTENCESCOUNT] = args.sentencescount
                self.mMyLog.d(f'{ARG_KEY_NAME_SENTENCESCOUNT}={args.sentencescount}')
            else:
                self.mMyLog.d(f'No {ARG_KEY_NAME_SENTENCESCOUNT}.')

            if args.sentenceslength:
                self.mAllArgDicts[ARG_KEY_NAME_SENTENCESLENGTH] = args.sentenceslength
                self.mInnerArgs[ARG_KEY_NAME_SENTENCESLENGTH] = args.sentenceslength
                self.mMyLog.d(f'{ARG_KEY_NAME_SENTENCESLENGTH}={args.sentenceslength}')
            else:
                self.mMyLog.d(f'No {ARG_KEY_NAME_SENTENCESLENGTH}.')

            if args.sentencescategory:
                self.mAllArgDicts[ARG_KEY_NAME_SENTENCESCATEGORY] = args.sentencescategory
                self.mInnerArgs[ARG_KEY_NAME_SENTENCESCATEGORY] = args.sentencescategory
                self.mMyLog.d(f'{ARG_KEY_NAME_SENTENCESCATEGORY}={args.sentencescategory}')
            else:
                self.mMyLog.d(f'No {ARG_KEY_NAME_SENTENCESCATEGORY}.')

            if args.totalsentencescnt:
                self.mAllArgDicts[ARG_KEY_NAME_TOTALSENTENCESCNT] = args.totalsentencescnt
                self.mInnerArgs[ARG_KEY_NAME_TOTALSENTENCESCNT] = args.totalsentencescnt
                self.mMyLog.d(f'{ARG_KEY_NAME_TOTALSENTENCESCNT}={args.totalsentencescnt}')
            else:
                self.mMyLog.d(f'No {ARG_KEY_NAME_TOTALSENTENCESCNT}.')

            if args.makesentencescnt:
                self.mAllArgDicts[ARG_KEY_NAME_MAKESENTENCESCNT] = args.makesentencescnt
                self.mInnerArgs[ARG_KEY_NAME_MAKESENTENCESCNT] = args.makesentencescnt
                self.mMyLog.d(f'{ARG_KEY_NAME_MAKESENTENCESCNT}={args.makesentencescnt}')
            else:
                self.mMyLog.d(f'No {ARG_KEY_NAME_MAKESENTENCESCNT}.')

            if args.threadnum:
                if int(args.threadnum) > GPT_PARALLEL_MAX_THREAD_LIMIT:
                    self.mMyLog.d(f'# ADJUST args.threadnum({args.threadnum})->({GPT_PARALLEL_MAX_THREAD_LIMIT}).')
                    args.threadnum = str(GPT_PARALLEL_MAX_THREAD_LIMIT)
                self.mAllArgDicts[ARG_KEY_NAME_THREADNUM] = args.threadnum
                self.mMyLog.d(f'{ARG_KEY_NAME_THREADNUM}={args.threadnum}')
            else:
                self.mAllArgDicts[ARG_KEY_NAME_THREADNUM] = GPT_PARALLEL_THREAD_COUNT
                self.mMyLog.d(f'{ARG_KEY_NAME_THREADNUM}={args.threadnum}')

            if args.inputcsvname:
                inputcsvname, _ = os.path.splitext(args.inputcsvname)  # remove extension
                inputcsvname = inputcsvname.strip() + r'.csv'
                self.mAllArgDicts[ARG_KEY_NAME_INPUTCSVNAME] = inputcsvname
                self.mInnerArgs[ARG_KEY_NAME_INPUTCSVNAME] = inputcsvname
                self.mMyLog.d(f'{ARG_KEY_NAME_INPUTCSVNAME}={inputcsvname}')
            else:
                self.mMyLog.d(f'No {ARG_KEY_NAME_INPUTCSVNAME}.')

            if args.inputdir:
                inputdir = args.inputdir.strip()
                if inputdir[-1] == r'\\':
                    inputdir = inputdir[:-1]
    
                inputdir = inputdir
                self.mAllArgDicts[ARG_KEY_NAME_INPUTDIR] = inputdir

                self.mMyLog.d(f'{ARG_KEY_NAME_INPUTDIR}={self.mAllArgDicts[ARG_KEY_NAME_INPUTDIR]}')
            else:
                self.mMyLog.d(f'No {ARG_KEY_NAME_INPUTDIR}.')

#            if args.icsvdir:
#                icsvdir = args.icsvdir.strip()
#                if icsvdir[-1] == r'\\':
#                    icsvdir = icsvdir[:-1]
#
#                self.mAllArgDicts[ARG_KEY_NAME_ICSVDIR] = icsvdir
#
#                self.mMyLog.d(f'{ARG_KEY_NAME_ICSVDIR}={self.mAllArgDicts[ARG_KEY_NAME_ICSVDIR]}')
#            else:
#                self.mMyLog.d(f'No {ARG_KEY_NAME_ICSVDIR}.')

            if args.iinimgdir:
                iinimgdir = args.iinimgdir.strip()
                if iinimgdir[-1] == r'\\':
                    iinimgdir = iinimgdir[:-1]

                self.mAllArgDicts[ARG_KEY_NAME_IINIMGDIR] = iinimgdir

                self.mMyLog.d(f'{ARG_KEY_NAME_IINIMGDIR}={self.mAllArgDicts[ARG_KEY_NAME_IINIMGDIR]}')
            else:
                self.mMyLog.d(f'No {ARG_KEY_NAME_IINIMGDIR}.')

            if args.ioutimgdir:
                ioutimgdir = args.ioutimgdir.strip()
                if ioutimgdir[-1] == r'\\':
                    ioutimgdir = ioutimgdir[:-1]

                self.mAllArgDicts[ARG_KEY_NAME_IOUTIMGDIR] = ioutimgdir

                self.mMyLog.d(f'{ARG_KEY_NAME_IOUTIMGDIR}={self.mAllArgDicts[ARG_KEY_NAME_IOUTIMGDIR]}')
            else:
                self.mMyLog.d(f'No {ARG_KEY_NAME_IOUTIMGDIR}.')
    
            if args.outputdir:
                outputdir = args.outputdir.strip()
                if outputdir[-1] == r'\\':
                    outputdir = outputdir[:-1]

                self.mAllArgDicts[ARG_KEY_NAME_OUTPUTDIR] = outputdir
                self.mMyLog.d(f'{ARG_KEY_NAME_OUTPUTDIR}={self.mAllArgDicts[ARG_KEY_NAME_OUTPUTDIR]}')
            else:
                self.mMyLog.d(f'No {ARG_KEY_NAME_OUTPUTDIR}.')

            if args.inputconfigname:    # for ASR GPTscenario
                inputconfigname, _ = os.path.splitext(args.inputconfigname)  # remove extension
                inputconfigname = inputconfigname.strip() + r'.cfg'
                cfgFilePath = None
                if "\\" in inputconfigname:
                    cfgFilePath = inputconfigname
                    inputconfigname = inputconfigname.split('\\')[-1]
                self.mAllArgDicts[ARG_KEY_NAME_INPUTCONFIGNAME] = inputconfigname
                self.mInnerArgs[ARG_KEY_NAME_INPUTCONFIGNAME] = inputconfigname
                self.mMyLog.d(f'{ARG_KEY_NAME_INPUTCONFIGNAME}={inputconfigname}')

                if not self.getValInGlobalArg(ARG_KEY_NAME_INPUTDIR):
                    self.mMyLog.e(msg=f"Critical error. {ARG_KEY_NAME_INPUTDIR} is None", argGoExit=True)
                else:
                    if not cfgFilePath:
                        cfgFilePath = os.path.join(self.getValInGlobalArg(ARG_KEY_NAME_INPUTDIR), inputconfigname)
                    self.mMyLog.d(f'cfgFilePath={cfgFilePath}')

                    if not os.path.exists(cfgFilePath):
                        self.mMyLog.e(f'Error: cfgFilePath is NOT exist. {cfgFilePath}', argGoExit=True)

                    with open(cfgFilePath, "r", encoding='utf-8-sig') as f:
                        cfgAllData = json.load(f)

                    print(cfgAllData)
                    self.mInnerArgs[ARG_KEY_CONFIG_NAME_SUBJECT] = cfgAllData[CONFIG_NAME_KEY_SUBJECT]
                    self.mInnerArgs[ARG_KEY_CONFIG_NAME_EXTRAPROMPT] = cfgAllData[CONFIG_NAME_KEY_EXTRAPROMPT]
                    self.mInnerArgs[ARG_KEY_CONFIG_NAME_CFGMOTHERLANGUAGE] = cfgAllData[CONFIG_NAME_KEY_CFGMOTHERLANGUAGE]
                    self.mInnerArgs[ARG_KEY_CONFIG_NAME_WORDCOUNTOF1LINE] = cfgAllData[CONFIG_NAME_KEY_WORDCOUNTOF1LINE]
                    self.mInnerArgs[ARG_KEY_CONFIG_NAME_TOTALCOUNTOFSENTENCES] = cfgAllData[CONFIG_NAME_KEY_TOTALCOUNTOFSENTENCES]

                    if cfgAllData[CONFIG_NAME_KEY_TOTALCOUNTOFSENTENCES] == 'dummy':
                        pass
                    else:
                        i_totalcount_of_sentences: int = int(cfgAllData[CONFIG_NAME_KEY_TOTALCOUNTOFSENTENCES])

                        if SENTENCES_MIN_TOTAL_COUNT <= i_totalcount_of_sentences <= SENTENCES_MAX_TOTAL_COUNT:
                            pass
                        else:
                            self.mMyLog.e(msg=f"Critical error. {ARG_KEY_CONFIG_NAME_TOTALCOUNTOFSENTENCES}[{cfgAllData[CONFIG_NAME_KEY_TOTALCOUNTOFSENTENCES]}] is NOT support.", argGoExit=True)

                    self.mInnerArgs[ARG_KEY_CONFIG_NAME_PERSONA1_AIVOICEENGINE] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][CONFIG_NAME_KEY_AIVOICEENGINE]
                    self.mInnerArgs[ARG_KEY_CONFIG_NAME_PERSONA1_AIVOICEID] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][CONFIG_NAME_KEY_AIVOICEID]
                    self.mInnerArgs[ARG_KEY_CONFIG_NAME_PERSONA1_NAME] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][CONFIG_NAME_KEY_NAME]
                    self.mInnerArgs[ARG_KEY_CONFIG_NAME_PERSONA1_GENDER] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][CONFIG_NAME_KEY_GENDER]
                    self.mInnerArgs[ARG_KEY_CONFIG_NAME_PERSONA1_AGE] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][CONFIG_NAME_KEY_AGE]
                    self.mInnerArgs[ARG_KEY_CONFIG_NAME_PERSONA1_OCCUPATION] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][CONFIG_NAME_KEY_OCCUPATION] if cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][CONFIG_NAME_KEY_OCCUPATION] else "Programmer"
                    self.mInnerArgs[ARG_KEY_CONFIG_NAME_PERSONA1_COUNTRYOFORIGIN] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][CONFIG_NAME_KEY_COUNTRYOFORIGIN] if cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][CONFIG_NAME_KEY_COUNTRYOFORIGIN] else "Korea"
                    self.mInnerArgs[ARG_KEY_CONFIG_NAME_PERSONA1_MYLANGUAGE] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][CONFIG_NAME_KEY_MYLANGUAGE]
                    self.mInnerArgs[ARG_KEY_CONFIG_NAME_PERSONA1_HOBBY] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][CONFIG_NAME_KEY_HOBBY] if cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][CONFIG_NAME_KEY_HOBBY] else "travel"
                    self.mInnerArgs[ARG_KEY_CONFIG_NAME_PERSONA1_PERSONALITY] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][CONFIG_NAME_KEY_PERSONALITY] if cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][CONFIG_NAME_KEY_PERSONALITY] else 'extroverted'
                    self.mInnerArgs[ARG_KEY_CONFIG_NAME_PERSONA1_ANNUALSALARY] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][CONFIG_NAME_KEY_ANNUALSALARY] if cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][CONFIG_NAME_KEY_ANNUALSALARY] else '100000'
                    self.mInnerArgs[ARG_KEY_CONFIG_NAME_PERSONA1_EXTRAPROMPT] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][CONFIG_NAME_KEY_EXTRAPROMPT]
                    self.mInnerArgs[ARG_KEY_CONFIG_NAME_PERSONA1_SPEAKINGSPEED] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][CONFIG_NAME_KEY_SPEAKINGSPEED] if cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][CONFIG_NAME_KEY_SPEAKINGSPEED] else '1.0'
                    self.mInnerArgs[ARG_KEY_CONFIG_NAME_PERSONA1_SPEAKINGPITCH] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][CONFIG_NAME_KEY_SPEAKINGPITCH] if cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][CONFIG_NAME_KEY_SPEAKINGPITCH] else 'middle'

                    if cfgAllData[CONFIG_NAME_KEY_MODE] == CONFIG_NAME_VALUE_LISTEN:
                        pass
                    elif cfgAllData[CONFIG_NAME_KEY_MODE] == CONFIG_NAME_VALUE_CONVERSATION:
                        self.mInnerArgs[ARG_KEY_CONFIG_NAME_PERSONA2_AIVOICEENGINE] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][1][CONFIG_NAME_KEY_AIVOICEENGINE]
                        self.mInnerArgs[ARG_KEY_CONFIG_NAME_PERSONA2_AIVOICEID] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][1][CONFIG_NAME_KEY_AIVOICEID]
                        self.mInnerArgs[ARG_KEY_CONFIG_NAME_PERSONA2_NAME] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][1][CONFIG_NAME_KEY_NAME]
                        self.mInnerArgs[ARG_KEY_CONFIG_NAME_PERSONA2_GENDER] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][1][CONFIG_NAME_KEY_GENDER]
                        self.mInnerArgs[ARG_KEY_CONFIG_NAME_PERSONA2_AGE] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][1][CONFIG_NAME_KEY_AGE]
                        self.mInnerArgs[ARG_KEY_CONFIG_NAME_PERSONA2_OCCUPATION] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][1][CONFIG_NAME_KEY_OCCUPATION] if cfgAllData[CONFIG_NAME_KEY_PERSONAS][1][CONFIG_NAME_KEY_OCCUPATION] else 'Programmer'
                        self.mInnerArgs[ARG_KEY_CONFIG_NAME_PERSONA2_COUNTRYOFORIGIN] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][1][CONFIG_NAME_KEY_COUNTRYOFORIGIN] if cfgAllData[CONFIG_NAME_KEY_PERSONAS][1][CONFIG_NAME_KEY_COUNTRYOFORIGIN] else 'America'
                        self.mInnerArgs[ARG_KEY_CONFIG_NAME_PERSONA2_MYLANGUAGE] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][1][CONFIG_NAME_KEY_MYLANGUAGE]
                        self.mInnerArgs[ARG_KEY_CONFIG_NAME_PERSONA2_HOBBY] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][1][CONFIG_NAME_KEY_HOBBY] if cfgAllData[CONFIG_NAME_KEY_PERSONAS][1][CONFIG_NAME_KEY_HOBBY] else 'computer game'
                        self.mInnerArgs[ARG_KEY_CONFIG_NAME_PERSONA2_PERSONALITY] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][1][CONFIG_NAME_KEY_PERSONALITY] if cfgAllData[CONFIG_NAME_KEY_PERSONAS][1][CONFIG_NAME_KEY_PERSONALITY] else 'extroverted'
                        self.mInnerArgs[ARG_KEY_CONFIG_NAME_PERSONA2_ANNUALSALARY] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][1][CONFIG_NAME_KEY_ANNUALSALARY] if cfgAllData[CONFIG_NAME_KEY_PERSONAS][1][CONFIG_NAME_KEY_ANNUALSALARY] else '100000'
                        self.mInnerArgs[ARG_KEY_CONFIG_NAME_PERSONA2_EXTRAPROMPT] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][1][CONFIG_NAME_KEY_EXTRAPROMPT]
                        self.mInnerArgs[ARG_KEY_CONFIG_NAME_PERSONA2_SPEAKINGSPEED] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][1][CONFIG_NAME_KEY_SPEAKINGSPEED] if cfgAllData[CONFIG_NAME_KEY_PERSONAS][1][CONFIG_NAME_KEY_SPEAKINGSPEED] else '1.0'
                        self.mInnerArgs[ARG_KEY_CONFIG_NAME_PERSONA2_SPEAKINGPITCH] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][1][CONFIG_NAME_KEY_SPEAKINGPITCH] if cfgAllData[CONFIG_NAME_KEY_PERSONAS][1][CONFIG_NAME_KEY_SPEAKINGPITCH] else 'middle'
                        pass
                    else:
                        self.mMyLog.e(msg=f"Critical error. {CONFIG_NAME_KEY_MODE} is wrong.", argGoExit=True)

                    self.mMyLog.d(f'cfgAllData={cfgAllData}')
            else:
                self.mMyLog.d(f'No {ARG_KEY_NAME_INPUTCONFIGNAME}.')

            if args.noresponseinout:
                self.mAllArgDicts[ARG_KEY_NAME_NORESPONSEINOUT] = args.noresponseinout
                self.mInnerArgs[ARG_KEY_NAME_NORESPONSEINOUT] = args.noresponseinout
                self.mMyLog.d(f'{ARG_KEY_NAME_NORESPONSEINOUT}={args.noresponseinout}')
            else:
                self.mMyLog.d(f'No {ARG_KEY_NAME_NORESPONSEINOUT}.')

            if args.skipgenaitts:
                self.mAllArgDicts[ARG_KEY_NAME_SKIPGENAITTS] = args.skipgenaitts
                self.mMyLog.d(f'{ARG_KEY_NAME_SKIPGENAITTS}={self.mAllArgDicts[ARG_KEY_NAME_SKIPGENAITTS]}')
            else:
                self.mMyLog.d(f'No {ARG_KEY_NAME_SKIPGENAITTS}.')

            if args.skipgensceninfile:
                pre_made_gpt_scen = args.skipgensceninfile.strip()
                if len(pre_made_gpt_scen) < 1 or pre_made_gpt_scen[-1] == r'\\':
                    self.mMyLog.e(f'Err pre_made_gpt_scen:{pre_made_gpt_scen}.', argGoExit=True)

                self.mAllArgDicts[ARG_KEY_NAME_SKIPGENSCENINFILE] = pre_made_gpt_scen
                self.mMyLog.d(f'{ARG_KEY_NAME_SKIPGENSCENINFILE}={self.mAllArgDicts[ARG_KEY_NAME_SKIPGENSCENINFILE]}')
            else:
                self.mMyLog.d(f'No {ARG_KEY_NAME_SKIPGENSCENINFILE}.')

            if args.voiceid:
                self.mAllArgDicts[ARG_KEY_NAME_VOICEID] = args.voiceid
                self.mMyLog.d(f'{ARG_KEY_NAME_VOICEID}={self.mAllArgDicts[ARG_KEY_NAME_VOICEID]}')
                voice_ids = str(args.voiceid).split(':')
                if len(voice_ids) >= 2:
                    self.mInnerArgs[ARG_KEY_CONFIG_NAME_PERSONA1_AIVOICEENGINE] = voice_ids[0]
                    self.mInnerArgs[ARG_KEY_CONFIG_NAME_PERSONA1_AIVOICEID] = voice_ids[1]
                    if cfgAllData[CONFIG_NAME_KEY_MODE] == CONFIG_NAME_VALUE_LISTEN:
                        pass
                    elif cfgAllData[CONFIG_NAME_KEY_MODE] == CONFIG_NAME_VALUE_CONVERSATION:
                        if len(voice_ids) >= 4:
                            self.mInnerArgs[ARG_KEY_CONFIG_NAME_PERSONA2_AIVOICEENGINE] = voice_ids[2]
                            self.mInnerArgs[ARG_KEY_CONFIG_NAME_PERSONA2_AIVOICEID] = voice_ids[3]
            else:
                self.mMyLog.d(f'No {ARG_KEY_NAME_VOICEID}.')

            # ================================================
            self.mMyLog.d()

            pass

    # # # # # # # # # # # # # # # # # # # #
    # for Both Args(Global/Inner)
    # # # # # # # # # # # # # # # # # # # #
    def update_BothArgs(self, argKey, argVal):
        if not self.mAllArgDicts == None:
            if argKey in self.mAllArgDicts:
                self.mAllArgDicts[argKey] = argVal

        if not self.mInnerArgs == None:
            if argKey in self.mInnerArgs:
                self.mInnerArgs[argKey] = argVal

    # # # # # # # # # # # # # # # # # # # # 
    # for GlobalArgs
    # # # # # # # # # # # # # # # # # # # #
    def hasKeyInGlobalArg(self, argKey, argDefValIfNone=None):
        if self.mAllArgDicts == None:
            self.mMyLog.e(msg="Critical error. mAllArgDicts is None[hasKeyInGlobalArg]", argGoExit=True)
            return argDefValIfNone

        return self.mAllArgDicts[argKey] if (argKey in self.mAllArgDicts) else argDefValIfNone

    def getValInGlobalArg(self, argKey, argDefValIfNone=None):
        if self.mAllArgDicts == None:
            self.mMyLog.d(msg="Critical error. mAllArgDicts is None[getValInGlobalArg]")
            return argDefValIfNone

        return self.mAllArgDicts[argKey] if (argKey in self.mAllArgDicts) else argDefValIfNone

    def setValInGlobalArg(self, argKey, argVal):
        if self.mAllArgDicts == None:
            self.mMyLog.e(msg="Critical error. mAllArgDicts is None[setValInGlobalArg]", argGoExit=True)
            return False

        self.mAllArgDicts[argKey] = argVal
        return True

    def copy_GlobalArgs(self):
        if self.mAllArgDicts == None:
            return None
        else:
            return self.mAllArgDicts.copy()

    def update_GlobalArgs(self, argGlobalArgs):
        self.mAllArgDicts = argGlobalArgs

    # # # # # # # # # # # # # # # # # # # # 
    # for InnerArgs
    # # # # # # # # # # # # # # # # # # # #
    def hasKeyInInnerArg(self, argKey, argDefValIfNone=None):
        if self.mInnerArgs == None:
            self.mMyLog.e(msg="Critical error. mAllArgDicts is None[hasKeyInInnerArg]", argGoExit=True)
            return argDefValIfNone

        return self.mInnerArgs[argKey] if (argKey in self.mInnerArgs) else argDefValIfNone

    def getValInnerArg(self, argKey, argDefValIfNone=None):
        if self.mInnerArgs == None:
            self.mMyLog.e(msg="Critical error. mInnerArgs is None[getValInnerArg]", argGoExit=True)
            return argDefValIfNone

        return self.mInnerArgs[argKey] if (argKey in self.mInnerArgs) else argDefValIfNone

    def setValInnerArg(self, argKey, argVal):
        if self.mInnerArgs == None:
            self.mMyLog.e(msg="Critical error. mInnerArgs is None[setValInnerArg]", argGoExit=True)
            return False

        self.mInnerArgs[argKey] = argVal
        return True

    def copy_InnerArgs(self):
        if self.mInnerArgs == None:
            return None
        else:
            return self.mInnerArgs.copy()

    def update_InnerArgs(self, argPromptArgs):
        self.mInnerArgs = argPromptArgs


    def __str__(self):
        retStr = f"■■■ ArgsGenerator: myId({id(self)}:)"

        if hasattr(self, "mMyName") and len(self.mMyName) > 0:
            retStr = retStr + f'self.mMyName : {self.mMyName}\n'

        if hasattr(self, f"mAllArgDicts") and len(self.mAllArgDicts) > 0:
            retStr = retStr + f'■ mAllArgDicts({id(self.mAllArgDicts)}) : \n'
            for key, value in self.mAllArgDicts.items():
                retStr = retStr + f'{key} -> {value}\n'
        else:
            retStr = retStr + "mAllArgDicts None.\n"

        retStr = f"{retStr}\n"

        if hasattr(self, f"mInnerArgs") and len(self.mInnerArgs) > 0:
            retStr = retStr + f'■ mInnerArgs({id(self.mInnerArgs)}) : \n'
            for key, value in self.mInnerArgs.items():
                retStr = retStr + f'{key} -> {value}\n'
        else:
            retStr = retStr + "mInnerArgs None.\n"

        # retStr = f"{retStr}\n"

        return retStr
