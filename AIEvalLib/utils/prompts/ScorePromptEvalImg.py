# -*- coding: utf-8 -*-
from GlobalVars import *
from prompts.IScorePrompt import IScorePrompt

class ScorePromptEvalImg(IScorePrompt):
    def __init__(self, argArgs):
        if argArgs is None:
            self.mArgs = None
            self.mUseKorPrompt = False
        else:
            self.mArgs = argArgs     # copy from org arg
            # self.mArgs.update_InnerArgs(self.mArgs.copy_InnerArgs())  # copy from org's prompt args

            if self.mArgs.getValInnerArg(ARG_KEY_NAME_MOTHERLANGUAGE).lower().startswith('ko_'):
                self.mUseKorPrompt = True
            elif self.mArgs.getValInnerArg(ARG_KEY_NAME_MOTHERLANGUAGE).lower() == 'korean':
                self.mUseKorPrompt = True
            else:
                self.mUseKorPrompt = False

        print(f'self.mUseKorPrompt:{self.mUseKorPrompt}')

    def get_my_keyname(self):
        return PROMPT_KEY_NAME_EVALIMG

    def get_my_csvname(self):
        if self.mArgs.getValInnerArg(ARG_KEY_NAME_INPUTCSVNAME) is not None:
            return self.mArgs.getValInnerArg(ARG_KEY_NAME_INPUTCSVNAME)

        return f'{PROMPT_KEY_NAME_EVALIMG}.csv'

    def get_noti_role_prompt(self):
        __PROMPT_EXTRA_CRITERIONS: str = \
            '''9. 프롬프트를 모두 정확하게 반영하였다면, Original image의 일부가 변경되거나 누락되었더라도 감점하지 말것.
10. 프롬프트를 모두 정확하게 반영하였다면, 원본이 크게 변화되지 않았더라도 감점하지 말것.''' \
                if self.mUseKorPrompt else \
                '''9. 프롬프트를 모두 정확하게 반영하였다면, Original image의 일부가 변경되거나 누락되었더라도 감점하지 말것.
10. 프롬프트를 모두 정확하게 반영하였다면, 원본이 크게 변화되지 않았더라도 감점하지 말것.'''

        if self.mArgs is None:
            return ''

        if self.mUseKorPrompt:
            return ('''당신은 지금부터 주어진 이미지가 Extra prompt와 Style을 정확하게 반영하여, 생성 되었는지를 Score로 판단하는 전문 판정위원 이야.
아래 "# 평가기준"을 정확하게 반영하여 평가해줘.
답변은 반드시 아래 "# 출력양식(예시)"을 지켜서 답변해줘.

# 평가기준
1. Score는 30점 만점이며, 25/20/15/10 단위로 평가할것. 
2. Extra prompt 반영여부는 점수에 80%반영하고, Style은 20%를 점수에 반영할것.
3. Extra prompt와 Style이 모두 정확하게 반영되었다면, 30점의 높은 점수를 부여할것.(30점)
4. Extra prompt가 부분적으로 누락되었더라도 전반적으로 반영되고, Style도 정확하게 반영되었으면 25점으로 부분 감점할것.(25점)
5. Extra prompt가 부분적으로 누락되었더라도 전반적으로 반영되고, Style이 정확하게 반영되지 않았으면 20점으로 부분 감점할것.(20점)
6. Extra prompt가 반영되지 않고, Style이 정확하게 반영되었으면 15점으로 부분 감점할것.(15점)
7. Extra prompt가 전혀 반영되지 않고, Style도 정확하게 반영되지 않았으면 10점으로 낮게 평가할것.(10점)
8. Score가 30점이면 "Reason"열에 "만점"으로만 표시하고, 만일 Score가 30점보다 적을 경우, 감점된 이유를 상세하게 "Reason"열에 적을것.
{inner_extra_criterions}

#  감정과 이미지의 표현관계
1. 행복, 기쁨, 사랑 : 꽃, 태양, 웃음, 하트 등의 이미지
2. 슬픔, 눈물 : 물방울 이미지
3. 짜증, 화남 : 눈썹이 올라간 표정, 천둥, 번개, 폭탄, 불 등의 이미지
4. 침울, 절망, 실망, 우울, 기운빠짐, 허탈 ,무너짐 : 축 처지거나 늘어진 모습, 전체적으로 회색톤의 어두운 이미지

# 출력양식(예시)
"No"열에는 주어된 No를 그대로 적을것.
"Score"열에는 Generated image가 "# 평가기준"을 반영하여 제대로 생성되었는지 여부를 점수로 판단할것.
"Reason"열에는 "Score"가 30점이 아닐 경우, 감점된 이유를 반드시 {innerMotherLanguage}언어로 상세하게 적고, 반영된 Extra prompt와 반영되지 않은 Extra prompt를 구분하여 적을것.
"Caption"열에는 앞부분에 전달된 Generated image의 파일명을 적은뒤 #을 붙일것. 그 다음에는 오직 Generated image의 객체들에 대해서 caption을 작성할것.
"Caption"내용은 시각 장애인의 이해를 돕기 위한 상세 설명이 필요하며, 그림을 보지 않은 사람에게 설명하듯이, "No"열에서 주어진 Generated image의 모든 객체에 대해서 정확하고 상세하게 묘사할것.({innerMotherLanguage}언어로 작성할것.)
아래와 같이 Header열이 포함된 MarkDown 테이블로만 답변할것.

|No|Score|Reason|Caption|
|---|---|---|---|
|1|30|만점|[각 No 1 에 일치되는 Generated image의 모든 객체에 대해 상세하게 표현할것]aaa.jpg#멋진 오로라가 있는 겨울 풍경을 보여줍니다. 밤하늘에 푸르스름한 빛이 흐르고, 반짝이는 별들이 보입니다. 하늘은 푸른색과 보라색으로 물들어 있으며, 땅에는 눈이 덮여 있습니다. 강물이 장면을 반사하여 환상적인 분위기를 더합니다. 주위의 침엽수림이 그림에 깊이감을 더해 주며, 자연의 평온함을 느낄 수 있습니다.|
|2|25|"행복해서 울고 싶어"라는 감정이 잘 반영되었으나, 물방울 이미지가 웃고 있어 슬픔의 느낌이 덜 표현됨.|[각 No 2 에 일치되는 Generated image의 모든 객체에 대해 상세하게 표현할것]bbb.jpg#물방울 모양에 귀여운 얼굴이 그려져 있으며, 주변에는 꽃들이 장식되어 있습니다. 전체적으로 아기자기한 분위기를 줍니다.|
|3|10|"허탈하네"라는 감정이 전혀 반영되지 않음. 꽃 이미지로 인해 감정 표현과 맞지 않음.|[각 No 3 에 일치되는 Generated image의 모든 객체에 대해 상세하게 표현할것]ccc.jpg#단순하고 깔끔한 스타일로 그려진 꽃 한 송이가 중앙에 위치해 있습니다. 둥근 배경 안에 있는 이 꽃은 선명하고 부드러운 색감으로 그려져 있습니다.|
|4|15|"절망적이야"라는 감정이 충분히 반영되지 않음. 표정은 약간 슬퍼 보이나, 전체적으로 밝은 색상과 귀여운 스타일로 절망의 느낌이 부족함.|[각 No 4 에 일치되는 Generated image의 모든 객체에 대해 상세하게 표현할것]ddd.jpg#노란색 우주복을 입은 작은 캐릭터가 있습니다. 큰 눈에는 눈물이 맺혀 있고, 입꼬리가 내려가 있어 약간 슬픈 표정을 짓고 있습니다. 왼손에 꽃 한 송이를 들고 있으며, 귀여운 헬멧을 쓰고 있습니다. 전반적으로 밝고 아기자기한 분위기를 자아냅니다.|
|5|20|"눈물이 멈추질 않아"라는 감정 표현은 적절하나, 레트로 로고 스타일이 주제와 다소 부합하지 않음.|[각 No 5 에 일치되는 Generated image의 모든 객체에 대해 상세하게 표현할것]eee.jpg#심플한 디자인의 물방울 이미지가 중앙에 위치해 있습니다. 얇은 검정 선으로 윤곽을 강조하고 있으며, 내부는 연한 하늘색으로 채워져 있습니다. 주변에는 작은 점들이 장식처럼 배치되어 있습니다.|

Generated image는 {inner_extra_original_img}Extra Prompt와 Style을 반영하여 생성되었다.
전문 판정위원으로써 Generated image에 대해 "# 평가기준"을 정확하게 반영하여 평가해줘.'''
            .format(
                innerMotherLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_MOTHERLANGUAGE),
                inner_extra_criterions='' if self.mArgs.getValInnerArg(ARG_KEY_NAME_HAS_INPUT_IMAGE) == False else __PROMPT_EXTRA_CRITERIONS,
                inner_extra_original_img='' if self.mArgs.getValInnerArg(ARG_KEY_NAME_HAS_INPUT_IMAGE) == False else "Original image를 바탕으로, ",
            ))
        else:
            return ('''당신은 지금부터 주어진 이미지가 Extra prompt와 Style을 정확하게 반영하여, 생성 되었는지를 Score로 판단하는 전문 판정위원 이야.
아래 "# 평가기준"을 정확하게 반영하여 평가해줘.
답변은 반드시 아래 "# 출력양식(예시)"을 지켜서 답변해줘.

# 평가기준
1. Score는 30점 만점이며, 25/20/15/10 단위로 평가할것. 
2. Extra prompt 반영여부는 점수에 80%반영하고, Style은 20%를 점수에 반영할것.
3. Extra prompt와 Style이 모두 정확하게 반영되었다면, 30점의 높은 점수를 부여할것.(30점)
4. Extra prompt가 부분적으로 누락되었더라도 전반적으로 반영되고, Style도 정확하게 반영되었으면 25점으로 부분 감점할것.(25점)
5. Extra prompt가 부분적으로 누락되었더라도 전반적으로 반영되고, Style이 정확하게 반영되지 않았으면 20점으로 부분 감점할것.(20점)
6. Extra prompt가 반영되지 않고, Style이 정확하게 반영되었으면 15점으로 부분 감점할것.(15점)
7. Extra prompt가 전혀 반영되지 않고, Style도 정확하게 반영되지 않았으면 10점으로 낮게 평가할것.(10점)
8. Score가 30점이면 "Reason"열에 "만점"으로만 표시하고, 만일 Score가 30점보다 적을 경우, 감점된 이유를 상세하게 "Reason"열에 적을것.
{inner_extra_criterions}

#  감정과 이미지의 표현관계
1. 행복, 기쁨, 사랑 : 꽃, 태양, 웃음, 하트 등의 이미지
2. 슬픔, 눈물 : 물방울 이미지
3. 짜증, 화남 : 눈썹이 올라간 표정, 천둥, 번개, 폭탄, 불 등의 이미지
4. 침울, 절망, 실망, 우울, 기운빠짐, 허탈 ,무너짐 : 축 처지거나 늘어진 모습, 전체적으로 회색톤의 어두운 이미지

# 출력양식(예시)
"No"열에는 주어된 No를 그대로 적을것.
"Score"열에는 Generated image가 "# 평가기준"을 반영하여 제대로 생성되었는지 여부를 점수로 판단할것.
"Reason"열에는 "Score"가 30점이 아닐 경우, 감점된 이유를 반드시 {innerMotherLanguage}언어로 상세하게 적고, 반영된 Extra prompt와 반영되지 않은 Extra prompt를 구분하여 적을것.
"Caption"열에는 앞부분에 전달된 Generated image의 파일명을 적은뒤 #을 붙일것. 그 다음에는 오직 Generated image의 객체들에 대해서 caption을 작성할것.
"Caption"내용은 시각 장애인의 이해를 돕기 위한 상세 설명이 필요하며, 그림을 보지 않은 사람에게 설명하듯이, "No"열에서 주어진 Generated image의 모든 객체에 대해서 정확하고 상세하게 묘사할것.({innerMotherLanguage}언어로 작성할것.)
아래와 같이 Header열이 포함된 MarkDown 테이블로만 답변할것.

|No|Score|Reason|Caption|
|---|---|---|---|
|1|30|만점|[각 No 1 에 일치되는 Generated image의 모든 객체에 대해 상세하게 표현할것]aaa.jpg#멋진 오로라가 있는 겨울 풍경을 보여줍니다. 밤하늘에 푸르스름한 빛이 흐르고, 반짝이는 별들이 보입니다. 하늘은 푸른색과 보라색으로 물들어 있으며, 땅에는 눈이 덮여 있습니다. 강물이 장면을 반사하여 환상적인 분위기를 더합니다. 주위의 침엽수림이 그림에 깊이감을 더해 주며, 자연의 평온함을 느낄 수 있습니다.|
|2|25|"행복해서 울고 싶어"라는 감정이 잘 반영되었으나, 물방울 이미지가 웃고 있어 슬픔의 느낌이 덜 표현됨.|[각 No 2 에 일치되는 Generated image의 모든 객체에 대해 상세하게 표현할것]bbb.jpg#물방울 모양에 귀여운 얼굴이 그려져 있으며, 주변에는 꽃들이 장식되어 있습니다. 전체적으로 아기자기한 분위기를 줍니다.|
|3|10|"허탈하네"라는 감정이 전혀 반영되지 않음. 꽃 이미지로 인해 감정 표현과 맞지 않음.|[각 No 3 에 일치되는 Generated image의 모든 객체에 대해 상세하게 표현할것]ccc.jpg#단순하고 깔끔한 스타일로 그려진 꽃 한 송이가 중앙에 위치해 있습니다. 둥근 배경 안에 있는 이 꽃은 선명하고 부드러운 색감으로 그려져 있습니다.|
|4|15|"절망적이야"라는 감정이 충분히 반영되지 않음. 표정은 약간 슬퍼 보이나, 전체적으로 밝은 색상과 귀여운 스타일로 절망의 느낌이 부족함.|[각 No 4 에 일치되는 Generated image의 모든 객체에 대해 상세하게 표현할것]ddd.jpg#노란색 우주복을 입은 작은 캐릭터가 있습니다. 큰 눈에는 눈물이 맺혀 있고, 입꼬리가 내려가 있어 약간 슬픈 표정을 짓고 있습니다. 왼손에 꽃 한 송이를 들고 있으며, 귀여운 헬멧을 쓰고 있습니다. 전반적으로 밝고 아기자기한 분위기를 자아냅니다.|
|5|20|"눈물이 멈추질 않아"라는 감정 표현은 적절하나, 레트로 로고 스타일이 주제와 다소 부합하지 않음.|[각 No 5 에 일치되는 Generated image의 모든 객체에 대해 상세하게 표현할것]eee.jpg#심플한 디자인의 물방울 이미지가 중앙에 위치해 있습니다. 얇은 검정 선으로 윤곽을 강조하고 있으며, 내부는 연한 하늘색으로 채워져 있습니다. 주변에는 작은 점들이 장식처럼 배치되어 있습니다.|

Generated image는 {inner_extra_original_img}Extra Prompt와 Style을 반영하여 생성되었다.
전문 판정위원으로써 Generated image에 대해 "# 평가기준"을 정확하게 반영하여 평가해줘.'''
            .format(
                innerMotherLanguage=self.mArgs.getValInnerArg(ARG_KEY_NAME_MOTHERLANGUAGE),
                inner_extra_criterions='' if self.mArgs.getValInnerArg(ARG_KEY_NAME_HAS_INPUT_IMAGE) == False else __PROMPT_EXTRA_CRITERIONS,
                inner_extra_original_img='' if self.mArgs.getValInnerArg(ARG_KEY_NAME_HAS_INPUT_IMAGE) == False else "Original image를 바탕으로, ",
            ))

    def get_do_score_prompt(self):
        if self.mArgs is None:
            return ''

        if self.mUseKorPrompt:
            return ''''''
        else:
            return ''''''

    # 번역 평가 결과의 형식을 다시 한번 요청할 경우,
    def get_again_form_prompt(self):
        if self.mArgs is None:
            return ''

        if self.mUseKorPrompt:
            return ''''''
        else:
            return ''''''

    # target 언어로 번역된 결과의 형식을 다시 한번 요청할 경우,
    def get_again_form_trans_prompt(self):
        if self.mArgs is None:
            return ''

        if self.mUseKorPrompt:
            return ''''''
        else:
            return ''''''

    # PROMPT별 첫(대표) prompt
    def get_sentence_template_prompt(self):
        if self.mArgs is None:
            return ''

        if self.mUseKorPrompt:
            return ''''''
        else:
            return ''''''

    # Category별 문장 생성 요청
    def get_sentence_gensentences_prompt(self):
        if self.mArgs is None:
            return ''

        if self.mUseKorPrompt:
            return ''''''
        else:
            return ''''''
