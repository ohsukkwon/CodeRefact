# -*- coding: utf-8 -*-
import json
import os
import sys

from utils.GlobalVars import *

################### ADD ###################
_JSON_PROD_CONFIG___ = None

def _load_json_config():
    global _JSON_PROD_CONFIG___

    # GET g_sys_my_pmt in main.py
    main_module = sys.modules.get("__main__")
    if main_module:
        sys_my_pmt = getattr(main_module, "g_sys_my_pmt", "NOT FOUND")
    else:
        sys_my_pmt = "NOT FOUND"

    print(f'# sys_my_pmt: {sys_my_pmt}')
    m_ailib_path = os.environ["AI_LIB_PATH"]

    if _JSON_PROD_CONFIG___:
        return
    else:
        _jsonCfgFilePath = os.path.abspath(os.path.join(m_ailib_path,'config_product', f'{sys_my_pmt}.json'))

    print(f'_jsonCfgFilePath={_jsonCfgFilePath}')

    if not os.path.exists(_jsonCfgFilePath):
        print(f'### OMG!!! Error: _jsonCfgFilePath is NOT exist. {_jsonCfgFilePath}')
        sys.exit(0)

    with open(_jsonCfgFilePath, "r", encoding='utf-8-sig') as f:
        _JSON_PROD_CONFIG___ = json.load(f)

    print(f'_JSON_PROD_CONFIG___: {_JSON_PROD_CONFIG___}')

################### SET ###################
def get_my_proj_home():
    _load_json_config()
    global _JSON_PROD_CONFIG___

    if _JSON_PROD_CONFIG___ is not None:
        MY_STR_KEY_HOME = _JSON_PROD_CONFIG___[ARG_KEY_CONFIG_NAME_HOMEDIR]
        return os.environ[MY_STR_KEY_HOME]
    else:
        return None

def get_my_proj_res():
    _load_json_config()
    global _JSON_PROD_CONFIG___

    if _JSON_PROD_CONFIG___ is not None:
        MY_STR_KEY_RES = _JSON_PROD_CONFIG___[ARG_KEY_CONFIG_NAME_RESDIR]
        return os.environ[MY_STR_KEY_RES]
    else:
        return None

def get_my_proj_result():
    _load_json_config()
    global _JSON_PROD_CONFIG___

    if _JSON_PROD_CONFIG___ is not None:
        MY_STR_KEY_RESULT = _JSON_PROD_CONFIG___[ARG_KEY_CONFIG_NAME_RESULTDIR]
        return os.environ[MY_STR_KEY_RESULT]
    else:
        return None

def get_my_proj_result_file_prefix():
    _load_json_config()
    global _JSON_PROD_CONFIG___

    if _JSON_PROD_CONFIG___ is not None:
        MY_RESULT_FILE_PREFIX = _JSON_PROD_CONFIG___[ARG_KEY_CONFIG_NAME_RESULTPREFIX]
        return MY_RESULT_FILE_PREFIX
    else:
        return None