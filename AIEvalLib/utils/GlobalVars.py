# -*- coding: utf-8 -*-

g_sys_my_pmt = None
g_str_token_split = r'@|@'
g_str_pattern_split = r'@\|@'
LIMIT_MIN_SENTENCE_LENGTH = 4
SENTENCES_SPLITTED_COUNT = 4
SENTENCES_MAX_COUNT = 3000

TEXT_PROMPT_MODE_ASSISTANT = 0
TEXT_PROMPT_MODE_COMPLETION = 1

# EVALIMG
LIMIT_MIN_INPUT_COLUMN_COUNT = 4

# AWS Variable
AI_VOICE_AWS_REGION_NAME = 'us-east-1'
AI_VOICE_AWS_SVC_NAME = 'polly'

AI_VOICE_SAVE_FILE_EXT = 'mp3'
AI_VOICE_AWS_ENGINE = 'neural'

# ElevenLabs
AI_VOICE_AWS_LANG_TYPE_MULTI_v2 = "eleven_multilingual_v2"
AI_VOICE_AWS_VOICE_TYPE_mp3_44100_128 = "mp3_44100_128"

ARGS_DEF_MOTHER_LANGUAGE = r'Korean'
ARGS_DEF_SOURCE_LANGUAGE = r'Korean'
ARGS_DEF_TARGET_LANGUAGE = r'English'
ARGS_DEF_SENTENCES_COUNT = r'4'
ARGS_DEF_SENTENCES_CATEGORY = r'economy'
SENTENCES_MIN_TOTAL_COUNT: int = 20
SENTENCES_MAX_TOTAL_COUNT: int = 100
ARGS_DEF_SENTENCES_TOTAL_COUNT: int = SENTENCES_MAX_TOTAL_COUNT
ARGS_DEF_INPUT_CSV_NAME = r'input.csv'
ARGS_DEF_NEED_RETRY_CFGS_NAME = r'need_retry_cfgs.txt'
ARGS_DEF_INPUT_DIR_PATH = None
ARGS_DEF_OUTPUT_DIR_PATH = None
ARGS_DEF_NORESPONSEINOUT = False

PROMPT_KEY_NAME_TRANS = r'trans'  # prompttype
PROMPT_KEY_NAME_CORRECT = r'correct'
PROMPT_KEY_NAME_EMOJI = r'emoji'
PROMPT_KEY_NAME_TONEPROFESSIONAL = r'toneprofessional'
PROMPT_KEY_NAME_TONECASUAL = r'tonecasual'
PROMPT_KEY_NAME_TONESOCIAL = r'tonesocial'
PROMPT_KEY_NAME_TONEPOLITE = r'tonepolite'
PROMPT_KEY_NAME_GENASR = r'genasr'
PROMPT_KEY_NAME_EVALIMG = r'evalimg'
PROMPT_KEY_NAME_EVALCAPTION = r'evalcaption'

PROMPT_COMMAND_KEY_NAME_NOTIROLE = r'noti_role'
PROMPT_COMMAND_KEY_NAME_DOSCORE = r'do_score'
PROMPT_COMMAND_KEY_NAME_AGAINFORM = r'again_form'
PROMPT_COMMAND_KEY_NAME_AGAINFORM_TRANS = r'again_trans'
PROMPT_COMMAND_KEY_NAME_TEMPLATE = r'make_templete'
PROMPT_COMMAND_KEY_NAME_GENSENTS = r'gen_sentences'

ARG_KEY_NAME_UNIQUE_TESTID: str = r'unique_testid'

ARG_KEY_NAME_ENGINETYPE = r'enginetype'
ARG_KEY_NAME_ENGINEMODEL = r'enginemodel'
ARG_KEY_NAME_ENGINEDEPLOYNAME = r'enginedeployname'
ARG_KEY_NAME_PROMPTTYPE = r'prompttype'
ARG_KEY_NAME_MOTHERLANGUAGE = r'motherlanguage'
ARG_KEY_NAME_SOURCELANGUAGE = r'sourcelanguage'
ARG_KEY_NAME_TARGETLANGUAGE = r'targetlanguage'
ARG_KEY_NAME_SENTENCESCOUNT = r'sentencescount'     # Split Sentences count per 1 cycle.
ARG_KEY_NAME_SENTENCESLENGTH = r'sentenceslength'
ARG_KEY_NAME_SENTENCESCATEGORY = r'sentencescategory'
ARG_KEY_NAME_TOTALSENTENCESCNT = r'totalsentencescnt'
ARG_KEY_NAME_MAKESENTENCESCNT = r'makesentencescnt'
ARG_KEY_NAME_INPUTCSVNAME = r'inputcsvname'
ARG_KEY_NAME_INPUTCONFIGNAME = r'inputconfigname'
ARG_KEY_NAME_INPUTDIR = r'inputdir'
ARG_KEY_NAME_INIMGDIR = r'inimgdir'
ARG_KEY_NAME_OUTIMGDIR = r'outimgdir'
ARG_KEY_NAME_OUTPUTDIR = r'outputdir'
ARG_KEY_NAME_THREADNUM = r'threadnum'
ARG_KEY_NAME_NORESPONSEINOUT = r'noresponseinout'

