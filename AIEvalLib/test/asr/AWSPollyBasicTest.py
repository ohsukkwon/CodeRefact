# -*- coding: utf-8 -*-

from AWS_AiVoiceUtils import gen_ai_voice_aws, get_client_ai_voice_aws
from GlobalVars import *
from GlobalUtil import get_date_file_name, get_dir_result_without_overlay
from MyKeyStore import *
import requests
requests.packages.urllib3.disable_warnings()

ASR_AWS_SUPPORT_LANGUAGES2 = [
    ["스페인어(미국)", "es-US", "Lupe"],           #10
    ["스페인어(미국)", "es-US", "Pedro"],          #11
    ["폴란드어", "pl-PL", "Ola"],         #12
    ["네덜란드어", "nl-NL", "Laura"],        #13
    ["스웨덴어", "sv-SE", "Elin"],         #14
    ["영어(호주)", "en-AU", "Olivia"],             #32
    ["중국어(광동어)", "yue-CN", "Hiujin"],            #33
    ["힌디어", "hi-IN", "Kajal"], #34
    ["아랍어", "are", "Hala"],#35
    ["아랍어", "are", "Zayd"],#35
    ["터키어", "tr-TR", "Burcu"]
]

___text = 'The C motif looks good, but the lack of LED treatment is surprising!'
___text_speed = '<speak><prosody rate="200%">The C motif looks good, but the lack of LED treatment is surprising!</prosody></speak>'

polly_client = get_client_ai_voice_aws()

my_target_dir = get_dir_result_without_overlay()
try:
    if not os.path.exists(my_target_dir):
        os.makedirs(my_target_dir)
except OSError:
    print("Error: Failed to create the directory.")

my_voice_save_file_name = f'AWS_{get_date_file_name()}.{AI_VOICE_SAVE_FILE_EXT}'
tmp_mp3_path = os.path.join(my_target_dir, my_voice_save_file_name)
print(f'tmp_mp3_path : {tmp_mp3_path}')

# # response = polly_client.synthesize_speech(VoiceId="Amy", OutputFormat=AI_VOICE_SAVE_FILE_EXT, Text=___text, Engine=AI_VOICE_AWS_ENGINE)
# response = polly_client.synthesize_speech(TextType='ssml', VoiceId="Amy", OutputFormat=AI_VOICE_SAVE_FILE_EXT, Text=___text_speed, Engine=AI_VOICE_AWS_ENGINE)
#
# file = open(tmp_mp3_path, 'wb')
# file.write(response['AudioStream'].read())
# file.close()

gen_ai_voice_aws(argFilePath=tmp_mp3_path, argText=___text, argIdxVoiceId=10, argSpeakingSpeed=1.0)