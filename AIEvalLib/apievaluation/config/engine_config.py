# -*- coding: utf-8 -*-
import random
import sys

from GlobalVars import *

# # # # # # # # # # # # # # # # # # # # # DO NOT MODIFY HERE!!! START # # # # # # # # # # # # # # # # # # # # #
# # # PROGRAM mode
GPT_PROGRAM_PROXY_MODE_OFFICE: str = 'office'     # Proxy
GPT_PROGRAM_PROXY_MODE_HOME: str = 'home'         # No Proxy
current_GPT_PROGRAM_PROXY_MODE: str=GPT_PROGRAM_PROXY_MODE_HOME
print(f'current_GPT_PROGRAM_PROXY_MODE:{current_GPT_PROGRAM_PROXY_MODE}')

# # # Engine name
# for OPEN AI
GPT_ENGINE_TYPE_OPENAI: str = 'openai'
GPT_ENGINE_TYPE_GPT: str = 'gpt'

GPT_ENGINE_NAME_GPT3_5_TURBO: str = 'gpt-3.5-turbo-0125'
GPT_ENGINE_NAME_GPT4: str = 'gpt-4'
GPT_ENGINE_NAME_GPT4_TURBO: str = 'gpt-4-turbo'
GPT_ENGINE_NAME_GPT4_TURBO_PREVIEW: str = 'gpt-4-turbo-preview'
GPT_ENGINE_NAME_GPT4_1: str = 'gpt-4.1'
GPT_ENGINE_NAME_GPT4o: str = 'gpt-4o'
GPT_ENGINE_NAME_GPT4o_mini: str = 'gpt-4o-mini'
GPT_ENGINE_NAME_GPT4o_2024_08_06: str = 'gpt-4o-2024-08-06'
GPT_ENGINE_NAME_GPT4o_2024_11_20: str = 'gpt-4o-2024-11-20'
GPT_ENGINE_NAME_GPT4_5_preview: str = 'gpt-4.5-preview'
GPT_ENGINE_NAME_o1_preview: str = 'o1-preview'
GPT_ENGINE_NAME_o1: str = 'o1'
GPT_ENGINE_NAME_o1_mini: str = 'o1-mini'
GPT_ENGINE_NAME_o3_mini: str = 'o3-mini'
GPT_ENGINE_NAME_o4_mini: str = 'o4-mini'

#for AZURE
GPT_ENGINE_TYPE_AZURE: str = 'azure'
GPT_ENGINE_NAME_AZURE_GPT4_SQE_01: str = r'SE-SQE-01'        #'gpt-4-turbo-preview'
GPT_ENGINE_NAME_AZURE_GPT4_SQE_03: str = r'SE-SQE-03'        #'gpt-4o'
GPT_ENGINE_NAME_AZURE_GPT4_SQE_04: str = r'SE-SQE-04'        #'gpt-4o-mini'
GPT_ENGINE_NAME_AZURE_GPT4_SQE_05: str = r'SE-SQE-05'        #'gpt-4o'
GPT_ENGINE_NAME_AZURE_GPT4_SQE_06: str = r'SE-SQE-06'        #'gpt-4o-mini'

GPT_ENGINE_NAME_AZURE_GPT4_SQE_10: str = r'SE-SQE-10'        #'tts-hd'  don't use in ENGINE_NAME

# # # Parallel Thread
THRESHOLD_SENTENCES_COUNT_FOR_M_THREAD = 5
GPT_PARALLEL_THREAD_COUNT:int = 1       # between 1 ~ 10
GPT_PARALLEL_MAX_THREAD_LIMIT:int = 20

# # # Engine parameter
GPT_PARAMETER_N = 1
GPT_PARAMETER_TEMPERATURE = 1.0
GPT_PARAMETER_TOP_P = 0.4
GPT_PARAMETER_PRESENCE_PENALTY = 0.5
GPT_PARAMETER_FREQUENCY_PENALTY = 0.7
GPT_PARAMETER_SEED = 20240401