ARG_KEY_NAME_IINIMGDIR = r'iinimgdir'
ARG_KEY_NAME_IOUTIMGDIR = r'ioutimgdir'
ARG_KEY_NAME_SKIPGENAITTS = r'skipgenaitts'
ARG_KEY_NAME_SKIPGENSCENINFILE = r'skipgensceninfile'

ARG_KEY_NAME_VOICEID = r'voiceid'
ARG_KEY_NAME_SKIPUNIQUETID = r'skipuniquetid'

ARG_KEY_NAME_HAS_INPUT_IMAGE = r'hasinputimage'

ASR_TABLE_HEADER_NO_STR = r'''No'''
ASR_TABLE_HEADER_PERSONNAME_STR = r'''PersonName'''
ASR_TABLE_HEADER_SENTENCE_STR = r'''Sentence'''
ASR_TABLE_HEADER_SENTENCE2_STR = r'''Sentence2'''
ASR_TABLE_HEADER_MOTHERLANGUAGETRANSLATION_STR = r'''MotherLanguageTranslation'''
ASR_TABLE_HEADER_STR = f'| {ASR_TABLE_HEADER_NO_STR} | {ASR_TABLE_HEADER_PERSONNAME_STR} | {ASR_TABLE_HEADER_SENTENCE_STR} | {ASR_TABLE_HEADER_SENTENCE2_STR} | {ASR_TABLE_HEADER_MOTHERLANGUAGETRANSLATION_STR} |'
ASR_TABLE_HEADER_DEVIDE_STR = f'|---|---|---|---|---|'

CONFIG_NAME_KEY_MODE = r'mode'

CONFIG_NAME_KEY_SUBJECT = r'subject'
ARG_KEY_CONFIG_NAME_SUBJECT = r'subject'

CONFIG_NAME_KEY_EXTRAPROMPT = r'extraprompt'
ARG_KEY_CONFIG_NAME_EXTRAPROMPT = r'extraprompt'
ARG_KEY_CONFIG_NAME_PERSONA1_EXTRAPROMPT = r'persona1_extraprompt'
ARG_KEY_CONFIG_NAME_PERSONA2_EXTRAPROMPT = r'persona2_extraprompt'

CONFIG_NAME_KEY_WORDCOUNTOF1LINE = r'wordscountof1line'
ARG_KEY_CONFIG_NAME_WORDCOUNTOF1LINE = r'wordscountof1line'

CONFIG_NAME_KEY_TOTALCOUNTOFSENTENCES = r'totalcountofsentences'
ARG_KEY_CONFIG_NAME_TOTALCOUNTOFSENTENCES = r'totalcountofsentences'    # Total count of conversation sentences for ASR GPTscenario.

CONFIG_NAME_KEY_PERSONAS = r'personas'

CONFIG_NAME_KEY_AIVOICEENGINE = r'aivoiceengine'
ARG_KEY_CONFIG_NAME_PERSONA1_AIVOICEENGINE = r'persona1_aivoiceengine'
ARG_KEY_CONFIG_NAME_PERSONA2_AIVOICEENGINE = r'persona2_aivoiceengine'

CONFIG_NAME_KEY_AIVOICEID = r'aivoiceid'
ARG_KEY_CONFIG_NAME_PERSONA1_AIVOICEID = r'persona1_aivoiceid'
ARG_KEY_CONFIG_NAME_PERSONA2_AIVOICEID = r'persona2_aivoiceid'

CONFIG_NAME_KEY_NAME = r'name'
ARG_KEY_CONFIG_NAME_PERSONA1_NAME = r'persona1_name'
ARG_KEY_CONFIG_NAME_PERSONA2_NAME = r'persona2_name'

