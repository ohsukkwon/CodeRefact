# -*- coding: utf-8 -*-
from GlobalVars import *
from GlobalUtil import get_date_file_name, get_dir_result_without_overlay
from MSA_AiVoiceUtils import gen_ai_voice_msa
from MyKeyStore import *

my_target_dir = get_dir_result_without_overlay()
try:
    if not os.path.exists(my_target_dir):
        os.makedirs(my_target_dir)
except OSError:
    print("Error: Failed to create the directory.")

my_voice_save_file_name = f'AzureTTS_{get_date_file_name()}.{AI_VOICE_SAVE_FILE_EXT}'
tmp_mp3_path = os.path.join(my_target_dir, my_voice_save_file_name)
print(f'tmp_mp3_path : {tmp_mp3_path}')

# ___text = '''Hello my name is AndyO. Nice to meet you. Now is ''' f'{get_timedate_now()}'
# print(f'text : {___text}')

text_nor = """The C motif looks good, but the lack of LED treatment is surprising!"""
text_speed = """<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-GB"><voice name="en-US-AvaNeural"><prosody rate="200%">안녕하세요, 약사님! 
이 약은 어떻게 복용하나요? 

안녕하세요! 
아, 이 약은 식사 후에 복용하셔야 해요. 

그러면 매일 몇 번 먹어야 하나요? 

하루에 두 번, 아침과 저녁에 복용하세요. 

알겠어요! 
감사합니다! 

도움이 되어서 기쁩니다! 
다른 질문 있으세요?</prosody></voice></speak>"""
text_pitch = """<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-GB"><voice name="en-US-AvaNeural"><prosody pitch="-5st">The C motif looks good, but the lack of LED treatment is surprising!</prosody></voice></speak>"""

gen_ai_voice_msa(tmp_mp3_path, text_nor, 140, argSpeakingSpeed=0.5, argSpeakingPitch='low')
