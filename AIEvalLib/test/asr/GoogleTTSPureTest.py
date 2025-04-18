# -*- coding: utf-8 -*-
import os

import google.cloud.texttospeech as tts
from google.cloud import texttospeech


def synthesize_text():
    """Synthesizes speech from the input string of text with proxy support."""

    # 프록시 설정
    os.environ["HTTP_PROXY"] = r'http://10.244.254.254:8080'
    os.environ["HTTPS_PROXY"] = r'http://10.244.254.254:8080'
    #
    os.environ['GRPC_DEFAULT_SSL_ROOTS_FILE_PATH'] = 'D:\cer_gumi.crt'
    os.environ['CURL_CA_BUNDLE'] = 'D:\cer_gumi.crt'

    client = tts.TextToSpeechClient()

    # 입력 텍스트
    text = "Hello there."
    input_text = texttospeech.SynthesisInput(text=text)

    # 음성 설정
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Standard-C",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
    )

    # 오디오 설정
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # API 요청
    response = client.synthesize_speech(
        request={"input": input_text, "voice": voice, "audio_config": audio_config}
    )

    # 결과 저장
    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')

# 함수 호출
synthesize_text()