CONFIG_NAME_KEY_GENDER = r'gender'
ARG_KEY_CONFIG_NAME_PERSONA1_GENDER = r'persona1_gender'
ARG_KEY_CONFIG_NAME_PERSONA2_GENDER = r'persona2_gender'
DEFAULT_GENDER = 'Male'

CONFIG_NAME_KEY_AGE = r'age'
ARG_KEY_CONFIG_NAME_PERSONA1_AGE = r'persona1_age'
ARG_KEY_CONFIG_NAME_PERSONA2_AGE = r'persona2_age'
DEFAULT_AGE = '30'

CONFIG_NAME_KEY_OCCUPATION = r'occupation'
ARG_KEY_CONFIG_NAME_PERSONA1_OCCUPATION = r'persona1_occupation'
ARG_KEY_CONFIG_NAME_PERSONA2_OCCUPATION = r'persona2_occupation'
DEFAULT_OCCUPATION = 'Student'

CONFIG_NAME_KEY_COUNTRYOFORIGIN = r'countryoforigin'
ARG_KEY_CONFIG_NAME_PERSONA1_COUNTRYOFORIGIN = r'persona1_countryoforigin'
ARG_KEY_CONFIG_NAME_PERSONA2_COUNTRYOFORIGIN = r'persona2_countryoforigin'

CONFIG_NAME_KEY_MYLANGUAGE = r'mylanguage'
ARG_KEY_CONFIG_NAME_PERSONA1_MYLANGUAGE = r'persona1_mylanguage'
ARG_KEY_CONFIG_NAME_PERSONA2_MYLANGUAGE = r'persona2_mylanguage'

CONFIG_NAME_KEY_HOBBY = r'hobby'
ARG_KEY_CONFIG_NAME_PERSONA1_HOBBY = r'persona1_hobby'
ARG_KEY_CONFIG_NAME_PERSONA2_HOBBY = r'persona2_hobby'
DEFAULT_HOBBY = "Playing a PC game"

CONFIG_NAME_KEY_PERSONALITY = r'personality'
ARG_KEY_CONFIG_NAME_PERSONA1_PERSONALITY = r'persona1_personality'
ARG_KEY_CONFIG_NAME_PERSONA2_PERSONALITY = r'persona2_personality'
DEFAULT_PERSONALITY = 'humorous'

CONFIG_NAME_KEY_ANNUALSALARY = r'annualsalary'
ARG_KEY_CONFIG_NAME_PERSONA1_ANNUALSALARY = r'persona1_annualsalary'
ARG_KEY_CONFIG_NAME_PERSONA2_ANNUALSALARY = r'persona2_annualsalary'
DEFAULT_ANNUALSALARY = '1 billions'

CONFIG_NAME_KEY_SPEAKINGSPEED = r'speakingspeed'
ARG_KEY_CONFIG_NAME_PERSONA1_SPEAKINGSPEED = r'persona1_speakingspeed'
ARG_KEY_CONFIG_NAME_PERSONA2_SPEAKINGSPEED = r'persona2_speakingspeed'

CONFIG_NAME_KEY_SPEAKINGPITCH = r'speakingpitch'
ARG_KEY_CONFIG_NAME_PERSONA1_SPEAKINGPITCH = r'persona1_speakingpitch'
ARG_KEY_CONFIG_NAME_PERSONA2_SPEAKINGPITCH = r'persona2_speakingpitch'

CONFIG_NAME_KEY_CFGMOTHERLANGUAGE = r'cfgmotherlanguage'
ARG_KEY_CONFIG_NAME_CFGMOTHERLANGUAGE = r'cfgmotherlanguage'

CONFIG_NAME_VALUE_LISTEN = r'genasrlisten'
CONFIG_NAME_VALUE_CONVERSATION = r'genasrconversation'
CONFIG_NAME_VALUE_EVALIMG = r'evalimg'
CONFIG_NAME_VALUE_EVALCAPTION = r'evalcaption'
CONFIG_NAME_VALUE_EVALDUMMY = r'evaldummy'

JSON_AI_VOICE_ALL_KEY_AIVOICE = r'AIvoice'
JSON_AI_VOICE_ALL_KEY_MANUAL = r'manual'
JSON_AI_VOICE_ALL_KEY_AUTO = r'auto'
JSON_AI_VOICE_ALL_KEY_ENGINE = r'engine'
JSON_AI_VOICE_ALL_KEY_VOICE_ID = r'idx'
JSON_AI_VOICE_ALL_KEY_BEST1 = 0
JSON_AI_VOICE_ALL_KEY_BEST2 = 1
JSON_AI_VOICE_ALL_KEY_BEST3 = 2
JSON_AI_VOICE_ALL_KEY_BEST4 = 3

