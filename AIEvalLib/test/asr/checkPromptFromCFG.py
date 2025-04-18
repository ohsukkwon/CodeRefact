# -*- coding: utf-8 -*-
import json

from GlobalVars import *


def returnCFGData(type="conv"):
    new_dict = {}
    if type == "conv":
        with open("genasrconversation.cfg", "r", encoding='utf-8-sig') as cfg_file:
            cfgAllData = json.load(cfg_file)

        new_dict[ARG_KEY_CONFIG_NAME_SUBJECT] = cfgAllData[CONFIG_NAME_KEY_SUBJECT]
        new_dict[ARG_KEY_CONFIG_NAME_EXTRAPROMPT] = cfgAllData[CONFIG_NAME_KEY_EXTRAPROMPT]
        new_dict[ARG_KEY_CONFIG_NAME_CFGMOTHERLANGUAGE] = cfgAllData[CONFIG_NAME_KEY_CFGMOTHERLANGUAGE]
        new_dict[ARG_KEY_CONFIG_NAME_WORDCOUNTOF1LINE] = cfgAllData[CONFIG_NAME_KEY_WORDCOUNTOF1LINE]
        new_dict[ARG_KEY_CONFIG_NAME_TOTALCOUNTOFSENTENCES] = cfgAllData[CONFIG_NAME_KEY_TOTALCOUNTOFSENTENCES]

        new_dict[ARG_KEY_CONFIG_NAME_PERSONA1_AIVOICEENGINE] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][
            CONFIG_NAME_KEY_AIVOICEENGINE]
        new_dict[ARG_KEY_CONFIG_NAME_PERSONA1_AIVOICEID] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][
            CONFIG_NAME_KEY_AIVOICEID]
        new_dict[ARG_KEY_CONFIG_NAME_PERSONA1_NAME] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][
            CONFIG_NAME_KEY_NAME]
        new_dict[ARG_KEY_CONFIG_NAME_PERSONA1_GENDER] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][
            CONFIG_NAME_KEY_GENDER]
        new_dict[ARG_KEY_CONFIG_NAME_PERSONA1_AGE] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][CONFIG_NAME_KEY_AGE]
        new_dict[ARG_KEY_CONFIG_NAME_PERSONA1_OCCUPATION] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][
            CONFIG_NAME_KEY_OCCUPATION]
        new_dict[ARG_KEY_CONFIG_NAME_PERSONA1_COUNTRYOFORIGIN] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][
            CONFIG_NAME_KEY_COUNTRYOFORIGIN]
        new_dict[ARG_KEY_CONFIG_NAME_PERSONA1_MYLANGUAGE] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][
            CONFIG_NAME_KEY_MYLANGUAGE]
        new_dict[ARG_KEY_CONFIG_NAME_PERSONA1_HOBBY] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][
            CONFIG_NAME_KEY_HOBBY]
        new_dict[ARG_KEY_CONFIG_NAME_PERSONA1_PERSONALITY] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][
            CONFIG_NAME_KEY_PERSONALITY]
        new_dict[ARG_KEY_CONFIG_NAME_PERSONA1_ANNUALSALARY] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][
            CONFIG_NAME_KEY_ANNUALSALARY]
        new_dict[ARG_KEY_CONFIG_NAME_PERSONA1_EXTRAPROMPT] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][
            CONFIG_NAME_KEY_EXTRAPROMPT]
        new_dict[ARG_KEY_CONFIG_NAME_PERSONA1_SPEAKINGSPEED] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][
            CONFIG_NAME_KEY_SPEAKINGSPEED]
        new_dict[ARG_KEY_CONFIG_NAME_PERSONA1_SPEAKINGPITCH] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][
            CONFIG_NAME_KEY_SPEAKINGPITCH]

        new_dict[ARG_KEY_CONFIG_NAME_PERSONA2_AIVOICEENGINE] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][1][
            CONFIG_NAME_KEY_AIVOICEENGINE]
        new_dict[ARG_KEY_CONFIG_NAME_PERSONA2_AIVOICEID] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][1][
            CONFIG_NAME_KEY_AIVOICEID]
        new_dict[ARG_KEY_CONFIG_NAME_PERSONA2_NAME] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][1][
            CONFIG_NAME_KEY_NAME]
        new_dict[ARG_KEY_CONFIG_NAME_PERSONA2_GENDER] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][1][
            CONFIG_NAME_KEY_GENDER]
        new_dict[ARG_KEY_CONFIG_NAME_PERSONA2_AGE] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][1][CONFIG_NAME_KEY_AGE]
        new_dict[ARG_KEY_CONFIG_NAME_PERSONA2_OCCUPATION] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][1][
            CONFIG_NAME_KEY_OCCUPATION]
        new_dict[ARG_KEY_CONFIG_NAME_PERSONA2_COUNTRYOFORIGIN] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][1][
            CONFIG_NAME_KEY_COUNTRYOFORIGIN]
        new_dict[ARG_KEY_CONFIG_NAME_PERSONA2_MYLANGUAGE] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][1][
            CONFIG_NAME_KEY_MYLANGUAGE]
        new_dict[ARG_KEY_CONFIG_NAME_PERSONA2_HOBBY] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][1][
            CONFIG_NAME_KEY_HOBBY]
        new_dict[ARG_KEY_CONFIG_NAME_PERSONA2_PERSONALITY] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][1][
            CONFIG_NAME_KEY_PERSONALITY]
        new_dict[ARG_KEY_CONFIG_NAME_PERSONA2_ANNUALSALARY] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][1][
            CONFIG_NAME_KEY_ANNUALSALARY]
        new_dict[ARG_KEY_CONFIG_NAME_PERSONA2_EXTRAPROMPT] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][1][
            CONFIG_NAME_KEY_EXTRAPROMPT]
        new_dict[ARG_KEY_CONFIG_NAME_PERSONA2_SPEAKINGSPEED] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][1][
            CONFIG_NAME_KEY_SPEAKINGSPEED]
        new_dict[ARG_KEY_CONFIG_NAME_PERSONA2_SPEAKINGPITCH] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][1][
            CONFIG_NAME_KEY_SPEAKINGPITCH]

    else:
        with open("genasrlisten.cfg", "r", encoding='utf-8-sig') as f:
            cfgAllData = json.load(f)

        new_dict[ARG_KEY_CONFIG_NAME_SUBJECT] = cfgAllData[CONFIG_NAME_KEY_SUBJECT]
        new_dict[ARG_KEY_CONFIG_NAME_EXTRAPROMPT] = cfgAllData[CONFIG_NAME_KEY_EXTRAPROMPT]
        new_dict[ARG_KEY_CONFIG_NAME_CFGMOTHERLANGUAGE] = cfgAllData[CONFIG_NAME_KEY_CFGMOTHERLANGUAGE]
        new_dict[ARG_KEY_CONFIG_NAME_WORDCOUNTOF1LINE] = cfgAllData[CONFIG_NAME_KEY_WORDCOUNTOF1LINE]
        new_dict[ARG_KEY_CONFIG_NAME_TOTALCOUNTOFSENTENCES] = cfgAllData[CONFIG_NAME_KEY_TOTALCOUNTOFSENTENCES]

        new_dict[ARG_KEY_CONFIG_NAME_PERSONA1_AIVOICEENGINE] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][
            CONFIG_NAME_KEY_AIVOICEENGINE]
        new_dict[ARG_KEY_CONFIG_NAME_PERSONA1_AIVOICEID] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][
            CONFIG_NAME_KEY_AIVOICEID]
        new_dict[ARG_KEY_CONFIG_NAME_PERSONA1_NAME] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][
            CONFIG_NAME_KEY_NAME]
        new_dict[ARG_KEY_CONFIG_NAME_PERSONA1_GENDER] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][
            CONFIG_NAME_KEY_GENDER]
        new_dict[ARG_KEY_CONFIG_NAME_PERSONA1_AGE] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][CONFIG_NAME_KEY_AGE]
        new_dict[ARG_KEY_CONFIG_NAME_PERSONA1_OCCUPATION] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][
            CONFIG_NAME_KEY_OCCUPATION]
        new_dict[ARG_KEY_CONFIG_NAME_PERSONA1_COUNTRYOFORIGIN] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][
            CONFIG_NAME_KEY_COUNTRYOFORIGIN]
        new_dict[ARG_KEY_CONFIG_NAME_PERSONA1_MYLANGUAGE] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][
            CONFIG_NAME_KEY_MYLANGUAGE]
        new_dict[ARG_KEY_CONFIG_NAME_PERSONA1_HOBBY] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][
            CONFIG_NAME_KEY_HOBBY]
        new_dict[ARG_KEY_CONFIG_NAME_PERSONA1_PERSONALITY] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][
            CONFIG_NAME_KEY_PERSONALITY]
        new_dict[ARG_KEY_CONFIG_NAME_PERSONA1_ANNUALSALARY] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][
            CONFIG_NAME_KEY_ANNUALSALARY]
        new_dict[ARG_KEY_CONFIG_NAME_PERSONA1_EXTRAPROMPT] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][
            CONFIG_NAME_KEY_EXTRAPROMPT]
        new_dict[ARG_KEY_CONFIG_NAME_PERSONA1_SPEAKINGSPEED] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][
            CONFIG_NAME_KEY_SPEAKINGSPEED]
        new_dict[ARG_KEY_CONFIG_NAME_PERSONA1_SPEAKINGPITCH] = cfgAllData[CONFIG_NAME_KEY_PERSONAS][0][
            CONFIG_NAME_KEY_SPEAKINGPITCH]
    return new_dict

