# -*- coding: utf-8 -*-

from MyKeyStore import *
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

        super()._default_generate_(arg_datas=arg_datas)
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
        self.mLog.d(f'[{self.mMyName}]■ do_eval : {slicedArrSentences}')

        return ERR_CODE_DUMMY, super()._make_dummy_table(slicedArrSentences), TokenRecord(0, 0, 0, 0,0)