CONFIG_NAME_KEY_PROMPT : str = r'prompt'
ARG_KEY_CONFIG_NAME_PROMPT : str  = r'prompt'
CONFIG_NAME_KEY_DESCRIPTION : str = r'description'
ARG_KEY_CONFIG_NAME_DESCRIPTION : str  = r'description'
CONFIG_NAME_KEY_VERSION : str = r'version'
ARG_KEY_CONFIG_NAME_VERSION : str  = r'version'
CONFIG_NAME_KEY_HOMEDIR : str = r'homedir'
ARG_KEY_CONFIG_NAME_HOMEDIR : str  = r'homedir'
CONFIG_NAME_KEY_RESDIR : str = r'resdir'
ARG_KEY_CONFIG_NAME_RESDIR : str  = r'resdir'
CONFIG_NAME_KEY_RESULTDIR : str = r'resultdir'
ARG_KEY_CONFIG_NAME_RESULTDIR : str  = r'resultdir'
CONFIG_NAME_KEY_RESULTPREFIX : str = r'resultprefix'
ARG_KEY_CONFIG_NAME_RESULTPREFIX : str  = r'resultprefix'

DIR_NAME_RES : str = 'res'
DIR_NAME_RES_CSV : str = 'Csv'
DIR_NAME_RES_InImage : str = 'InImage'
DIR_NAME_RES_OutImage : str = 'OutImage'
DIR_NAME_RESULT : str = 'result'
DIR_NAME_SAMPLE_DATAS : str = 'sample_datas'
DIR_NAME_SAMPLE_DATAS_IMG : str = 'img'

FILE_EXTENSION_WITHOUT_DOT_XLSX = r'xlsx'
FILE_EXTENSION_WITHOUT_DOT_CSV = r'csv'
FILE_EXTENSION_WITHOUT_DOT_LOG = r'log'

ARG_KEY_CSV_PATH = 1
ARG_KEY_CFG_UNIQUE_ID = 2
ARG_KEY_CFG_MODE = 3

LOG_BUFFER_SIZE_NO_FLUSH = -1

SETTINGS_NAME_PREDICTIVE_TEXT = [u'Predictive text', u'문구 추천']
SETTINGS_NAME_WRITING_STYLE = [u'Writing assist', u'글쓰기 어시스트']
SETTINGS_NAME_CORRECTION = [u'Correction', u'Correction']
SETTINGS_NAME_TRANSLATE = [u'Translation', u'번역']
SETTINGS_NAME_ONDEVICEMODE = [u'On-device mode', u'온디바이스 모드']

TONE_NAME_PROFESSIONAL = [u'전문가', u'professional']
TONE_NAME_CASUAL = [u'일상어', u'casual']
TONE_NAME_POLITE = [u'공손', 'polite']

BUTTON_NAME_TONE_CHANGE = [u'문장 스타일', u'Writing style']

# ================== Type enum =================
SYSTEM_TYPE_API = r'api'  # GPT api       / "api"

IDX_ENGINE_NAME_GPT = 0  # "gpt"
IDX_ENGINE_NAME_AZURE = 1  # "azure"

IDX_ALL_SENTENCES_INPUT_ORIGINAL = 0
IDX_ALL_SENTENCES_INPUT_TRANSLATED = 1
IDX_ALL_SENTENCES_INPUT_SCORE = 2

INIT_NOT_TRANSLATED = None
INIT_NOT_SCORED = -1

TBL_HEADER_NAME_SCORE = r'score'

TBL_HEADER_NAME_NATIVESCORE = r'Native_Score'
TBL_HEADER_NAME_NATIVEREASON = r'reason'
TBL_HEADER_NAME_NATIVEINPUT = r'input'
TBL_HEADER_NAME_NATIVEOUTPUT = r'output'
TBL_HEADER_NAME_NATIVERECOMMEND = r'recommend'

TBL_HEADER_NAME_GPTSCORE = r'GPT_Score'
TBL_HEADER_NAME_GPTREASON = r'GPT_Reason'
TBL_HEADER_NAME_GPTINPUT = r'GPT_Input'
TBL_HEADER_NAME_GPTOUTPUT = r'GPT_Output'
TBL_HEADER_NAME_GPTRECOMMEND = r'GPT_Recommend'

IDX_ALL_SENTENCES_OUTPUT_SCORE = 0
IDX_ALL_SENTENCES_OUTPUT_REASON = 1
IDX_ALL_SENTENCES_OUTPUT_ORIGINAL = 2
IDX_ALL_SENTENCES_OUTPUT_TRANSLATED = 3
IDX_ALL_SENTENCES_OUTPUT_RECOMMEND = 4

