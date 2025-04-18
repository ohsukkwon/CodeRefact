# -*- coding: utf-8 -*-
import os

# OpType : (REL)OfficeKeys / (DEV)MyPersonalKeys

# SolutionType : GPTScenario / AIvoice
# SolutionCompony : Azure/OpenAI/AWS/Google/OpenAI/NCP/Elevenlabs
# SolutionCategory : (Azure-)OpenAI/(Azure-)SpeechService/(Azure-)AIservicesLanguage/OpenAI/AWS/Google/NCP/Elevenlabs
### SolutionType_SolutionCompany_SolutionCategory

from typing import Final

___OPTYPE_OFFICE : Final = 1
___OPTYPE_HOME : Final = 2

def convert_to_str(argOpType):
    if argOpType == ___OPTYPE_OFFICE:
        return str("OFFICE")
    elif argOpType == ___OPTYPE_HOME:
        return str("HOME")

___current_op_type = ___OPTYPE_OFFICE

print(f'# # # # ___current_op_type : {convert_to_str(___current_op_type)}')
print()

KEYTYPE_IDX_GPTScenario_Azure_OpenAI_GPT4o: Final  = 0
KEYTYPE_IDX_GPTScenario_Azure_OpenAI_GPT4o_mini: Final  = 1
KEYTYPE_IDX_GPTScenario_Azure_OpenAI_o1: Final  = 9
KEYTYPE_IDX_GPTScenario_Azure_OpenAI_tts_hd: Final  = 2
KEYTYPE_IDX_GPTScenario_OpenAI_NONE_NONE: Final  = 3

KEYTYPE_IDX_GPTScenario_Azure_AIservicesLanguage_NONE: Final = 4
KEYTYPE_IDX_AIvoice_Azure_SpeechService_NONE: Final = 5
KEYTYPE_IDX_AIvoice_AWS_NONE_NONE: Final = 6
KEYTYPE_IDX_AIvoice_NCP_NONE_NONE : Final= 7
KEYTYPE_IDX_AIvoice_Elevenlabs_NONE_NONE: Final = 8

if ___current_op_type == ___OPTYPE_OFFICE:
    ___KEYTYPE_GPTScenario_Azure_OpenAI_GPT4o: Final = os.environ['SEC_AZURE_1KEY_2OpenAI_3gpt-4o_4SE-SQE-05_5NONE']
    ___KEYTYPE_GPTScenario_Azure_OpenAI_GPT4o_mini: Final = os.environ['SEC_AZURE_1KEY_2OpenAI_3gpt-4o-mini_4SE-SQE-04_5NONE']
    ___KEYTYPE_GPTScenario_Azure_OpenAI_o1: Final = os.environ['SEC_AZURE_1KEY_2OpenAI_3gpt-o1_4SE-SQE-03-o1_5NONE']
    ___KEYTYPE_GPTScenario_Azure_OpenAI_tts_hd : Final = os.environ['SEC_AZURE_1KEY_2OpenAI_3tts-hd_4SE-SQE-10_5NONE']
    ___KEYTYPE_GPTScenario_OpenAI_NONE_NONE: Final = os.environ['SEC_OpenAI_1KEY_2OpenAI_3NONE_4NONE_5NONE']

    ___KEYTYPE_GPTScenario_Azure_AIservicesLanguage_NONE: Final = os.environ['SEC_AZURE_1KEY_2AIServices_3LANGUAGEDETECTION_4NONE_5NONE']
    ___KEYTYPE_AIvoice_Azure_SpeechService_NONE: Final = os.environ['SEC_AZURE_1KEY_2SpeechServices_3NONE_4NONE_5NONE']
    ___KEYTYPE_AIvoice_AWS_NONE_NONE: Final = os.environ['SEC_AWS_1KEY_2AWS_3NONE_4NONE_5NONE']
    ___KEYTYPE_AIvoice_NCP_NONE_NONE: Final = os.environ['SEC_NCP_1KEY_2NCP_3NONE_4NONE_5NONE']
    ___KEYTYPE_AIvoice_Elevenlabs_NONE_NONE: Final = os.environ['SEC_ElevenLabs_1KEY_2NONE_3NONE_4NONE_5NONE']
    pass
