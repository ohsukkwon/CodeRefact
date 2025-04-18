# -*- coding: utf-8 -*-
from elevenlabs import VoiceSettings, save

from GlobalUtil import get_client_ai_voice_elv
from GlobalVars import AI_VOICE_AWS_LANG_TYPE_MULTI_v2, AI_VOICE_AWS_VOICE_TYPE_mp3_44100_128

client = get_client_ai_voice_elv()

IDX_ASR_ELV_SUPPORT_LANGUAGES_NAME      = 0  # # # Don't USE it.
IDX_ASR_ELV_SUPPORT_LANGUAGES_VOICEID   = 1  # # # VOICEID
IDX_ASR_ELV_SUPPORT_LANGUAGES_GENDER    = 2  # # # GENDER
IDX_ASR_ELV_SUPPORT_LANGUAGES_COUNTRY   = 3  # # # COUNTRY

# https://elevenlabs.io/docs/product/voices/default-voices
ASR_ELV_SUPPORT_LANGUAGES = [
    ["Alice", "Xb7hH8MSUJpSbSDYk0k2", "female", "British"],		    #000
    ["Aria", "9BWtsMINqrJLrRacOk9x", "female", "American"],		    #001
    ["Bill", "pqHfZKP75CvOlQylNhV4", "male", "American"],		    #002
    ["Brian", "nPczCjzI2devNBz1zQrb", "male", "American"],		    #003
    ["Callum", "N2lVS1w4EtoT3dr4eOWO", "male", "Transatlantic"],    #004
    ["Charlie", "IKne3meq5aSn9XLyUdCD", "male", "Australian"],	    #005
    ["Charlotte", "XB0fDUnXU5powFXDhCwa", "female", "Swedish"],	    #006
    ["Chris", "iP95p4xoKVk53GoZ742B", "male", "American"],		    #007
    ["Daniel", "onwK4e9ZLuTAKqWW03F9", "male", "British"],		    #008
    ["Eric", "cjVigY5qzO86Huf0OWal", "male", "American"],		    #009
    ["George", "JBFqnCBsd6RMkjVDRZzb", "male", "British"],		    #010
    ["Jessica", "cgSgspJ2msm6clMCkdW9", "female", "American"],	    #011
    ["Laura", "FGY2WhTYpPnrIDTdsKH5", "female", "American"],	    #012
    ["Liam", "TX3LPaxmHKxFdv7VOQHJ", "male", "American"],		    #013
    ["Lily", "pFZP5JQG7iQjIQuC4Bku", "female", "British"],		    #014
    ["Matilda", "XrExE9yKIg1WjnnlVkGX", "female", "American"],	    #015
    ["River", "SAz9YHcvj6GT2YYXdXww", "non-binary", "American"],    #016
    ["Roger", "CwhRBWXzGAHq8TQ4Fs17", "male", "American"],		    #017
    ["Sarah", "EXAVITQu4vr4xnSDxMaL", "female", "American"],	    #018
    ["Will", "bIHbv24MWmeRgasZH58o", "male", "American"],		    #019
    ["Adam", "pNInz6obpgDQGcFmaJgB", "male", "american"],		    #020
    ["Antoni", "ErXwobaYiN019PkySvjV", "male", "american"],		    #021
    ["Arnold", "VR6AewLTigWG4xSOukaG", "male", "american"],		    #022
    ["Clyde", "2EiwWnXFnvU5JabPnv8n", "male", "American"],		    #023
    ["Dave", "CYw3kZ02Hs0563khs1Fj", "male", "British"],		    #024
    ["Dorothy", "ThT5KcBeYPX3keUQqHPh", "female", "British"],	    #025
    ["Drew", "29vD33N1CtxCmqQRPOHJ", "male", "American"],		    #026
    ["Emily", "LcfcDJNUP1GQjkzn1xUU", "female", "American"],	    #027
    ["Ethan", "g5CIjZEefAph4nQFvHAz", "male", "American"],		    #028
    ["Fin", "D38z5RcWu1voky8WS1ja", "male", "Irish"],		        #029
    ["Freya", "jsCqWAovK2LkecY7zXl4", "female", "American"],	    #030
    ["George", "Yko7PKHZNXotIFUBG7I9", "male", "british"],		    #031
    ["Gigi", "jBpfuIE2acCO8z3wKNLl", "female", "American"],		    #032
    ["Giovanni", "zcAOhNBS3c14rBihAFp1", "male", "Italian"],	    #033
    ["Glinda", "z9fAnlkpzviPz146aGWa", "female", "American"],	    #034
    ["Grace", "oWAxZDx7w5VEj9dCyTzz", "female", "American"],	    #035
    ["Harry", "SOYHLrjzK2X1ezoPC6cr", "male", "American"],		    #036
    ["James", "ZQe5CZNOzWyzPSCn5a3c", "male", "Australian"],	    #037
    ["Jeremy", "bVMeCyTHy58xNoL34h3p", "male", "Irish"],		    #038
    ["Jessie", "t0jbNlBVZ17f02VDIeMI", "male", "American"],		    #039
    ["Joseph", "Zlb1dXrM653N07WRdFW3", "male", "British"],		    #040
    ["Josh", "TxGEqnHWrfWFTfGW9XjX", "male", "american"],		    #041
    ["Michael", "flq6f7yk4E4fJM5XTYuZ", "male", "American"],	    #042
    ["Mimi", "zrHiDhphv9ZnVXBqCLjz", "female", "Swedish"],		    #043
    ["Nicole", "piTKgcLEGmPE4e6mEKli", "female", "American"],	    #044
    ["Patrick", "ODq5zmih8GrVes37Dizd", "male", "American"],	    #045
    ["Paul", "5Q0t7uMcjvnagumLfvZi", "male", "American"],		    #046
    ["Rachel", "21m00Tcm4TlvDq8ikWAM", "female", "american"],	    #047
    ["Sam", "yoZ06aMxZJJ28mfd3POQ", "male", "american"],		    #048
    ["Serena", "pMsXgVXv3BLzUgSXRplE", "female", "American"],	    #049
    ["Thomas", "GBv7mTt0atIp3Br8iCZE", "male", "American"]		    #050
]

