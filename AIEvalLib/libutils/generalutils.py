# -*- coding: utf-8 -*-
import importlib
import os
import sys
from abc import ABC, abstractmethod

import pandas as pd
from tabulate import tabulate

from GlobalUtil import attach_img_to_excel
from GlobalVars import *

_MY_PROMPT:str = 'GeneralUtils'

_MY_MODULE_NAME = 'def_func'
_SUP_CLS_NAME = 'ClsAbsGeneralLib'
_IMPL_CLS_NAME = 'ClsGeneralLibImpl'

def myprint(msg : str):
    print(f'[{_MY_PROMPT}]:{msg}')

class ClsAbsGeneralLib(ABC):
    def __init__(self, argname='None'):
        self.mMyName = f'(def:{self.__class__.__name__}):{argname}'
        pass

    @abstractmethod
    def do_print(self, argmsg: str):

        pass

    def __str__(self):
        return f'[{self.mMyName}]'

class ClsAbsGenerateOutput(ABC):
    def __init__(self, arg_args, arg_my_log, argname='None'):
        self.mMyName = f'(def:{self.__class__.__name__}):{argname}'
        self.mArgs = arg_args
        self.mLog = arg_my_log
        pass

    @abstractmethod
    def do_generate(self, arg_datas):

        pass

    def _default_generate_(self, arg_datas):
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

def _inner_load_module_class(arg_folder_name: str, arg_module_name: str, arg_class_name: str, arg_sup_class_name):
    module_path = f"dynamic_src.{arg_folder_name}.{arg_module_name}"
    try:
        imported_module = importlib.import_module(module_path)
    except ModuleNotFoundError:
        raise ImportError(f"모듈 '{module_path}' 을 찾을 수 없습니다.")

    try:
        cls = getattr(imported_module, arg_class_name)
    except AttributeError:
        raise ImportError(f"'{module_path}' 모듈에 '{arg_class_name}' 클래스가 없습니다.")

    if not issubclass(cls, arg_sup_class_name):
        raise TypeError(f"{arg_class_name} 클래스는 BaseModule 을 상속해야 합니다.")

    return cls

def load_class_impl__(folder_name: str = 'evaldummy', module_name: str=_MY_MODULE_NAME, cls_name: str=_IMPL_CLS_NAME, sup_name = ClsAbsGeneralLib):
    _my_cls = _inner_load_module_class(arg_folder_name=folder_name, arg_module_name=module_name, arg_class_name=cls_name, arg_sup_class_name=sup_name)

    if not issubclass(_my_cls, sup_name):
        raise TypeError(f"{_IMPL_CLS_NAME} 클래스는 {_SUP_CLS_NAME}을 상속해야 합니다.")

    return _my_cls
