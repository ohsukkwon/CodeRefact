# -*- coding: utf-8 -*-
from typing import List

from pydantic import BaseModel

from GlobalUtil import get_client_ai_gpt_gpt

___prompt = """Act As Korean teacher.
경제 관련된 문장을 50글자 길이와 Korean문장으로 1개 만들어서, English 문법에 정확하게 맞도록 번역해줘.
출력 형식은 
"
input 1: ~~~.
output 1: ~~~.
" 
이렇게 표현해줘."""

client = get_client_ai_gpt_gpt()

class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: List[str]

    def __str__(self) -> str:
        retStr = f'name: {self.name}, date: {self.date}, participants: {self.participants}'
        return retStr

completion = client.beta.chat.completions.parse(
    model="gpt-4o-2024-08-06",
    messages=[
        {"role": "system", "content": "Extract the event information."},
        {"role": "user", "content": "Alice and Bob are going to a science fair on Friday."},
    ],
    response_format=CalendarEvent,
)

event = completion.choices[0].message.parsed

print(event)