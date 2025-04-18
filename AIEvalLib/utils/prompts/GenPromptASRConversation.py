# -*- coding: utf-8 -*-
from GlobalUtil import langname_from_locale
from prompts.IScorePrompt import IScorePrompt
from utils.GlobalVars import *

class GenPromptASRConversation(IScorePrompt):
    def __init__(self, argArgs):
        if argArgs is None:
            self.mArgs = None
            self.mUseKorPrompt = False
        else:
            self.mArgs = argArgs     # copy from org arg
            # self.mArgs.update_InnerArgs(self.mArgs.copy_InnerArgs())  # copy from org's prompt args

            if self.mArgs.getValInnerArg(ARG_KEY_NAME_MOTHERLANGUAGE).lower() == 'korean':
                self.mUseKorPrompt = True
            else:
                self.mUseKorPrompt = False

        print(f'self.mUseKorPrompt:{self.mUseKorPrompt}')

    def get_my_keyname(self):
        return CONFIG_NAME_VALUE_CONVERSATION

    def get_my_csvname(self):
        if self.mArgs.getValInnerArg(ARG_KEY_NAME_PROMPTTYPE) is not None:
            return self.mArgs.getValInnerArg(ARG_KEY_NAME_PROMPTTYPE)

        return f'sentences_{CONFIG_NAME_VALUE_CONVERSATION}.csv'

    def get_noti_role_prompt(self):
        if self.mArgs is None:
            return ''

        if self.mUseKorPrompt:
            return \
                '''지금부터 {innerPersonaPerson1Name},{innerPersonaPerson2Name} 두사람이 직접 일상적인 대화를 나누는 문장을 작성해줘.
일상적인 대화처럼 쉬운 단어와 문장을 주로 사용하고, 상대방의 말에 가벼운 질문과 농담, 칭찬, 조언도 섞어서 함께 사용할 것.

# 문장생성 주요기준(12가지)
1) 열의 순서는 {innerAsrTableHeaderNoStr},{innerAsrTableHeaderPersonNameStr},{innerAsrTableHeaderSentenceStr},{innerAsrTableHeaderSentence2Str},{innerAsrTableHeaderMotherLanguageTranslationStr} 순서대로 작성할 것.
2) {innerAsrTableHeaderSentenceStr}열과 {innerAsrTableHeaderSentence2Str}열의 문장에는 문법 오류 및 철자 오류, 욕설, 비속어는 포함하지 말고, 주어진 대화 주제가 유지되도록 할 것.
3) 대화 이외의 묘사나 서술(예: '(차량 방향제를 찾으러 가며)', '(혼잣말)', '(손님을 도우며)' 등) 문장은 절대 사용하지 말고, 오직 대화만 작성할 것.
4) 대화 문장들은 동일 문장의 반복 없이, 복합 문장을 다양하게 사용하여 작성할 것.
5) 감사의 인사나 작별 인사는 절대 반복하지 말고, 반복되는 의미의 문장은 다른 형식의 문장으로 표현할 것.
6) 실제 대화에서 일어날 수 있는 대화 내용으로 다양한 표현을 사용하는 문장으로 작성할 것.
7) {innerIntTotalCountOfSentences}번째 문장까지는 대화가 주제에 맞도록 일관성이 유지되어야 하여, 감사의 인사나 작별 인사는 {innerIntTotalCountOfSentences}번째 문장이후부터 할것.
8) {innerAsrTableHeaderSentenceStr}열의 문장은 {innerPersonaPerson1MyLanguage} 언어로 작성할 것.
9) {innerAsrTableHeaderSentence2Str}열의 문장은 {innerPersonaPerson2MyLanguage} 언어로 작성할 것.
10) {innerAsrTableHeaderMotherLanguageTranslationStr}열은 {innerPersonaPerson1Name}의 언어가 {innerCfgMotherLanguage}이면, {innerAsrTableHeaderSentenceStr} 문장을 변경없이 {innerAsrTableHeaderMotherLanguageTranslationStr}열에 적고, 만일 언어가 다르면 {innerAsrTableHeaderSentenceStr} 열의 문장을 {innerCfgMotherLanguage} 언어로 번역한 문장을 적을것.
11) 대화의 시작은 반드시 {innerPersonaPerson1Name}가 먼저 시작할 것.
12) 만일 대화 문장생성이 실패하여, 답변이 "I'm sorry, I can't assist with that request."이면, 이유를 {innerCfgMotherLanguage} 언어로 같이 설명해줘.

# 답변 주요기준(3가지)
1) 답변은 반드시 "#답변 형식"의 Markdown Table 로만 작성하고, Table은 ** 반드시 ** 1개만 사용할 것.
2) 답변에는 Markdown Table 이외 문장을 ** 절대 ** 사용하지 말것.
3) Markdown Table의 모든 열은 ** 반드시 ** "|"로 시작하여 "|"로 끝나야 할것.

# 답변 형식
{innerAsrTableHeaderStr}
{innerAsrTableHeaderDevideStr}
| 1 | {innerPersonaPerson1Name} | [{innerPersonaPerson1Name}의 대화 문장을 ** 반드시 ** {innerPersonaPerson1MyLanguage} 언어로 작성할 것] | [{innerAsrTableHeaderSentenceStr}열의 문장을 ** 반드시 ** {innerPersonaPerson2MyLanguage} 언어로 번역하여 {innerAsrTableHeaderSentence2Str}열에 작성할 것] | [{innerAsrTableHeaderSentenceStr}열의 문장을 ** 반드시 ** {innerCfgMotherLanguage} 언어로 {innerAsrTableHeaderMotherLanguageTranslationStr}열에 작성할 것 | 
| 2 | {innerPersonaPerson2Name} | [{innerPersonaPerson2Name}의 대화 문장을 ** 반드시 ** {innerPersonaPerson1MyLanguage} 언어로 작성할 것] | [{innerAsrTableHeaderSentenceStr}열의 문장을 ** 반드시 ** {innerPersonaPerson2MyLanguage} 언어로 번역하여 {innerAsrTableHeaderSentence2Str}열에 작성할 것] | [{innerAsrTableHeaderSentenceStr}열의 문장을 ** 반드시 ** {innerCfgMotherLanguage} 언어로 {innerAsrTableHeaderMotherLanguageTranslationStr}열에 작성할 것 |

전체 {innerTotalCountOfSentences}개 대화 문장이 완성되도록
"# 문장생성 주요기준", "# 답변 주요기준", "# 답변 형식"을 ** 반드시 ** 지켜서 답변해줘.''' \
                    .format(
                            innerPersonaSubject=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_SUBJECT),
                            innerPersonaPerson1Name=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_NAME),
                            innerPersonaPerson1MyLanguage=langname_from_locale(locale=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_MYLANGUAGE)),

                            innerPersonaPerson2Name=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA2_NAME),
                            innerPersonaPerson2MyLanguage=langname_from_locale(locale=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA2_MYLANGUAGE)),

                            innerCfgMotherLanguage=langname_from_locale(locale=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_CFGMOTHERLANGUAGE)),
                            innerAsrTableHeaderNoStr=ASR_TABLE_HEADER_NO_STR,
                            innerAsrTableHeaderPersonNameStr=ASR_TABLE_HEADER_PERSONNAME_STR,
                            innerAsrTableHeaderSentenceStr=ASR_TABLE_HEADER_SENTENCE_STR,
                            innerAsrTableHeaderSentence2Str=ASR_TABLE_HEADER_SENTENCE2_STR,
                            innerAsrTableHeaderDevideStr=ASR_TABLE_HEADER_DEVIDE_STR,
                            innerAsrTableHeaderMotherLanguageTranslationStr=ASR_TABLE_HEADER_MOTHERLANGUAGETRANSLATION_STR,
                            innerAsrTableHeaderStr=ASR_TABLE_HEADER_STR,
                            innerTotalCountOfSentences=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_TOTALCOUNTOFSENTENCES),
                            innerIntTotalCountOfSentences=int(self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_TOTALCOUNTOFSENTENCES)),
                    )
        else:
            return \
                '''From now on, please write sentences where {innerPersonaPerson1Name} and {innerPersonaPerson2Name} engage in everyday conversations directly. 
Use simple words and sentences like in everyday conversations, and include light questions, jokes, compliments, and advice when responding to the other person.

# Main criteria for sentence creation (12 rules)
1) The order of columns should be written as {innerAsrTableHeaderNoStr}, {innerAsrTableHeaderPersonNameStr}, {innerAsrTableHeaderSentenceStr}, {innerAsrTableHeaderSentence2Str}, and {innerAsrTableHeaderMotherLanguageTranslationStr}.
2) The sentences in the {innerAsrTableHeaderSentenceStr} column and {innerAsrTableHeaderSentence2Str} column should not contain any grammatical or spelling errors, swear words, or slang, and should maintain the given conversation topic.
3) Do not use descriptions or narration other than the dialogues themselves (e.g., '(while looking for the car freshener)', '(talking to themselves)', '(helping a customer)'). Only write dialogues.
4) The conversation sentences should be diverse, avoiding repetitive sentences, and use varied compound sentences.
5) Avoid repeating gratitude or farewells, and express similar meanings using different sentence structures.
6) Write dialogues using diverse expressions that can realistically occur in a conversation.
7) Ensure the dialogue maintains consistency with the topic up until the {innerIntTotalCountOfSentences}th sentence, and gratitude or farewells should be written only after the {innerIntTotalCountOfSentences}th sentence.
8) The {innerAsrTableHeaderSentenceStr} column sentences should be written in the {innerPersonaPerson1MyLanguage}.
9) The {innerAsrTableHeaderSentence2Str} column sentences should be written in the {innerPersonaPerson2MyLanguage}.
10) In the {innerAsrTableHeaderMotherLanguageTranslationStr} column, if {innerPersonaPerson1Name}'s language is {innerCfgMotherLanguage}, write the {innerAsrTableHeaderSentenceStr} sentence as is; if the language is different, translate the sentence in the {innerAsrTableHeaderSentenceStr} column into the {innerCfgMotherLanguage}.
11) Always start the dialogue with {innerPersonaPerson1Name}.
12) If the generation of the conversation sentences fails, resulting in "I'm sorry, I can't assist with that request.", explain the reason in {innerCfgMotherLanguage}.

# Main criteria for response (3 rules)
1) Responses should only be written as a "#Response Format" Markdown Table, and ** must ** include exactly one table.
2) Do not include any sentences other than the Markdown Table in the response.
3) All columns in the Markdown Table ** must ** begin and end with "|".

# Response Format
{innerAsrTableHeaderStr}
{innerAsrTableHeaderDevideStr}
| 1 | {innerPersonaPerson1Name} | [The conversation sentence of {innerPersonaPerson1Name} ** must ** be written in {innerPersonaPerson1MyLanguage}] | [The sentence in the {innerAsrTableHeaderSentenceStr} column ** must ** be translated into {innerPersonaPerson2MyLanguage} and written in the {innerAsrTableHeaderSentence2Str} column] | [The sentence in the {innerAsrTableHeaderSentenceStr} column ** must ** be translated into {innerCfgMotherLanguage} and written in the {innerAsrTableHeaderMotherLanguageTranslationStr} column] | 
| 2 | {innerPersonaPerson2Name} | [The conversation sentence of {innerPersonaPerson2Name} ** must ** be written in {innerPersonaPerson1MyLanguage}] | [The sentence in the {innerAsrTableHeaderSentenceStr} column ** must ** be translated into {innerPersonaPerson2MyLanguage} and written in the {innerAsrTableHeaderSentence2Str} column] | [The sentence in the {innerAsrTableHeaderSentenceStr} column ** must ** be translated into {innerCfgMotherLanguage} and written in the {innerAsrTableHeaderMotherLanguageTranslationStr} column] |

Ensure the dialogue completes with a total of {innerTotalCountOfSentences} conversation sentences while strictly following the "# Main criteria for sentence creation", "# Main criteria for response", and "# Response Format".''' \
                    .format(innerPersonaSubject=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_SUBJECT),
                            innerPersonaPerson1Name=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_NAME),
                            innerPersonaPerson1MyLanguage=langname_from_locale(locale=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_MYLANGUAGE)),

                            innerPersonaPerson2Name=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA2_NAME),
                            innerPersonaPerson2MyLanguage=langname_from_locale(locale=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA2_MYLANGUAGE)),

                            innerCfgMotherLanguage=langname_from_locale(locale=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_CFGMOTHERLANGUAGE)),
                            innerAsrTableHeaderNoStr=ASR_TABLE_HEADER_NO_STR,
                            innerAsrTableHeaderPersonNameStr=ASR_TABLE_HEADER_PERSONNAME_STR,
                            innerAsrTableHeaderSentenceStr=ASR_TABLE_HEADER_SENTENCE_STR,
                            innerAsrTableHeaderSentence2Str=ASR_TABLE_HEADER_SENTENCE2_STR,
                            innerAsrTableHeaderDevideStr=ASR_TABLE_HEADER_DEVIDE_STR,
                            innerAsrTableHeaderMotherLanguageTranslationStr=ASR_TABLE_HEADER_MOTHERLANGUAGETRANSLATION_STR,
                            innerAsrTableHeaderStr=ASR_TABLE_HEADER_STR,
                            innerTotalCountOfSentences=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_TOTALCOUNTOFSENTENCES),
                            innerIntTotalCountOfSentences=int(self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_TOTALCOUNTOFSENTENCES)),
                            )

    def get_do_score_prompt(self):
        if self.mArgs is None:
            return ''

        if self.mUseKorPrompt:
            return '''두 사람은 "{innerPersonaSubject}"에 대해 대화를 나누고 있고,
{innerPersonaExtraPrompt}

아래와 같이 대화자 역할을 각각 정의한다.
이름:{innerPersonaPerson1Name}
나이:{innerPersonaPerson1Age}
성별:{innerPersonaPerson1Gender}
출신국가:{innerPersonaPerson1CountryOfOrigin}
직업:{innerPersonaPerson1Occupation}
취미:{innerPersonaPerson1Hobby}
성격:{innerPersonaPerson1Personality}
연봉:{innerPersonaPerson1AnnualSalary}
{innerPersonaPerson1ExtraPrompt}

이름:{innerPersonaPerson2Name}
나이:{innerPersonaPerson2Age}
성별:{innerPersonaPerson2Gender}
출신국가:{innerPersonaPerson2CountryOfOrigin}
직업:{innerPersonaPerson2Occupation}
취미:{innerPersonaPerson2Hobby}
성격:{innerPersonaPerson2Personality}
연봉:{innerPersonaPerson2AnnualSalary}
{innerPersonaPerson2ExtraPrompt}

주제에 맞는 자연스러운 문장을 사용하여, 5분 이상의 대화가 이어질수 있도록 전체 {innerTotalCountOfSentences}개를 작성해줘.
만일 제시된 주제와 상황이 너무 구체적이어서 자연스러운 대화 작성에 어려움이 있으면, 상황을 다시 단순화 시켜서 반드시 대화를 작성해줘.''' \
                .format(innerPersonaPerson1Name=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_NAME),
                        innerPersonaPerson1Age=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_AGE,DEFAULT_AGE),
                        innerPersonaPerson1Gender=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_GENDER,DEFAULT_GENDER),
                        innerPersonaPerson1CountryOfOrigin=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_COUNTRYOFORIGIN, langname_from_locale(locale=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_MYLANGUAGE))),
                        innerPersonaPerson1MyLanguage=langname_from_locale(locale=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_MYLANGUAGE)),
                        innerPersonaPerson1Occupation=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_OCCUPATION, DEFAULT_OCCUPATION),
                        innerPersonaPerson1Hobby=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_HOBBY, DEFAULT_HOBBY),
                        innerPersonaPerson1Personality=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_PERSONALITY, DEFAULT_PERSONALITY),
                        innerPersonaPerson1AnnualSalary=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_ANNUALSALARY, DEFAULT_ANNUALSALARY),
                        innerPersonaPerson1ExtraPrompt=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_EXTRAPROMPT),

                        innerPersonaPerson2Name=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA2_NAME),
                        innerPersonaPerson2Age=DEFAULT_AGE if(self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA2_AGE) == '') else (self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA2_AGE)),
                        innerPersonaPerson2Gender=DEFAULT_GENDER if(self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA2_GENDER) == '') else (self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA2_GENDER)),
                        innerPersonaPerson2CountryOfOrigin=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA2_COUNTRYOFORIGIN, langname_from_locale(locale=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA2_MYLANGUAGE))),
                        innerPersonaPerson2MyLanguage=langname_from_locale(locale=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA2_MYLANGUAGE)),
                        innerPersonaPerson2Occupation=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA2_OCCUPATION, DEFAULT_OCCUPATION),
                        innerPersonaPerson2Hobby=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA2_HOBBY, DEFAULT_HOBBY),
                        innerPersonaPerson2Personality=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA2_PERSONALITY, DEFAULT_PERSONALITY),
                        innerPersonaPerson2AnnualSalary=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA2_ANNUALSALARY, DEFAULT_ANNUALSALARY),
                        innerPersonaPerson2ExtraPrompt=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA2_EXTRAPROMPT),

                        innerPersonaSubject=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_SUBJECT),
                        innerPersonaExtraPrompt=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_EXTRAPROMPT),
                        innerTotalCountOfSentences=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_TOTALCOUNTOFSENTENCES),
                        )
        else:
            return ''''The two individuals are having a conversation about "{innerPersonaSubject}",  
{innerPersonaExtraPrompt}  

The roles of the speakers are defined as follows:  
Name: {innerPersonaPerson1Name}  
Age: {innerPersonaPerson1Age}  
Gender: {innerPersonaPerson1Gender}  
Country of Origin: {innerPersonaPerson1CountryOfOrigin}  
Occupation: {innerPersonaPerson1Occupation}  
Hobby: {innerPersonaPerson1Hobby}  
Personality: {innerPersonaPerson1Personality}  
Annual Salary: {innerPersonaPerson1AnnualSalary}  
{innerPersonaPerson1ExtraPrompt}  

Name: {innerPersonaPerson2Name}  
Age: {innerPersonaPerson2Age}  
Gender: {innerPersonaPerson2Gender}  
Country of Origin: {innerPersonaPerson2CountryOfOrigin}  
Occupation: {innerPersonaPerson2Occupation}  
Hobby: {innerPersonaPerson2Hobby}  
Personality: {innerPersonaPerson2Personality}  
Annual Salary: {innerPersonaPerson2AnnualSalary}  
{innerPersonaPerson2ExtraPrompt}  

Using natural sentences that suit the topic, create a conversation of {innerTotalCountOfSentences} lines to allow for at least 5 minutes of interaction.  
If the given topic and situation are too specific, making it difficult to create a natural conversation, please simplify the situation and make sure to write the conversation.''' \
                .format(innerPersonaPerson1Name=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_NAME),
                        innerPersonaPerson1Age=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_AGE, DEFAULT_AGE),
                        innerPersonaPerson1Gender=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_GENDER, DEFAULT_GENDER),
                        innerPersonaPerson1CountryOfOrigin=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_COUNTRYOFORIGIN, langname_from_locale(locale=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_MYLANGUAGE))),
                        innerPersonaPerson1MyLanguage=langname_from_locale(locale=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_MYLANGUAGE)),
                        innerPersonaPerson1Occupation=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_OCCUPATION, DEFAULT_OCCUPATION),
                        innerPersonaPerson1Hobby=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_HOBBY, DEFAULT_HOBBY),
                        innerPersonaPerson1Personality=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_PERSONALITY, DEFAULT_PERSONALITY),
                        innerPersonaPerson1AnnualSalary=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_ANNUALSALARY, DEFAULT_ANNUALSALARY),
                        innerPersonaPerson1ExtraPrompt=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA1_EXTRAPROMPT),

                        innerPersonaPerson2Name=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA2_NAME),
                        innerPersonaPerson2Age=DEFAULT_AGE if (self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA2_AGE) == '') else (self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA2_AGE)),
                        innerPersonaPerson2Gender=DEFAULT_GENDER if (self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA2_GENDER) == '') else (self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA2_GENDER)),
                        innerPersonaPerson2CountryOfOrigin=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA2_COUNTRYOFORIGIN, langname_from_locale(locale=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA2_MYLANGUAGE))),
                        innerPersonaPerson2MyLanguage=langname_from_locale(locale=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA2_MYLANGUAGE)),
                        innerPersonaPerson2Occupation=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA2_OCCUPATION, DEFAULT_OCCUPATION),
                        innerPersonaPerson2Hobby=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA2_HOBBY, DEFAULT_HOBBY),
                        innerPersonaPerson2Personality=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA2_PERSONALITY, DEFAULT_PERSONALITY),
                        innerPersonaPerson2AnnualSalary=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA2_ANNUALSALARY, DEFAULT_ANNUALSALARY),
                        innerPersonaPerson2ExtraPrompt=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_PERSONA2_EXTRAPROMPT),

                        innerPersonaSubject=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_SUBJECT),
                        innerPersonaExtraPrompt=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_EXTRAPROMPT),
                        innerTotalCountOfSentences=self.mArgs.getValInnerArg(ARG_KEY_CONFIG_NAME_TOTALCOUNTOFSENTENCES),
                        )

    # 번역 평가 결과의 형식을 다시 한번 요청할 경우,
    def get_again_form_prompt(self):
        if self.mArgs is None:
            return ''

        if self.mUseKorPrompt:
            return ''
        else:
            return ''

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