else:
    ___KEYTYPE_GPTScenario_Azure_OpenAI_GPT4o: Final = os.environ['ANDYO_AZURE_1KEY_2OpenAI_3gpt-4o_4osk-eval_gpt-4o_5NONE']
    ___KEYTYPE_GPTScenario_Azure_OpenAI_GPT4o_mini: Final = os.environ['ANDYO_AZURE_1KEY_2OpenAI_3gpt-4o-mini_4SQE-scenario-gpt-4o-mini_5NONE']
    ___KEYTYPE_GPTScenario_Azure_OpenAI_o1: Final = os.environ['ANDYO_AZURE_1KEY_2OpenAI_3gpt-o1_4SE-SQE-03-o1_5NONE']
    ___KEYTYPE_GPTScenario_Azure_OpenAI_tts_hd: Final = os.environ['ANDYO_AZURE_1KEY_2OpenAI_3tts-hd_4sqe-asr-azure-gpt-tts-hd_5NONE']
    ___KEYTYPE_GPTScenario_OpenAI_NONE_NONE: Final = os.environ['ANDYO_OpenAI_1KEY_2OpenAI_3NONE_4NONE_5NONE']

    ___KEYTYPE_GPTScenario_Azure_AIservicesLanguage_NONE: Final = os.environ['ANDYO_AZURE_1KEY_2AIServices_3LANGUAGEDETECTION_4SQE4-ASR-AI-services-languagedetection_5NONE']
    ___KEYTYPE_AIvoice_Azure_SpeechService_NONE: Final = os.environ['ANDYO_AZURE_1KEY_2SpeechServices_3NONE_4SQE-ASR-AI-voice_5NONE']
    ___KEYTYPE_AIvoice_AWS_NONE_NONE: Final = os.environ['ANDYO_AWS_1KEY_2AWS_3NONE_4NONE_5NONE']
    ___KEYTYPE_AIvoice_NCP_NONE_NONE: Final = os.environ['ANDYO_NCP_1KEY_2NCP_3NONE_4NONE_5NONE']
    ___KEYTYPE_AIvoice_Elevenlabs_NONE_NONE: Final = os.environ['ANDYO_ElevenLabs_1KEY_2NONE_3NONE_4NONE_5NONE']
    pass

EPTYPE_IDX_GPTScenario_Azure_OpenAI_GPT4o: Final = 0
EPTYPE_IDX_GPTScenario_Azure_OpenAI_GPT4o_mini: Final = 1
EPTYPE_IDX_GPTScenario_Azure_OpenAI_o1: Final = 4
EPTYPE_IDX_GPTScenario_Azure_OpenAI_tts_hd: Final = 2
EPTYPE_IDX_GPTScenario_Azure_AIservicesLanguage_NONE: Final = 3
if ___current_op_type == ___OPTYPE_OFFICE:
    ___EPTYPE_GPTScenario_Azure_OpenAI_GPT4o : Final = os.environ['SEC_AZURE_1EP_2OpenAI_3gpt-4o_4SE-SQE-05_5NONE']
    ___EPTYPE_GPTScenario_Azure_OpenAI_GPT4o_mini : Final = os.environ['SEC_AZURE_1EP_2OpenAI_3gpt-4o-mini_4SE-SQE-04_5NONE']
    ___EPTYPE_GPTScenario_Azure_OpenAI_o1: Final = os.environ['SEC_AZURE_1EP_2OpenAI_3gpt-o1_4SE-SQE-03-o1_5NONE']
    ___EPTYPE_GPTScenario_Azure_OpenAI_tts_hd : Final = os.environ['SEC_AZURE_1EP_2OpenAI_3tts-hd_4SE-SQE-10_5NONE']
    ___EPTYPE_GPTScenario_Azure_AIservicesLanguage_NONE : Final = os.environ['SEC_AZURE_1EP_2AIServices_3LANGUAGEDETECTION_4NONE_5NONE']
    pass
