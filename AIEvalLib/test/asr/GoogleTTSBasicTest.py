# -*- coding: utf-8 -*-
import os
from typing import Sequence

import google.cloud.texttospeech as tts

from GGC_AiVoiceUtils import gen_ai_voice_ggc
from GlobalUtil import get_date_file_name, get_client_ai_voice_ggc, get_dir_result_without_overlay
from GlobalVars import *

def unique_languages_from_voices(voices: Sequence[tts.Voice]):
    language_set = set()
    for voice in voices:
        for language_code in voice.language_codes:
            language_set.add(language_code)
    return language_set


def list_languages():
    client = get_client_ai_voice_ggc()
    response = client.list_voices()
    languages = unique_languages_from_voices(response.voices)

    print(f" Languages: {len(languages)} ".center(60, "-"))
    for i, language in enumerate(sorted(languages)):
        print(f"{language:>10}", end="\n" if i % 5 == 4 else "")

if __name__ == "__main__":
    list_languages()

    ___text = """Hello, today I will talk about the impact of YouTube on society.
    YouTube is a platform where individuals can create and share content.
    The MZ generation is leading new trends through YouTube."""

    my_target_dir = get_dir_result_without_overlay()
    try:
        if not os.path.exists(my_target_dir):
            os.makedirs(my_target_dir)
    except OSError:
        print("Error: Failed to create the directory.")

    my_voice_save_file_name = f'GoogleTTS_{get_date_file_name()}.{AI_VOICE_SAVE_FILE_EXT}'

    tmp_mp3_path = os.path.join(my_target_dir, my_voice_save_file_name)
    print(f'tmp_mp3_path : {tmp_mp3_path}')

    gen_ai_voice_ggc(tmp_mp3_path, ___text, argIdxVoiceId=9, argSpeakingSpeed=0.5, argSpeakingPitch='low')