TBL_HEADER_NAME_GEN_ASR_NO = r'NO'
TBL_HEADER_NAME_GEN_ASR_1ST = r'1ST'
TBL_HEADER_NAME_GEN_ASR_2ND = r'2ND'
TBL_HEADER_NAME_GEN_ASR_3RD = r'3RD'
TBL_HEADER_NAME_GEN_ASR_4TH = r'4TH'

IDX_ALL_SENTENCES_OUTPUT_GEN_ASR_NO = 0
IDX_ALL_SENTENCES_OUTPUT_GEN_ASR_1ST = 1
IDX_ALL_SENTENCES_OUTPUT_GEN_ASR_2ND = 2
IDX_ALL_SENTENCES_OUTPUT_GEN_ASR_3RD = 3
IDX_ALL_SENTENCES_OUTPUT_GEN_ASR_4TH = 4

IDX_ALL_SENTENCES_OUTPUT_GEN_ASR_LAST_IDX = IDX_ALL_SENTENCES_OUTPUT_GEN_ASR_4TH

IDX_EVALIMG_OUTPUT_NO = 0
IDX_EVALIMG_OUTPUT_PROMPT = 1
IDX_EVALIMG_OUTPUT_STYLE = 2
IDX_EVALIMG_OUTPUT_OUTIMAGE = 3
IDX_EVALIMG_OUTPUT_INIMAGE = 4

IDX_ALL_SENTENCES_OUTPUT_EVALIMG_LAST_IDX = IDX_EVALIMG_OUTPUT_INIMAGE

IDX_EVALIMG_OUTPUT_SCORE = 1
IDX_EVALIMG_OUTPUT_REASON = 2
IDX_EVALIMG_OUTPUT_CAPTION = 3

TBL_HEADER_NAME_EVALIMG_NO = r'No'
TBL_HEADER_NAME_EVALIMG_PROMPT = r'Prompt'
TBL_HEADER_NAME_EVALIMG_STYLE = r'Style'
TBL_HEADER_NAME_EVALIMG_OUTIMAGE = r'OutImage'
TBL_HEADER_NAME_EVALIMG_INIMAGE = r'InImage'
TBL_HEADER_NAME_EVALIMG_SCORE = r'Score'
TBL_HEADER_NAME_EVALIMG_REASON = r'Reason'
TBL_HEADER_NAME_EVALIMG_CAPTION = r'Caption'
TBL_HEADER_COLUMNS_EVALIMG = [TBL_HEADER_NAME_EVALIMG_NO, TBL_HEADER_NAME_EVALIMG_PROMPT, TBL_HEADER_NAME_EVALIMG_STYLE, TBL_HEADER_NAME_EVALIMG_OUTIMAGE,
                              TBL_HEADER_NAME_EVALIMG_INIMAGE, TBL_HEADER_NAME_EVALIMG_SCORE, TBL_HEADER_NAME_EVALIMG_REASON, TBL_HEADER_NAME_EVALIMG_CAPTION]

IDX_RESPONSE_DETECT_PERSONA1_LANGUAGE = 0
IDX_RESPONSE_DETECT_PERSONA2_LANGUAGE = 1
IDX_RESPONSE_DETECT_MOTHER_LANGUAGE = -1

ASR_MIN_RESPONSE_COUNT_PER_RESPONSE = 3 # minimum record's count of response. if it's under this, OMG!! retry it.
ASR_LANGUAGE_CHECK_COUNT = 5            # To validate the language, DO check whether it's the correct language for 5 sentences.

ASR_RESPONSE_COUNT_PER_RESPONSE = 20    # **** DO NOT CHANGE IT ****
ASR_RESPONSE_COUNT_PER_RESPONSE_FIXED_LOW = 10

ASR_MAX_RETRY_COUNT = 15  # 최대 재시도 횟수
ASR_RETRY_SLEEPTIME = 10  # Fail이후 sleep time

ASR_GEN_RESULT_FILE_PREFIX = 'asr_gen_result_'
ASR_VOICE_RESULT_FOLDER_NAME = 'voice'
IDX_ASR_GEN_RESULT_CFG_PERSONA1 = 0
IDX_ASR_GEN_RESULT_CFG_PERSONA2 = 1

