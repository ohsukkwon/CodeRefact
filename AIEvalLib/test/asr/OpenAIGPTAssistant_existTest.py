# -*- coding: utf-8 -*-
import re
import time

import pandas as pd

from GlobalVars import *
from GlobalUtil import get_date_file_name, get_client_ai_gpt_gpt, get_dir_result_without_overlay
from MyKeyStore import *

#================================================================ All util functions
___access_key_id = keystore_get_key_type(argType=KEYTYPE_IDX_GPTScenario_OpenAI_NONE_NONE)

g_client = None

# for client
def prepare_client():
    client = get_client_ai_gpt_gpt()
    return client

# for assistant
def prepare_assistant_and_id(argClient, argAsistantName="An expert lecturer"
                             , argInstructions="You are an expert lecturer in all fields of society, including politics, economics, culture, IT, travel, and psychology."
                             , argModel=ASR_NAME_GPT_MODEL
                             , argTemperature = ASR_NAME_GPT_PARAM_TEMPERATURE
                             , argTop_p = ASR_NAME_GPT_PARAM_TOP_P):
    assistant = argClient.beta.assistants.create(
        name=argAsistantName,
        instructions=argInstructions,
        model=argModel,
        temperature=argTemperature,
        top_p=argTop_p
    )
    return assistant, assistant.id

def delete_assistant(argClient, argAssistantId):
    return argClient.beta.assistants.delete(argAssistantId)

# for client
def prepare_thread(argClient):
    thread = argClient.beta.threads.create()
    return thread, thread.id

def delete_thread(argClient, argThreadId):
    return argClient.beta.threads.delete(argThreadId)

# for message
def prepare_message(argClient, argThreadId, argUserPrompt):
    return argClient.beta.threads.messages.create(thread_id=argThreadId, role="user" , content=argUserPrompt)

def delete_message(argClient, argThreadId, argMessageId):
    return argClient.beta.threads.messages.delete(message_id=argMessageId, thread_id=argThreadId)

# for run
def prepare_run(argClient, argThreadId, argAssistantId):
    run = argClient.beta.threads.runs.create( thread_id=argThreadId, assistant_id=argAssistantId)
    return run

def cancel_run(argClient, argThreadId, argRunId):
    return argClient.beta.threads.runs.cancel(argThreadId, argRunId)

def submit_message_and_run(argClient, argAssistantId, argThreadId, argUserPrompt):
    message = prepare_message(argClient, argThreadId, argUserPrompt)
    show_json(message)

    run = prepare_run(argClient, argThreadId, argAssistantId)
    show_json(run)
    return message, run

########### utils
def show_json(obj):
    print(obj.model_dump_json(indent=4))

def print_message(response):
    for res in response:
        print(f"[{res.role.upper()}]\n{res.content[0].text.value}\n")
    print("---" * 20)

def wait_on_run(run, client, thread):
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )
        # API 요청 사이에 잠깐의 대기 시간을 두어 서버 부하를 줄입니다.
        time.sleep(0.5)
    return run

def get_response(client, thread, message):
    return client.beta.threads.messages.list(thread_id=thread.id, order="asc", after=message.id)