else:
    ___EPTYPE_GPTScenario_Azure_OpenAI_GPT4o : Final = os.environ['ANDYO_AZURE_1EP_2OpenAI_3gpt-4o_4osk-eval_gpt-4o_5NONE']
    ___EPTYPE_GPTScenario_Azure_OpenAI_GPT4o_mini: Final = os.environ['ANDYO_AZURE_1EP_2OpenAI_3gpt-4o-mini_4SQE-scenario-gpt-4o-mini_5NONE']
    ___EPTYPE_GPTScenario_Azure_OpenAI_o1: Final = os.environ['ANDYO_AZURE_1EP_2OpenAI_3gpt-o1_4SE-SQE-03-o1_5NONE']
    ___EPTYPE_GPTScenario_Azure_OpenAI_tts_hd: Final = os.environ['ANDYO_AZURE_1EP_2OpenAI_3tts-hd_4sqe-asr-azure-gpt-tts-hd_5NONE']
    ___EPTYPE_GPTScenario_Azure_AIservicesLanguage_NONE: Final = os.environ['ANDYO_AZURE_1EP_2AIServices_3LANGUAGEDETECTION_4SQE4-ASR-AI-services-languagedetection_5NONE']
    pass

APIVERSIONTYPE_IDX_GPTScenario_Azure_OpenAI_GPT4o: Final = 0
APIVERSIONTYPE_IDX_GPTScenario_Azure_OpenAI_GPT4o_mini: Final = 1
APIVERSIONTYPE_IDX_GPTScenario_Azure_OpenAI_o1: Final = 3
APIVERSIONTYPE_IDX_GPTScenario_Azure_OpenAI_tts_hd: Final = 2
if ___current_op_type == ___OPTYPE_OFFICE:
    ___APIVERSIONTYPE_GPTScenario_Azure_OpenAI_GPT4o : Final = os.environ['SEC_AZURE_1APIVERSION_2OpenAI_3gpt-4o_4SE-SQE-05_5NONE']
    ___APIVERSIONTYPE_GPTScenario_Azure_OpenAI_GPT4o_mini: Final = os.environ['SEC_AZURE_1APIVERSION_2OpenAI_3gpt-4o-mini_4SE-SQE-04_5NONE']
    ___APIVERSIONTYPE_GPTScenario_Azure_OpenAI_o1: Final = os.environ['SEC_AZURE_1APIVERSION_2OpenAI_3gpt-o1_4SE-SQE-03-o1_5NONE']
    ___APIVERSIONTYPE_GPTScenario_Azure_OpenAI_tts_hd: Final = os.environ['SEC_AZURE_1APIVERSION_2OpenAI_3tts-hd_4SE-SQE-10_5NONE']
    pass
else:
    ___APIVERSIONTYPE_GPTScenario_Azure_OpenAI_GPT4o : Final = os.environ['ANDYO_AZURE_1APIVERSION_2OpenAI_3gpt-4o_4osk-eval_gpt-4o_5NONE']
    ___APIVERSIONTYPE_GPTScenario_Azure_OpenAI_GPT4o_mini: Final = os.environ['ANDYO_AZURE_1APIVERSION_2OpenAI_3gpt-4o-mini_4SQE-scenario-gpt-4o-mini_5NONE']
    ___APIVERSIONTYPE_GPTScenario_Azure_OpenAI_o1: Final = os.environ['ANDYO_AZURE_1APIVERSION_2OpenAI_3gpt-o1_4SE-SQE-03-o1_5NONE']
    ___APIVERSIONTYPE_GPTScenario_Azure_OpenAI_tts_hd: Final = os.environ['ANDYO_AZURE_1APIVERSION_2OpenAI_3tts-hd_4sqe-asr-azure-gpt-tts-hd_5NONE']
    pass