def gen_ai_voice_elv(argFilePath, argText, argIdxVoiceId, argSpeakingSpeed=1, argSpeakingPitch='middle', argLog=None):

    __person_name = ASR_ELV_SUPPORT_LANGUAGES[argIdxVoiceId][IDX_ASR_ELV_SUPPORT_LANGUAGES_NAME]
    __person_voiceid = ASR_ELV_SUPPORT_LANGUAGES[argIdxVoiceId][IDX_ASR_ELV_SUPPORT_LANGUAGES_VOICEID]
    __person_gender = ASR_ELV_SUPPORT_LANGUAGES[argIdxVoiceId][IDX_ASR_ELV_SUPPORT_LANGUAGES_GENDER]
    __person_country = ASR_ELV_SUPPORT_LANGUAGES[argIdxVoiceId][IDX_ASR_ELV_SUPPORT_LANGUAGES_COUNTRY]

    audio = client.text_to_speech.convert(
        voice_id=__person_voiceid,
        optimize_streaming_latency="0",
        output_format=AI_VOICE_AWS_VOICE_TYPE_mp3_44100_128,
        text=argText,
        model_id=AI_VOICE_AWS_LANG_TYPE_MULTI_v2,
        voice_settings=VoiceSettings(
            stability=0.1,
            similarity_boost=0.3,
            style=0.2,
        ),
    )

    dbg_msg = f'▶ [elv]argFilePath[Vid:{argIdxVoiceId}:{__person_voiceid}:{__person_name}:{__person_gender}:{__person_country}] : {argFilePath} : {argText}'
    if argLog:
        argLog.e(dbg_msg)
    else:
        print(dbg_msg)

    save(audio, argFilePath)
