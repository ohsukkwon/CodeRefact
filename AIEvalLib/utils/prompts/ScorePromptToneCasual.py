# -*- coding: utf-8 -*-
import copy

from prompts.IScorePrompt import IScorePrompt
from utils.GlobalVars import *


class ScorePromptToneCasual(IScorePrompt):
    def __init__(self, argArgs):
        if argArgs == None:
            self.mArgs = None
        else:
            self.mArgs = copy.copy(argArgs)  # copy from org arg
            self.mArgs.update_InnerArgs(self.mArgs.copy_InnerArgs())  # copy from org's prompt args

    def get_my_keyname(self):
        return PROMPT_KEY_NAME_TONECASUAL

    def get_my_csvname(self):
        if self.mArgs.getValInnerArg(ARG_KEY_NAME_INPUTCSVNAME) != None:
            return self.mArgs.getValInnerArg(ARG_KEY_NAME_INPUTCSVNAME)

        return f'sentences_{PROMPT_KEY_NAME_TONECASUAL}.csv'

    def get_noti_role_prompt(self):
        if self.mArgs == None:
            return ''

        return \
            '''# 지시사항
당신은 {innerSrcLanguage} 선생님이야. 
input이 캐주얼한 비격식체 대화톤으로 문장이 적절하게 변경되었는지 판단 기준에 근거하여 채점할 거야.
채점이 필요한 문장을 제시해 줄테니, 아직 채점은 시작하지 말고, 채점 준비되면 알려줘. 반드시 {innerMotherLanguage} 으로 표현해줘.

#채점 주요기준 6가지
1) input과 output의 문장이 완전히 일치한다면, 10점으로 판단할 것.
2) output이 {innerSrcLanguage} 문법에 맞지 않다면, 15점 보다 낮은 점수로 판단할 것.
3) output의 문맥이 부자연스럽거나 오류가 있으면, 15점보다 낮은 점수로 판단할 것.
4) output이 input과 의미가 같지 않다면, 15점보다 낮은 점수로 판단할 것.
5) output문장 내에 격식체와 비격식체가 혼재해 있다면, 20점 보다 낮은 점수로 판단할 것.
6) output이 input을 캐주얼한 톤으로 변경한 형태로써 적절하지 않다면, 20점보다 낮은 점수로 판단할 것.


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
| 저도 아쉽지만, 여행 때문에 어쩔 수가 없습니다. | 아쉽지만 여행 때문에 어쩔 수 없어. |
| 우리 거기서 연극 보기로 약속했잖아요. 왜 갑자기 장소를 바꾸려고 하세요? | 우리 거기서 연극 보기로 약속했잖아. 왜 갑자기 장소를 바꾸려고 해? |
''' \
        .format( innerSrcLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_SOURCELANGUAGE),
                 innerTgtLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_TARGETLANGUAGE),
                 innerMotherLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_MOTHERLANGUAGE))

    def get_do_score_prompt(self):
        if self.mArgs == None:
            return ''

        return \
'''당신은 학생이 제출한 아래 문장에 대해서 총30점 기준으로 평가하고, 점수와 reason을 알려주고, reason 은 반드시 {innerMotherLanguage}으로 표현해줘.
만일 result 점수가 30점보다 낮으면, 제시된 output 문장을 최소로 수정한 {innerTgtLanguage} 문장만 recommend 해줘.

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
아래 주어진 {innerSentenceCount}개의 {innerSrcLanguage} 문장을 캐주얼한 비격식체 대화톤으로 문장으로 변경해줘.

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
| 저도 아쉽지만, 여행 때문에 어쩔 수가 없습니다. | 아쉽지만 여행 때문에 어쩔 수 없어. |
| 우리 거기서 연극 보기로 약속했잖아요. 왜 갑자기 장소를 바꾸려고 하세요? | 우리 거기서 연극 보기로 약속했잖아. 왜 갑자기 장소를 바꾸려고 해? |
... 

#톤변경이 필요한 문장 {innerSentenceCount}가지
''' \
            .format(innerSrcLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_SOURCELANGUAGE),
                    innerTgtLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_TARGETLANGUAGE),
                    innerSentenceCount=self.mArgs.getValInnerArg(ARG_KEY_NAME_SENTENCESCOUNT))
