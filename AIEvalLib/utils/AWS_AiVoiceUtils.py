# -*- coding: utf-8 -*-

from GlobalVars import *
from GlobalUtil import get_client_ai_voice_aws

IDX_ASR_AWS_SUPPORT_LANGUAGES_COUNTRY = 0  # # # Don't USE it.
IDX_ASR_AWS_SUPPORT_LANGUAGES_LOCALE  = 1  # # # Don't USE it.
IDX_ASR_AWS_SUPPORT_LANGUAGES_VOICEID = 2  # # # index of VOICEID

ASR_AWS_LANGUAGES_IDX_KO_KR = 47
ASR_AWS_LANGUAGES_IDX_EN_US = 18
ASR_AWS_LANGUAGES_IDX_JP_JP = 44

# https://docs.aws.amazon.com/polly/latest/dg/available-voices.html
ASR_AWS_SUPPORT_LANGUAGES = [
    ["아랍어(걸프)", "ar-AE", "Hala"],        		#000
    ["아랍어(걸프)", "ar-AE", "Zayd"],        		#001
    ["네덜란드어(벨기에)", "nl-BE", "Lisa"],   		#002
    ["카탈루냐어", "ca-ES", "Arlet"],         		#003
    ["체코어", "cs-CZ", "Jitka"],            		#004
    ["중국어(광동어)", "yue-CN", "Hiujin"],   		#005
    ["표준 중국어", "cmn-CN", "Zhiyu"],       		#006
    ["덴마크어", "da-DK", "Sofie"],          		#007
    ["네덜란드어", "nl-NL", "Laura"],         		#008
    ["영어(호주)", "en-AU", "Olivia"],       		#009
    ["영어(영국)", "en-GB", "Amy"],          		#010
    ["영어(영국)", "en-GB", "Emma"],         		#011
    ["영어(영국)", "en-GB", "Brian"],        		#012
    ["영어(영국)", "en-GB", "Arthur"],       		#013
    ["영어(인도)", "en-IN", "Kajal"],        		#014
    ["영어(아일랜드)", "en-IE", "Niamh"],      		#015
    ["영어(뉴질랜드)", "en-NZ", "Aria"],       		#016
    ["영어(남아프리카)", "en-ZA", "Ayanda"],   		#017
    ["영어(미국)", "en-US", "Danielle"],     		#018
    ["영어(미국)", "en-US", "Gregory"],      		#019
    ["영어(미국)", "en-US", "Ivy"],          		#020
    ["영어(미국)", "en-US", "Joanna"],       		#021
    ["영어(미국)", "en-US", "Kendra"],       		#022
    ["영어(미국)", "en-US", "Kimberly"],     		#023
    ["영어(미국)", "en-US", "Salli"],        		#024
    ["영어(미국)", "en-US", "Joey"],         		#025
    ["영어(미국)", "en-US", "Justin"],       		#026
    ["영어(미국)", "en-US", "Kevin"],        		#027
    ["영어(미국)", "en-US", "Matthew"],      		#028
    ["영어(미국)", "en-US", "Ruth"],         		#029
    ["영어(미국)", "en-US", "Stephen"],      		#030
    ["핀란드어", "fi-FI", "Suvi"],           		#031
    ["프랑스어", "fr-FR", "Lea"],            		#032
    ["프랑스어", "fr-FR", "Remi"],           		#033
    ["프랑스어(벨기에)", "fr-BE", "Isabelle"], 		#034
    ["프랑스어(캐나다)", "fr-CA", "Gabrielle"],		#035
    ["프랑스어(캐나다)", "fr-CA", "Liam"],     		#036
    ["독일어", "de-DE", "Vicki"],            		#037
    ["독일어", "de-DE", "Daniel"],           		#038
    ["독일어(오스트리아)", "de-AT", "Hannah"], 		#039
    ["독일어(스위스)", "de-CH", "Sabrina"],    		#040
    ["힌디어", "hi-IN", "Kajal"],            		#041
    ["이탈리아어", "it-IT", "Bianca"],        		#042
    ["이탈리아어", "it-IT", "Adriano"],       		#043
    ["일본어", "ja-JP", "Takumi"],           		#044
    ["일본어", "ja-JP", "Kazuha"],           		#045
    ["일본어", "ja-JP", "Tomoko"],           		#046
    ["한국어", "ko-KR", "Seoyeon"],          		#047
    ["노르웨이어", "nb-NO", "Ida"],           		#048
    ["폴란드어", "pl-PL", "Ola"],            		#049
    ["포르투갈어(브라질)", "pt-BR", "Camila"],  		#050
    ["포르투갈어(브라질)", "pt-BR", "Vitoria"], 		#051
    ["포르투갈어(브라질)", "pt-BR", "Thiago"],  		#052
    ["포르투갈어(유럽)", "pt-PT", "Ines"],     		#053
    ["스페인어(유럽)", "es-ES", "Lucia"],      		#054
    ["스페인어(유럽)", "es-ES", "Sergio"],     		#055
    ["스페인어(멕시코)", "es-MX", "Mia"],      		#056
    ["스페인어(멕시코)", "es-MX", "Andres"],   		#057
    ["스페인어(미국)", "es-US", "Lupe"],       		#058
    ["스페인어(미국)", "es-US", "Pedro"],      		#059
    ["스웨덴어", "sv-SE", "Elin"],           		#060
    ["터키어", "tr-TR", "Burcu"]             		#061
]

def get_speed_value(speed):
    if speed > 2.0:
        speed = 2.0
    elif speed < 0.5:
        speed = 0.5
    return f'{str(speed * 100)}%'

def get_pitch_value(pitch):
    if pitch == 'high':
        return '100%'
    elif pitch == 'low':
        return '-100%'
    else:
        return '0'

def gen_ai_voice_aws(argFilePath, argText, argIdxVoiceId, argSpeakingSpeed=1, argSpeakingPitch='middle', argLog=None):
    __ai_voice_country = ASR_AWS_SUPPORT_LANGUAGES[0][IDX_ASR_AWS_SUPPORT_LANGUAGES_COUNTRY]
    __ai_voice_id = ASR_AWS_SUPPORT_LANGUAGES[0][IDX_ASR_AWS_SUPPORT_LANGUAGES_VOICEID]
    try:
        __ai_voice_country = ASR_AWS_SUPPORT_LANGUAGES[argIdxVoiceId][IDX_ASR_AWS_SUPPORT_LANGUAGES_COUNTRY]
        __ai_voice_id = ASR_AWS_SUPPORT_LANGUAGES[argIdxVoiceId][IDX_ASR_AWS_SUPPORT_LANGUAGES_VOICEID]
    except TypeError:
        print(f'argFilePath={argFilePath}, argText={argText}, argIdxVoiceId={argIdxVoiceId}')

    polly_client = get_client_ai_voice_aws()

    ___text = f'<speak><prosody rate="{get_speed_value(argSpeakingSpeed)}">{argText}</prosody></speak>'

    response = polly_client.synthesize_speech(TextType='ssml', VoiceId=__ai_voice_id, OutputFormat=AI_VOICE_SAVE_FILE_EXT, Text=___text, Engine=AI_VOICE_AWS_ENGINE)

    dbg_msg = f'▶ [aws]argFilePath[Vid:{argIdxVoiceId}:{__ai_voice_id}:{__ai_voice_country}] : {argFilePath} : {argText}'
    if argLog:
        argLog.e(dbg_msg)
    else:
        print(dbg_msg)

    file = open(argFilePath, 'wb')
    file.write(response['AudioStream'].read())
    file.close()

