# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import tiktoken
from openai import OpenAIError

from GlobalUtil import *
from MyKeyStore import *
from apievaluation.engines.query_table import *
from config.engine_config import *


class AbstractApiEngine(ABC):
    def __init__(self, argThreadId, argArgs, argEngineVars, argTargetPrompt, argMyLog, argSentencesList):
        self.my_retry_count : int = 0
        self.mMyThreadId = argThreadId
        self.mArgs = argArgs
        self.mEngineVars = argEngineVars
        self.mTargetPrompt = argTargetPrompt
        self.mMyLog = argMyLog
        self.mSentencesList = argSentencesList
        self.timeout_sec = 60  # 최대 10초 대기

    def _inner_encoding_getter(self, encoding_type: str):
        return tiktoken.encoding_for_model(encoding_type)

    def _inner_tokenizer(self, string: str, encoding_type: str) -> list:
        encoding = self._inner_encoding_getter(encoding_type)
        # print (encoding)
        tokens = encoding.encode(string)
        return tokens

    def _token_counter(self, string: str, encoding_type: str) -> int:
        num_tokens = len(self._inner_tokenizer(string, encoding_type))
        return num_tokens

    def _make_dummy_table(self, argSlicedArrSentences):
        self.mMyLog.d(f'_make_dummy_table(tid:{self.mMyThreadId})')
        arrDummyResultAllTables = []

        if self.mArgs.getValInGlobalArg(ARG_KEY_NAME_PROMPTTYPE) == CONFIG_NAME_VALUE_LISTEN or \
                self.mArgs.getValInGlobalArg(ARG_KEY_NAME_PROMPTTYPE) == CONFIG_NAME_VALUE_CONVERSATION:
            for _idx_loop in range(0, 1):  # for dummy
                queryResultOneTable = QueryOneTableEvalImg(self.mArgs)
                arrDummyResultAllTables.append(queryResultOneTable)
                for _idx in range(0, int(self.mArgs.getValInnerArg(CONFIG_NAME_KEY_TOTALCOUNTOFSENTENCES))):
                    queryResultOneTable.add_record('0000', 'FAKE', 'FAKE', 'FAKE', 'FAKE')
            pass
        else:
            for _idx_loop in range(0, 1):  # for dummy
                queryResultOneTable = QueryOneTableEvalImg(self.mArgs)
                arrDummyResultAllTables.append(queryResultOneTable)
                try:
                    for _idx in range(0, int(self.mArgs.getValInGlobalArg(ARG_KEY_NAME_SENTENCESCOUNT))):
                        queryResultOneTable.add_fake_record(arg_idx = 0)
                except TypeError:
                    print(f'OMG!!! tid:{self.mMyThreadId}, self.mArgs.getValInGlobalArg(ARG_KEY_NAME_SENTENCESCOUNT):{self.mArgs.getValInGlobalArg(ARG_KEY_NAME_SENTENCESCOUNT)}')

            pass

        return arrDummyResultAllTables

    def _get_completion_response_from(self, argEnumEngineName, argUserPromptContent, argSystemPromptContent = None, usedTokenCount = 0):

        if argEnumEngineName == IDX_ENGINE_NAME_GPT:
            g_client = get_client_ai_gpt_gpt()

            response = g_client.chat.completions.create(
                model=self.mEngineVars.config_GPT_ENGINE_NAME,
                messages=[
                    {
                        "role": "user",
                        "content": argUserPromptContent
                    }
                ],
                temperature=self.mEngineVars.config_GPT_PARAMETER_TEMPERATURE,
                # top_p=self.mEngineVars.config_GPT_PARAMETER_TOP_P,
                seed=self.mEngineVars.config_GPT_PARAMETER_SEED,
                n=self.mEngineVars.config_GPT_PARAMETER_N,
                # frequency_penalty=self.mEngineVars.config_GPT_PARAMETER_FREQUENCY_PANALTY,
                # presence_penalty=self.mEngineVars.config_GPT_PARAMETER_PRESENCE_PENALTY,
                # max_tokens=self.mEngineVars.config_GPT_ENGINE_SUPPORT_MAX_TOKEN - usedTokenCount
            )

            return response

        elif argEnumEngineName == IDX_ENGINE_NAME_AZURE:
            # g_client = get_client_ai_gpt_msa(self.mEngineVars.config_GPT_ENGINE_NAME)
            g_client = get_client_ai_gpt_msa(argEngineName=self.mEngineVars.config_GPT_ENGINE_NAME, argDeployModel=self.mEngineVars.config_g_GPT_DEPLOY)
            response = g_client.chat.completions.create(
                # model=self.mEngineVars.config_GPT_ENGINE_NAME,
                model=self.mEngineVars.config_g_GPT_DEPLOY,
                messages=[
                    {
                        "role": "user",
                        "content": argUserPromptContent
                    }
                ],
                temperature=self.mEngineVars.config_GPT_PARAMETER_TEMPERATURE,
                # top_p=self.mEngineVars.config_GPT_PARAMETER_TOP_P,
                seed=self.mEngineVars.config_GPT_PARAMETER_SEED,
                n=self.mEngineVars.config_GPT_PARAMETER_N,
                # frequency_penalty=self.mEngineVars.config_GPT_PARAMETER_FREQUENCY_PANALTY,
                # presence_penalty=self.mEngineVars.config_GPT_PARAMETER_PRESENCE_PENALTY,
                # max_tokens=self.mEngineVars.config_GPT_ENGINE_SUPPORT_MAX_TOKEN - usedTokenCount
            )
            return response

    # ===================================================================================
    def __delattr__(self, __name):
        super().__delattr__(__name)

    # ===================================================================================
    # for client
    def prepare_client(self):
        client = None
        retries = 0
        while retries < ASR_MAX_RETRY_COUNT:
            try:
                if self.mEngineVars.config_GPT_ENGINE_TYPE_IDX == IDX_ENGINE_NAME_AZURE:

                    if self.mEngineVars.config_GPT_ENGINE_NAME == GPT_ENGINE_NAME_GPT4o:
                        ___engine_api_key = keystore_get_key_type(argType=KEYTYPE_IDX_GPTScenario_Azure_OpenAI_GPT4o)
                        ___engine_ep = keystore_get_ep_type(argType=EPTYPE_IDX_GPTScenario_Azure_OpenAI_GPT4o)
                        ___engine_api_version = keystore_get_apiversion_type(argType=APIVERSIONTYPE_IDX_GPTScenario_Azure_OpenAI_GPT4o)
                    elif self.mEngineVars.config_GPT_ENGINE_NAME == GPT_ENGINE_NAME_GPT4o_mini:
                        ___engine_api_key = keystore_get_key_type(argType=KEYTYPE_IDX_GPTScenario_Azure_OpenAI_GPT4o_mini)
                        ___engine_ep = keystore_get_ep_type(argType=EPTYPE_IDX_GPTScenario_Azure_OpenAI_GPT4o_mini)
                        ___engine_api_version = keystore_get_apiversion_type(argType=APIVERSIONTYPE_IDX_GPTScenario_Azure_OpenAI_GPT4o_mini)
                    else:
                        ___engine_api_key = keystore_get_key_type(argType=KEYTYPE_IDX_GPTScenario_Azure_OpenAI_GPT4o)
                        ___engine_ep = keystore_get_ep_type(argType=EPTYPE_IDX_GPTScenario_Azure_OpenAI_GPT4o)
                        ___engine_api_version = keystore_get_apiversion_type(argType=APIVERSIONTYPE_IDX_GPTScenario_Azure_OpenAI_GPT4o)
                        self.mMyLog.e(f"ERROR EngineName.{self.mEngineVars.config_GPT_ENGINE_NAME}", argGoExit=True)

                    client = AzureOpenAI(api_key=___engine_api_key,
                                         azure_endpoint=___engine_ep,
                                         api_version=___engine_api_version,
                                         http_client=None if (self.mEngineVars.config_g_PROGRAM_MODE == GPT_PROGRAM_PROXY_MODE_HOME) else (
                                             httpx.Client(verify=False, proxy=HTTP_PROXY_IP_ADDRESS)),
                                         timeout=self.timeout_sec)
                elif self.mEngineVars.config_GPT_ENGINE_TYPE_IDX == IDX_ENGINE_NAME_GPT:
                    api_key = keystore_get_key_type(argType=KEYTYPE_IDX_GPTScenario_OpenAI_NONE_NONE)

                    client = OpenAI(api_key=api_key,
                                    default_headers={"OpenAI-Beta": "assistants=v2"},
                                    http_client=None if (self.mEngineVars.config_g_PROGRAM_MODE == GPT_PROGRAM_PROXY_MODE_HOME) else (
                                        httpx.Client(verify=False, proxy=HTTP_PROXY_IP_ADDRESS)),
                                    timeout=self.timeout_sec)
                    pass
                else:
                    self.mMyLog.e(f"ERROR Engine Type.{self.mEngineVars.config_GPT_ENGINE_TYPE_IDX}", argGoExit=True)

                return client
            except OpenAIError as e:
                # Prcessing all OpenAI API error with TimeoutError
                retries += 1
                print(f"Error occurred: {e}. Retrying {retries}/{ASR_MAX_RETRY_COUNT}...")
                time.sleep(2)  # retry

        if retries >= ASR_MAX_RETRY_COUNT:
            return None
        else:
            print(f"OMG!!({retries}) prepare_client : check retries.")
            return None

    # for assistant
    def prepare_assistant_and_id(self, argClient, argAsistantName="An expert lecturer"
                                 , argInstructions=""
                                 , argModel=GPT_ENGINE_NAME_GPT4o_mini
                                 , argTemperature=1.8
                                 , argTop_p=0.9):
        retries = 0

        while retries < ASR_MAX_RETRY_COUNT:
            try:
                assistant = argClient.beta.assistants.create(
                    name=argAsistantName,
                    instructions=argInstructions,
                    model=argModel,
                    temperature=argTemperature,
                    top_p=argTop_p,
                    timeout=self.timeout_sec,
                )
                return assistant, assistant.id
            except OpenAIError as e:
                # Prcessing all OpenAI API error with TimeoutError
                retries += 1
                print(f"Error occurred: {e}. Retrying {retries}/{ASR_MAX_RETRY_COUNT}...")
                time.sleep(2)  # retry
        if retries >= ASR_MAX_RETRY_COUNT:
            return None, None
        else:
            print(f"OMG!!({retries}) prepare_assistant_and_id : check retries.")
            return None, None

    def update_assistant(self, argClient, argInstructions=""):
        retries = 0

        while retries < ASR_MAX_RETRY_COUNT:
            try:
                assistant = argClient.beta.assistants.update(
                    instructions=argInstructions,
                    timeout=self.timeout_sec,
                )
                return assistant, assistant.id
            except OpenAIError as e:
                # Prcessing all OpenAI API error with TimeoutError
                retries += 1
                print(f"Error occurred: {e}. Retrying {retries}/{ASR_MAX_RETRY_COUNT}...")
                time.sleep(2)  # retry
        if retries >= ASR_MAX_RETRY_COUNT:
            return None, None
        else:
            print(f"OMG!!({retries}) update_assistant : check retries.")
            return None, None

    def delete_assistant(self, argClient, argAssistantId):
        retries = 0

        while retries < ASR_MAX_RETRY_COUNT:
            try:
                return argClient.beta.assistants.delete(argAssistantId, timeout=self.timeout_sec)
            except OpenAIError as e:
                # Prcessing all OpenAI API error with TimeoutError
                retries += 1
                print(f"Error occurred: {e}. Retrying {retries}/{ASR_MAX_RETRY_COUNT}...")
                time.sleep(2)  # retry

        if retries >= ASR_MAX_RETRY_COUNT:
            return None
        else:
            print(f"OMG!!({retries}) delete_assistant : check retries.")
            return None

    def retrieve_assistant_and_id(self, argClient, arg_exist_assistantId):
        retries = 0

        while retries < ASR_MAX_RETRY_COUNT:
            try:
                assistant = argClient.beta.assistants.retrieve(arg_exist_assistantId)
                if assistant:
                    return assistant, assistant.id
                else:
                    return None, None
            except OpenAIError as e:
                # Prcessing all OpenAI API error with TimeoutError
                retries += 1
                print(f"Error occurred: {e}. Retrying {retries}/{ASR_MAX_RETRY_COUNT}...")
                time.sleep(2)  # retry

        if retries >= ASR_MAX_RETRY_COUNT:
            return None, None
        else:
            print(f"OMG!!({retries}) retrieve_assistant_and_id : check retries.")
            return None, None

    # for thread
    def prepare_thread(self, argClient):
        retries = 0
        while retries < ASR_MAX_RETRY_COUNT:
            try:
                thread = argClient.beta.threads.create(timeout=self.timeout_sec)
                return thread, thread.id
            except OpenAIError as e:
                # Prcessing all OpenAI API error with TimeoutError
                retries += 1
                print(f"Error occurred: {e}. Retrying {retries}/{ASR_MAX_RETRY_COUNT}...")
                time.sleep(2)  # retry

        if retries >= ASR_MAX_RETRY_COUNT:
            return None, None
        else:
            print(f"OMG!!({retries}) prepare_thread : check retries.")
            return None, None

    def delete_thread(self, argClient, argThreadId):
        retries = 0
        while retries < ASR_MAX_RETRY_COUNT:
            try:
                return argClient.beta.threads.delete(argThreadId, timeout=self.timeout_sec)
            except OpenAIError as e:
                # Prcessing all OpenAI API error with TimeoutError
                retries += 1
                print(f"Error occurred: {e}. Retrying {retries}/{ASR_MAX_RETRY_COUNT}...")
                time.sleep(2)  # retry

        if retries >= ASR_MAX_RETRY_COUNT:
            return None
        else:
            print(f"OMG!!({retries}) delete_thread : check retries.")
            return None

    # for message
    def prepare_message(self, argClient, argThreadId, argRole, argUserPrompt):
        retries = 0

        while retries < ASR_MAX_RETRY_COUNT:
            try:
                return argClient.beta.threads.messages.create(thread_id=argThreadId, role=argRole, content = argUserPrompt, timeout=self.timeout_sec)
            except OpenAIError as e:
                # Prcessing all OpenAI API error with TimeoutError
                retries += 1
                print(f"Error occurred: {e}. Retrying {retries}/{ASR_MAX_RETRY_COUNT}...")
                time.sleep(2)  # retry

        if retries >= ASR_MAX_RETRY_COUNT:
            return None
        else:
            print(f"OMG!!({retries}) prepare_message : check retries.")
            return None

    def delete_message(self, argClient, argThreadId, argMessageId):
        retries = 0
        while retries < ASR_MAX_RETRY_COUNT:
            try:
                return argClient.beta.threads.messages.delete(message_id=argMessageId, thread_id=argThreadId, timeout=self.timeout_sec)
            except OpenAIError as e:
                # Prcessing all OpenAI API error with TimeoutError
                retries += 1
                print(f"Error occurred: {e}. Retrying {retries}/{ASR_MAX_RETRY_COUNT}...")
                time.sleep(2)  # retry

        if retries >= ASR_MAX_RETRY_COUNT:
            return None
        else:
            print(f"OMG!!({retries}) delete_message : check retries.")
            return None

    # for run
    def prepare_run(self, argClient, argThreadId, argAssistantId):
        retries = 0
        while retries < ASR_MAX_RETRY_COUNT:
            try:
                run = argClient.beta.threads.runs.create(thread_id=argThreadId, assistant_id=argAssistantId, timeout=self.timeout_sec)
                return run
            except OpenAIError as e:
                # Prcessing all OpenAI API error with TimeoutError
                retries += 1
                print(f"Error occurred: {e}. Retrying {retries}/{ASR_MAX_RETRY_COUNT}...")
                time.sleep(2)  # retry

        if retries >= ASR_MAX_RETRY_COUNT:
            return None
        else:
            print(f"OMG!!({retries}) prepare_run : check retries.")
            return None

    def cancel_run(self, argClient, argThreadId, argRunId):
        return argClient.beta.threads.runs.cancel(argThreadId, argRunId)

    def submit_message_and_run(self, argClient, argAssistantId, argThreadId, argRole, argUserPrompt):
        message = self.prepare_message(argClient, argThreadId, argRole, argUserPrompt)
        # self.show_json(obj=message)

        run = self.prepare_run(argClient, argThreadId, argAssistantId)
        # self.show_json(obj=run)
        return message, run

    ########### utils
    def show_json(self, obj):
        self.mMyLog.d(obj.model_dump_json(indent=4))

    def print_message(self, response):
        for res in response:
            self.mMyLog.d(f"[{res.role.upper()}]\n{res.content[0].text.value}\n")
        self.mMyLog.d("---" * 20)

    def wait_on_run(self, run, client, thread):
        retries = 0
        while retries < ASR_MAX_RETRY_COUNT:
            try:
                while run.status == "queued" or run.status == "in_progress":
                    run = client.beta.threads.runs.retrieve(
                        thread_id=thread.id,
                        run_id=run.id,
                        timeout=self.timeout_sec
                    )
                    # sleep time
                    time.sleep(0.5)
                return run
            except OpenAIError as e:
                # Prcessing all OpenAI API error with TimeoutError
                retries += 1
                print(f"Error occurred: {e}. Retrying {retries}/{ASR_MAX_RETRY_COUNT}...")
                time.sleep(2)  # retry

        if retries >= ASR_MAX_RETRY_COUNT:
            return None
        else:
            print(f"OMG!!({retries}) wait_on_run : check retries.")
            return None

    def get_response(self, client, thread, message):
        retries = 0
        while retries < ASR_MAX_RETRY_COUNT:
            try:
                return client.beta.threads.messages.list(thread_id=thread.id, order="asc", after=message.id, timeout=self.timeout_sec)
            except OpenAIError as e:
                # Prcessing all OpenAI API error with TimeoutError
                retries += 1
                print(f"Error occurred: {e}. Retrying {retries}/{ASR_MAX_RETRY_COUNT}...")
                time.sleep(2)  # retry

        if retries >= ASR_MAX_RETRY_COUNT:
            return None
        else:
            print(f"OMG!!({retries}) get_response : check retries.")
            return None

    # ===================================================================================
    @abstractmethod
    def do_eval(self, slicedArrSentences):
        # To do here in the impl-class
        pass

    def change_to_myLog(self, argNewMyLog):
        self.mMyLog = argNewMyLog

    def clear_client(self, argClient, argAssistantId, argThreadId, argMessge):
        ## Delete Message
        delete_message_response = self.delete_message(argClient=argClient, argThreadId=argThreadId, argMessageId=argMessge.id)

        ################################# Delete Thread
        delete_thread_response = self.delete_thread(argClient, argThreadId)
        self.mMyLog.d(f'[[[___DELETE Thread___]]]')
        self.mMyLog.d(delete_thread_response)
        self.mMyLog.d()

        ################################# Delete Assistant
        delete_assistant_response = self.delete_assistant(argClient, argAssistantId)
        self.mMyLog.d(f'[[[___Delete Assistant___]]]')
        self.show_json(delete_assistant_response)
        pass