if __name__ == "__main__":
    total_start_time = time.time()

    ################################# Create Client and Assistant
    g_client = prepare_client()
    #g_assistant, g_assistant_id = prepare_assistant_and_id(g_client)
    #print(f'[[[___CREATE Client___]]]', end=' : ')
    #show_json(g_assistant)

    g_assistant_id = ASR_ASSISTANTS_EXIST_ID_DEV

    ################################# Create Thread
    g_thread, g_thread_id = prepare_thread(g_client)
    print(f'[[[___CREATE Thread___]]]', end=' : ')
    show_json(g_thread)

    print(f"[[[NEW Thread ID]]] : {g_thread_id}")
    print()

    total_want_count = 60
    block_count_per_one = 30

    prompt_full_str = f'''
지금부터 한명이 청중에게 발표하는 형식의 발표 스크립트를 작성해줘.

발표자인 AndyO의 역할을 정의한다.
나이는 30, 성별은 female, 출신 국가는 korea, 직업은 programmer 이고,
취미는 computer game, 성격은 extroverted, 연봉은 100000 이다.
IT전문가로써 Youtube가 사회변화에 미치는 영향에 대해 깊은 지식을 가지고 있다.

발표자는 Youtube의 발전이 사회 전반에 미치는 변화에 대하여 구체적인 예시를 통해 상세하게 장단점을 설명할 것이다.
참조 문서 및 구체적인 예시는 각종 신문 기사 및 블로그 내용을 참고하고,
일반인들이 충분히 이해할수 있는 쉬운 수준의 단어를 사용하여 구어체적인 문장을 작성할것.

발표 시간은 1시간이상의 분량으로 작성하고 
이야기의 내용은 자연스럽게 이어지고, 주제는 명확하고 일관되게 유지되어야 해.
내용은 서론/본론/결론의 형식에 맞도록 작성해줘.

#문장생성 주요기준(4가지)
1) "Sentence" 열의 문장은 문법과 철자에 오류가 전혀 없어야 함.
2) "Sentence" 열의 문장에 인종차별,욕설,비속어가 포함되면 안됨.
3) "Sentence" 열의 문장에 개인정보와 민감한 정보가 포함되면 안됨.
4) "MotherLanaugeTranslation" 열의 문장은 모국어인 Engilsh로 작성할 것.

#답변 주요기준(7가지)
1) 답변은 반드시 표 형식으로만 이뤄져야 함.
2) 표 이전,이후에 절대 문장을 적지 말것.
3) 열은 No,PersonName,Sentence,MotherLanaugeTranslation 순서대로 작성할 것.
4) "Sentence"열은 korean로 작성할 것.
5) "Sentence"열에는 생성된 대화 문장을 적을것.
6) "MotherLanaugeTranslation"열은 "Sentence"열에서 생성된 문장을 Engilsh로 번역한 문장을 적을것.
7) 전체 스크립트 내용에 절대 같은 문장을 반복하지 말것.

#답변 형식
| No | PersonName | Sentence | MotherLanaugeTranslation |
|---|---|---|---|
|1|AndyO|korean 언어로 생성된 문장|"Sentence"열에서 생성된 문장을 Engilsh로 번역한 문장|
|2|AndyO|korean 언어로 생성된 문장|"Sentence"열에서 생성된 문장을 Engilsh로 번역한 문장|

#예시 문장(모국어가 영어일 경우)
| No | PersonName | Sentence | MotherLanaugeTranslation |
|---|---|---|---|
|1|AndyO|안녕하세요 지금부터 영화에 대해 소개를 하겠습니다.|Hello, I will now introduce a movie.|
|2|AndyO|오늘 소개할 영화는 스티븐 킹이 1982년에 집필한 <리타 헤이워스와 쇼생크 탈출>을 원작으로 하는 '쇼생크 탈출'입니다.|The movie I will introduce today is 'The Shawshank Redemption', based on Stephen King's 1982 novella 'Rita Hayworth and Shawshank Redemption'.|

전체 스크립트는 총 {total_want_count}문장으로 작성하고,답변할 때, 반드시 {block_count_per_one}문장씩 구분해서 답변해줘.
표가 분리 되더라도 발표 스크립트 내용은 지속적으로 이어지는 형태로 작성되어야 한다.
'''
    print(f'prompt_full_str : {prompt_full_str}')

    prompt_sub_str = '''계속해서 더 작성해줘.'''

    mArrQueryResultAllTables = []
    idx_count = 0   # total count
    p = re.compile(r'^\|.*$', re.MULTILINE)
    mRunResponseMessageList = None
    mMessage = None
    while idx_count < (total_want_count - 1):
        ################################# Create Message & Run
        mMessage, mRun = submit_message_and_run(g_client, g_assistant_id, g_thread_id, prompt_full_str if idx_count == 0 else prompt_sub_str)
        print(f'[[[___CREATE Message___]]]', end=' : ')
        show_json(mMessage)
        print()

        print(f'[[[___CREATE Run___]]]', end=' : ')
        show_json(mRun)
        print()

        mRunResponse = wait_on_run(mRun, g_client, g_thread)
        print(f'[[[___Response Run___]]]', end=' : ')
        show_json(mRunResponse)
        print()

        mRunResponseMessageList = get_response(g_client, g_thread, mMessage)
        print(f'[[[___Response mRunResponseMessageList___]]]', end=' : ')
        show_json(mRunResponseMessageList)
        print()

        trimedResponseStr = mRunResponseMessageList.data[0].content[0].text.value.strip()

        print('trimedResponseStr : ')
        print(trimedResponseStr)
        print('====================================')

        arrSplitedJustOneLine = p.findall(trimedResponseStr)

        for inner_idx, oneLineItem in enumerate(arrSplitedJustOneLine[2:]):
            itemArr = (oneLineItem.strip()[1:-1].split(r'|'))  # Remove the | at both ends of the sentence.
            if len(itemArr) != 4:
                mArrQueryResultAllTables.append(['0000', 'FAKE', 'FAKE', 'FAKE'])
                print(f'oneLineItem : {oneLineItem}')
            else:
                # | No | PersonName | Sentence | MotherLanaugeTranslation |
                # |1|AndyO|안녕하세요!|Hello!|
                try:
                    mArrQueryResultAllTables.append(['{0:04d}'.format(int(itemArr[0])), itemArr[1], itemArr[2], itemArr[3]])
                except ValueError:
                    print(f'oneLineItem : {oneLineItem}, inner_idx:{inner_idx}')

            idx_count = idx_count+1

    print('mArrQueryResultAllTables:')
    # print(mArrQueryResultAllTables)
    for oneLineItem in mArrQueryResultAllTables:
        print(f'{oneLineItem[0]}___{oneLineItem[1]}___{oneLineItem[2]}___{oneLineItem[3]}')

    column_name = ['No', 'PersonName', 'Sentence', 'MotherLanaugeTranslation']
    df_total_results = pd.DataFrame.from_records(mArrQueryResultAllTables, columns=column_name)
    df_total_results.index = df_total_results.index + 1  # change index from 0 to 1
    df_total_results.head()

    inner_dir_name = get_dir_result_without_overlay()

    result_excel_full_path  = os.path.join(f"{inner_dir_name}", f'{get_date_file_name()}.{FILE_EXTENSION_WITHOUT_DOT_XLSX}')
    result_csv_full_path    = os.path.join(f"{inner_dir_name}", f'{get_date_file_name()}.{FILE_EXTENSION_WITHOUT_DOT_CSV}')
    print(f'result_excel_full_path: {result_excel_full_path}')
    print(f'result_csv_full_path: {result_csv_full_path}')

    with pd.ExcelWriter(result_excel_full_path, engine='xlsxwriter') as excel_writer:
        df_total_results.to_excel(excel_writer, sheet_name=NAME_EXCEL_SHEET_SUMMARY, na_rep='EMPTY')

    df_total_results.to_csv(result_csv_full_path, sep='|', na_rep='EMPTY', encoding='utf-8-sig', header=False, index=False)

    ## Delete Message
    delete_message_response = delete_message(g_client, g_thread_id, mMessage.id)

    ################################# Delete Thread
    # delete_thread_response = delete_thread(g_client, g_thread_id)
    #print(f'[[[___DELETE Thread___]]]', end=' : ')
    #print(delete_thread_response)
    #print()

    # DON'T delete assistant.
    ################################# Delete assistant
    delete_assistant(g_client, g_assistant_id)

    total_elasped_time = time.time() - total_start_time
    print(f'<<<<<<<<<<<< E N D : [{total_elasped_time:0.9f} second(s)]')
    print()
