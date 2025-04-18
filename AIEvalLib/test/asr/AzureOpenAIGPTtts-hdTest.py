# -*- coding: utf-8 -*-
from GlobalUtil import get_date_file_name, get_client_ai_voice_msa, get_dir_result_without_overlay
from GlobalVars import *
from MyKeyStore import *

# Setting destination files for TTS output
my_target_dir = get_dir_result_without_overlay()
try:
    if not os.path.exists(my_target_dir):
        os.makedirs(my_target_dir)
except OSError:
    print("Error: Failed to create the directory.")

my_voice_save_file_name = f'AzureOpeAIGPTtts-hd_{get_date_file_name()}.{AI_VOICE_SAVE_FILE_EXT}'

tmp_mp3_path = os.path.join(my_target_dir, my_voice_save_file_name)
print(f'tmp_mp3_path : {tmp_mp3_path}')

# Instantiate Azure OpenAI client
client =get_client_ai_voice_msa()

# Producing text-to-speech
response = client.audio.speech.create(
    model = "tts-1",
    voice = "alloy",
    input = "Menu options include vegetarian lasagna, beef bourguignon, and pan-seared salmon."
)
# Saving TTS output to file
response.write_to_file(tmp_mp3_path)