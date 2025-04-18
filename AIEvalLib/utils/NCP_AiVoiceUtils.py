# -*- coding: utf-8 -*-
import urllib.request

from MyKeyStore import *
from config.engine_config import *

___client_id = keystore_get_key_type(argType=KEYTYPE_IDX_AIvoice_NCP_NONE_NONE)
___client_secret = keystore_get_secret_type(argType=SECRETTYPE_IDX_AIvoice_NCP_NONE_NONE)

IDX_ASR_NCP_SUPPORT_LANGUAGES_LANGUAGE  = 0  # # # Don't USE it.
IDX_ASR_NCP_SUPPORT_LANGUAGES_VOICEID   = 1  # # # index of VOICEID

ASR_NCP_LANGUAGES_IDX_KO_KR = 1

# https://api.ncloud-docs.com/docs/ai-naver-clovavoice-ttspremium
ASR_NCP_SUPPORT_LANGUAGES = [
["Korean","nara"],              	        #000
["Korean","nara_call"],	                   	#001
["Korean","nminyoung"],	                   	#002
["Korean","nyejin"],	                   	#003
["Korean","jinho"],             	        #004
["English","clara"],	                   	#005
["English","matt"],	                   	    #006
["Japanese","shinji"],	                   	#007
["Chinese","meimei"],	                   	#008
["Chinese","liangliang"],       	                   	#009
["Spanish","jose"],	                   	    #010
["Spanish","carmen"],	                   	#011
["Korean","nminsang"],	                   	#012
["Korean","nsinu"],	                   	    #013
["Korean","nhajun"],            	        #014
["Korean","ndain"],	                   	    #015
["Korean","njiyun"],	                   	#016
["Korean","nsujin"],	                   	#017
["Korean","njinho"],	                   	#018
["Korean","njihun"],            	        #019
["Korean","njooahn"],	                   	#020
["Korean","nseonghoon"],	                #021
["Korean","njihwan"],	                   	#022
["Korean","nsiyoon"],	                   	#023
["Korean","ngaram"],            	        #024
["Japanese","ntomoko"],	                   	#025
["Japanese","nnaomi"],	                   	#026
["Japanese","dnaomi_joyful"],	            #027
["Japanese","dnaomi_formal"],	            #028
["Japanese","driko"],           	        #029
["Japanese","deriko"],	                   	#030
["Japanese","nsayuri"],	                   	#031
["Korean","ngoeun"],	                   	#032
["Korean","neunyoung"],	                   	#033
["Korean","nsunkyung"],         	        #034
["Korean","nyujin"],	                   	#035
["Korean","ntaejin"],	                   	#036
["Korean","nyoungil"],	                   	#037
["Korean","nseungpyo"],	                   	#038
["Korean","nwontak"],           	        #039
["Korean","dara_ang"],	                   	#040
["Korean","nsunhee"],	                   	#041
["Korean","nminseo"],	                   	#042
["Korean","njiwon"],	                   	#043
["Korean","nbora"],             	        #044
["Korean","njonghyun"],	                   	#045
["Korean","njoonyoung"],	                #046
["Korean","njaewook"],	                   	#047
["English","danna"],	                   	#048
["English","djoey"],            	        #049
["Japanese","dhajime"],	                   	#050
["Japanese","ddaiki"],	                   	#051
["Japanese","dayumu"],	                   	#052
["Japanese","dmio"],	                   	#053
["Taiwanese","chiahua"],        	        #054
["Taiwanese","kuanlin"],	                #055
["Korean","nes_c_hyeri"],	                #056
["Korean","nes_c_sohyun"],	                #057
["Korean","nes_c_mikyung"],	                #058
["Korean","nes_c_kihyo"],       	        #059
["Korean","ntiffany"],	                   	#060
["Korean","napple"],	                   	#061
["Korean","njangj"],	                   	#062
["Korean","noyj"],	                   	    #063
["Korean","neunseo"],           	        #064
["Korean","nheera"],	                   	#065
["Korean","nyoungmi"],	                   	#066
["Korean","nnarae"],	                   	#067
["Korean","nyeji"],	                   	    #068
["Korean","nyuna"],             	        #069
["Korean","nkyunglee"],	                   	#070
["Korean","nminjeong"],	                   	#071
["Korean","nihyun"],	                   	#072
["Korean","nraewon"],	                   	#073
["Korean","nkyuwon"],           	        #074
["Korean","nkitae"],	                   	#075
["Korean","neunwoo"],	                   	#076
["Korean","nkyungtae"],	                   	#077
["Korean","nwoosik"],	                   	#078
["Korean","vara"],              	        #079
["Korean","vmikyung"],	                   	#080
["Korean","vdain"],             	        # # # # #081
["Korean","vyuna"],             	        # # # # #082
["Korean","vhyeri"],            	        # # # # #083
["Korean + English (U.S.)","dara-danna"],   #084
["Korean + English (U.S.)","dsinu-matt"],	#085
["Korean","nsabina"],	                   	#086
["Korean","nmammon"],	                   	#087
["Korean","nmeow"],	                   	    #088
["Korean","nwoof"],             	        #089
["Korean","nreview"],	                   	#090
["Korean","nyounghwa"],	                   	#091
["Korean","nmovie"],	                   	#092
["Korean","nsangdo"],	                   	#093
["Korean","nshasha"],           	        #094
["Korean","nian"],	                   	    #095
["Korean","ndonghyun"],	                   	#096
["Korean","vian"],              	        # # # # #097
["Korean","vdonghyun"],	                   	#098
["Japanese","dsayuri"],         	        #099
["Japanese","dtomoko"],	                   	#100
["Japanese","dnaomi"],	                   	#101
["Korean","vgoeun"],	                   	#102
["Korean","vdaeseong"],	                   	#103
["Korean","ngyeongjun"],        	        #104
["Korean","ndaeseong"],	                   	#105
["Korean","njonghyeok"]         	        #106
]

