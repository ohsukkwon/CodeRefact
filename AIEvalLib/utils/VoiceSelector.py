# -*- coding: utf-8 -*-
import traceback

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# # # # # # # # # DON"T remove it # # # # # # # # #
from AWS_AiVoiceUtils import gen_ai_voice_aws
from ELV_AiVoiceUtils import gen_ai_voice_elv
from GGC_AiVoiceUtils import gen_ai_voice_ggc
from GPT_AiVoiceUtils import gen_ai_voice_gpt
from MSA_AiVoiceUtils import gen_ai_voice_msa
from NCP_AiVoiceUtils import gen_ai_voice_ncp
from MyKeyStore import *
# # # # # # # # # # # # # # # # # # # # # # # # # #


VOICE_SOLUTION_FOR_LANGUAGE = {
    "ko-KR": "ncp",
    "en-US": "msa",
    "en-GB": "aws",
    "en-AU": "elv",
    "en-IN": "aws",
    "fr-FR": "aws",
    "de-DE": "gpt",
    "it-IT": "msa",
    "es-ES": "aws",
    "es-US": "msa",
    "es-MX": "msa",
    "pt-BR": "msa",
    "zh-CN": "aws",
    "ja-JP": "aws",
    "pl-PL": "gpt", # 미정
    "nl-NL": "msa",
    "sv-SE": "gpt",
    "ro-RO": "elv",
    "vi-VN": "gpt",
    "th-TH": "msa",
    "id-ID": "gpt",
    "zh-HK": "gpt",
    "zh-TW": "gpt",
    "hi-IN": "gpt",
    "ru-RU": "gpt", # 미정
    "ar-AE": "aws",
    "tr-TR": "gpt",
    "pt-PT": "gpt", # 미정
    "fr-CA": "gpt", # 미정
}

# Authenticate the client using your key and endpoint
def authenticate_client():
    ta_credential = AzureKeyCredential(keystore_get_key_type(KEYTYPE_IDX_GPTScenario_Azure_AIservicesLanguage_NONE))
    text_analytics_client = TextAnalyticsClient(
        endpoint=keystore_get_ep_type(EPTYPE_IDX_GPTScenario_Azure_AIservicesLanguage_NONE),
        credential=ta_credential)
    return text_analytics_client

def select_voice_solution(argLog, arg_path, arg_text, arg_voice_engine, arg_voice_id, arg_speaking_speed, arg_speaking_pitch, locale):
    # print(f"select_voice_solution(arg_path:{arg_path}, arg_text:{arg_text}, arg_voice_engine:{arg_voice_engine}, arg_voice_id:{arg_voice_id}, locale:{locale})")
    try:
        call_func = f"gen_ai_voice_{arg_voice_engine}"
        # if argLog:
        #     argLog.d(call_func)
        # else:
        #     print(call_func)

            # for debugging
            # gen_ai_voice_gpt(argLog, arg_path, arg_text, 0)
            # gen_ai_voice_ncp(argLog, arg_path, arg_text, arg_voice_id)
            # gen_ai_voice_aws(argLog, arg_path, arg_text, arg_voice_id)
            # gen_ai_voice_elv(argLog, arg_path, arg_text, arg_voice_id)
            # gen_ai_voice_ggc(argLog, arg_path, arg_text, arg_voice_id)
            # gen_ai_voice_msa(argLog, arg_path, arg_text, arg_voice_id)
        globals()[call_func](argFilePath=arg_path, argText=arg_text, argIdxVoiceId=arg_voice_id, argSpeakingSpeed=arg_speaking_speed, argSpeakingPitch=arg_speaking_pitch, argLog=argLog)

    except Exception as err:
        print("Encountered exception2. {}".format(err))
        print(f"{traceback.print_exc()}")