# AI Voice Engine name(only lower case)
AI_VOICE_ENGINE_NAME_NCP = "ncp" # Naver Cloud Platform
AI_VOICE_ENGINE_NAME_AWS = "aws" # Amazon Web Service
AI_VOICE_ENGINE_NAME_MSA = "msa" # MicroSoft Azure
AI_VOICE_ENGINE_NAME_GPT = "gpt" # OpenAI GPT
AI_VOICE_ENGINE_NAME_GGC = "ggc" # GooGle Cloud
AI_VOICE_ENGINE_NAME_ELV = "elv" # ELeVen labs

ASR_NAME_GPT_MODEL = "gpt-4o-mini"
ASR_NAME_GPT_PARAM_TEMPERATURE = 2.0
ASR_NAME_GPT_PARAM_TOP_P = 0.95
ASR_ASSISTANTS_EXIST_ID_DEV = 'asst_jR3BLrmIwSPD6lXc3gcUxWjW'

# excel sheet name
NAME_EXCEL_SHEET_SUMMARY = r'summary'
NAME_EXCEL_SHEET_RAW = r'raw_data'
NAME_EXCEL_SHEET_RAW2 = r'raw_data2'

# Error type
ERR_CODE_NONE = 0
ERR_CODE_NOT_EQU_COUNT_BETWEEN_INPUT_AND_OUTPUT = 1
ERR_CODE_RESPONSE_IS_TOO_SHORT = 2
ERR_CODE_OUTPUT_NULL = 5
ERR_CODE_DUMMY = 6

# retry type
RETRY_CODE_NONE = 0
RETRY_CODE_OUTPUT_NULL = 1
RETRY_CODE_LANGUAGE_VALIDATION_FAIL = 2
RETRY_CODE_OUTPUT_WRONG_FORMAT = 3

# https://learn.microsoft.com/ko-kr/azure/ai-services/language-service/language-detection/language-support
# https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html#wp1252447
azure_language_detection_support_dict_langcode_langname = {
    "af":"Afrikaans",     #000
    "sq":"Albanian",     #001
    "am":"Amharic",     #002
    "ar":"Arabic",     #003
    "hy":"Armenian",     #004
    "as":"Assamese",     #005
    "az":"Azerbaijani",     #006
    "ba":"Bashkir",     #007
    "eu":"Basque",     #008
    "be":"Belarusian",     #009
    "bn":"Bengali",     #010
    "bs":"Bosnian",     #011
    "bg":"Bulgarian",     #012
    "my":"Burmese",     #013
    "ca":"Catalan",     #014
    "km":"Central Khmer",     #015
    "zh_chs":"Chinese_Simplified",     #016
    "zh_cht":"Chinese_Traditional",     #017
    "cv":"Chuvash",     #018
    "co":"Corsican",     #019
    # "hr":"Croatian",     # NOT support
    "cs":"Czech",     #020
    "da":"Danish",     #021
    "prs":"Dari",     #022
    "dv":"Divehi",     #023
    "nl":"Dutch",     #024
    "en":"English",     #025
    "eo":"Esperanto",     #026
    "et":"Estonian",     #027
    "fo":"Faroese",     #028
    "fj":"Fijian",     #029
    "fi":"Finnish",     #030
    "fr":"French",     #031
    "gl":"Galician",     #032
    "ka":"Georgian",     #033
    "de":"German",     #034
    "el":"Greek",     #035
    "gu":"Gujarati",     #036
    "ht":"Haitian",     #037
    "ha":"Hausa",     #038
    "he":"Hebrew",     #039
    "hi":"Hindi",     #040
    "mww":"Hmong Daw",     #041
    "hu":"Hungarian",     #042
    "is":"Icelandic",     #043
    "ig":"Igbo",     #044
    "id":"Indonesian",    #045
    "iu":"Inuktitut",   #046
    "ga":"Irish",     #047
    "it":"Italian",     #048
    "ja":"Japanese",    #049
    # "jv":"Javanese",     # NOT support
    "kn":"Kannada",    #050
    "kk":"Kazakh",     #051
    "rw":"Kinyarwanda",     #052
    "ky":"Kirghiz",    #053
    "ko":"Korean",     #054
    "ku":"Kurdish",    #055
    "lo":"Lao",     #056
    "la":"Latin",     #057
    "lv":"Latvian",     #058
    "lt":"Lithuanian",     #059
    "lb":"Luxembourgish",     #060
    "mk":"Macedonian",     #061
    "mg":"Malagasy",     #062
    "ms":"Malay",     #063
    "ml":"Malayalam",     #064
    "mt":"Maltese",     #065
    "mi":"Maori",     #066
    "mr":"Marathi",     #067
    "mn":"Mongolian",     #068
    "ne":"Nepali",     #069
    "nn":"Norwegian Nynorsk",       #070
    "no":"Norwegian",     #071
    "or":"Odia",     #072
    "ps":"Pashto",     #073
    # "fa":"Persian",     # NOT support
    "pl":"Polish",     #074
    "pt":"Portuguese",     #075
    "pa":"Punjabi",     #076
    "otq":"Queretaro Otomi",   #077
    "ro":"Romanian",     #078
    "ru":"Russian",     #079
    "sm":"Samoan",     #080
    "sr":"Serbian",     #081
    "sn":"Shona",     #082
    "sd":"Sindhi",     #083
    "si":"Sinhala",     #084
    "sk":"Slovak",     #085
    "sl":"Slovenian",     #086
    "so":"Somali",     #087
    "es":"Spanish",     #088
    "su":"Sundanese",     #089
    "sw":"Swahili",     #090
    "sv":"Swedish",     #091
    "tl":"Tagalog",     #092
    "ty":"Tahitian",     #093
    "tg":"Tajik",     #094
    "ta":"Tamil",     #095
    "tt":"Tatar",     #096
    "te":"Telugu",     #097
    "th":"Thai",     #098
    "bo":"Tibetan",     #099
    "ti":"Tigrinya",     #100
    "to":"Tongan",     #101
    "tr":"Turkish",     #102
    "tk":"Turkmen",     #103
    "uk":"Ukrainian",       #104
    "hsb":"Upper Sorbian",     #105
    "ur":"Urdu",     #106
    "ug":"Uyghur",     #107
    "uz":"Uzbek",     #108
    "vi":"Vietnamese",     #109
    "cy":"Welsh",     #110
    # "xh":"Xhosa",     # NOT support
    "yi":"Yiddish",     #111
    "yo":"Yoruba",     #112
    "yua":"Yucatec Maya",     #113
    "zu":"Zulu",     #114
    }

