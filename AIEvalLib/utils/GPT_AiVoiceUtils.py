# -*- coding: utf-8 -*-
import warnings

from GlobalUtil import get_client_ai_gpt_gpt

g_client = get_client_ai_gpt_gpt()

# https://platform.openai.com/docs/guides/text-to-speech
ASR_GPT_SUPPORT_LANGUAGES : list = [
    "alloy",    #000
    "echo",     #001
    "fable",    #002
    "onyx",     #003
    "nova",     #004
    "shimmer"   #005
]

def get_speed_value(speed):
    if speed > 2.0:
        speed = 2.0
    elif speed < 0.5:
        speed = 0.5
    return speed

def gen_ai_voice_gpt(argFilePath, argText, argIdxVoiceId, argSpeakingSpeed=1, argSpeakingPitch='middle', argLog=None):
    # Ignore DeprecationWarning
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    __item_voiceId = ASR_GPT_SUPPORT_LANGUAGES[argIdxVoiceId]

    dbg_msg = f'▶ [gpt]argFilePath[Vid:{argIdxVoiceId}:{__item_voiceId}] : {argFilePath} : {argText}'
    if argLog:
        argLog.e(dbg_msg)
    else:
        print(dbg_msg)

    response = g_client.audio.speech.create(
        model="tts-1",
        voice=__item_voiceId,
        input=argText,
        speed=get_speed_value(argSpeakingSpeed)
    )

    response.stream_to_file(argFilePath)