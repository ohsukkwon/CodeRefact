# -*- coding: utf-8 -*-
import os

from GlobalVars import *
from GlobalUtil import get_date_file_name, get_dir_result_without_overlay
from NCP_AiVoiceUtils import gen_ai_voice_ncp

encText = """안녕하세요, 오늘은 유튜브가 사회에 미치는 영향에 대해 이야기하겠습니다.
유튜브는 개인이 콘텐츠를 제작하고 공유할 수 있는 플랫폼입니다.
MZ세대는 유튜브를 통해 새로운 트렌드를 주도하고 있습니다."""

my_target_dir = get_dir_result_without_overlay()
try:
    if not os.path.exists(my_target_dir):
        os.makedirs(my_target_dir)
except OSError:
    print("Error: Failed to create the directory.")

my_voice_save_file_name = f'{AI_VOICE_ENGINE_NAME_NCP}_{get_date_file_name()}.{AI_VOICE_SAVE_FILE_EXT}'
tmp_mp3_path = os.path.join(my_target_dir, my_voice_save_file_name)
print(f'tmp_mp3_path : {tmp_mp3_path}')

gen_ai_voice_ncp(argFilePath=tmp_mp3_path, argText=encText, argIdxVoiceId=82, argSpeakingSpeed=0.5, argSpeakingPitch='low')