GPT_TOKEN_PRICE_QUERY_DOLLER_GPT3_5_TURBO: float                    = 0.5      #'gpt-3.5-turbo-0125'
GPT_TOKEN_PRICE_QUERY_CACHED_DOLLER_GPT3_5_TURBO: float             = 0.5      #'gpt-3.5-turbo-0125'
GPT_TOKEN_PRICE_RESPONSE_DOLLER_GPT3_5_TURBO: float                 = 1.5

GPT_TOKEN_PRICE_QUERY_DOLLER_GPT4: float                            = 30.0     #'gpt-4'
GPT_TOKEN_PRICE_QUERY_CACHED_DOLLER_GPT4: float                     = 30.0     #'gpt-4'
GPT_TOKEN_PRICE_RESPONSE_DOLLER_GPT4: float                         = 60.0

GPT_TOKEN_PRICE_QUERY_DOLLER_GPT4_1: float                          = 2.0     #'gpt-4.1'
GPT_TOKEN_PRICE_QUERY_CACHED_DOLLER_GPT4_1: float                   = 0.5     #'gpt-4.1'
GPT_TOKEN_PRICE_RESPONSE_DOLLER_GPT4_1: float                       = 8.0

GPT_TOKEN_PRICE_QUERY_DOLLER_GPT4_TURBO_PREVIEW: float              = 10.0     #'gpt-4_turbo_preview'
GPT_TOKEN_PRICE_QUERY_CACHED_DOLLER_GPT4_TURBO_PREVIEW: float       = 10.0     #'gpt-4_turbo_preview'
GPT_TOKEN_PRICE_RESPONSE_DOLLER_GPT4_TURBO_PREVIEW: float           = 30.0

GPT_TOKEN_PRICE_QUERY_DOLLER_GPT4_o: float                          = 2.5      #'gpt-4o'
GPT_TOKEN_PRICE_QUERY_CACHED_DOLLER_GPT4_o: float                   = 1.25     #'gpt-4o'
GPT_TOKEN_PRICE_RESPONSE_DOLLER_GPT4_o: float                       = 10.0

GPT_TOKEN_PRICE_QUERY_DOLLER_GPT4_o_mini: float                     = 0.15     #'gpt-4o-mini'
GPT_TOKEN_PRICE_QUERY_CACHED_DOLLER_GPT4_o_mini: float              = 0.075    #'gpt-4o-mini'
GPT_TOKEN_PRICE_RESPONSE_DOLLER_GPT4_o_mini: float                  = 0.6

GPT_TOKEN_PRICE_QUERY_DOLLER_GPT4_o_2024_08_06: float               = 2.5      #'gpt-4o_2024_08_06'
GPT_TOKEN_PRICE_QUERY_CACHED_DOLLER_GPT4_o_2024_08_06: float        = 1.25     #'gpt-4o_2024_08_06'
GPT_TOKEN_PRICE_RESPONSE_DOLLER_GPT4_o_2024_08_06: float            = 10.0

GPT_TOKEN_PRICE_QUERY_DOLLER_GPT4_o_2024_11_20: float               = 2.5      #'gpt-4o_2024_11_20'
GPT_TOKEN_PRICE_QUERY_CACHED_DOLLER_GPT4_o_2024_11_20: float        = 1.25     #'gpt-4o_2024_11_20'
GPT_TOKEN_PRICE_RESPONSE_DOLLER_GPT4_o_2024_11_20: float            = 10.0

GPT_TOKEN_PRICE_QUERY_DOLLER_GPT4_5_PREVIEW: float                  = 75.0     #'gpt-4.5-preview'
GPT_TOKEN_PRICE_QUERY_CACHED_DOLLER_GPT4_5_PREVIEW: float           = 37.5     #'gpt-4.5-preview'
GPT_TOKEN_PRICE_RESPONSE_DOLLER_GPT4_5_PREVIEW: float               = 150.0

