# -*- coding: utf-8 -*-

from GlobalUtil import do_get_all_assisant_list, get_client_ai_gpt_gpt

if __name__ == '__main__':
    myClient = get_client_ai_gpt_gpt()
    do_get_all_assisant_list(argLog=None, arg_client=myClient, do_delete=False)