# azure 의 language detection 함수에서 아래 langcode 일 경우, 잘못된 값이 return 됨
# # # ['Bosnian', 'bs', 'hr', 'Kada gledam crveni zalazak sunca, osjećam se kao da se vraćam u svoje djetinjstvo, kada sam bezbrižno trčao i igrao se. Uzeo sam trenutak da se prisjetim svog djetinjstva. Bilo je divno provesti lijepo vrijeme zajedno. Iskreno sam zahvalan.']
# # # ['Dari', 'prs', 'fa', 'زمانیکه من به غروب سرخ نگاه میکنم، من احساس میکنم که من به دوران طفولیت خود برگشته ام زمانیکه من میتوانستم آزادانه بدوم و بازی کنم. من یک لحظه وقت گرفتم تا به طفولیت خود نگاه کنم. این واقعاً خوب بود که قادر به داشتن وقت خوب با هم بودیم. تشکر زیاد از شما.']
# # # ['Malay', 'ms', 'id', 'Apabila saya melihat matahari terbenam merah, saya rasa seperti kembali ke zaman kanak-kanak saya, ketika saya bermain tanpa beban. Saya mengambil masa sejenak untuk merenung tentang zaman kanak-kanak saya. Sangat indah menghabiskan masa yang baik bersama. Saya sangat berterima kasih.']
# # # ['Sundanese', 'su', 'jv', 'Nalika kuring ningali panonpoé surup beureum, kuring ngarasa siga kuring balik deui ka budak leutik kuring, nalika kuring maén tanpa pikiran. Kuring nyandak waktos kanggo ngémutan budak leutik kuring. Éta endah pisan nyéépkeun waktos anu saé babarengan.']
# # # ['Zulu', 'zu', 'xh', 'Lapho ngibuka ukushona kwelanga okubomvu, ngizizwa sengathi ngibuyela ebuntwaneni bami, lapho ngidlala ngaphandle kokukhathazeka. Ngithathe isikhashana ukuzindla ngobuntwana bami. Kwakumnandi kakhulu ukuchitha isikhathi esihle ndawonye. Ngiyabonga ngobuqotho.']