def get_speed_value(speed):
    if speed == 1.0:
        return '0'
    if speed > 2.0:
        speed = 2.0
    elif speed < 0.5:
        speed = 0.5
    if speed > 1.0:
        return f'{str(speed * 2 * -1)}'
    else:
        return f'{str(speed * 8)}'

def get_pitch_value(pitch):
    if pitch == 'high':
        return '-5.0'
    elif pitch == 'low':
        return '5.0'
    else:
        return '0'

def gen_ai_voice_ncp(argFilePath, argText, argIdxVoiceId, argSpeakingSpeed=1, argSpeakingPitch='middle', argLog = None):
    if argText is None:
        return

    __item_target_persona_lang = ASR_NCP_SUPPORT_LANGUAGES[argIdxVoiceId][IDX_ASR_NCP_SUPPORT_LANGUAGES_LANGUAGE]
    __item_target_persona_id = ASR_NCP_SUPPORT_LANGUAGES[argIdxVoiceId][IDX_ASR_NCP_SUPPORT_LANGUAGES_VOICEID]

    dbg_msg = f'▶ [ncp]argFilePath[Vid:{argIdxVoiceId}:{__item_target_persona_id}:{__item_target_persona_lang}:{__item_target_persona_id}] : {argFilePath} : {argText}'
    if argLog:
        argLog.e(dbg_msg)
    else:
        print(dbg_msg)

    parent_dir = os.path.dirname(argFilePath)
    try:
        if not os.path.exists(parent_dir):
            os.makedirs(parent_dir)
    except OSError:
        print('Error: NCP_make_ai_voice() Creating directory. ' + parent_dir)

    def set_http_proxy(arg_proxy):
        if arg_proxy is None:  # Use system default setting
            proxy_support = urllib.request.ProxyHandler()
        elif arg_proxy == '':  # Don't use any proxy
            proxy_support = urllib.request.ProxyHandler({})
        else:  # Use proxy
            proxy_support = urllib.request.ProxyHandler({'http': '%s' % arg_proxy, 'https': '%s' % arg_proxy})
        opener = urllib.request.build_opener(proxy_support)
        urllib.request.install_opener(opener)

    _proxy = None if (current_GPT_PROGRAM_PROXY_MODE==GPT_PROGRAM_PROXY_MODE_HOME) else 'http://10.244.254.254:8080'
    set_http_proxy(_proxy)

    encText = urllib.parse.quote(argText)
    # print(get_speed_value(argSpeakingSpeed))
    # print(get_pitch_value(argSpeakingPitch))
    data = f"speaker={__item_target_persona_id}&volume=0&speed={get_speed_value(argSpeakingSpeed)}&pitch={get_pitch_value(argSpeakingPitch)}&format=mp3&text=" + encText
    url = "https://naveropenapi.apigw.ntruss.com/tts-premium/v1/tts"
    request = urllib.request.Request(url)
    request.add_header("X-NCP-APIGW-API-KEY-ID", ___client_id)
    request.add_header("X-NCP-APIGW-API-KEY", ___client_secret)

    response = urllib.request.urlopen(request, data=data.encode('utf-8'))
    rescode = response.getcode()

    if rescode == 200:
        response_body = response.read()
        with open(argFilePath, 'wb') as f:
            f.write(response_body)
    else:
        print("### OMG!! Error Code:" + rescode + ", encText=" + encText)