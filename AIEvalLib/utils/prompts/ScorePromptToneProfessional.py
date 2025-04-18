# -*- coding: utf-8 -*-
import copy

from prompts.IScorePrompt import IScorePrompt
from utils.GlobalVars import *


class ScorePromptToneProfessional(IScorePrompt):
    def __init__(self, argArgs):
        if argArgs == None:
            self.mArgs = None
        else:
            self.mArgs = copy.copy(argArgs)  # copy from org arg
            self.mArgs.update_InnerArgs(self.mArgs.copy_InnerArgs())  # copy from org's prompt args

    def get_my_keyname(self):
        return PROMPT_KEY_NAME_TONEPROFESSIONAL

    def get_my_csvname(self):
        if self.mArgs.getValInnerArg(ARG_KEY_NAME_INPUTCSVNAME) != None:
            return self.mArgs.getValInnerArg(ARG_KEY_NAME_INPUTCSVNAME)

        return f'sentences_{PROMPT_KEY_NAME_TONEPROFESSIONAL}.csv'

    def get_noti_role_prompt(self):
        if self.mArgs == None:
            return ''

        return \
            '''From now act as a 40-year-old male {innerTgtLanguage} teacher.
당신은 학생이 제출한 Professional 톤변경 문장이 올바른지 채점을 할것이며, 판단기준을 설명할께.
채점이 필요한 문장을 제시해 줄테니, 아직 채점은 시작하지 말고, 채점 준비되면 알려줘. 반드시 {innerMotherLanguage} 으로 표현해줘.

#채점 주요기준 7가지
1) 주어진 output 문장에 철자가 틀린 단어가 있으면, 20점보다 낮은 점수로 판단할것.
2) 주어진 output 문장이 {innerTgtLanguage} 에 맞게 완벽하게 professional 톤변경되어 있지 않으면, 20점보다 낮은 점수로 판단할것.
3) 주어진 output 문장이 {innerTgtLanguage} 문법에 맞지 않으면, 20점보다 낮은 점수로 판단할것.
4) input 문장의 의미가 output 문장에서 변경되었다면, 15점보다 낮은 점수로 판단할것.
5) 주어진 output 문장의 문맥에 오류가 있으면, 15점보다 낮은 점수로 판단할것.
6) 주어진 output 문장의 문맥이 부자연스러우면, 15점보다 낮은 점수로 판단할것.
7) 주어진 output 문장이 착하거나 나쁜 내용에 대해서는 판단하지 말것.

#답변 주요형식 8가지
1) 반드시 markdown형태로 표현 할 것.
2) result, reason, original input, original output, recommend 태그에 대해 누락없이 답변 할 것. 
3) result 점수는 총점 30점 기준으로 판단 할 것.
4) 만일 result 점수가 30점이면, recommend : 뒤에 "N/A"를 적을 것.
5) 만일 result 점수가 30점보다 낮으면, 제시된 output 문장을 수정한 {innerTgtLanguage} 문장을 recommend : 뒤에 적을 것.
6) 검은색 테이블은 사용하지 말 것.
7) markdown 형태의 답변 형식 이외의 문장은 적지 말것.
8) 채점이 필요한 문장의 순서를 바꾸지 말 것.

#답변 형식
| 점수 | reason | input | output | recommend |
|-----| ------- | ------ | ------ | -------- |
| [총30점 기준으로 판단할것] 총30점중 ??점 | [반드시 {innerMotherLanguage}으로 표현할것] | [제시된 input 문장 그대로 적을것] | [제시된 output 문장 그대로 적을것] | [제시된 output 문장을 최소로 수정한 {innerTgtLanguage} recommend 문장만 적을것]
| [총30점 기준으로 판단할것] 총30점중 ??점 | [반드시 {innerMotherLanguage}으로 표현할것] | [제시된 input 문장 그대로 적을것] | [제시된 output 문장 그대로 적을것] | [제시된 output 문장을 최소로 수정한 {innerTgtLanguage} recommend 문장만 적을것]
...

평가의 정확도를 높이기 위해 더 자연스러운 문장 2개를 제시해 줄테니, 참조해서 평가해줘.
| input | output |
| ----- | ------ |
| 아쉽긴 한데, 여행 때문에 어쩔 수 없어. | 유감스럽지만 여행 일정 때문에 어쩔 수 없습니다. |
| 우리 거기서 연극 보기로 했잖아. 왜 갑자기 장소를 바꾸려고 해? | 우리는 거기서 연극을 보기로 했습니다. 왜 갑자기 장소를 바꾸려고 합니까? |
''' \
        .format( innerSrcLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_SOURCELANGUAGE),
                 innerTgtLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_TARGETLANGUAGE),
                 innerMotherLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_MOTHERLANGUAGE))

    def get_do_score_prompt(self):
        if self.mArgs == None:
            return ''

        return \