azure_language_detection_support_dict_langname_langcode = {
    "Afrikaans":"af",     #000
    "Albanian":"sq",     #001
    "Amharic":"am",     #002
    "Arabic":"ar",     #003
    "Armenian":"hy",     #004
    "Assamese":"as",     #005
    "Azerbaijani":"az",     #006
    "Bashkir":"ba",     #007
    "Basque":"eu",     #008
    "Belarusian":"be",     #009
    "Bengali":"bn",     #010
    "Bosnian":"bs",     #011
    "Bulgarian":"bg",     #012
    "Burmese":"my",     #013
    "Catalan":"ca",     #014
    "Central Khmer":"km",     #015
    "Chinese Simplified":"zh_chs",     #016
    "Chinese Traditional":"zh_cht",     #017
    "Chuvash":"cv",     #018
    "Corsican":"co",     #019
    # "Croatian":"hr",     # NOT support
    "Czech":"cs",     #020
    "Danish":"da",     #021
    "Dari":"prs",     #022
    "Divehi":"dv",     #023
    "Dutch":"nl",     #024
    "English":"en",     #025
    "Esperanto":"eo",     #026
    "Estonian":"et",     #027
    "Faroese":"fo",     #028
    "Fijian":"fj",     #029
    "Finnish":"fi",     #030
    "French":"fr",     #031
    "Galician":"gl",     #032
    "Georgian":"ka",     #033
    "German":"de",     #034
    "Greek":"el",     #035
    "Gujarati":"gu",     #036
    "Haitian":"ht",     #037
    "Hausa":"ha",     #038
    "Hebrew":"he",     #039
    "Hindi":"hi",     #040
    "Hmong Daw":"mww",     #041
    "Hungarian":"hu",     #042
    "Icelandic":"is",     #043
    "Igbo":"ig",     #044
    "Indonesian":"id",     #045
    "Inuktitut":"iu",     #046
    "Irish":"ga",     #047
    "Italian":"it",     #048
    "Japanese":"ja",     #049
    # "Javanese":"jv",     # NOT support
    "Kannada":"kn",     #050
    "Kazakh":"kk",     #051
    "Kinyarwanda":"rw",     #052
    "Kirghiz":"ky",     #053
    "Korean":"ko",     #054
    "Kurdish":"ku",     #055
    "Lao":"lo",     #056
    "Latin":"la",     #057
    "Latvian":"lv",     #058
    "Lithuanian":"lt",     #059
    "Luxembourgish":"lb",     #060
    "Macedonian":"mk",     #061
    "Malagasy":"mg",     #062
    "Malay":"ms",     #063
    "Malayalam":"ml",     #064
    "Maltese":"mt",     #065
    "Maori":"mi",     #066
    "Marathi":"mr",     #067
    "Mongolian":"mn",     #068
    "Nepali":"ne",     #069
    "Norwegian Nynorsk":"nn",     #070
    "Norwegian":"no",     #071
    "Odia":"or",     #072
    "Pashto":"ps",     #073
    # "Persian":"fa",     # NOT support
    "Polish":"pl",      #074
    "Portuguese":"pt",     #075
    "Punjabi":"pa",     #076
    "Queretaro Otomi":"otq",     #077
    "Romanian":"ro",        #078
    "Russian":"ru",     #079
    "Samoan":"sm",     #080
    "Serbian":"sr",     #081
    "Shona":"sn",     #082
    "Sindhi":"sd",     #083
    "Sinhala":"si",     #084
    "Slovak":"sk",     #085
    "Slovenian":"sl",     #086
    "Somali":"so",     #087
    "Spanish":"es",     #088
    "Sundanese":"su",     #089
    "Swahili":"sw",     #090
    "Swedish":"sv",     #091
    "Tagalog":"tl",     #092
    "Tahitian":"ty",     #093
    "Tajik":"tg",     #094
    "Tamil":"ta",     #095
    "Tatar":"tt",     #096
    "Telugu":"te",     #097
    "Thai":"th",     #098
    "Tibetan":"bo",     #099
    "Tigrinya":"ti",     #100
    "Tongan":"to",     #101
    "Turkish":"tr",     #102
    "Turkmen":"tk",     #103
    "Ukrainian":"uk",     #104
    "Upper Sorbian":"hsb",     #105
    "Urdu":"ur",     #106
    "Uyghur":"ug",     #107
    "Uzbek":"uz",     #108
    "Vietnamese":"vi",     #109
    "Welsh":"cy",     #110
    # "Xhosa":"xh",     # NOT support
    "Yiddish":"yi",     #111
    "Yoruba":"yo",     #112
    "Yucatec Maya":"yua",     #113
    "Zulu":"zu",     #114
    }

PROMPT_EXTRA_IMG_ITEM : str = '''

No:{inner_no}
Extra prompt:{innerPrompt}
Style:{innerStyle}
Generated image:{inner_out_img}
{inner_in_img_extra}'''
