# -*- coding: utf-8 -*-
from GlobalUtil import get_date_file_name, get_dir_result_without_overlay
from MyKeyStore import *
from NCP_AiVoiceUtils import gen_ai_voice_ncp

ASR_NCP_SUPPORT_LANGUAGES = [
    ["Korean", "vgoeun"],
    ["Korean", "vara"],
    ["Korean", "vhyeri"],
    ["Korean", "vmikyung"],
    ["Korean", "vdain"],
    ["Korean", "vyuna"],
    ["Korean", "vdaeseong"],
    ["Korean", "vian"],
    ["Korean", "vdonghyun"]
]

ASR_NCP_SUPPORT_LANGUAGES2 = [
    ["taiwan", "chiahua"],
    # ["taiwan", "kuanlin"],
]

top_level_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

___client_id = keystore_get_key_type(argType=KEYTYPE_IDX_AIvoice_NCP_NONE_NONE)
___client_secret = keystore_get_secret_type(argType=SECRETTYPE_IDX_AIvoice_NCP_NONE_NONE)

encText = f'''
你好，今天我要談談 YouTube 對社會的影響。
YouTube 是一個讓人們可以創作和分享內容的平台。
MZ 世代透過 YouTube 引領新潮流。
這個平台已經成為教育和資訊傳播的新方法。
在這裡很容易找到在傳統媒體中難以獲得的多元資訊。
YouTube 也對商業模式的改變產生了重大影響。
品牌和個人利用 YouTube 與更多消費者溝通。
已經創造出一個讓公眾可以直接參與的空間。
這也有助於政治觀點的形成。
例如，各種活動透過 YouTube 廣泛傳播。
'''

for i in range(0, len(ASR_NCP_SUPPORT_LANGUAGES2)):
    target_persona = ASR_NCP_SUPPORT_LANGUAGES2[i][1]

    my_target_dir = get_dir_result_without_overlay()

    try:
        if not os.path.exists(my_target_dir):
            os.makedirs(my_target_dir)
    except OSError:
        print("Error: Failed to create the directory.")

    my_target_path = os.path.join(my_target_dir, f'{i:02d}_{target_persona.strip("v")}_{get_date_file_name()}.mp3')

    gen_ai_voice_ncp(argFilePath=my_target_path, argText=encText, argIdxVoiceId=54)