def makeScript(type="conv", lang="kor"):
    cfg = returnCFGData(type)

    if type == "conv":
        if lang == "kor":
            return '''
지금부터 {innerPersonaPerson1Name},{innerPersonaPerson2Name} 2명이 대화하는 형식의 대화 스크립트를 작성해줘.
두 사람은 {innerPersonaSubject} 주제로 대화를 한다.
{innerPersonaExtraPrompt}

먼저 {innerPersonaPerson1Name}의 역할을 정의한다.
나이는 {innerPersonaPerson1Age}, 성별은 {innerPersonaPerson1Gender}, 출신 국가는 {innerPersonaPerson1CountryOfOrigin}, 직업은 {innerPersonaPerson1Occupation} 이고,
취미는 {innerPersonaPerson1Hobby}, 성격은 {innerPersonaPerson1Personality}, 연봉은 {innerPersonaPerson1AnualSalary} 이다.
{innerPersonaPerson1ExtraPrompt}

다음으로 {innerPersonaPerson2Name}의 역할을 정의한다.
나이는 {innerPersonaPerson2Age}, 성별은 {innerPersonaPerson2Gender}, 출신 국가는 {innerPersonaPerson2CountryOfOrigin}, 직업은 {innerPersonaPerson2Occupation} 이고,
취미는 {innerPersonaPerson2Hobby}, 성격은 {innerPersonaPerson2Personality}, 연봉은 {innerPersonaPerson2AnualSalary} 이다.
{innerPersonaPerson2ExtraPrompt}

서로 {innerPersonaSubject} 주제에 대하여 대화한다.
일반인들이 충분히 이해할 수 있는 쉬운 단어와 문장으로 작성하고 대화체로 작성해줘.
분량은 총 {innerTotalCountOfSentences}개 문장이 될때까지 작성하고, 이야기의 내용은 자연스럽게 이어져야 해.
일상의 대화처럼 상대방의 말에 ** 질문, 감탄, 부정, 동의 하는 등의 감정 표현 ** 및 농담도 섞어가면서 대화하는 내용으로 작성해줘. 

#문장생성 주요기준(10가지)
1) 열의 순서는 {innerAsrTableHeaderNoStr}, {innerAsrTableHeaderPersonNameStr}, {innerAsrTableHeaderSentenceStr}, {innerAsrTableHeaderSentence2Str}, {innerAsrTableHeaderMotherLanguageTranslationStr} 이런 순서대로 작성할 것.
2) {innerAsrTableHeaderSentenceStr}열과 {innerAsrTableHeaderSentence2Str}열의 문장은 문법과 철자에 오류가 전혀 없어야 함.
3) {innerAsrTableHeaderSentenceStr}열과 {innerAsrTableHeaderSentence2Str}열의 문장에 인종차별,욕설,비속어가 포함되면 안됨.
4) {innerAsrTableHeaderSentenceStr}열과 {innerAsrTableHeaderSentence2Str}열의 문장에 개인정보와 민감한 정보가 포함되면 안됨.
5) {innerAsrTableHeaderSentenceStr}열은 ** 반드시 {innerPersonaPerson1MyLanguage} 언어 **로 작성할 것.
6) {innerAsrTableHeaderSentence2Str}열은 ** 반드시 {innerPersonaPerson2MyLanguage} 언어 **로 작성할 것.
7) {innerAsrTableHeaderSentenceStr}열과 {innerAsrTableHeaderSentence2Str}열은 최대 {innerPersonaWordCountOf1Line} 단어를 넘지 않도록 작성할 것.
8) {innerAsrTableHeaderSentenceStr}열은 각각의 대화 문장을 {innerPersonaPerson1MyLanguage} 언어로 작성할 것
9) 만일 두사람의 언어가 같으면, {innerAsrTableHeaderSentenceStr} 문장을 그대로 {innerAsrTableHeaderSentence2Str}열에 적고, 언어가 다르면 {innerAsrTableHeaderSentenceStr} 문장을 {innerPersonaPerson2MyLanguage} 언어로 {innerAsrTableHeaderSentence2Str}열에 작성할 것. 
10) 만일 {innerAsrTableHeaderSentenceStr}열의 언어가 {innerCfgMotherLanguage}이면, {innerAsrTableHeaderSentenceStr} 문장을 그대로 {innerAsrTableHeaderMotherLanguageTranslationStr}열에 적고, 만일 {innerAsrTableHeaderSentenceStr}열의 언어가 {innerCfgMotherLanguage}가 아니면, {innerAsrTableHeaderSentenceStr} 문장을 {innerCfgMotherLanguage} 언어로 {innerAsrTableHeaderMotherLanguageTranslationStr}열에 작성할 것.   

#답변 주요기준(4가지)
1) 답변은 아래 "#답변 형식" 처럼 ** 반드시 1개 **의 표 형식으로 작성할 것.
2) 표 이외의 다른 문장은 절대 적지 말것.
3) 전체 스크립트 내용에 같은 문장을 절대 반복 하지 말것.
4) 표의 각 열은 ** 반드시 |로 시작하여 |로 끝나야 하며 **, 각열에서 마지막은 **반드시 |로 끝나야 ** 할것.

#답변 형식
{innerAsrTableHeaderStr}
{innerAsrTableHeaderDevideStr}
| 1 | {innerPersonaPerson1Name} | [{innerPersonaPerson1Name}의 대화 문장을 ** 반드시 {innerPersonaPerson1MyLanguage} 언어 **로 작성할 것] | [두사람이 같은 언어를 사용한다면, ** 반드시 {innerAsrTableHeaderSentenceStr} 문장을 그대로 적고 **, 두사람이 다른 언어를 사용한다면, {innerAsrTableHeaderSentenceStr}열의 문장을 {innerPersonaPerson2MyLanguage} 언어로 {innerAsrTableHeaderSentence2Str}열에 적을것] | [만일 {innerAsrTableHeaderSentenceStr}열의 언어가 {innerCfgMotherLanguage}이면, ** 반드시 {innerAsrTableHeaderSentenceStr} 문장을 그대로 ** {innerAsrTableHeaderMotherLanguageTranslationStr}열에 적고, 만일 {innerAsrTableHeaderSentenceStr}열의 언어가 {innerCfgMotherLanguage}가 아니면, {innerAsrTableHeaderSentenceStr} 문장을 {innerCfgMotherLanguage} 언어로 {innerAsrTableHeaderMotherLanguageTranslationStr}열에 작성할 것] | 
| 2 | {innerPersonaPerson2Name} | [{innerPersonaPerson2Name}의 대화 문장을 ** 반드시 {innerPersonaPerson1MyLanguage} 언어 **로 작성할 것] | [두사람이 같은 언어를 사용한다면, ** 반드시 {innerAsrTableHeaderSentenceStr} 문장을 그대로 적고 **, 두사람의 다른 언어를 사용한다면, {innerAsrTableHeaderSentenceStr}열의 문장을 {innerPersonaPerson2MyLanguage} 언어로 {innerAsrTableHeaderSentence2Str}열에 적을것] | [만일 {innerAsrTableHeaderSentenceStr}열의 언어가 {innerCfgMotherLanguage}이면, ** 반드시 {innerAsrTableHeaderSentenceStr} 문장을 그대로 ** {innerAsrTableHeaderMotherLanguageTranslationStr}열에 적고, 만일 {innerAsrTableHeaderSentenceStr}열의 언어가 {innerCfgMotherLanguage}가 아니면, {innerAsrTableHeaderSentenceStr} 문장을 {innerCfgMotherLanguage} 언어로 {innerAsrTableHeaderMotherLanguageTranslationStr}열에 작성할 것] |
 
발표 스크립트의 내용은 자연스럽게 이어져야 하며, 총 {innerTotalCountOfSentences}개 문장이 되기 전까지 계속 요청할 것이다. 
먼저 {innerResponseCountPerResponse}개 문장을 답변해 줘.
''' \
            .format(innerPersonaPerson1Name=cfg[ARG_KEY_CONFIG_NAME_PERSONA1_NAME],
                    innerPersonaPerson1Age=cfg[ARG_KEY_CONFIG_NAME_PERSONA1_AGE],
                    innerPersonaPerson1Gender=cfg[ARG_KEY_CONFIG_NAME_PERSONA1_GENDER],
                    innerPersonaPerson1CountryOfOrigin=cfg[ARG_KEY_CONFIG_NAME_PERSONA1_COUNTRYOFORIGIN],
                    innerPersonaPerson1MyLanguage=cfg[ARG_KEY_CONFIG_NAME_PERSONA1_MYLANGUAGE],
                    innerPersonaPerson1Occupation=cfg[ARG_KEY_CONFIG_NAME_PERSONA1_OCCUPATION],
                    innerPersonaPerson1Hobby=cfg[ARG_KEY_CONFIG_NAME_PERSONA1_HOBBY],
                    innerPersonaPerson1Personality=cfg[ARG_KEY_CONFIG_NAME_PERSONA1_PERSONALITY],
                    innerPersonaPerson1AnualSalary=cfg[ARG_KEY_CONFIG_NAME_PERSONA1_ANNUALSALARY],
                    innerPersonaPerson1ExtraPrompt=cfg[ARG_KEY_CONFIG_NAME_PERSONA1_EXTRAPROMPT],

                    innerPersonaPerson2Name=cfg[ARG_KEY_CONFIG_NAME_PERSONA2_NAME],
                    innerPersonaPerson2Age=cfg[ARG_KEY_CONFIG_NAME_PERSONA2_AGE],
                    innerPersonaPerson2Gender=cfg[ARG_KEY_CONFIG_NAME_PERSONA2_GENDER],
                    innerPersonaPerson2CountryOfOrigin=cfg[ARG_KEY_CONFIG_NAME_PERSONA2_COUNTRYOFORIGIN],
                    innerPersonaPerson2MyLanguage=cfg[ARG_KEY_CONFIG_NAME_PERSONA2_MYLANGUAGE],
                    innerPersonaPerson2Occupation=cfg[ARG_KEY_CONFIG_NAME_PERSONA2_OCCUPATION],
                    innerPersonaPerson2Hobby=cfg[ARG_KEY_CONFIG_NAME_PERSONA2_HOBBY],
                    innerPersonaPerson2Personality=cfg[ARG_KEY_CONFIG_NAME_PERSONA2_PERSONALITY],
                    innerPersonaPerson2AnualSalary=cfg[ARG_KEY_CONFIG_NAME_PERSONA2_ANNUALSALARY],
                    innerPersonaPerson2ExtraPrompt=cfg[ARG_KEY_CONFIG_NAME_PERSONA2_EXTRAPROMPT],

                    innerPersonaSubject=cfg[ARG_KEY_CONFIG_NAME_SUBJECT],
                    innerPersonaExtraPrompt=cfg[ARG_KEY_CONFIG_NAME_EXTRAPROMPT],
                    innerPersonaWordCountOf1Line=cfg[ARG_KEY_CONFIG_NAME_WORDCOUNTOF1LINE],
                    innerCfgMotherLanguage=cfg[ARG_KEY_CONFIG_NAME_CFGMOTHERLANGUAGE],
                    innerAsrTableHeaderNoStr=ASR_TABLE_HEADER_NO_STR,
                    innerAsrTableHeaderPersonNameStr=ASR_TABLE_HEADER_PERSONNAME_STR,
                    innerAsrTableHeaderSentenceStr=ASR_TABLE_HEADER_SENTENCE_STR,
                    innerAsrTableHeaderSentence2Str=ASR_TABLE_HEADER_SENTENCE2_STR,
                    innerAsrTableHeaderDevideStr=ASR_TABLE_HEADER_DEVIDE_STR,
                    innerAsrTableHeaderMotherLanguageTranslationStr=ASR_TABLE_HEADER_MOTHERLANGUAGETRANSLATION_STR,
                    innerAsrTableHeaderStr=ASR_TABLE_HEADER_STR,
                    innerTotalCountOfSentences=cfg[ARG_KEY_CONFIG_NAME_TOTALCOUNTOFSENTENCES],
                    innerResponseCountPerResponse=ASR_RESPONSE_COUNT_PER_RESPONSE
                    )
        else:
            return '''
From now on, please write a dialogue script where two people, {innerPersonaPerson1Name} and {innerPersonaPerson2Name}, are having a conversation.
The two will talk on the topic of {innerPersonaSubject}.
{innerPersonaExtraPrompt}

First, let's define the role of {innerPersonaPerson1Name}.
Their age is {innerPersonaPerson1Age}, gender is {innerPersonaPerson1Gender}, country of origin is {innerPersonaPerson1CountryOfOrigin}, occupation is {innerPersonaPerson1Occupation},
hobby is {innerPersonaPerson1Hobby}, personality is {innerPersonaPerson1Personality}, and annual salary is {innerPersonaPerson1AnualSalary}.
{innerPersonaPerson1ExtraPrompt}

Next, let's define the role of {innerPersonaPerson2Name}.
Their age is {innerPersonaPerson2Age}, gender is {innerPersonaPerson2Gender}, country of origin is {innerPersonaPerson2CountryOfOrigin}, occupation is {innerPersonaPerson2Occupation},
hobby is {innerPersonaPerson2Hobby}, personality is {innerPersonaPerson2Personality}, and annual salary is {innerPersonaPerson2AnualSalary}.
{innerPersonaPerson2ExtraPrompt}

The two will converse on the topic of {innerPersonaSubject}.
Please write it using simple words and sentences that the general public can easily understand, in a conversational style.
Write until the total reaches {innerTotalCountOfSentences} sentences, with the conversation flowing naturally.
Make sure to include expressions like asking questions, admiration, disagreement, agreement, and mixing jokes, just as in everyday conversation.

#Main Criteria for Sentence Generation (9 points)
1) The sentences in the {innerAsrTableHeaderSentenceStr} and {innerAsrTableHeaderSentence2Str} columns must be free of grammatical and spelling errors.
2) The sentences in the {innerAsrTableHeaderSentenceStr} and {innerAsrTableHeaderSentence2Str} columns must not contain any racial discrimination, profanity, or slang.
3) The sentences in the {innerAsrTableHeaderSentenceStr} and {innerAsrTableHeaderSentence2Str} columns must not include any personal or sensitive information.
4) The column order must follow: {innerAsrTableHeaderNoStr}, {innerAsrTableHeaderPersonNameStr}, {innerAsrTableHeaderSentenceStr}, {innerAsrTableHeaderSentence2Str}, {innerAsrTableHeaderMotherLanguageTranslationStr}. 
5) The {innerAsrTableHeaderSentenceStr} column must be written in {innerPersonaPerson1MyLanguage}, and the {innerAsrTableHeaderSentence2Str} column must be written in {innerPersonaPerson2MyLanguage}.
6) The sentences in the {innerAsrTableHeaderSentenceStr} and {innerAsrTableHeaderSentence2Str} columns must not exceed {innerPersonaWordCountOf1Line} words.
7) Each dialogue sentence in the {innerAsrTableHeaderSentenceStr} column must be written in {innerPersonaPerson1MyLanguage}.
8) If both people speak the same language, copy the sentence from the {innerAsrTableHeaderSentenceStr} column to the {innerAsrTableHeaderSentence2Str} column. If they speak different languages, translate the sentence from the {innerAsrTableHeaderSentenceStr} column into {innerPersonaPerson2MyLanguage} and write it in the {innerAsrTableHeaderSentence2Str} column.
9) If the sentence in the {innerAsrTableHeaderSentenceStr} column is in {innerCfgMotherLanguage}, copy the sentence to the {innerAsrTableHeaderMotherLanguageTranslationStr} column. If not, translate the sentence from the {innerAsrTableHeaderSentenceStr} column into {innerCfgMotherLanguage} and write it in the {innerAsrTableHeaderMotherLanguageTranslationStr} column.

#Main Criteria for Responses (4 points)
1) The response must be formatted as a single table as shown below in the "#Answer Format".
2) Do not write any sentences outside of the table.
3) Never repeat the same sentences throughout the entire script.
4) Each column in the table must start and end with |, and each row must also end with |.

#Answer Format
{innerAsrTableHeaderStr}
{innerAsrTableHeaderDevideStr}
| 1 | {innerPersonaPerson1Name} | [Write {innerPersonaPerson1Name}'s dialogue in {innerPersonaPerson1MyLanguage}] | [If both people speak the same language, copy the sentence from {innerAsrTableHeaderSentenceStr}, but if they speak different languages, translate the sentence in the {innerAsrTableHeaderSentenceStr} column into {innerPersonaPerson2MyLanguage} and write it in the {innerAsrTableHeaderSentence2Str} column] | [If the sentence in the {innerAsrTableHeaderSentenceStr} column is in {innerCfgMotherLanguage}, copy it into the {innerAsrTableHeaderMotherLanguageTranslationStr} column. If not, translate it into {innerCfgMotherLanguage} and write it in this column] | 
| 2 | {innerPersonaPerson2Name} | [Write {innerPersonaPerson2Name}'s dialogue in {innerPersonaPerson1MyLanguage}] | [If both people speak the same language, copy the sentence from {innerAsrTableHeaderSentenceStr}, but if they speak different languages, translate the sentence in the {innerAsrTableHeaderSentenceStr} column into {innerPersonaPerson2MyLanguage} and write it in the {innerAsrTableHeaderSentence2Str} column] | [If the sentence in the {innerAsrTableHeaderSentenceStr} column is in {innerCfgMotherLanguage}, copy it into the {innerAsrTableHeaderMotherLanguageTranslationStr} column. If not, translate it into {innerCfgMotherLanguage} and write it in this column] | 
The content of the conversation should flow naturally, and I will continue to request until the total number of sentences reaches {innerTotalCountOfSentences}.
Please provide {innerResponseCountPerResponse} sentences in response first.
''' \
            .format(innerPersonaPerson1Name=cfg[ARG_KEY_CONFIG_NAME_PERSONA1_NAME],
                    innerPersonaPerson1Age=cfg[ARG_KEY_CONFIG_NAME_PERSONA1_AGE],
                    innerPersonaPerson1Gender=cfg[ARG_KEY_CONFIG_NAME_PERSONA1_GENDER],
                    innerPersonaPerson1CountryOfOrigin=cfg[ARG_KEY_CONFIG_NAME_PERSONA1_COUNTRYOFORIGIN],
                    innerPersonaPerson1MyLanguage=cfg[ARG_KEY_CONFIG_NAME_PERSONA1_MYLANGUAGE],
                    innerPersonaPerson1Occupation=cfg[ARG_KEY_CONFIG_NAME_PERSONA1_OCCUPATION],
                    innerPersonaPerson1Hobby=cfg[ARG_KEY_CONFIG_NAME_PERSONA1_HOBBY],
                    innerPersonaPerson1Personality=cfg[ARG_KEY_CONFIG_NAME_PERSONA1_PERSONALITY],
                    innerPersonaPerson1AnualSalary=cfg[ARG_KEY_CONFIG_NAME_PERSONA1_ANNUALSALARY],
                    innerPersonaPerson1ExtraPrompt=cfg[ARG_KEY_CONFIG_NAME_PERSONA1_EXTRAPROMPT],
                    innerPersonaPerson2Name=cfg[ARG_KEY_CONFIG_NAME_PERSONA2_NAME],
                    innerPersonaPerson2Age=cfg[ARG_KEY_CONFIG_NAME_PERSONA2_AGE],
                    innerPersonaPerson2Gender=cfg[ARG_KEY_CONFIG_NAME_PERSONA2_GENDER],
                    innerPersonaPerson2CountryOfOrigin=cfg[ARG_KEY_CONFIG_NAME_PERSONA2_COUNTRYOFORIGIN],
                    innerPersonaPerson2MyLanguage=cfg[ARG_KEY_CONFIG_NAME_PERSONA2_MYLANGUAGE],
                    innerPersonaPerson2Occupation=cfg[ARG_KEY_CONFIG_NAME_PERSONA2_OCCUPATION],
                    innerPersonaPerson2Hobby=cfg[ARG_KEY_CONFIG_NAME_PERSONA2_HOBBY],
                    innerPersonaPerson2Personality=cfg[ARG_KEY_CONFIG_NAME_PERSONA2_PERSONALITY],
                    innerPersonaPerson2AnualSalary=cfg[ARG_KEY_CONFIG_NAME_PERSONA2_ANNUALSALARY],
                    innerPersonaPerson2ExtraPrompt=cfg[ARG_KEY_CONFIG_NAME_PERSONA2_EXTRAPROMPT],
                    innerPersonaSubject=cfg[ARG_KEY_CONFIG_NAME_SUBJECT],
                    innerPersonaExtraPrompt=cfg[ARG_KEY_CONFIG_NAME_EXTRAPROMPT],
                    innerPersonaWordCountOf1Line=cfg[ARG_KEY_CONFIG_NAME_WORDCOUNTOF1LINE],
                    innerCfgMotherLanguage=cfg[ARG_KEY_CONFIG_NAME_CFGMOTHERLANGUAGE],
                    innerAsrTableHeaderNoStr=ASR_TABLE_HEADER_NO_STR,
                    innerAsrTableHeaderPersonNameStr=ASR_TABLE_HEADER_PERSONNAME_STR,
                    innerAsrTableHeaderSentenceStr=ASR_TABLE_HEADER_SENTENCE_STR,
                    innerAsrTableHeaderSentence2Str=ASR_TABLE_HEADER_SENTENCE2_STR,
                    innerAsrTableHeaderDevideStr=ASR_TABLE_HEADER_DEVIDE_STR,
                    innerAsrTableHeaderMotherLanguageTranslationStr=ASR_TABLE_HEADER_MOTHERLANGUAGETRANSLATION_STR,
                    innerAsrTableHeaderStr=ASR_TABLE_HEADER_STR,
                    innerTotalCountOfSentences=cfg[ARG_KEY_CONFIG_NAME_TOTALCOUNTOFSENTENCES],
                    innerResponseCountPerResponse=ASR_RESPONSE_COUNT_PER_RESPONSE
                    )
    else:
        if lang == "kor":
            return '''
지금부터 {innerPersonaPerson1Name} 발표자 1명이 관객들 앞에서 강의를 하기 위해 준비 하는 발표 스크립트를 작성해줘.

발표자인 {innerPersonaPerson1Name}의 역할을 정의해 줄께.
나이는 {innerPersonaPerson1Age}, 성별은 {innerPersonaPerson1Gender}, 출신 국가는 {innerPersonaPerson1CountryOfOrigin}, 직업은 {innerPersonaPerson1Occupation} 이고,
취미는 {innerPersonaPerson1Hobby}, 성격은 {innerPersonaPerson1Personality}, 연봉은 {innerPersonaPerson1AnualSalary} 이다.
{innerPersonaPerson1Name}는 모국어인 {innerPersonaPerson1MyLanguage} 로 발표를 한다.
{innerPersonaPerson1ExtraPrompt}

발표자는 {innerPersonaSubject} 주제에 대하여 구체적인 예시를 제시하면서 자세하게 설명할 것이다.
참고문서와 구체적인 예시는 각종 신문 기사나 블로그를 활용하고, 일반인들이 충분히 이해할 수 있는 쉬운 단어와 문장으로 작성해줘.
분량은 1시간 이상이 될수 있도록 작성하고, 이야기의 내용은 자연스럽게 이어져야 하며, 주제는 명확하고 일관되어야 해.
본문의 흐름은 서론/본론/결론의 형식에 맞도록 작성해줘.
{innerPersonaExtraPrompt}

#문장생성 주요기준(3가지)
1) "{innerAsrTableHeaderSentenceStr}" 열의 문장은 문법과 철자에 오류가 전혀 없어야 함.
2) "{innerAsrTableHeaderSentenceStr}" 열의 문장에 인종차별,욕설,비속어가 포함되면 안됨.
3) "{innerAsrTableHeaderSentenceStr}" 열의 문장에 개인정보와 민감한 정보가 포함되면 안됨.

#답변 주요기준(9가지)
1) 답변은 아래 "#답변 형식" 처럼 반드시 1개의 표 형식으로 작성할 것.
2) 표 이외의 다른 문장은 절대 적지 말것.
3) 열은 "{innerAsrTableHeaderNoStr}","{innerAsrTableHeaderPersonNameStr}","{innerAsrTableHeaderSentenceStr}","{innerAsrTableHeaderSentence2Str}","{innerAsrTableHeaderMotherLanguageTranslationStr}" 순서대로 작성할 것.
4) "{innerAsrTableHeaderSentenceStr}"열은 모국어인 {innerPersonaPerson1MyLanguage} 언어로 작성할 것.
5) "{innerAsrTableHeaderSentenceStr}"열은 {innerPersonaSubject} 주제에 맞게 생성된 문장을 최대 {innerPersonaWordCountOf1Line} 단어를 넘지 않도록 작성할 것.
6) "{innerAsrTableHeaderSentence2Str}"열은 "DUMMY"로 작성할 것.
7) "{innerAsrTableHeaderMotherLanguageTranslationStr}" 열은 "{innerAsrTableHeaderSentenceStr}" 열에서 생성된 문장을 {innerCfgMotherLanguage} 언어로 번역한 문장을 작성할 것.
8) 전체 스크립트 내용에 같은 문장을 절대 반복 하지 말것.
9) 표의 각 열은 반드시 |로 시작하여 |로 끝나야 할것.

#답변 형식
{innerAsrTableHeaderStr}
{innerAsrTableHeaderDevideStr}
| 1|{innerPersonaPerson1Name}|{innerPersonaSubject} 주제에 맞게 생성된 문장을 모국어인 {innerPersonaPerson1MyLanguage} 언어로 작성할 것|DUMMY|"{innerAsrTableHeaderSentenceStr}"열에서 생성된 문장을 {innerCfgMotherLanguage} 언어로 번역한 문장을 작성할 것 |
| 2|{innerPersonaPerson1Name}|{innerPersonaSubject} 주제에 맞게 생성된 문장을 모국어인 {innerPersonaPerson1MyLanguage} 언어로 작성할 것|DUMMY|"{innerAsrTableHeaderSentenceStr}"열에서 생성된 문장을 {innerCfgMotherLanguage} 언어로 번역한 문장을 작성할 것 |

#예시 문장(경우. 발표자의 모국어가 한국어 이고, 영어로 번역을 하는 경우)
{innerAsrTableHeaderStr}
{innerAsrTableHeaderDevideStr}
| 1|{innerPersonaPerson1Name}|안녕하세요 지금부터 영화에 대해 소개를 하겠습니다.|DUMMY|Hello, I will now introduce a movie. |
| 2|{innerPersonaPerson1Name}|오늘 소개할 영화는 스티븐 킹이 1982년에 집필한 <리타 헤이워스와 쇼생크 탈출>을 원작으로 하는 '쇼생크 탈출'입니다.|DUMMY|The movie I will introduce today is 'The Shawshank Redemption', based on Stephen King's 1982 novella 'Rita Hayworth and Shawshank Redemption'. |

발표 스크립트의 내용은 자연스럽게 이어져야 하며, 총 {innerTotalCountOfSentences}개 문장이 되기 전까지 계속 요청할 것이다. 
먼저 {innerResponseCountPerResponse}개 문장을 답변해 줘.
''' \
            .format(innerPersonaPerson1Name=cfg[ARG_KEY_CONFIG_NAME_PERSONA1_NAME],
                    innerPersonaPerson1Age=cfg[ARG_KEY_CONFIG_NAME_PERSONA1_AGE],
                    innerPersonaPerson1Gender=cfg[ARG_KEY_CONFIG_NAME_PERSONA1_GENDER],
                    innerPersonaPerson1CountryOfOrigin=cfg[ARG_KEY_CONFIG_NAME_PERSONA1_COUNTRYOFORIGIN],
                    innerPersonaPerson1MyLanguage=cfg[ARG_KEY_CONFIG_NAME_PERSONA1_MYLANGUAGE],
                    innerPersonaPerson1Occupation=cfg[ARG_KEY_CONFIG_NAME_PERSONA1_OCCUPATION],
                    innerPersonaPerson1Hobby=cfg[ARG_KEY_CONFIG_NAME_PERSONA1_HOBBY],
                    innerPersonaPerson1Personality=cfg[ARG_KEY_CONFIG_NAME_PERSONA1_PERSONALITY],
                    innerPersonaPerson1AnualSalary =cfg[ARG_KEY_CONFIG_NAME_PERSONA1_ANNUALSALARY],
                    innerPersonaPerson1ExtraPrompt=cfg[ARG_KEY_CONFIG_NAME_PERSONA1_EXTRAPROMPT],

                    innerPersonaSubject=cfg[ARG_KEY_CONFIG_NAME_SUBJECT],
                    innerPersonaWordCountOf1Line=cfg[ARG_KEY_CONFIG_NAME_WORDCOUNTOF1LINE],
                    innerCfgMotherLanguage=cfg[ARG_KEY_CONFIG_NAME_CFGMOTHERLANGUAGE],
                    innerPersonaExtraPrompt = cfg[ARG_KEY_CONFIG_NAME_EXTRAPROMPT],
                    innerAsrTableHeaderNoStr=ASR_TABLE_HEADER_NO_STR,
                    innerAsrTableHeaderPersonNameStr=ASR_TABLE_HEADER_PERSONNAME_STR,
                    innerAsrTableHeaderSentenceStr=ASR_TABLE_HEADER_SENTENCE_STR,
                    innerAsrTableHeaderSentence2Str=ASR_TABLE_HEADER_SENTENCE2_STR,
                    innerAsrTableHeaderDevideStr=ASR_TABLE_HEADER_DEVIDE_STR,
                    innerAsrTableHeaderMotherLanguageTranslationStr=ASR_TABLE_HEADER_MOTHERLANGUAGETRANSLATION_STR,
                    innerAsrTableHeaderStr = ASR_TABLE_HEADER_STR,
                    innerTotalCountOfSentences = cfg[ARG_KEY_CONFIG_NAME_TOTALCOUNTOFSENTENCES],
                    innerResponseCountPerResponse = ASR_RESPONSE_COUNT_PER_RESPONSE
                    )
        else:
            return '''
From now on, please write a presentation script where one presenter, {innerPersonaPerson1Name}, is preparing to give a lecture in front of an audience.

I will define the role of the presenter {innerPersonaPerson1Name}.
The presenter's age is {innerPersonaPerson1Age}, gender is {innerPersonaPerson1Gender}, country of origin is {innerPersonaPerson1CountryOfOrigin}, occupation is {innerPersonaPerson1Occupation}, 
hobby is {innerPersonaPerson1Hobby}, personality is {innerPersonaPerson1Personality}, and annual salary is {innerPersonaPerson1AnualSalary}.
{innerPersonaPerson1Name} will deliver the presentation in their native language, {innerPersonaPerson1MyLanguage}. 
{innerPersonaPerson1ExtraPrompt}

The presenter will provide specific examples on the topic of {innerPersonaSubject} and explain them in detail.
Reference materials and specific examples should be based on various newspaper articles or blogs, and the sentences should be written using easy-to-understand vocabulary and phrasing for the general public.
The script should be written to last more than 1 hour, with the content naturally flowing, and the topic being clear and consistent. 
The structure should follow the format of introduction/body/conclusion.
{innerPersonaExtraPrompt}

#Main Criteria for Sentence Generation (3 points)
1) The sentence in the "{innerAsrTableHeaderSentenceStr}" column must be free of grammatical and spelling errors.
2) The sentence in the "{innerAsrTableHeaderSentenceStr}" column must not contain any racial discrimination, profanity, or slang.
3) The sentence in the "{innerAsrTableHeaderSentenceStr}" column must not include any personal or sensitive information.

#Main Criteria for Responses (9 points)
1) The response must be formatted as a single table as shown below in the "#Answer Format".
2) Do not write any sentences other than the table.
3) The columns must be written in the following order: "{innerAsrTableHeaderNoStr}", "{innerAsrTableHeaderPersonNameStr}", "{innerAsrTableHeaderSentenceStr}", "{innerAsrTableHeaderSentence2Str}", "{innerAsrTableHeaderMotherLanguageTranslationStr}".
4) The sentence in the "{innerAsrTableHeaderSentenceStr}" column must be written in the native language {innerPersonaPerson1MyLanguage}.
5) The sentence in the "{innerAsrTableHeaderSentenceStr}" column must be generated based on the topic of {innerPersonaSubject} and written with no more than {innerPersonaWordCountOf1Line} words.
6) The "{innerAsrTableHeaderSentence2Str}" column must be filled with "DUMMY".
7) The sentence in the "{innerAsrTableHeaderMotherLanguageTranslationStr}" column must translate the sentence from the "{innerAsrTableHeaderSentenceStr}" column into {innerCfgMotherLanguage}.
8) Never repeat the same sentences throughout the entire script.
9) Each column in the table must start and end with |.

#Answer Format
{innerAsrTableHeaderStr}
|---|---|---|---|
| 1|{innerPersonaPerson1Name}|Write a sentence generated based on the topic {innerPersonaSubject} in the native language {innerPersonaPerson1MyLanguage}|DUMMY|Translate the sentence from the "{innerAsrTableHeaderSentenceStr}" column into {innerCfgMotherLanguage} |
| 2|{innerPersonaPerson1Name}|Write a sentence generated based on the topic {innerPersonaSubject} in the native language {innerPersonaPerson1MyLanguage}|DUMMY|Translate the sentence from the "{innerAsrTableHeaderSentenceStr}" column into {innerCfgMotherLanguage} |

#Example Sentences (Case: The presenter's native language is Korean, and the translation is being made into English)
{innerAsrTableHeaderStr}
{innerAsrTableHeaderDevideStr}
| 1|{innerPersonaPerson1Name}|안녕하세요 지금부터 영화에 대해 소개를 하겠습니다.|DUMMY|Hello, I will now introduce a movie. |
| 2|{innerPersonaPerson1Name}|오늘 소개할 영화는 스티븐 킹이 1982년에 집필한 <리타 헤이워스와 쇼생크 탈출>을 원작으로 하는 '쇼생크 탈출'입니다.|DUMMY|The movie I will introduce today is 'The Shawshank Redemption', based on Stephen King's 1982 novella 'Rita Hayworth and Shawshank Redemption'. |

The content of the presentation script should flow naturally, and I will continue to request until the total number of sentences reaches {innerTotalCountOfSentences}.
Please provide {innerResponseCountPerResponse} sentences in response first.
''' \
            .format(innerPersonaPerson1Name=cfg[ARG_KEY_CONFIG_NAME_PERSONA1_NAME],
                    innerPersonaPerson1Age=cfg[ARG_KEY_CONFIG_NAME_PERSONA1_AGE],
                    innerPersonaPerson1Gender=cfg[ARG_KEY_CONFIG_NAME_PERSONA1_GENDER],
                    innerPersonaPerson1CountryOfOrigin=cfg[ARG_KEY_CONFIG_NAME_PERSONA1_COUNTRYOFORIGIN],
                    innerPersonaPerson1MyLanguage=cfg[ARG_KEY_CONFIG_NAME_PERSONA1_MYLANGUAGE],
                    innerPersonaPerson1Occupation=cfg[ARG_KEY_CONFIG_NAME_PERSONA1_OCCUPATION],
                    innerPersonaPerson1Hobby=cfg[ARG_KEY_CONFIG_NAME_PERSONA1_HOBBY],
                    innerPersonaPerson1Personality=cfg[ARG_KEY_CONFIG_NAME_PERSONA1_PERSONALITY],
                    innerPersonaPerson1AnualSalary =cfg[ARG_KEY_CONFIG_NAME_PERSONA1_ANNUALSALARY],
                    innerPersonaPerson1ExtraPrompt=cfg[ARG_KEY_CONFIG_NAME_PERSONA1_EXTRAPROMPT],

                    innerPersonaSubject=cfg[ARG_KEY_CONFIG_NAME_SUBJECT],
                    innerPersonaWordCountOf1Line=cfg[ARG_KEY_CONFIG_NAME_WORDCOUNTOF1LINE],
                    innerCfgMotherLanguage=cfg[ARG_KEY_CONFIG_NAME_CFGMOTHERLANGUAGE],
                    innerPersonaExtraPrompt = cfg[ARG_KEY_CONFIG_NAME_EXTRAPROMPT],
                    innerAsrTableHeaderNoStr=ASR_TABLE_HEADER_NO_STR,
                    innerAsrTableHeaderPersonNameStr=ASR_TABLE_HEADER_PERSONNAME_STR,
                    innerAsrTableHeaderSentenceStr=ASR_TABLE_HEADER_SENTENCE_STR,
                    innerAsrTableHeaderSentence2Str=ASR_TABLE_HEADER_SENTENCE2_STR,
                    innerAsrTableHeaderDevideStr=ASR_TABLE_HEADER_DEVIDE_STR,
                    innerAsrTableHeaderMotherLanguageTranslationStr=ASR_TABLE_HEADER_MOTHERLANGUAGETRANSLATION_STR,
                    innerAsrTableHeaderStr = ASR_TABLE_HEADER_STR,
                    innerTotalCountOfSentences = cfg[ARG_KEY_CONFIG_NAME_TOTALCOUNTOFSENTENCES],
                    innerResponseCountPerResponse = ASR_RESPONSE_COUNT_PER_RESPONSE
                    )

print(makeScript())