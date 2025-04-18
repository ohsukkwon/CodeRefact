# -*- coding: utf-8 -*-
from dotenv import load_dotenv

from GlobalUtil import get_client_ai_gpt_gpt
from MyKeyStore import *

load_dotenv()

___access_key_id = keystore_get_key_type(argType=KEYTYPE_IDX_GPTScenario_OpenAI_NONE_NONE)

___prompt = """Act As Korean teacher.
경제 관련된 문장을 50글자 길이와 Korean문장으로 1개 만들어서, English 문법에 정확하게 맞도록 번역해줘.
출력 형식은 
"
input 1: ~~~.
output 1: ~~~.
" 
이렇게 표현해줘."""

client = get_client_ai_gpt_gpt()

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": ___prompt
        }
    ],
    model="gpt-4o-mini",
    temperature = 0,
    max_tokens = 100,
    top_p = 1,
    frequency_penalty = 0.0,
    presence_penalty = 0.0
)

print(chat_completion.choices[0].message)