DEPLOYMENTTYPE_IDX_GPTScenario_Azure_OpenAI_GPT4o: Final = 0
DEPLOYMENTTYPE_IDX_GPTScenario_Azure_OpenAI_GPT4o_mini: Final = 1
DEPLOYMENTTYPE_IDX_GPTScenario_Azure_OpenAI_o1: Final = 3
DEPLOYMENTTYPE_IDX_GPTScenario_Azure_OpenAI_tts_hd: Final = 2
if ___current_op_type == ___OPTYPE_OFFICE:
    ___DEPLOYMENTTYPE_GPTScenario_Azure_OpenAI_GPT4o : Final = os.environ['SEC_AZURE_1DEPLOY_2OpenAI_3gpt-4o_4SE-SQE-05_5NONE']
    ___DEPLOYMENTTYPE_GPTScenario_Azure_OpenAI_GPT4o_mini: Final = os.environ['SEC_AZURE_1DEPLOY_2OpenAI_3gpt-4o-mini_4SE-SQE-04_5NONE']
    ___DEPLOYMENTTYPE_GPTScenario_Azure_OpenAI_o1: Final = os.environ['SEC_AZURE_1DEPLOY_2OpenAI_3gpt-o1_4SE-SQE-03-o1_5NONE']
    ___DEPLOYMENTTYPE_GPTScenario_Azure_OpenAI_tts_hd: Final = os.environ['SEC_AZURE_1DEPLOY_2OpenAI_3tts-hd_4SE-SQE-10_5NONE']
    pass
else:
    ___DEPLOYMENTTYPE_GPTScenario_Azure_OpenAI_GPT4o : Final = os.environ['ANDYO_AZURE_1DEPLOY_2OpenAI_3gpt-4o_4osk-eval_gpt-4o_5NONE']
    ___DEPLOYMENTTYPE_GPTScenario_Azure_OpenAI_GPT4o_mini: Final = os.environ['ANDYO_AZURE_1DEPLOY_2OpenAI_3gpt-4o-mini_4SQE-scenario-gpt-4o-mini_5NONE']
    ___DEPLOYMENTTYPE_GPTScenario_Azure_OpenAI_o1: Final = os.environ['ANDYO_AZURE_1DEPLOY_2OpenAI_3gpt-o1_4SE-SQE-03-o1_5NONE']
    ___DEPLOYMENTTYPE_GPTScenario_Azure_OpenAI_tts_hd: Final = os.environ['ANDYO_AZURE_1DEPLOY_2OpenAI_3tts-hd_4sqe-asr-azure-gpt-tts-hd_5NONE']
    pass

REGIONTYPE_IDX_AIvoice_Azure_SpeechServices_NONE: Final = 0
if ___current_op_type == ___OPTYPE_OFFICE:
    ___REGIONTYPE_AIvoice_Azure_SpeechServices_NONE: Final = os.environ['SEC_AZURE_1REGION_2SpeechServices_3NONE_4NONE_5NONE']
    pass
else:
    ___REGIONTYPE_AIvoice_Azure_SpeechServices_NONE: Final = os.environ['ANDYO_AZURE_1REGION_2SpeechServices_3NONE_4SQE-ASR-AI-voice_5NONE']
    pass

SECRETTYPE_IDX_AIvoice_AWS_NONE_NONE: Final  = 0
SECRETTYPE_IDX_AIvoice_NCP_NONE_NONE: Final  = 1
if ___current_op_type == ___OPTYPE_OFFICE:
    ___SECRETTYPE_AIvoice_AWS_NONE_NONE: Final = os.environ['SEC_AWS_1SECRET_2AWS_3NONE_4NONE_5NONE']
    ___SECRETTYPE_AIvoice_NCP_NONE_NONE: Final = os.environ['SEC_NCP_1SECRET_2NCP_3NONE_4NONE_5NONE']
    pass
else:
    ___SECRETTYPE_AIvoice_AWS_NONE_NONE: Final = os.environ['ANDYO_AWS_1SECRET_2AWS_3NONE_4NONE_5NONE']
    ___SECRETTYPE_AIvoice_NCP_NONE_NONE: Final = os.environ['ANDYO_NCP_1SECRET_2NCP_3NONE_4NONE_5NONE']
    pass

JSONTYPE_IDX_Google_APPLICATION_CREDENTIALS: Final = 0
if ___current_op_type == ___OPTYPE_OFFICE:
    ___JSONTYPE_AIvoice_Google_APPLICATION_CREDENTIALS: Final = os.environ['GOOGLE_APPLICATION_CREDENTIALS']
    pass