GPT_TOKEN_PRICE_QUERY_DOLLER_o1_preview: float                      = 15.0     #'o1-preview'
GPT_TOKEN_PRICE_QUERY_CACHED_DOLLER_o1_preview: float               = 7.5      #'o1-preview'
GPT_TOKEN_PRICE_RESPONSE_DOLLER_o1_preview: float                   = 60.0

GPT_TOKEN_PRICE_QUERY_DOLLER_o1: float                              = 15.0     #'o1'
GPT_TOKEN_PRICE_QUERY_CACHED_DOLLER_o1: float                       = 7.5      #'o1'
GPT_TOKEN_PRICE_RESPONSE_DOLLER_o1: float                           = 60.0

GPT_TOKEN_PRICE_QUERY_DOLLER_o1_mini: float                         = 1.10     #'o1-mini'
GPT_TOKEN_PRICE_QUERY_CACHED_DOLLER_o1_mini: float                  = 0.55     #'o1-mini'
GPT_TOKEN_PRICE_RESPONSE_DOLLER_o1_mini: float                      = 4.40

GPT_TOKEN_PRICE_QUERY_DOLLER_o3_mini: float                         = 1.10     #'o3-mini'
GPT_TOKEN_PRICE_QUERY_CACHED_DOLLER_o3_mini: float                  = 0.55     #'o3-mini'
GPT_TOKEN_PRICE_RESPONSE_DOLLER_o3_mini: float                      = 4.40

GPT_TOKEN_PRICE_QUERY_DOLLER_o4_mini: float                         = 1.10     #'o4-mini'
GPT_TOKEN_PRICE_QUERY_CACHED_DOLLER_o4_mini: float                  = 0.55     #'o4-mini'
GPT_TOKEN_PRICE_RESPONSE_DOLLER_o4_mini: float                      = 4.40

# # # Money per 1-token
GPT_TOKEN_QUERY_1M_GPT: int = 1000000
GPT_TOKEN_RESPONSE_1M_GPT: int = 1000000

# # # Token Limit
TOKEN_LIMIT_BUF = 48
GPT_ENGINE_TOKEN_RESPONSE_LIMIT_GPT3_5_TURBO = 4096 - TOKEN_LIMIT_BUF
GPT_ENGINE_TOKEN_RESPONSE_LIMIT_GPT4 = 8192 - TOKEN_LIMIT_BUF
GPT_ENGINE_TOKEN_RESPONSE_LIMIT_GPT4_1 = 16384 - TOKEN_LIMIT_BUF
GPT_ENGINE_TOKEN_RESPONSE_LIMIT_GPT4_TURBO = 4096 - TOKEN_LIMIT_BUF
GPT_ENGINE_TOKEN_RESPONSE_LIMIT_GPT4_TURBO_PREVIEW = 4096 - TOKEN_LIMIT_BUF
GPT_ENGINE_TOKEN_RESPONSE_LIMIT_GPT4o = 16384 - TOKEN_LIMIT_BUF
GPT_ENGINE_TOKEN_RESPONSE_LIMIT_GPT4o_mini = 16384 - TOKEN_LIMIT_BUF
GPT_ENGINE_TOKEN_RESPONSE_LIMIT_GPT4o_2024_08_06 = 16384 - TOKEN_LIMIT_BUF
GPT_ENGINE_TOKEN_RESPONSE_LIMIT_GPT4o_2024_11_20 = 16384 - TOKEN_LIMIT_BUF
GPT_ENGINE_TOKEN_RESPONSE_LIMIT_GPT4_5_PREVIEW = 16384 - TOKEN_LIMIT_BUF
GPT_ENGINE_TOKEN_RESPONSE_LIMIT_o1_preview = 32768 - TOKEN_LIMIT_BUF
GPT_ENGINE_TOKEN_RESPONSE_LIMIT_o1 = 100000 - TOKEN_LIMIT_BUF
GPT_ENGINE_TOKEN_RESPONSE_LIMIT_o1_mini = 65536 - TOKEN_LIMIT_BUF
GPT_ENGINE_TOKEN_RESPONSE_LIMIT_o3_mini = 100000 - TOKEN_LIMIT_BUF
GPT_ENGINE_TOKEN_RESPONSE_LIMIT_o4_mini = 100000 - TOKEN_LIMIT_BUF
# # # # # # # # # # # # # # # # # # # # # DO NOT MODIFY HERE!!! E N D # # # # # # # # # # # # # # # # # # # # #



