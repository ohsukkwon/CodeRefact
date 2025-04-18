# -*- coding: utf-8 -*-
import sys

from google.cloud import texttospeech

from GlobalUtil import get_client_ai_voice_ggc

IDX_ASR_GGC_SUPPORT_LANGUAGES_VOICDID = 0  # # # voiceID
IDX_ASR_GGC_SUPPORT_LANGUAGES_GENDER  = 1  # # # Don't USE it.

# https://cloud.google.com/text-to-speech/docs/voices?hl=ko
ASR_GGC_SUPPORT_LANGUAGES : list = [
    ["da-DK-Neural2-D", "FEMALE"],		#000
    ["en-AU-Neural2-A", "FEMALE"],		#001
    ["en-AU-Neural2-B", "MALE"],		#002
    ["en-AU-Neural2-C", "FEMALE"],		#003
    ["en-AU-Neural2-D", "MALE"],		#004
    ["en-IN-Neural2-A", "FEMALE"],		#005
    ["en-IN-Neural2-B", "MALE"],		#006
    ["en-IN-Neural2-C", "MALE"],		#007
    ["en-IN-Neural2-D", "FEMALE"],		#008
    ["en-GB-Neural2-A", "FEMALE"],		#009
    ["en-GB-Neural2-B", "MALE"],		#010
    ["en-GB-Neural2-C", "FEMALE"],		#011
    ["en-GB-Neural2-D", "MALE"],		#012
    ["en-GB-Neural2-F", "FEMALE"],		#013
    ["en-US-Neural2-A", "MALE"],		#014
    ["en-US-Neural2-C", "FEMALE"],		#015
    ["en-US-Neural2-D", "MALE"],		#016
    ["en-US-Neural2-E", "FEMALE"],		#017
    ["en-US-Neural2-F", "FEMALE"],		#018
    ["en-US-Neural2-G", "FEMALE"],		#019
    ["en-US-Neural2-H", "FEMALE"],		#020
    ["en-US-Neural2-I", "MALE"],		#021
    ["en-US-Neural2-J", "MALE"],		#022
    ["fil-ph-Neural2-A", "FEMALE"],		#023
    ["fil-ph-Neural2-D", "MALE"],		#024
    ["fr-CA-Neural2-A", "FEMALE"],		#025
    ["fr-CA-Neural2-B", "MALE"],		#026
    ["fr-CA-Neural2-C", "FEMALE"],		#027
    ["fr-CA-Neural2-D", "MALE"],		#028
    ["fr-FR-Neural2-A", "FEMALE"],		#029
    ["fr-FR-Neural2-B", "MALE"],		#030
    ["fr-FR-Neural2-C", "FEMALE"],		#031
    ["fr-FR-Neural2-D", "MALE"],		#032
    ["fr-FR-Neural2-E", "FEMALE"],		#033
    ["de-DE-Neural2-A", "FEMALE"],		#034
    ["de-DE-Neural2-B", "MALE"],		#035
    ["de-DE-Neural2-C", "FEMALE"],		#036
    ["de-DE-Neural2-D", "MALE"],		#037
    ["de-DE-Neural2-F", "FEMALE"],		#038
    ["hi-IN-Neural2-A", "FEMALE"],		#039
    ["hi-IN-Neural2-B", "MALE"],		#040
    ["hi-IN-Neural2-C", "MALE"],		#041
    ["hi-IN-Neural2-D", "FEMALE"],		#042
    ["it-IT-Neural2-A", "FEMALE"],		#043
    ["it-IT-Neural2-C", "MALE"],		#044
    ["ja-JP-Neural2-B", "FEMALE"],		#045
    ["ja-JP-Neural2-C", "MALE"],		#046
    ["ja-JP-Neural2-D", "MALE"],		#047
    ["ko-KR-Neural2-A", "FEMALE"],		#048
    ["ko-KR-Neural2-B", "FEMALE"],		#049
    ["ko-KR-Neural2-C", "MALE"],		#050
    ["pt-BR-Neural2-A", "FEMALE"],		#051
    ["pt-BR-Neural2-B", "MALE"],		#052
    ["pt-BR-Neural2-C", "FEMALE"],		#053
    ["es-ES-Neural2-A", "FEMALE"],		#054
    ["es-ES-Neural2-B", "MALE"],		#055
    ["es-ES-Neural2-C", "FEMALE"],		#056
    ["es-ES-Neural2-D", "FEMALE"],		#057
    ["es-ES-Neural2-E", "FEMALE"],		#058
    ["es-ES-Neural2-F", "MALE"],		#059
    ["es-US-Neural2-A", "FEMALE"],		#060
    ["es-US-Neural2-B", "MALE"],		#061
    ["es-US-Neural2-C", "MALE"],		#062
    ["th-TH-Neural2-C", "FEMALE"],		#063
    ["vi-VN-Neural2-A", "FEMALE"],		#064
    ["vi-VN-Neural2-D", "MALE"],		#065
    ["sv-SE-Wavenet-C", "FEMALE"],		#066
    ["sv-SE-Wavenet-E", "MALE"],		#067
    ["ru-RU-Wavenet-A", "FEMALE"],		#068
    ["ru-RU-Wavenet-B", "MALE"]		    #069
]

def get_speed_value(speed):
    if speed > 2.0:
        speed = 2.0
    elif speed < 0.5:
        speed = 0.5
    return speed

def get_pitch_value(pitch):
    if pitch == 'high':
        return 3.0
    elif pitch == 'low':
        return -3.0
    else:
        return 0

def gen_ai_voice_ggc(argFilePath, argText, argIdxVoiceId, argSpeakingSpeed=1, argSpeakingPitch='middle', argLog=None):
    # client = texttospeech.TextToSpeechClient()
    client = get_client_ai_voice_ggc()
    input_text = texttospeech.SynthesisInput(text=argText)

    __item_voiceId = ASR_GGC_SUPPORT_LANGUAGES[argIdxVoiceId][IDX_ASR_GGC_SUPPORT_LANGUAGES_VOICDID]
    __item_gender = ASR_GGC_SUPPORT_LANGUAGES[argIdxVoiceId][IDX_ASR_GGC_SUPPORT_LANGUAGES_GENDER]
    split_arr_lang = __item_voiceId.split(r'-')
    if len(split_arr_lang) == 4:

        pass
    else:
        sys.exit("OMG!! split_arr_lang SHOULD be 4.")

    dbg_msg = f'▶ [ggc]argFilePath[Vid:{argIdxVoiceId}:{__item_voiceId}:{__item_gender}] : {argFilePath} : {argText}'
    if argLog:
        argLog.e(dbg_msg)
    else:
        print(dbg_msg)
    pass

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice_config = texttospeech.VoiceSelectionParams(
        language_code=ASR_GGC_SUPPORT_LANGUAGES[argIdxVoiceId][0][:5],
        name=ASR_GGC_SUPPORT_LANGUAGES[argIdxVoiceId][0],
        # ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        speaking_rate=get_speed_value(argSpeakingSpeed),
        pitch=get_pitch_value(argSpeakingPitch)
    )

    response = client.synthesize_speech(
        request={"input": input_text, "voice": voice_config, "audio_config": audio_config}
    )

    with open(argFilePath, "wb") as out:
        out.write(response.audio_content)
        # print(f'Audio content written to file {argFilePath}')