else:
    ___JSONTYPE_AIvoice_Google_APPLICATION_CREDENTIALS: Final = os.environ['GOOGLE_APPLICATION_CREDENTIALS']
    pass



def keystore_get_key_type(argType = 0):
    if argType == KEYTYPE_IDX_GPTScenario_Azure_OpenAI_GPT4o:
        __current_ret_val = ___KEYTYPE_GPTScenario_Azure_OpenAI_GPT4o
    elif argType == KEYTYPE_IDX_GPTScenario_Azure_OpenAI_GPT4o_mini:
        __current_ret_val = ___KEYTYPE_GPTScenario_Azure_OpenAI_GPT4o_mini
    elif argType == KEYTYPE_IDX_GPTScenario_Azure_OpenAI_o1:
        __current_ret_val = ___KEYTYPE_GPTScenario_Azure_OpenAI_o1
    elif argType == KEYTYPE_IDX_GPTScenario_Azure_OpenAI_tts_hd:
        __current_ret_val = ___KEYTYPE_GPTScenario_Azure_OpenAI_tts_hd
    elif argType == KEYTYPE_IDX_GPTScenario_OpenAI_NONE_NONE:
        __current_ret_val = ___KEYTYPE_GPTScenario_OpenAI_NONE_NONE
    elif argType == KEYTYPE_IDX_GPTScenario_Azure_AIservicesLanguage_NONE:
        __current_ret_val = ___KEYTYPE_GPTScenario_Azure_AIservicesLanguage_NONE
    elif argType == KEYTYPE_IDX_AIvoice_Azure_SpeechService_NONE:
        __current_ret_val = ___KEYTYPE_AIvoice_Azure_SpeechService_NONE
    elif argType == KEYTYPE_IDX_AIvoice_AWS_NONE_NONE:
        __current_ret_val = ___KEYTYPE_AIvoice_AWS_NONE_NONE
    elif argType == KEYTYPE_IDX_AIvoice_NCP_NONE_NONE:
        __current_ret_val = ___KEYTYPE_AIvoice_NCP_NONE_NONE
    elif argType == KEYTYPE_IDX_AIvoice_Elevenlabs_NONE_NONE:
        __current_ret_val = ___KEYTYPE_AIvoice_Elevenlabs_NONE_NONE
    else:
        print(f"# # # OMG!! Error:KEYTYPE{argType}")
        __current_ret_val = ___KEYTYPE_GPTScenario_Azure_OpenAI_GPT4o

    # print(f"___KEYTYPE : {__current_ret_val}")

    return __current_ret_val

def keystore_get_ep_type(argType = 0):
    if argType == EPTYPE_IDX_GPTScenario_Azure_OpenAI_GPT4o:
        __current_ret_val = ___EPTYPE_GPTScenario_Azure_OpenAI_GPT4o
    elif argType == EPTYPE_IDX_GPTScenario_Azure_OpenAI_GPT4o_mini:
        __current_ret_val = ___EPTYPE_GPTScenario_Azure_OpenAI_GPT4o_mini
    elif argType == EPTYPE_IDX_GPTScenario_Azure_OpenAI_o1:
        __current_ret_val = ___EPTYPE_GPTScenario_Azure_OpenAI_o1
    elif argType == EPTYPE_IDX_GPTScenario_Azure_OpenAI_tts_hd:
        __current_ret_val = ___EPTYPE_GPTScenario_Azure_OpenAI_tts_hd
    elif argType == EPTYPE_IDX_GPTScenario_Azure_AIservicesLanguage_NONE:
        __current_ret_val = ___EPTYPE_GPTScenario_Azure_AIservicesLanguage_NONE
    else:
        print(f"# # # OMG!! Error:EPTYPE{argType}")
        __current_ret_val = ___EPTYPE_GPTScenario_Azure_OpenAI_GPT4o

    # print(f"___EPTYPE : {__current_ret_val}")

    return __current_ret_val

