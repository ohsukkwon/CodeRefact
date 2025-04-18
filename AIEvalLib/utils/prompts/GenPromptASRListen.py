# -*- coding: utf-8 -*-
from GlobalUtil import langname_from_locale, get_response_count
from prompts.IScorePrompt import IScorePrompt
from utils.GlobalVars import *

class GenPromptASRListen(IScorePrompt):
    def __init__(self, argArgs):
        if argArgs == None:
            self.mArgs = None
            self.mUseKorPrompt = False
        else:
            self.mArgs = argArgs     # copy from org arg
            # self.mArgs.update_InnerArgs(self.mArgs.copy_InnerArgs())  # copy from org's prompt args

            if self.mArgs.getValInnerArg(ARG_KEY_NAME_MOTHERLANGUAGE).lower() == 'korean':  # use ARG_KEY_NAME_MOTHERLANGUAGE(in the arguments : "-Mlang Engilsh")
                self.mUseKorPrompt = True
            else:
                self.mUseKorPrompt = False

        print(f'self.mUseKorPrompt:{self.mUseKorPrompt}')

    def get_my_keyname(self):
        return CONFIG_NAME_VALUE_LISTEN

    def get_my_csvname(self):
        if self.mArgs.getValInnerArg(ARG_KEY_NAME_PROMPTTYPE) != None:
            return self.mArgs.getValInnerArg(ARG_KEY_NAME_PROMPTTYPE)

        return f'sentences_{CONFIG_NAME_VALUE_LISTEN}.csv'

    def get_noti_role_prompt(self):
        if self.mArgs == None:
            return ''

        if self.mUseKorPrompt:
            return \
                '''지금부터 {innerPersonaPerson1Name} 발표자 1명이 관객들 앞에서 강의를 하기 위한 발표 스크립트를 작성해줘.

발표자인 {innerPersonaPerson1Name}의 역할을 정의해 줄께.
나이는 {innerPersonaPerson1Age}, 성별은 {innerPersonaPerson1Gender}, 출신 국가는 {innerPersonaPerson1CountryOfOrigin}, 직업은 {innerPersonaPerson1Occupation} 이고,
취미는 {innerPersonaPerson1Hobby}, 성격은 {innerPersonaPerson1Personality}, 연봉은 {innerPersonaPerson1AnualSalary} 이다.
{innerPersonaPerson1Name}는 {innerPersonaPerson1MyLanguage} 언어로 발표를 한다.
{innerPersonaPerson1ExtraPrompt}

발표자는 {innerPersonaSubject} 주제에 대하여 구체적인 예시를 제시하면서 자세하게 설명한다.
참고문서와 구체적인 예시는 각종 신문 기사나 블로그를 활용하고, 일반인들이 충분히 이해할 수 있는 쉬운 단어와 문장으로 작성해줘.
이야기의 내용은 자연스럽게 이어져야 하며, 주제는 명확하고 일관되어야 해.
발표 시간은 1시간 이상이 될수 있도록 작성하고, 전체 문장은 총 {innerTotalCountOfSentences}개 문장이 될때까지 작성해줘.
{innerPersonaExtraPrompt}

#문장생성 주요기준(8가지)
1) 열의 순서는 {innerAsrTableHeaderNoStr},{innerAsrTableHeaderPersonNameStr},{innerAsrTableHeaderSentenceStr},{innerAsrTableHeaderSentence2Str},{innerAsrTableHeaderMotherLanguageTranslationStr} 이런 순서대로 작성할 것.
2) "{innerAsrTableHeaderSentenceStr}" 열의 문장은 문법과 철자에 오류가 전혀 없어야 함.
3) "{innerAsrTableHeaderSentenceStr}" 열의 문장에 인종차별,욕설,비속어가 포함되면 안됨.
4) "{innerAsrTableHeaderSentenceStr}" 열의 문장에 개인정보와 민감한 정보가 포함되면 안됨.
5) "{innerAsrTableHeaderSentenceStr}"열은 ** 반드시 {innerPersonaPerson1MyLanguage} 언어 **로 작성할 것.
6) "{innerAsrTableHeaderSentenceStr}"열은 최대 {innerPersonaWordCountOf1Line} 단어를 넘지 않도록 작성할 것.
7) "{innerAsrTableHeaderSentence2Str}"열은 ** 반드시 "DUMMY" **로 작성할 것.
8) "{innerAsrTableHeaderMotherLanguageTranslationStr}" 열은 ** 반드시 "{innerAsrTableHeaderSentenceStr}" 열에서 생성된 문장을 {innerCfgMotherLanguage} 언어 **로 번역한 문장을 작성할 것.

#답변 주요기준(4가지)
1) 답변은 아래 "#답변 형식" 처럼 ** 반드시 1개 **의 표 형식으로 작성할 것.
2) 표 이외의 다른 문장은 절대 적지 말것.
3) 전체 스크립트 내용에 같은 문장을 절대 반복 하지 말것.
4) 표의 각 열은 ** 반드시 |로 시작하여 |로 끝나야 하며 **, 각열에서 마지막은 ** 반드시 |로 끝나야 ** 할것.

#답변 형식
{innerAsrTableHeaderStr}
{innerAsrTableHeaderDevideStr}
| 1 | {innerPersonaPerson1Name} | [{innerPersonaSubject} 주제에 맞게 생성된 문장을 ** 반드시 {innerPersonaPerson1MyLanguage} 언어 **로 작성할 것] | DUMMY | ["{innerAsrTableHeaderSentenceStr}"열에서 생성된 문장을 ** 반드시 {innerCfgMotherLanguage} 언어 **로 번역한 문장을 작성할 것] |
| 2 | {innerPersonaPerson1Name} | [{innerPersonaSubject} 주제에 맞게 생성된 문장을 ** 반드시 {innerPersonaPerson1MyLanguage} 언어 **로 작성할 것] | DUMMY | ["{innerAsrTableHeaderSentenceStr}"열에서 생성된 문장을 ** 반드시 {innerCfgMotherLanguage} 언어 **로 번역한 문장을 작성할 것] | 

발표 스크립트의 내용은 자연스럽게 이어져야 하며, 총 {innerTotalCountOfSentences}개 문장이 되기 전까지 계속 요청할 것이다. 
먼저 {innerResponseCountPerResponse}개 문장을 답변해 줘.
''' \
            .format(innerPersonaPerson1Name=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_NAME),
                    innerPersonaPerson1Age=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_AGE),
                    innerPersonaPerson1Gender=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_GENDER),
                    innerPersonaPerson1CountryOfOrigin=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_COUNTRYOFORIGIN),
                    innerPersonaPerson1MyLanguage=langname_from_locale(locale=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_MYLANGUAGE)),
                    innerPersonaPerson1Occupation=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_OCCUPATION),
                    innerPersonaPerson1Hobby=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_HOBBY),
                    innerPersonaPerson1Personality=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_PERSONALITY),
                    innerPersonaPerson1AnualSalary =self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_ANNUALSALARY),
                    innerPersonaPerson1ExtraPrompt=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_EXTRAPROMPT),

                    innerPersonaSubject=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_SUBJECT),
                    innerPersonaWordCountOf1Line=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_WORDCOUNTOF1LINE),
                    innerCfgMotherLanguage=langname_from_locale(locale=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_CFGMOTHERLANGUAGE)),
                    innerPersonaExtraPrompt = self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_EXTRAPROMPT),
                    innerAsrTableHeaderNoStr=ASR_TABLE_HEADER_NO_STR,
                    innerAsrTableHeaderPersonNameStr=ASR_TABLE_HEADER_PERSONNAME_STR,
                    innerAsrTableHeaderSentenceStr=ASR_TABLE_HEADER_SENTENCE_STR,
                    innerAsrTableHeaderSentence2Str=ASR_TABLE_HEADER_SENTENCE2_STR,
                    innerAsrTableHeaderDevideStr=ASR_TABLE_HEADER_DEVIDE_STR,
                    innerAsrTableHeaderMotherLanguageTranslationStr=ASR_TABLE_HEADER_MOTHERLANGUAGETRANSLATION_STR,
                    innerAsrTableHeaderStr = ASR_TABLE_HEADER_STR,
                    innerTotalCountOfSentences = self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_TOTALCOUNTOFSENTENCES),
                    innerResponseCountPerResponse=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_TOTALCOUNTOFSENTENCES) if int(self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_TOTALCOUNTOFSENTENCES)) <= get_response_count(locale=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_MYLANGUAGE)) else get_response_count(locale=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_MYLANGUAGE)),
                    )
        else:
            return \
                '''From now on, please write a presentation script for {innerPersonaPerson1Name}, where the presenter will give a lecture in front of the audience.

Let me define the role of the presenter, {innerPersonaPerson1Name}.
Their age is {innerPersonaPerson1Age}, gender is {innerPersonaPerson1Gender}, country of origin is {innerPersonaPerson1CountryOfOrigin}, occupation is {innerPersonaPerson1Occupation},
hobby is {innerPersonaPerson1Hobby}, personality is {innerPersonaPerson1Personality}, and annual salary is {innerPersonaPerson1AnualSalary}.
{innerPersonaPerson1Name} will give the presentation in {innerPersonaPerson1MyLanguage}.
{innerPersonaPerson1ExtraPrompt}

The presenter will provide specific examples and explain in detail about the topic of {innerPersonaSubject}.
Use various news articles and blogs for reference materials and specific examples, and write in simple words and sentences that the general public can easily understand.
The content of the presentation should flow naturally, and the subject must be clear and consistent.
Make sure the presentation lasts more than an hour, and write the entire script until it reaches a total of {innerTotalCountOfSentences} sentences.
{innerPersonaExtraPrompt}

#Main Criteria for Sentence Generation (8 points)
1) The column order must follow: {innerAsrTableHeaderNoStr}, {innerAsrTableHeaderPersonNameStr}, {innerAsrTableHeaderSentenceStr}, {innerAsrTableHeaderSentence2Str}, {innerAsrTableHeaderMotherLanguageTranslationStr}.
2) The sentences in the "{innerAsrTableHeaderSentenceStr}" column must be free of grammatical and spelling errors.
3) The sentences in the "{innerAsrTableHeaderSentenceStr}" column must not contain any racial discrimination, profanity, or slang.
4) The sentences in the "{innerAsrTableHeaderSentenceStr}" column must not include any personal or sensitive information.
5) The "{innerAsrTableHeaderSentenceStr}" column must be written in {innerPersonaPerson1MyLanguage}.
6) The sentences in the "{innerAsrTableHeaderSentenceStr}" column must not exceed {innerPersonaWordCountOf1Line} words.
7) The "{innerAsrTableHeaderSentence2Str}" column must be written as "DUMMY".
8) The "{innerAsrTableHeaderMotherLanguageTranslationStr}" column must be written by translating the sentence from the "{innerAsrTableHeaderSentenceStr}" column into {innerCfgMotherLanguage}.

#Main Criteria for Responses (4 points)
1) The response must be formatted as exactly one table as shown below in the "#Answer Format".
2) Do not write any sentences outside of the table.
3) Never repeat the same sentences throughout the entire script.
4) Each column in the table must start and end with |, and each row must end with |.
{innerAsrTableHeaderStr}
{innerAsrTableHeaderDevideStr}
| 1 | {innerPersonaPerson1Name} | [Write the sentence related to {innerPersonaSubject} in {innerPersonaPerson1MyLanguage}] | DUMMY | [Translate the sentence from the "{innerAsrTableHeaderSentenceStr}" column into {innerCfgMotherLanguage}] | 
| 2 | {innerPersonaPerson1Name} | [Write the sentence related to {innerPersonaSubject} in {innerPersonaPerson1MyLanguage}] | DUMMY | [Translate the sentence from the "{innerAsrTableHeaderSentenceStr}" column into {innerCfgMotherLanguage}] | 

The content of the presentation should flow naturally, and I will continue to request until it reaches a total of {innerTotalCountOfSentences} sentences.
Please respond with {innerResponseCountPerResponse} sentences first.
''' \
            .format(innerPersonaPerson1Name=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_NAME),
                    innerPersonaPerson1Age=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_AGE),
                    innerPersonaPerson1Gender=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_GENDER),
                    innerPersonaPerson1CountryOfOrigin=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_COUNTRYOFORIGIN),
                    innerPersonaPerson1MyLanguage=langname_from_locale(locale=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_MYLANGUAGE)),
                    innerPersonaPerson1Occupation=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_OCCUPATION),
                    innerPersonaPerson1Hobby=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_HOBBY),
                    innerPersonaPerson1Personality=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_PERSONALITY),
                    innerPersonaPerson1AnualSalary =self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_ANNUALSALARY),
                    innerPersonaPerson1ExtraPrompt=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_EXTRAPROMPT),

                    innerPersonaSubject=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_SUBJECT),
                    innerPersonaWordCountOf1Line=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_WORDCOUNTOF1LINE),
                    innerCfgMotherLanguage=langname_from_locale(locale=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_CFGMOTHERLANGUAGE)),
                    innerPersonaExtraPrompt = self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_EXTRAPROMPT),
                    innerAsrTableHeaderNoStr=ASR_TABLE_HEADER_NO_STR,
                    innerAsrTableHeaderPersonNameStr=ASR_TABLE_HEADER_PERSONNAME_STR,
                    innerAsrTableHeaderSentenceStr=ASR_TABLE_HEADER_SENTENCE_STR,
                    innerAsrTableHeaderSentence2Str=ASR_TABLE_HEADER_SENTENCE2_STR,
                    innerAsrTableHeaderDevideStr=ASR_TABLE_HEADER_DEVIDE_STR,
                    innerAsrTableHeaderMotherLanguageTranslationStr=ASR_TABLE_HEADER_MOTHERLANGUAGETRANSLATION_STR,
                    innerAsrTableHeaderStr = ASR_TABLE_HEADER_STR,
                    innerTotalCountOfSentences = self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_TOTALCOUNTOFSENTENCES),
                    innerResponseCountPerResponse=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_TOTALCOUNTOFSENTENCES) if int(self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_TOTALCOUNTOFSENTENCES)) <= get_response_count(locale=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_MYLANGUAGE)) else get_response_count(locale=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_MYLANGUAGE)),
                    )

    def get_do_score_prompt(self):
        if self.mArgs == None:
            return ''

        if self.mUseKorPrompt:
            return ''''''
        else:
            return ''''''

    # 번역 평가 결과의 형식을 다시 한번 요청할 경우,
    def get_again_form_prompt(self):
        if self.mArgs == None:
            return ''

        if self.mUseKorPrompt:
            return '''내가 원하는 답변 형식이 아니야. 아래 내용으로 답변할것.

#문장생성 주요기준(8가지)
1) 열의 순서는 {innerAsrTableHeaderNoStr},{innerAsrTableHeaderPersonNameStr},{innerAsrTableHeaderSentenceStr},{innerAsrTableHeaderSentence2Str},{innerAsrTableHeaderMotherLanguageTranslationStr} 이런 순서대로 작성할 것.
2) "{innerAsrTableHeaderSentenceStr}" 열의 문장은 문법과 철자에 오류가 전혀 없어야 함.
3) "{innerAsrTableHeaderSentenceStr}" 열의 문장에 인종차별,욕설,비속어가 포함되면 안됨.
4) "{innerAsrTableHeaderSentenceStr}" 열의 문장에 개인정보와 민감한 정보가 포함되면 안됨.
5) "{innerAsrTableHeaderSentenceStr}"열은 ** 반드시 {innerPersonaPerson1MyLanguage} 언어 **로 작성할 것.
6) "{innerAsrTableHeaderSentenceStr}"열은 최대 {innerPersonaWordCountOf1Line} 단어를 넘지 않도록 작성할 것.
7) "{innerAsrTableHeaderSentence2Str}"열은 ** 반드시 "DUMMY" **로 작성할 것.
8) "{innerAsrTableHeaderMotherLanguageTranslationStr}" 열은 ** 반드시 "{innerAsrTableHeaderSentenceStr}" 열에서 생성된 문장을 {innerCfgMotherLanguage} 언어 **로 번역한 문장을 작성할 것.

#답변 주요기준(4가지)
1) 답변은 아래 "#답변 형식" 처럼 ** 반드시 1개 **의 표 형식으로 작성할 것.
2) 표 이외의 다른 문장은 절대 적지 말것.
3) 전체 스크립트 내용에 같은 문장을 절대 반복 하지 말것.
4) 표의 각 열은 ** 반드시 |로 시작하여 |로 끝나야 하며 **, 각열에서 마지막은 ** 반드시 |로 끝나야 ** 할것.

#답변 형식
{innerAsrTableHeaderStr}
{innerAsrTableHeaderDevideStr}
| 1 | {innerPersonaPerson1Name} | [{innerPersonaSubject} 주제에 맞게 생성된 문장을 ** 반드시 {innerPersonaPerson1MyLanguage} 언어 **로 작성할 것] | DUMMY | ["{innerAsrTableHeaderSentenceStr}"열에서 생성된 문장을 ** 반드시 {innerCfgMotherLanguage} 언어 **로 번역한 문장을 작성할 것] |
| 2 | {innerPersonaPerson1Name} | [{innerPersonaSubject} 주제에 맞게 생성된 문장을 ** 반드시 {innerPersonaPerson1MyLanguage} 언어 **로 작성할 것] | DUMMY | ["{innerAsrTableHeaderSentenceStr}"열에서 생성된 문장을 ** 반드시 {innerCfgMotherLanguage} 언어 **로 번역한 문장을 작성할 것] | 
''' \
                    .format(innerPersonaPerson1Name=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_NAME),
                            innerPersonaSubject=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_SUBJECT),
                            innerPersonaWordCountOf1Line=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_WORDCOUNTOF1LINE),
                            innerPersonaPerson1MyLanguage=langname_from_locale(locale=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_MYLANGUAGE)),
                            innerCfgMotherLanguage=langname_from_locale(locale=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_CFGMOTHERLANGUAGE)),
                            innerAsrTableHeaderNoStr=ASR_TABLE_HEADER_NO_STR,
                            innerAsrTableHeaderPersonNameStr=ASR_TABLE_HEADER_PERSONNAME_STR,
                            innerAsrTableHeaderSentenceStr=ASR_TABLE_HEADER_SENTENCE_STR,
                            innerAsrTableHeaderSentence2Str=ASR_TABLE_HEADER_SENTENCE2_STR,
                            innerAsrTableHeaderDevideStr=ASR_TABLE_HEADER_DEVIDE_STR,
                            innerAsrTableHeaderMotherLanguageTranslationStr=ASR_TABLE_HEADER_MOTHERLANGUAGETRANSLATION_STR,
                            innerAsrTableHeaderStr = ASR_TABLE_HEADER_STR
                            )
        else:
            return '''This is not the answer format I want. Please respond according to the content below.

#Main Criteria for Sentence Generation (8 points)
1) The column order must follow: {innerAsrTableHeaderNoStr}, {innerAsrTableHeaderPersonNameStr}, {innerAsrTableHeaderSentenceStr}, {innerAsrTableHeaderSentence2Str}, {innerAsrTableHeaderMotherLanguageTranslationStr}.
2) The sentences in the "{innerAsrTableHeaderSentenceStr}" column must be free of grammatical and spelling errors.
3) The sentences in the "{innerAsrTableHeaderSentenceStr}" column must not contain any racial discrimination, profanity, or slang.
4) The sentences in the "{innerAsrTableHeaderSentenceStr}" column must not include any personal or sensitive information.
5) The "{innerAsrTableHeaderSentenceStr}" column must be written in {innerPersonaPerson1MyLanguage}.
6) The sentences in the "{innerAsrTableHeaderSentenceStr}" column must not exceed {innerPersonaWordCountOf1Line} words.
7) The "{innerAsrTableHeaderSentence2Str}" column must be written as "DUMMY".
8) The "{innerAsrTableHeaderMotherLanguageTranslationStr}" column must be written by translating the sentence from the "{innerAsrTableHeaderSentenceStr}" column into {innerCfgMotherLanguage}.

#Main Criteria for Responses (4 points)
1) The response must be formatted as exactly one table as shown below in the "#Answer Format".
2) Do not write any sentences outside of the table.
3) Never repeat the same sentences throughout the entire script.
4) Each column in the table must start and end with |, and each row must end with |.
{innerAsrTableHeaderStr}
{innerAsrTableHeaderDevideStr}
| 1 | {innerPersonaPerson1Name} | [Write the sentence related to {innerPersonaSubject} in {innerPersonaPerson1MyLanguage}] | DUMMY | [Translate the sentence from the "{innerAsrTableHeaderSentenceStr}" column into {innerCfgMotherLanguage}] |  
| 2 | {innerPersonaPerson1Name} | [Write the sentence related to {innerPersonaSubject} in {innerPersonaPerson1MyLanguage}] | DUMMY | [Translate the sentence from the "{innerAsrTableHeaderSentenceStr}" column into {innerCfgMotherLanguage}] | 
'''\
                    .format(innerPersonaPerson1Name=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_NAME),
                            innerPersonaSubject=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_SUBJECT),
                            innerPersonaWordCountOf1Line=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_WORDCOUNTOF1LINE),
                            innerPersonaPerson1MyLanguage=langname_from_locale(locale=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_MYLANGUAGE)),
                            innerCfgMotherLanguage=langname_from_locale(locale=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_CFGMOTHERLANGUAGE)),
                            innerAsrTableHeaderNoStr=ASR_TABLE_HEADER_NO_STR,
                            innerAsrTableHeaderPersonNameStr=ASR_TABLE_HEADER_PERSONNAME_STR,
                            innerAsrTableHeaderSentenceStr=ASR_TABLE_HEADER_SENTENCE_STR,
                            innerAsrTableHeaderSentence2Str=ASR_TABLE_HEADER_SENTENCE2_STR,
                            innerAsrTableHeaderDevideStr=ASR_TABLE_HEADER_DEVIDE_STR,
                            innerAsrTableHeaderMotherLanguageTranslationStr=ASR_TABLE_HEADER_MOTHERLANGUAGETRANSLATION_STR,
                            innerAsrTableHeaderStr = ASR_TABLE_HEADER_STR
                            )

    # target 언어로 번역된 결과의 형식을 다시 한번 요청할 경우,
    def get_again_form_trans_prompt(self):
        if self.mArgs == None:
            return ''

        if self.mUseKorPrompt:
            return ''''''
        else:
            return ''''''

    # PROMPT별 첫(대표) prompt
    def get_sentence_template_prompt(self):
        if self.mArgs == None:
            return ''

        if self.mUseKorPrompt:
            return ''''''
        else:
            return ''''''

    # Category별 문장 생성 요청
    def get_sentence_gensentences_prompt(self):
        if self.mArgs == None:
            return ''

        if self.mUseKorPrompt:
            return ''''''
        else:
            return ''''''
