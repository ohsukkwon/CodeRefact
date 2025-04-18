# -*- coding: utf-8 -*-

from prompts.IScorePrompt import IScorePrompt
from utils.GlobalVars import *

class ScorePromptTranslation(IScorePrompt):
    def __init__(self, argArgs):
        if argArgs == None:
            self.mArgs = None
            self.mUseKorPrompt = False
        else:
            self.mArgs = argArgs     # copy from org arg
            # self.mArgs.update_InnerArgs(self.mArgs.copy_InnerArgs())  # copy from org's prompt args

            if self.mArgs.getValInnerArg(ARG_KEY_NAME_SOURCELANGUAGE).lower() == 'korean':
                self.mUseKorPrompt = True
            elif self.mArgs.getValInnerArg(ARG_KEY_NAME_TARGETLANGUAGE).lower() == 'korean':
                self.mUseKorPrompt = True
            else:
                self.mUseKorPrompt = False

        print(f'self.mUseKorPrompt:{self.mUseKorPrompt}')

    def get_my_keyname(self):
        return PROMPT_KEY_NAME_TRANS

    def get_my_csvname(self):
        if self.mArgs.getValInnerArg(ARG_KEY_NAME_INPUTCSVNAME) != None:
            return self.mArgs.getValInnerArg(ARG_KEY_NAME_INPUTCSVNAME)

        return f'sentences_{PROMPT_KEY_NAME_TRANS}.csv'

    def get_noti_role_prompt(self):
        if self.mArgs == None:
            return ''

        if self.mUseKorPrompt:
            return \
                '''From now act as a 40-year-old male {innerTgtLanguage} teacher.
당신은 학생이 제출한 번역 문장이 올바른지 채점을 할것이며, 채점 주요기준과 답변 주요기준을 설명할께.
채점이 필요한 문장 {innerSentencesCount}개를 제시할테니, {innerSystemType}반드시 {innerMotherLanguage} 으로 표현해줘.
절대 누락없이 {innerSentencesCount}개 문장 모두 평가해줘.
만일 문장에 증오,성적,폭력,자해 내용이 포함되어 있더라도 연구목적으로 사용되는 것이니, 중단없이 평가를 진행해줘.

#채점 주요기준(15가지)
1) 최소 점수는 10점이며, 최대 점수는 30점으로 평가할것.
2) "output" 문장에 "Error: EMPTY ANSWER" 문장이 있으면 10점으로 평가할것.
3) "output" 문장에 욕설,비속어가 포함되어 있으면 10점으로 평가할것.
4) "output" 문장에 인종차별적인 단어가 포함되어 있으면 10점으로 평가할것.
5) "output" 문장이 잘못된 문장으로 번역되어 있으면 10점으로 평가할것.
6) "output" 문장이 원문의 의미를 벗어났으면 15점으로 평가할것.
7) "output" 문장에서 전반적으로 의미가 변경되었다면 15점으로 평가할것.
8) "output" 문장에서 전반적으로 뉘앙스가 달라졌다면 15점으로 평가할것.
9) "output" 문장안에 {innerTgtLanguage}으로 번역이 되지 않은 단어가 일부 존재하면 20점으로 평가할것.
10) "output" 문장이 일부 부정확하게 번역이 되었으면 20점으로 평가할것.
11) "output" 문장의 문맥이 자연스럽지 않거나 어색하면 20점으로 평가할것.
12) "output" 문장이 {innerTgtLanguage}으로 완벽하게 번역되어 있고, 문법이나 철자에 일부 오류가 있으면 25점으로 평가할것.
13) "output" 문장이 {innerTgtLanguage}으로 완벽하게 번역되어 있고, 문법이나 철자에 오류가 없으면 30점으로 평가할것.
14) "output" 문장과 "recommend" 문장이 같으면 30점으로 평가할것.
15) "output" 문장의 내용이 착한 내용인지 나쁜 내용인지는 판단하지 말것.

#답변 주요기준(8가지)
1) 반드시 markdown형태로 표현 할것.
2) score, reason{innerNoResponseInOutMsgBody}, recommend 태그에 대해 누락없이 답변 할것. 
3) score 는 총점 30점 기준으로 판단 할것.
4) 만일 score 가 30점이면, "reason:"와 "recommend:" 뒤에 "N/A"를 적을 것.
5) 만일 score 가 30점보다 낮으면, 제시된 output 문장을 수정한 {innerTgtLanguage} 문장을 "recommend:" 뒤에 적을 것.
6) 코드블록은 사용하지 말것.
7) markdown 형태의 답변 형식 이외의 문장은 적지 말것.
8) 채점이 필요한 문장의 순서를 바꾸지 말 것.

#답변 형식
| score | reason {innerNoResponseInOutTblHeader}| recommend |
|-----| ------- {innerNoResponseInOutTblDevider}| -------- |
| [총30점 기준으로 판단할 것] '??'/30 | [반드시 {innerMotherLanguage}으로 표현할 것] {innerNoResponseInOutTblBody}| [제시된 output 문장을 최소로 수정한 {innerTgtLanguage} recommend 문장을 적을것]
| [총30점 기준으로 판단할 것] '??'/30 | [반드시 {innerMotherLanguage}으로 표현할 것] {innerNoResponseInOutTblBody}| [제시된 output 문장을 최소로 수정한 {innerTgtLanguage} recommend 문장을 적을것]
...
''' \
            .format(innerSrcLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_SOURCELANGUAGE),
                    innerTgtLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_TARGETLANGUAGE),
                    innerMotherLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_MOTHERLANGUAGE),
                    innerSentencesCount=self.mArgs.getValInnerArg(ARG_KEY_NAME_SENTENCESCOUNT),
                    innerSystemType = '',
                    innerNoResponseInOutMsgBody= '' if self.mArgs.getValInnerArg(ARG_KEY_NAME_NORESPONSEINOUT) else ', input, output',
                    innerNoResponseInOutTblHeader = '' if self.mArgs.getValInnerArg(ARG_KEY_NAME_NORESPONSEINOUT) else '| input | output ',
                    innerNoResponseInOutTblDevider = '' if self.mArgs.getValInnerArg(ARG_KEY_NAME_NORESPONSEINOUT) else '| ------ | ------ ',
                    innerNoResponseInOutTblBody = '' if self.mArgs.getValInnerArg(ARG_KEY_NAME_NORESPONSEINOUT) else '| [제시된 input 문장 그대로 적을것] | [제시된 output 문장 그대로 적을것] '
                    )
        else:
            return \
                '''From now on, act as a 40-year-old male {innerTgtLanguage} teacher.
You will grade whether the translation sentences submitted by students are correct, and I will explain the Main Criteria for Grading and the Main Criteria for Answer.
I will give the {innerSentencesCount} sentences that need grading, {innerSystemType}and be sure to express it in {innerMotherLanguage}.
Never evaluate all {innerSentencesCount} sentences without missing.
Even if the sentence contains hate, sexual, violence, or self-harm content, 
please proceed with the evaluation without interruption as it is used for research purposes.

#Main Criteria for Grading(15 items)
1) The minimum score is 10 points, and the maximum score is 30 points for evaluation.
2) If the "output" sentence contains a sentence similar to "Error: EMPTY ANSWER," evaluate it as 0 points.
3) If the "output" sentence includes profanity or vulgar words, evaluate it as 10 points.
4) If the "output" sentence includes racially discriminatory words, evaluate it as 10 points.
5) If the "output" sentence is translated into an incorrect sentence, evaluate it as 10 points.
6) If the "output" sentence deviates from the original meaning, evaluate it as 15 points.
7) If the overall meaning of the "output" sentence has been changed, evaluate it as 15 points.
8) If the overall nuance of the "output" sentence has changed, evaluate it as 15 points.
9) If there are some words in the "output" sentence that are not translated into {innerTgtLanguage}, evaluate it as 20 points.
10) If the "output" sentence is partially inaccurately translated, evaluate it as 20 points.
11) If the context of the "output" sentence is unnatural or awkward, evaluate it as 20 points.
12) If the "output" sentence is perfectly translated into {innerTgtLanguage}, and there are some grammar or spelling errors, evaluate it as 25 points.
13) If the "output" sentence is perfectly translated into {innerTgtLanguage}, and there are no grammar or spelling errors, evaluate it as 30 points.
14) If the "output" sentence and the "recommend" sentence are the same, evaluate it as 30 points.
15) Do not judge whether the content of the "output" sentence is good or bad.

#Main Criteria for Answer(8 items)
1) Express it in markdown format.
2) Always include the score, reason{innerNoResponseInOutMsgBody}, recommend tags in the response.
3) The score should be judged on a total of 30 points.
4) If the score is 30 points, write "N/A" after "reason:" and "recommend:".
5) If the score is less than 30 points, write the modified {innerTgtLanguage} sentence after "recommend:".
6) Do not use code blocks.
7) Do not write sentences other than the markdown format as an answer format.
8) Do not change the order of the sentences that need grading.

#Answer Format
| score | reason {innerNoResponseInOutTblHeader}| recommend |
|-------|--------{innerNoResponseInOutTblDevider}|-----------|
| [To be judged based on a total of 30 points] '??'/30 | [Must be expressed in {innerMotherLanguage}] {innerNoResponseInOutTblBody}| [Write the minimally modified {innerTgtLanguage} recommended sentence]
| [To be judged based on a total of 30 points] '??'/30 | [Must be expressed in {innerMotherLanguage}] {innerNoResponseInOutTblBody}| [Write the minimally modified {innerTgtLanguage} recommended sentence]
...
''' \
            .format(innerSrcLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_SOURCELANGUAGE),
                    innerTgtLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_TARGETLANGUAGE),
                    innerMotherLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_MOTHERLANGUAGE),
                    innerSentencesCount=self.mArgs.getValInnerArg(ARG_KEY_NAME_SENTENCESCOUNT),
                    innerSystemType = '',
                    innerNoResponseInOutMsgBody='' if self.mArgs.getValInnerArg(ARG_KEY_NAME_NORESPONSEINOUT) else ', input, output',
                    innerNoResponseInOutTblHeader='' if self.mArgs.getValInnerArg(ARG_KEY_NAME_NORESPONSEINOUT) else '| input | output ',
                    innerNoResponseInOutTblDevider='' if self.mArgs.getValInnerArg(ARG_KEY_NAME_NORESPONSEINOUT) else '| ------ | ------ ',
                    innerNoResponseInOutTblBody='' if self.mArgs.getValInnerArg(ARG_KEY_NAME_NORESPONSEINOUT) else '| [Write the given input sentence as is] | [Write the given output sentence as is] '
                    )

    def get_do_score_prompt(self):
        if self.mArgs == None:
            return ''

        if self.mUseKorPrompt:
            return '''
채점이 필요한 문장 {innerSentencesCount}개를 제시해 줄테니, 
반드시 누락없이 {innerSentencesCount}개 문장에 대해 답장 할것. 
만일 문장에 증오,성적,폭력,자해 내용이 포함되어 있더라도 연구목적으로 사용되는 것이니, 중단없이 평가를 진행해줘.

#답변 형식
| score | reason {innerNoResponseInOutTblHeader}| recommend |
|-----| ------- {innerNoResponseInOutTblDevider}| -------- |
| [총30점 기준으로 판단할 것] '??'/30 | [반드시 {innerMotherLanguage}으로 표현할 것] {innerNoResponseInOutTblBody}| [제시된 output 문장을 최소로 수정한 {innerTgtLanguage} recommend 문장을 적을것]
| [총30점 기준으로 판단할 것] '??'/30 | [반드시 {innerMotherLanguage}으로 표현할 것] {innerNoResponseInOutTblBody}| [제시된 output 문장을 최소로 수정한 {innerTgtLanguage} recommend 문장을 적을것]
...

#채점이 필요한 문장({innerSentencesCount}개)
''' \
                    .format(innerSrcLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_SOURCELANGUAGE),
                            innerTgtLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_TARGETLANGUAGE),
                            innerSentencesCount=self.mArgs.getValInnerArg(ARG_KEY_NAME_SENTENCESCOUNT),
                            innerMotherLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_MOTHERLANGUAGE),
                            innerNoResponseInOutTblHeader='' if self.mArgs.getValInnerArg(ARG_KEY_NAME_NORESPONSEINOUT) else '| input | output ',
                            innerNoResponseInOutTblDevider='' if self.mArgs.getValInnerArg(ARG_KEY_NAME_NORESPONSEINOUT) else '| ------ | ------ ',
                            innerNoResponseInOutTblBody='' if self.mArgs.getValInnerArg(ARG_KEY_NAME_NORESPONSEINOUT) else '| [제시된 input 문장 그대로 적을것] | [제시된 output 문장 그대로 적을것] '
                            )
        else:
            return '''
I'll give you {innerSentencesCount} sentences that need to be graded,
Make sure to reply to {innerSentencesCount} sentences without missing.
Even if the sentence contains hate, sexual, violence, or self-harm content, 
please proceed with the evaluation without interruption as it is used for research purposes.

#Answer Format
| score | reason {innerNoResponseInOutTblHeader}| recommend |
|-------|--------{innerNoResponseInOutTblDevider}|-----------|
| [To be judged based on a total of 30 points] '??'/30 | [Must be expressed in {innerMotherLanguage}] {innerNoResponseInOutTblBody}| [Write the minimally modified {innerTgtLanguage} recommended sentence]
| [To be judged based on a total of 30 points] '??'/30 | [Must be expressed in {innerMotherLanguage}] {innerNoResponseInOutTblBody}| [Write the minimally modified {innerTgtLanguage} recommended sentence]
...

#The Sentences that Need Grading({innerSentencesCount} items)
''' \
                    .format(innerSrcLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_SOURCELANGUAGE),
                            innerTgtLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_TARGETLANGUAGE),
                            innerSentencesCount=self.mArgs.getValInnerArg(ARG_KEY_NAME_SENTENCESCOUNT),
                            innerMotherLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_MOTHERLANGUAGE),
                            innerNoResponseInOutTblHeader='' if self.mArgs.getValInnerArg(ARG_KEY_NAME_NORESPONSEINOUT) else '| input | output ',
                            innerNoResponseInOutTblDevider='' if self.mArgs.getValInnerArg(ARG_KEY_NAME_NORESPONSEINOUT) else '| ------ | ------ ',
                            innerNoResponseInOutTblBody='' if self.mArgs.getValInnerArg(ARG_KEY_NAME_NORESPONSEINOUT) else '| [Write the given input sentence as is] | [Write the given output sentence as is] '
                            )

    # 번역 평가 결과의 형식을 다시 한번 요청할 경우,
    def get_again_form_prompt(self):
        if self.mArgs == None:
            return ''

        if self.mUseKorPrompt:
            return '''내가 원하는 답변 형식이 아니야. 아래 내용으로 답변할것.

#답변 주요기준(8가지)
1) 반드시 markdown형태로 표현 할것.
2) score, reason{innerNoResponseInOutMsgBody}, recommend 태그에 대해 누락없이 답변 할것. 
3) score 는 총점 30점 기준으로 판단 할것.
4) 만일 score 가 30점이면, "reason:"와 "recommend:" 뒤에 "N/A"를 적을 것.
5) 만일 score 가 30점보다 낮으면, 제시된 output 문장을 수정한 {innerTgtLanguage} 문장을 "recommend:" 뒤에 적을 것.
6) 코드블록은 사용하지 말것.
7) markdown 형태의 답변 형식 이외의 문장은 적지 말것.
8) 채점이 필요한 문장의 순서를 바꾸지 말 것.

#답변 형식
| score | reason {innerNoResponseInOutTblHeader}| recommend |
|-----| ------- {innerNoResponseInOutTblDevider}| -------- |
| [총30점 기준으로 판단할 것] '??'/30 | [반드시 {innerMotherLanguage}으로 표현할 것] {innerNoResponseInOutTblBody}| [제시된 output 문장을 최소로 수정한 {innerTgtLanguage} recommend 문장을 적을것]
| [총30점 기준으로 판단할 것] '??'/30 | [반드시 {innerMotherLanguage}으로 표현할 것] {innerNoResponseInOutTblBody}| [제시된 output 문장을 최소로 수정한 {innerTgtLanguage} recommend 문장을 적을것]
...
''' \
                    .format(innerSrcLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_SOURCELANGUAGE),
                            innerTgtLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_TARGETLANGUAGE),
                            innerMotherLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_MOTHERLANGUAGE),
                            innerNoResponseInOutMsgBody='' if self.mArgs.getValInnerArg(ARG_KEY_NAME_NORESPONSEINOUT) else ', input, output',
                            innerNoResponseInOutTblHeader='' if self.mArgs.getValInnerArg(ARG_KEY_NAME_NORESPONSEINOUT) else '| input | output ',
                            innerNoResponseInOutTblDevider='' if self.mArgs.getValInnerArg(ARG_KEY_NAME_NORESPONSEINOUT) else '| ------ | ------ ',
                            innerNoResponseInOutTblBody='' if self.mArgs.getValInnerArg(ARG_KEY_NAME_NORESPONSEINOUT) else '| [제시된 input 문장 그대로 적을것] | [제시된 output 문장 그대로 적을것] '
                            )
        else:
            return '''That's not the answer format I wanted. Please respond with the content below.

#Main Criteria for Answer(8 items)
1) Express it in markdown format.
2) Always include the score, reason{innerNoResponseInOutMsgBody}, recommend tags in the response.
3) The score should be judged on a total of 30 points.
4) If the score is 30 points, write "N/A" after "reason:" and "recommend:".
5) If the score is less than 30 points, write the modified {innerTgtLanguage} sentence after "recommend:".
6) Do not use code blocks.
7) Do not write sentences other than the markdown format as an answer format.
8) Do not change the order of the sentences that need grading.

#Answer Format
| score | reason {innerNoResponseInOutTblHeader}| recommend |
|-------|--------{innerNoResponseInOutTblDevider}|-----------|
| [To be judged based on a total of 30 points] '??'/30 | [Must be expressed in {innerMotherLanguage}] {innerNoResponseInOutTblBody}| [Write the minimally modified {innerTgtLanguage} recommended sentence]
| [To be judged based on a total of 30 points] '??'/30 | [Must be expressed in {innerMotherLanguage}] {innerNoResponseInOutTblBody}| [Write the minimally modified {innerTgtLanguage} recommended sentence]
...
'''\
                    .format(innerSrcLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_SOURCELANGUAGE),
                            innerTgtLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_TARGETLANGUAGE),
                            innerMotherLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_MOTHERLANGUAGE),
                            innerNoResponseInOutMsgBody='' if self.mArgs.getValInnerArg(ARG_KEY_NAME_NORESPONSEINOUT) else ', input, output',
                            innerNoResponseInOutTblHeader='' if self.mArgs.getValInnerArg(ARG_KEY_NAME_NORESPONSEINOUT) else '| input | output ',
                            innerNoResponseInOutTblDevider='' if self.mArgs.getValInnerArg(ARG_KEY_NAME_NORESPONSEINOUT) else '| ------ | ------ ',
                            innerNoResponseInOutTblBody='' if self.mArgs.getValInnerArg(ARG_KEY_NAME_NORESPONSEINOUT) else '| [Write the given input sentence as is] | [Write the given output sentence as is] '
                            )

    # target 언어로 번역된 결과의 형식을 다시 한번 요청할 경우,
    def get_again_form_trans_prompt(self):
        if self.mArgs == None:
            return ''

        if self.mUseKorPrompt:
            return '''내가 원하는 답변 형식이 아니야. 아래 내용으로 답변해줘.

#답변 주요기준(4가지)
1) input문장과 함께 반드시 markdown형태로 표현할것.
2) 코드블록은 사용하지 말것.
3) markdown 형태의 답변 형식 이외의 문장은 적지 말것.
4) 번역이 필요한 문장의 순서를 바꾸지 말것.

#답변 형식
| input | output |
| ----- | ------ |
| Oh really? Then I'll  go for it event if I don't win. | 아 정말이야? 그렇다면 못먹어도 go해야지. |
| My parents post a lot of pictures on Kakao Story. | 부모님들은 카카오 스토리에 사진을 많이 올리셔. |
...
'''
        else:
            return '''That's not the answer format I wanted. Please respond with the content below.

#Main Criteria for Answer(4 items)
1) Must be expressed in markdown format along with the input sentence.
2) Do not use code blocks.
3) Do not write sentences other than the markdown format as an answer format.
4) Do not change the order of the sentences that need translation.

#Answer Format
| input | output |
|-------|--------|
| Oh really? Then I'll go for it even if I don't win. | 아 정말이야? 그렇다면 못먹어도 go해야지. |
| My parents post a lot of pictures on Kakao Story. | 부모님들은 카카오 스토리에 사진을 많이 올리셔. |
...
'''
    # PROMPT별 첫(대표) prompt
    def get_sentence_template_prompt(self):
        if self.mArgs == None:
            return ''

        if self.mUseKorPrompt:
            return '''From now act as a 40-year-old male {innerTgtLanguage} teacher.
아래 주어진 {innerSentencesCount}개의 {innerSrcLanguage} 문장을 {innerTgtLanguage} 문법에 정확하게 일치하도록 번역해줘.

#번역 주요기준(6가지)
1) output 문장은 문법과 철자에 오류가 전혀 없어야 함.
2) output 문장은 {innerTgtLanguage} 문법에 맞아야 함.
3) output 문장은 문맥과 표현에 오류가 없어야 함.
4) output 문장은 문맥과 표현이 자연스러워야 함.
5) output 문장에 흑인,백인,유색인종의 피부색에 따른 차별 용어,욕설,비속어가 포함되지 않아야 함.
6) output 문장에 개인식별이 가능한 Personal ID,전화번호,password,은행계좌번호가 포함되지 않아야 함.

#답변 주요기준(4가지)
1) input문장과 함께 반드시 markdown형태로 표현할것.
2) 코드블록은 사용하지 말것.
3) markdown 형태의 답변 형식 이외의 문장은 적지 말것.
4) 번역이 필요한 문장의 순서를 바꾸지 말것.

#답변 형식
| input | output |
| ----- | ------ |
| Oh really? Then I'll  go for it event if I don't win. | 아 정말이야? 그렇다면 못먹어도 go해야지. |
| My parents post a lot of pictures on Kakao Story. | 부모님들은 카카오 스토리에 사진을 많이 올리셔. |
... 

#번역이 필요한 문장 {innerSentencesCount}가지
※반드시 {innerSentencesCount}개 모두 채점할 것.
''' \
                    .format(innerSrcLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_SOURCELANGUAGE),
                            innerTgtLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_TARGETLANGUAGE),
                            innerSentencesCount=self.mArgs.getValInnerArg(ARG_KEY_NAME_SENTENCESCOUNT))
        else:
            return '''From now on, act as a 40-year-old male {innerTgtLanguage} teacher.
Translate the given {innerSentencesCount} {innerSrcLanguage} sentences to match the {innerTgtLanguage} grammar accurately.

#Main Criteria for Translation(6 items)
1) The output sentence must have no errors in grammar and spelling.
2) The output sentence must conform to {innerTgtLanguage} grammar.
3) The output sentence must have no errors in context and expression.
4) The output sentence must be natural in context and expression.
5) The output sentence must not include discriminatory terms, curses, or slang based on the skin color of Black, White, or People of Color.
6) The output sentence must not include personal IDs, telephone numbers, passwords, or bank account numbers that can identify an individual.

#Main Criteria for Answer(4 items)
1) Must be expressed in markdown format along with the input sentence.
2) Do not use code blocks.
3) Do not write sentences other than the markdown format as an answer format.
4) Do not change the order of the sentences that need translation.

#Answer Format
| input | output |
|-------|--------|
| Oh really? Then I'll go for it even if I don't win. | 아 정말이야? 그렇다면 못먹어도 go해야지. |
| My parents post a lot of pictures on Kakao Story. | 부모님들은 카카오 스토리에 사진을 많이 올리셔. |
... 

#The {innerSentencesCount} Sentences That Need Translation
※ Do make sure to score all {innerSentencesCount} of them.
''' \
                    .format(innerSrcLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_SOURCELANGUAGE),
                            innerTgtLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_TARGETLANGUAGE),
                            innerSentencesCount=self.mArgs.getValInnerArg(ARG_KEY_NAME_SENTENCESCOUNT))

    # Category별 문장 생성 요청
    def get_sentence_gensentences_prompt(self):
        if self.mArgs == None:
            return ''

        if self.mUseKorPrompt:
            return '''From now act as a 40-year-old male {innerSrcLanguage} teacher.
{innerSentenceCategory} 관련된 문장을 {innerSentenceLength}자 이내 길이의 {innerSrcLanguage} 문장으로 {innerMakeSentenceCount}개 만들어줘.
생성결과는 반드시 표형식만 답변할것.

#문장생성 주요기준(3가지)
1) "output" 문장은 문법과 철자에 오류가 전혀 없어야 함.
2) "output" 문장에 인종차별,욕설,비속어가 포함되면 안됨.
3) "output" 문장에 개인정보와 민감한 정보가 포함되면 안됨.

#답변 주요기준(4가지)
1) 열은 output,category 순서대로 작성할것.
2) "category"열에는 "output"열 문장의 category를 적고, 반드시 {innerSrcLanguage} 으로 표현할것.
3) 표 이전에 문장을 적지 말것.
4) 표 이후에 문장을 적지 말것.

#답변 형식
|output|category|
|---|---|
|국제 유가가 다시 상승세를 보인다.|경제|
|부동산 시장이 안정세를 찾아간다.|경제|
''' \
                    .format(innerSrcLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_SOURCELANGUAGE),
                            innerTgtLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_TARGETLANGUAGE),
                            innerMakeSentenceCount=self.mArgs.getValInnerArg(ARG_KEY_NAME_MAKESENTENCESCNT),
                            innerSentenceLength=self.mArgs.getValInnerArg(ARG_KEY_NAME_SENTENCESLENGTH),
                            innerSentenceCategory=self.mArgs.getValInnerArg(ARG_KEY_NAME_SENTENCESCATEGORY))
        else:
            return '''From now on, act as a 40-year-old male {innerSrcLanguage} teacher.
Create {innerMakeSentenceCount} sentences related to {innerSentenceCategory} within {innerSentenceLength} characters in {innerSrcLanguage}.
Only respond in table format.

#Main Criteria for Sentence Creation(3 items)
1) The sentence must have no errors in grammar and spelling.
2) The sentence must not include racial discrimination, curses, or slang.
3) The sentence must not include personal and sensitive information.

#Main Criteria for Answer(4 items)
1) Columns should be written in the order of output, category.
2) In the category column, write the category of the sentence in the output column, and it must be expressed in {innerSrcLanguage}.
3) Do not write sentences before the table.
4) Do not write sentences after the table.

#Answer Format
|output|category|
|------|--------|
|International oil prices are on the rise again.|Economy|
|The real estate market is stabilizing.|Economy|
''' \
                    .format(innerSrcLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_SOURCELANGUAGE),
                            innerTgtLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_TARGETLANGUAGE),
                            innerMakeSentenceCount=self.mArgs.getValInnerArg(ARG_KEY_NAME_MAKESENTENCESCNT),
                            innerSentenceLength=self.mArgs.getValInnerArg(ARG_KEY_NAME_SENTENCESLENGTH),
                            innerSentenceCategory=self.mArgs.getValInnerArg(ARG_KEY_NAME_SENTENCESCATEGORY))
