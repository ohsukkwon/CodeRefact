# -*- coding: utf-8 -*-

from GPT_AiVoiceUtils import gen_ai_voice_gpt
from GlobalVars import *
from GlobalUtil import get_date_file_name, get_dir_result_without_overlay
from MyKeyStore import *

___access_key_id = keystore_get_key_type(argType=KEYTYPE_IDX_GPTScenario_OpenAI_NONE_NONE)

___text = """I see skies of blue and clouds of white
             The bright blessed days, the dark sacred nights
             And I think to myself
             What a wonderful world"""

my_target_dir = get_dir_result_without_overlay()
try:
    if not os.path.exists(my_target_dir):
        os.makedirs(my_target_dir)
except OSError:
    print("Error: Failed to create the directory.")

my_voice_save_file_name = f'OpenAI_{get_date_file_name()}.{AI_VOICE_SAVE_FILE_EXT}'

tmp_mp3_path = os.path.join(my_target_dir, my_voice_save_file_name)
print(f'tmp_mp3_path : {tmp_mp3_path}')

gen_ai_voice_gpt(argFilePath=tmp_mp3_path, argText=___text, argIdxVoiceId=0, argSpeakingSpeed=0.5)

