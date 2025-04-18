# -*- coding: utf-8 -*-
from GlobalUtil import get_client_ai_gpt_msa, do_get_all_assisant_list
from config.engine_config import GPT_ENGINE_NAME_GPT4o

if __name__ == '__main__':
    client = get_client_ai_gpt_msa(argEngineName=GPT_ENGINE_NAME_GPT4o)
    do_get_all_assisant_list(argLog=None, arg_client=client, do_delete=False)
