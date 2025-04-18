# -*- coding: utf-8 -*-
from env.env_vars import *


def valid_check(argLog, argType=PROMPT_KEY_NAME_GENASR):
    if argType == PROMPT_KEY_NAME_GENASR:
        DIR_PATH_HOME = get_my_proj_home()
        if not DIR_PATH_HOME:
            argLog.e("=== OMG!! NO GEN_ASR_AIvoice_HOME. check it.", argGoExit=True)

        DIR_PATH_RES = get_my_proj_res()
        if not DIR_PATH_RES:
            argLog.e("=== OMG!! NO GEN_ASR_AIvoice_RES. check it.", argGoExit=False)

        DIR_PATH_RESULT = get_my_proj_result()
        if not DIR_PATH_RESULT:
            argLog.e("=== OMG!! NO GEN_ASR_AIvoice_RESULT. check it.", argGoExit=False)
    elif argType == PROMPT_KEY_NAME_EVALIMG:
        DIR_PATH_HOME = get_my_proj_home()
        if not DIR_PATH_HOME:
            argLog.e(f"=== OMG!! NO MY_STR_KEY_HOME. check it.", argGoExit=True)

        DIR_PATH_RES = get_my_proj_res()
        if not DIR_PATH_RES:
            argLog.e(f"=== OMG!! NO MY_STR_KEY_RES. check it.", argGoExit=False)

        DIR_PATH_RESULT = get_my_proj_result()
        if not DIR_PATH_RESULT:
            argLog.e(f"=== OMG!! NO MY_STR_KEY_RESULT. check it.", argGoExit=False)

    argLog.d(f'valid_check: {argType}')
    argLog.d(f'DIR_PATH_HOME: {DIR_PATH_HOME}')
    argLog.d(f'DIR_PATH_RES: {DIR_PATH_RES}')
    argLog.d(f'DIR_PATH_RESULT: {DIR_PATH_RESULT}')

    argLog.flush_buffer()