def keystore_get_apiversion_type(argType = 0):
    if argType == APIVERSIONTYPE_IDX_GPTScenario_Azure_OpenAI_GPT4o:
        __current_ret_val = ___APIVERSIONTYPE_GPTScenario_Azure_OpenAI_GPT4o
    elif argType == APIVERSIONTYPE_IDX_GPTScenario_Azure_OpenAI_GPT4o_mini:
        __current_ret_val = ___APIVERSIONTYPE_GPTScenario_Azure_OpenAI_GPT4o_mini
    elif argType == APIVERSIONTYPE_IDX_GPTScenario_Azure_OpenAI_o1:
        __current_ret_val = ___APIVERSIONTYPE_GPTScenario_Azure_OpenAI_o1
    elif argType == APIVERSIONTYPE_IDX_GPTScenario_Azure_OpenAI_tts_hd:
        __current_ret_val = ___APIVERSIONTYPE_GPTScenario_Azure_OpenAI_tts_hd
    else:
        print(f"# # # OMG!! Error:APIVERSIONTYPE{argType}")
        __current_ret_val = ___APIVERSIONTYPE_GPTScenario_Azure_OpenAI_GPT4o

    # print(f"___APIVERSIONTYPE : {__current_ret_val}")

    return __current_ret_val

def keystore_get_deployment_type(argType = 0):
    if argType == DEPLOYMENTTYPE_IDX_GPTScenario_Azure_OpenAI_GPT4o:
        __current_ret_val = ___DEPLOYMENTTYPE_GPTScenario_Azure_OpenAI_GPT4o
    elif argType == DEPLOYMENTTYPE_IDX_GPTScenario_Azure_OpenAI_GPT4o_mini:
        __current_ret_val = ___DEPLOYMENTTYPE_GPTScenario_Azure_OpenAI_GPT4o_mini
    elif argType == DEPLOYMENTTYPE_IDX_GPTScenario_Azure_OpenAI_o1:
        __current_ret_val = ___DEPLOYMENTTYPE_GPTScenario_Azure_OpenAI_o1
    elif argType == DEPLOYMENTTYPE_IDX_GPTScenario_Azure_OpenAI_tts_hd:
        __current_ret_val = ___DEPLOYMENTTYPE_GPTScenario_Azure_OpenAI_tts_hd
    else:
        print(f"# # # OMG!! Error:DEPLOYMENTTYPE{argType}")
        __current_ret_val = ___DEPLOYMENTTYPE_GPTScenario_Azure_OpenAI_GPT4o

    # print(f"___DEPLOYMENTTYPE : {__current_ret_val}")

    return __current_ret_val

def keystore_get_region_type(argType = 0):
    if argType == REGIONTYPE_IDX_AIvoice_Azure_SpeechServices_NONE:
        __current_ret_val = ___REGIONTYPE_AIvoice_Azure_SpeechServices_NONE
    else:
        print(f"# # # OMG!! Error:REGIONTYPE{argType}")
        __current_ret_val = ___REGIONTYPE_AIvoice_Azure_SpeechServices_NONE

    # print(f"___REGIONTYPE : {__current_ret_val}")

    return __current_ret_val

def keystore_get_secret_type(argType = 0):
    if argType == SECRETTYPE_IDX_AIvoice_AWS_NONE_NONE:
        __current_ret_val = ___SECRETTYPE_AIvoice_AWS_NONE_NONE
    elif argType == SECRETTYPE_IDX_AIvoice_NCP_NONE_NONE:
        __current_ret_val = ___SECRETTYPE_AIvoice_NCP_NONE_NONE
    else:
        print(f"# # # OMG!! Error:SECRETTYPE{argType}")
        __current_ret_val = ___SECRETTYPE_AIvoice_AWS_NONE_NONE

    return __current_ret_val

def keystore_get_json_type(argType = 0):
    if argType == JSONTYPE_IDX_Google_APPLICATION_CREDENTIALS:
        __current_ret_val = ___JSONTYPE_AIvoice_Google_APPLICATION_CREDENTIALS
    else:
        print(f"# # # OMG!! Error:JSONTYPE{argType}")
        __current_ret_val = ___JSONTYPE_AIvoice_Google_APPLICATION_CREDENTIALS

    return __current_ret_val