'''#지시사항
아래에 제시된 문장들은 input 문장을 output 문장으로 professional 톤변경한 결과야.
톤변경된 output 문장을 위의 판단기준에 따라 총점 30점 기준으로 채점하고, 점수와 reason 을 알려주고, reason 은 반드시 {innerTgtLanguage} 으로 표현해줘.
만일 result 점수가 30점보다 낮으면, output 문장에 대한 수정문장을 recommend 해줘.
답변은 아래의 답변형식에 따라 작성해줘.

#답변 주요형식 8가지
1) 반드시 markdown형태로 표현 할것.
2) result, reason, original input, original output, recommend 태그에 대해 누락없이 답변 할것. 
3) result 점수는 총점 30점 기준으로 판단 할것.
4) 만일 result 점수가 30점이면, recommend : 뒤에 "N/A"를 적을 것.
5) 만일 result 점수가 30점보다 낮으면, 제시된 output 문장을 수정한 {innerTgtLanguage} 문장을 recommend : 뒤에 적을 것.
6) 검은색 테이블은 사용하지 말것.
7) markdown 형태의 답변 형식 이외의 문장은 적지 말것.
8) 채점이 필요한 문장의 순서를 바꾸지 말 것.

#답변 형식
| 점수 | reason | input | output | recommend |
|-----| ------- | ------ | ------ | -------- |
| [총30점 기준으로 판단할것] 총30점중 ??점 | [반드시 {innerMotherLanguage}으로 표현할것] | [제시된 input 문장 그대로 적을것] | [제시된 output 문장 그대로 적을것] | [제시된 output 문장을 최소로 수정한 {innerTgtLanguage} recommend 문장만 적을것]
| [총30점 기준으로 판단할것] 총30점중 ??점 | [반드시 {innerMotherLanguage}으로 표현할것] | [제시된 input 문장 그대로 적을것] | [제시된 output 문장 그대로 적을것] | [제시된 output 문장을 최소로 수정한 {innerTgtLanguage} recommend 문장만 적을것]
...

#채점이 필요한 문장 {innerSentencesCount}가지
''' \
    .format(innerSrcLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_SOURCELANGUAGE),
            innerTgtLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_TARGETLANGUAGE),
            innerSentencesCount=self.mArgs.getValInnerArg(ARG_KEY_NAME_SENTENCESCOUNT),
            innerMotherLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_MOTHERLANGUAGE))

    def get_again_form_prompt(self):
        if self.mArgs == None:
            return ''

        return \
'''내가 원하는 답변 형식이 아니야. 아래 내용으로 답변해줘.

#답변 주요형식 8가지
1) 반드시 markdown형태로 표현 할것.
2) result, reason, original input, original output, recommend 태그에 대해 누락없이 답변 할것. 
3) result 점수는 총점 30점 기준으로 판단 할것.
4) 만일 result 점수가 30점이면, recommend : 뒤에 "N/A"를 적을 것.
5) 만일 result 점수가 30점보다 낮으면, 제시된 output 문장을 수정한 {innerTgtLanguage} 문장을 recommend : 뒤에 적을 것.
6) 검은색 테이블은 사용하지 말것.
7) markdown 형태의 답변 형식 이외의 문장은 적지 말것.
8) 채점이 필요한 문장의 순서를 바꾸지 말 것.

#답변 형식
| 점수 | reason | input | output | recommend |
|-----| ------- | ------ | ------ | -------- |
| [총30점 기준으로 판단할것] 총30점중 ??점 | [반드시 {innerMotherLanguage}으로 표현할것] | [제시된 input 문장 그대로 적을것] | [제시된 output 문장 그대로 적을것] | [제시된 output 문장을 최소로 수정한 {innerTgtLanguage} recommend 문장만 적을것]
| [총30점 기준으로 판단할것] 총30점중 ??점 | [반드시 {innerMotherLanguage}으로 표현할것] | [제시된 input 문장 그대로 적을것] | [제시된 output 문장 그대로 적을것] | [제시된 output 문장을 최소로 수정한 {innerTgtLanguage} recommend 문장만 적을것]
... 
''' \
    .format(innerSrcLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_SOURCELANGUAGE),
            innerTgtLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_TARGETLANGUAGE),
            innerMotherLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_MOTHERLANGUAGE))

    def get_sentence_template_prompt(self):
        if self.mArgs == None:
            return ''

        return \
        '''너는 {innerTgtLanguage} 선생님이야.
아래 주어진 {innerSentenceCount}개의 {innerSrcLanguage} 문장을 Professional톤으로 변경해줘.

# 주요기준 6가지
아래 내용에 해당하지 않는 문장으로 작성해줘.
1) 문장에 철자가 틀린 단어가 전혀 없어야 함.
2) 문장은 {innerTgtLanguage} 문법에 맞아야 함.
3) 문맥과 표현에 오류가 없어야 함.
4) 문맥과 표현이 자연스러워야 함.
5) 문장에 흑인,백인,유색인종의 피부색에 따른 차별 용어,욕설,비속어가 포함되지 않아야 함.
6) 문장에 개인식별이 가능한 Personal ID,전화번호,password,은행계좌번호가 포함되지 않아야 함.

#답변 주요형식 4가지
1) input문장과 함께 markdown형태로 표현할 것.
2) 검은색 테이블은 사용하지 말것.
3) markdown 형태의 답변 형식 이외의 문장은 적지 말것.
4) 번역이 필요한 문장의 순서를 바꾸지 말 것.

#답변 예시
| input | output |
| ----- | ------ |
| 아쉽긴 한데, 여행 때문에 어쩔 수 없어. | 유감스럽지만 여행 일정 때문에 어쩔 수 없습니다. |
| 우리 거기서 연극 보기로 했잖아. 왜 갑자기 장소를 바꾸려고 해? | 우리는 거기서 연극을 보기로 했습니다. 왜 갑자기 장소를 바꾸려고 합니까? |... 

#톤변경이 필요한 문장 {innerSentenceCount}가지
''' \
            .format(innerSrcLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_SOURCELANGUAGE),
                    innerTgtLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_TARGETLANGUAGE),
                    innerSentenceCount=self.mArgs.getValInnerArg(ARG_KEY_NAME_SENTENCESCOUNT))
