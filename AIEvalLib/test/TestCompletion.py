# -*- coding: utf-8 -*-

from pydantic import BaseModel
from openai import OpenAI, AzureOpenAI

client = OpenAI()
# client = AzureOpenAI(
#     azure_endpoint = "https://se-sqe-03.openai.azure.com/",
#     azure_deployment="SE-SQE-03-o1",
#     api_key="1VW3ftR1OM6WYLJuvqi4obH2wkvPqGMAhIWb2MlwLRkwmbWwp5EDJQQJ99BCACfhMk5XJ3w3AAABACOGmGvZ",
#     api_version="2024-12-01-preview")

class Step(BaseModel):
    explanation: str
    output: str

    def dispMe(self, prefix: str) -> str:
        retStr : str
        retStr = f"[{prefix}] : {self.__str__()}"
        retStr = retStr.replace(r'\\', "")
        return retStr

    def __str__(self) -> str:
        retStr : str

        retStr = f'{{'
        retStr = f'{retStr}#step.explanation → {self.explanation}'
        retStr = f'{retStr}||'
        retStr = f'{retStr}#step.output → {self.output}'
        retStr = f'{retStr}}}'

        return retStr


class MathReasoning(BaseModel):
    steps: list[Step]
    final_answer: str

    def __str__(self):
        retStr : str = ''
        idx : int = 0

        for step in self.steps:
            retStr = f'{retStr}{step.dispMe(str(idx))}'
            idx += 1
            if idx < len(self.steps):
                retStr = f'{retStr}\n'

        return retStr

if __name__ == '__main__':
    completion = client.beta.chat.completions.parse(
        model="o1",
        messages=[
            {"role": "system", "content": "You are a helpful math tutor. Guide the user through the solution step by step. 답변은 한글로 할것."},
            {"role": "user", "content": "how can I solve 8x + 7 = -23"}
        ],
        response_format=MathReasoning,
    )

    math_reasoning = completion.choices[0].message.parsed

    print('-' * 50)
    print(math_reasoning)
    print('=' * 50)