class EngineVars:
    def __init__(self, argProgramMode = GPT_PROGRAM_PROXY_MODE_OFFICE, argGptType = GPT_ENGINE_TYPE_OPENAI, argGptModel = GPT_ENGINE_NAME_GPT4o, argDeployName = None):
        # # # 1. set PROGRAM MODE below,
        self.config_g_PROGRAM_MODE: str = argProgramMode

        # # # 2. set GPT MODE below,
        self.config_g_GPT_TYPE: str = argGptType

        if self.config_g_GPT_TYPE == GPT_ENGINE_TYPE_AZURE:
            self.config_GPT_ENGINE_TYPE_IDX = IDX_ENGINE_NAME_AZURE
        else:
            self.config_GPT_ENGINE_TYPE_IDX = IDX_ENGINE_NAME_GPT

        if self.config_g_GPT_TYPE == GPT_ENGINE_TYPE_AZURE:
            # Convert SE_SQE_XXXX model to GPT engine
            if argGptModel == GPT_ENGINE_NAME_AZURE_GPT4_SQE_01:
                self.config_g_GPT_MODEL = GPT_ENGINE_NAME_GPT4_TURBO_PREVIEW
            elif argGptModel == GPT_ENGINE_NAME_AZURE_GPT4_SQE_03:
                self.config_g_GPT_MODEL = GPT_ENGINE_NAME_GPT4o
            elif argGptModel == GPT_ENGINE_NAME_AZURE_GPT4_SQE_06:
                self.config_g_GPT_MODEL = GPT_ENGINE_NAME_GPT4o_mini
            else:
                self.config_g_GPT_MODEL: str = argGptModel
        else:
            self.config_g_GPT_MODEL: str = argGptModel

        self.config_g_GPT_DEPLOY: str = argDeployName

        # # # =============================== START Point =============================== # # #
        if self.config_g_GPT_MODEL == GPT_ENGINE_NAME_GPT3_5_TURBO:
            self.config_GPT_ENGINE_NAME = GPT_ENGINE_NAME_GPT3_5_TURBO
            self.config_GPT_ENGINE_SUPPORT_MAX_TOKEN = GPT_ENGINE_TOKEN_RESPONSE_LIMIT_GPT3_5_TURBO
            self.config_GPT_TIKTOKEN_ENGINE_NAME = self.config_GPT_ENGINE_NAME

            self.GPT_TOKEN_QUERY_DOLLOR_PER_1M = GPT_TOKEN_PRICE_QUERY_DOLLER_GPT3_5_TURBO
            self.GPT_TOKEN_QUERY_CACHED_DOLLOR_PER_1M = GPT_TOKEN_PRICE_QUERY_CACHED_DOLLER_GPT3_5_TURBO
            self.GPT_TOKEN_RESPONSE_DOLLOR_PER_1M = GPT_TOKEN_PRICE_RESPONSE_DOLLER_GPT3_5_TURBO

        elif self.config_g_GPT_MODEL == GPT_ENGINE_NAME_GPT4:                    # gpt-4
            self.config_GPT_ENGINE_NAME = GPT_ENGINE_NAME_GPT4
            self.config_GPT_ENGINE_SUPPORT_MAX_TOKEN = GPT_ENGINE_TOKEN_RESPONSE_LIMIT_GPT4
            self.config_GPT_TIKTOKEN_ENGINE_NAME = self.config_GPT_ENGINE_NAME

            self.GPT_TOKEN_QUERY_DOLLOR_PER_1M = GPT_TOKEN_PRICE_QUERY_DOLLER_GPT4
            self.GPT_TOKEN_QUERY_CACHED_DOLLOR_PER_1M = GPT_TOKEN_PRICE_QUERY_CACHED_DOLLER_GPT4
            self.GPT_TOKEN_RESPONSE_DOLLOR_PER_1M = GPT_TOKEN_PRICE_RESPONSE_DOLLER_GPT4

        elif self.config_g_GPT_MODEL == GPT_ENGINE_NAME_GPT4_1:                    # gpt-4.1
            self.config_GPT_ENGINE_NAME = GPT_ENGINE_NAME_GPT4_1
            self.config_GPT_ENGINE_SUPPORT_MAX_TOKEN = GPT_ENGINE_TOKEN_RESPONSE_LIMIT_GPT4_1
            self.config_GPT_TIKTOKEN_ENGINE_NAME = self.config_GPT_ENGINE_NAME

            self.GPT_TOKEN_QUERY_DOLLOR_PER_1M = GPT_TOKEN_PRICE_QUERY_DOLLER_GPT4_1
            self.GPT_TOKEN_QUERY_CACHED_DOLLOR_PER_1M = GPT_TOKEN_PRICE_QUERY_CACHED_DOLLER_GPT4_o_mini
            self.GPT_TOKEN_RESPONSE_DOLLOR_PER_1M = GPT_TOKEN_PRICE_RESPONSE_DOLLER_GPT4_1

        elif self.config_g_GPT_MODEL == GPT_ENGINE_NAME_GPT4o:                    # gpt-4o
            self.config_GPT_ENGINE_NAME = GPT_ENGINE_NAME_GPT4o
            self.config_GPT_ENGINE_SUPPORT_MAX_TOKEN = GPT_ENGINE_TOKEN_RESPONSE_LIMIT_GPT4o
            self.config_GPT_TIKTOKEN_ENGINE_NAME = self.config_GPT_ENGINE_NAME

            self.GPT_TOKEN_QUERY_DOLLOR_PER_1M = GPT_TOKEN_PRICE_QUERY_DOLLER_GPT4_o
            self.GPT_TOKEN_QUERY_CACHED_DOLLOR_PER_1M = GPT_TOKEN_PRICE_QUERY_CACHED_DOLLER_GPT4_o
            self.GPT_TOKEN_RESPONSE_DOLLOR_PER_1M = GPT_TOKEN_PRICE_RESPONSE_DOLLER_GPT4_o

        elif self.config_g_GPT_MODEL == GPT_ENGINE_NAME_GPT4o_mini:                    # gpt-4o-mini
            self.config_GPT_ENGINE_NAME = GPT_ENGINE_NAME_GPT4o_mini
            self.config_GPT_ENGINE_SUPPORT_MAX_TOKEN = GPT_ENGINE_TOKEN_RESPONSE_LIMIT_GPT4o_mini
            self.config_GPT_TIKTOKEN_ENGINE_NAME = self.config_GPT_ENGINE_NAME

            self.GPT_TOKEN_QUERY_DOLLOR_PER_1M = GPT_TOKEN_PRICE_QUERY_DOLLER_GPT4_o_mini
            self.GPT_TOKEN_QUERY_CACHED_DOLLOR_PER_1M = GPT_TOKEN_PRICE_QUERY_CACHED_DOLLER_GPT4_o_mini
            self.GPT_TOKEN_RESPONSE_DOLLOR_PER_1M = GPT_TOKEN_PRICE_RESPONSE_DOLLER_GPT4_o_mini

        elif self.config_g_GPT_MODEL == GPT_ENGINE_NAME_GPT4o_2024_08_06:                    # gpt-4o-2024-08-06
            self.config_GPT_ENGINE_NAME = GPT_ENGINE_NAME_GPT4o_2024_08_06
            self.config_GPT_ENGINE_SUPPORT_MAX_TOKEN = GPT_ENGINE_TOKEN_RESPONSE_LIMIT_GPT4o_2024_08_06
            self.config_GPT_TIKTOKEN_ENGINE_NAME = self.config_GPT_ENGINE_NAME

            self.GPT_TOKEN_QUERY_DOLLOR_PER_1M = GPT_TOKEN_PRICE_QUERY_DOLLER_GPT4_o_2024_08_06
            self.GPT_TOKEN_QUERY_CACHED_DOLLOR_PER_1M = GPT_TOKEN_PRICE_QUERY_CACHED_DOLLER_GPT4_o_2024_08_06
            self.GPT_TOKEN_RESPONSE_DOLLOR_PER_1M = GPT_TOKEN_PRICE_RESPONSE_DOLLER_GPT4_o_2024_08_06

        elif self.config_g_GPT_MODEL == GPT_ENGINE_NAME_GPT4o_2024_11_20:                    # gpt-4o-2024-11-20
            self.config_GPT_ENGINE_NAME = GPT_ENGINE_NAME_GPT4o_2024_11_20
            self.config_GPT_ENGINE_SUPPORT_MAX_TOKEN = GPT_ENGINE_TOKEN_RESPONSE_LIMIT_GPT4o_2024_08_06
            self.config_GPT_TIKTOKEN_ENGINE_NAME = self.config_GPT_ENGINE_NAME

            self.GPT_TOKEN_QUERY_DOLLOR_PER_1M = GPT_TOKEN_PRICE_QUERY_DOLLER_GPT4_o_2024_08_06
            self.GPT_TOKEN_QUERY_CACHED_DOLLOR_PER_1M = GPT_TOKEN_PRICE_QUERY_CACHED_DOLLER_GPT4_o_2024_08_06
            self.GPT_TOKEN_RESPONSE_DOLLOR_PER_1M = GPT_TOKEN_PRICE_RESPONSE_DOLLER_GPT4_o_2024_08_06

        elif self.config_g_GPT_MODEL == GPT_ENGINE_NAME_GPT4_5_preview:                    # gpt-4.5-preview
            self.config_GPT_ENGINE_NAME = GPT_ENGINE_NAME_GPT4_5_preview
            self.config_GPT_ENGINE_SUPPORT_MAX_TOKEN = GPT_ENGINE_TOKEN_RESPONSE_LIMIT_GPT4o_2024_08_06
            self.config_GPT_TIKTOKEN_ENGINE_NAME = self.config_GPT_ENGINE_NAME

            self.GPT_TOKEN_QUERY_DOLLOR_PER_1M = GPT_TOKEN_PRICE_QUERY_DOLLER_GPT4_o_2024_08_06
            self.GPT_TOKEN_QUERY_CACHED_DOLLOR_PER_1M = GPT_TOKEN_PRICE_QUERY_CACHED_DOLLER_GPT4_o_2024_08_06
            self.GPT_TOKEN_RESPONSE_DOLLOR_PER_1M = GPT_TOKEN_PRICE_RESPONSE_DOLLER_GPT4_o_2024_08_06

        elif self.config_g_GPT_MODEL == GPT_ENGINE_NAME_o1_preview:                    # o1-preview
            self.config_GPT_ENGINE_NAME = GPT_ENGINE_NAME_o1_preview
            self.config_GPT_ENGINE_SUPPORT_MAX_TOKEN = GPT_ENGINE_TOKEN_RESPONSE_LIMIT_o1_preview
            self.config_GPT_TIKTOKEN_ENGINE_NAME = self.config_GPT_ENGINE_NAME

            self.GPT_TOKEN_QUERY_DOLLOR_PER_1M = GPT_TOKEN_PRICE_QUERY_DOLLER_o1_preview
            self.GPT_TOKEN_QUERY_CACHED_DOLLOR_PER_1M = GPT_TOKEN_PRICE_QUERY_CACHED_DOLLER_o1_preview
            self.GPT_TOKEN_RESPONSE_DOLLOR_PER_1M = GPT_TOKEN_PRICE_RESPONSE_DOLLER_o1_preview

        elif self.config_g_GPT_MODEL == GPT_ENGINE_NAME_o1:                         # o1
            self.config_GPT_ENGINE_NAME = GPT_ENGINE_NAME_o1
            self.config_GPT_ENGINE_SUPPORT_MAX_TOKEN = GPT_ENGINE_TOKEN_RESPONSE_LIMIT_o1
            self.config_GPT_TIKTOKEN_ENGINE_NAME = self.config_GPT_ENGINE_NAME

            self.GPT_TOKEN_QUERY_DOLLOR_PER_1M = GPT_TOKEN_PRICE_QUERY_DOLLER_o1
            self.GPT_TOKEN_QUERY_CACHED_DOLLOR_PER_1M = GPT_TOKEN_PRICE_QUERY_CACHED_DOLLER_o1
            self.GPT_TOKEN_RESPONSE_DOLLOR_PER_1M = GPT_TOKEN_PRICE_RESPONSE_DOLLER_o1

        elif self.config_g_GPT_MODEL == GPT_ENGINE_NAME_o1_mini:                    # o1-mini
            self.config_GPT_ENGINE_NAME = GPT_ENGINE_NAME_o1_mini
            self.config_GPT_ENGINE_SUPPORT_MAX_TOKEN = GPT_ENGINE_TOKEN_RESPONSE_LIMIT_o1_mini
            self.config_GPT_TIKTOKEN_ENGINE_NAME = self.config_GPT_ENGINE_NAME

            self.GPT_TOKEN_QUERY_DOLLOR_PER_1M = GPT_TOKEN_PRICE_QUERY_DOLLER_o1_mini
            self.GPT_TOKEN_QUERY_CACHED_DOLLOR_PER_1M = GPT_TOKEN_PRICE_QUERY_CACHED_DOLLER_o1_mini
            self.GPT_TOKEN_RESPONSE_DOLLOR_PER_1M = GPT_TOKEN_PRICE_RESPONSE_DOLLER_o1_mini

        elif self.config_g_GPT_MODEL == GPT_ENGINE_NAME_o3_mini:                    # o3-mini
            self.config_GPT_ENGINE_NAME = GPT_ENGINE_NAME_o3_mini
            self.config_GPT_ENGINE_SUPPORT_MAX_TOKEN = GPT_ENGINE_TOKEN_RESPONSE_LIMIT_o3_mini
            self.config_GPT_TIKTOKEN_ENGINE_NAME = self.config_GPT_ENGINE_NAME

            self.GPT_TOKEN_QUERY_DOLLOR_PER_1M = GPT_TOKEN_PRICE_QUERY_DOLLER_o3_mini
            self.GPT_TOKEN_QUERY_CACHED_DOLLOR_PER_1M = GPT_TOKEN_PRICE_QUERY_CACHED_DOLLER_o3_mini
            self.GPT_TOKEN_RESPONSE_DOLLOR_PER_1M = GPT_TOKEN_PRICE_RESPONSE_DOLLER_o3_mini

        elif self.config_g_GPT_MODEL == GPT_ENGINE_NAME_o4_mini:                    # o4-mini
            self.config_GPT_ENGINE_NAME = GPT_ENGINE_NAME_o4_mini
            self.config_GPT_ENGINE_SUPPORT_MAX_TOKEN = GPT_ENGINE_TOKEN_RESPONSE_LIMIT_o4_mini
            self.config_GPT_TIKTOKEN_ENGINE_NAME = self.config_GPT_ENGINE_NAME

            self.GPT_TOKEN_QUERY_DOLLOR_PER_1M = GPT_TOKEN_PRICE_QUERY_DOLLER_o4_mini
            self.GPT_TOKEN_QUERY_CACHED_DOLLOR_PER_1M = GPT_TOKEN_PRICE_QUERY_CACHED_DOLLER_o4_mini
            self.GPT_TOKEN_RESPONSE_DOLLOR_PER_1M = GPT_TOKEN_PRICE_RESPONSE_DOLLER_o4_mini

        else:
            sys.exit("Critical error. mAllArgDicts is None[EngineVars_init]")

        self.config_GPT_PARAMETER_TEMPERATURE = GPT_PARAMETER_TEMPERATURE
        self.config_GPT_PARAMETER_TOP_P = GPT_PARAMETER_TOP_P
        self.config_GPT_PARAMETER_SEED = (random.randint(1, 99))  #GPT_PARAMETER_SEED
        self.config_GPT_PARAMETER_N = GPT_PARAMETER_N
        self.config_GPT_PARAMETER_FREQUENCY_PANALTY = GPT_PARAMETER_FREQUENCY_PENALTY
        self.config_GPT_PARAMETER_PRESENCE_PENALTY = GPT_PARAMETER_PRESENCE_PENALTY
        self.config_GPT_TOKEN_MONEY_QUERY_PER_1token = self.GPT_TOKEN_QUERY_DOLLOR_PER_1M / GPT_TOKEN_QUERY_1M_GPT
        self.config_GPT_TOKEN_MONEY_QUERY_CACHE_PER_1token = self.GPT_TOKEN_QUERY_CACHED_DOLLOR_PER_1M / GPT_TOKEN_QUERY_1M_GPT
        self.config_GPT_TOKEN_MONEY_RESPONSE_PER_1token = self.GPT_TOKEN_RESPONSE_DOLLOR_PER_1M / GPT_TOKEN_RESPONSE_1M_GPT
        self.config_GPT_TOKEN_QUERY_ADJ = 7
        self.config_GPT_TOKEN_RESPONSE_ADJ = 0

    def __str__(self):
        retStr = f"■ EngineVars : \n"

        retStr = retStr + f'config_g_PROGRAM_MODE:{self.config_g_PROGRAM_MODE}\n' \
                          f'config_g_GPT_MODEL:{self.config_g_GPT_MODEL}\n' \
                          f'config_g_GPT_DEPLOY:{self.config_g_GPT_DEPLOY}\n' \
                          f'config_GPT_ENGINE_NAME:{self.config_GPT_ENGINE_NAME}\n' \
                          f'config_GPT_ENGINE_TYPE_IDX:{self.config_GPT_ENGINE_TYPE_IDX}\n' \
                          f'config_GPT_TIKTOKEN_ENGINE_NAME:{self.config_GPT_TIKTOKEN_ENGINE_NAME}\n' \
                          f'config_GPT_ENGINE_SUPPORT_MAX_TOKEN:{self.config_GPT_ENGINE_SUPPORT_MAX_TOKEN}\n' \
                          f'config_GPT_PARAMETER_TEMPERATURE:{self.config_GPT_PARAMETER_TEMPERATURE}\n' \
                          f'config_GPT_PARAMETER_TOP_P:{self.config_GPT_PARAMETER_TOP_P}\n' \
                          f'config_GPT_PARAMETER_SEED:{self.config_GPT_PARAMETER_SEED}\n' \
                          f'config_GPT_PARAMETER_N:{self.config_GPT_PARAMETER_N}\n' \
                          f'config_GPT_PARAMETER_FREQUENCY_PANALTY:{self.config_GPT_PARAMETER_FREQUENCY_PANALTY}\n' \
                          f'config_GPT_PARAMETER_PRESENCE_PENALTY:{self.config_GPT_PARAMETER_PRESENCE_PENALTY}\n' \
                          f'config_GPT_TOKEN_MONEY_QUERY_PER_1token:{self.config_GPT_TOKEN_MONEY_QUERY_PER_1token:.8f}\n' \
                          f'config_GPT_TOKEN_MONEY_QUERY_CACHE_PER_1token:{self.config_GPT_TOKEN_MONEY_QUERY_CACHE_PER_1token:.8f}\n' \
                          f'config_GPT_TOKEN_MONEY_RESPONSE_PER_1token:{self.config_GPT_TOKEN_MONEY_RESPONSE_PER_1token:.8f}\n' \
                          f'config_GPT_TOKEN_QUERY_ADJ:{self.config_GPT_TOKEN_QUERY_ADJ}\n' \
                          f'config_GPT_TOKEN_RESPONSE_ADJ:{self.config_GPT_TOKEN_RESPONSE_ADJ}\n'
        retStr = f'{retStr}\n'

        return retStr
