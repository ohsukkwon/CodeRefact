# -*- coding: utf-8 -*-
import csv
import datetime
import os
import re
import sys
import time

import pandas as pd
from openai import OpenAI
from openpyxl import load_workbook
from openpyxl.drawing.image import Image
from openpyxl.styles import Alignment
from tabulate import tabulate

from GlobalVars import *
from GlobalUtil import create_image_content
from test.TikTokenCalculator import get_tiktoken_count
from utils.GlobalUtil import get_date_file_name, process_image

__TAG_KEY_NO : str = 'No'
__EXCEL_COL_NO : str = 'A'

__TAG_KEY_PROMPT : str = 'Prompt'
__EXCEL_COL_PROMPT : str = 'B'

__TAG_KEY_STYLE : str = 'Style'
__EXCEL_COL_STYLE : str = 'C'

__TAG_KEY_IN_IMG : str = 'InImage'
__EXCEL_COL_INIMG : str = 'D'

__TAG_KEY_OUT_IMG : str = 'OutImage'
__EXCEL_COL_OUTIMG : str = 'E'

__TAG_KEY_SCORE : str = 'Score'
__EXCEL_COL_SCORE : str = 'F'

__TAG_KEY_REASON : str = 'Reason'
__EXCEL_COL_REASON : str = 'G'

__TAG_KEY_CAPTION : str = 'Caption'
__EXCEL_COL_CAPTION : str = 'H'

__PROMPT_IMG_EVAL : str = '''너는 지금부터 주어지는 이미지가 이미지 생성 Prompt를 제대로 반영하여 생성되었는지를 판단하는 전문판정위원 역할이야.
아래 "# 평가기준"을 정확하게 반영하여 평가해줘.
최종 답변은 반드시 아래 "# 출력양식(예시)"을 지켜서 답변해줘.

# 평가기준
1. 30점 만점 기준이며, 5점 단위로 평가해줘.
2. 프롬프트가 모두 정확히 반영이 되었다면, 30점 수준의 높은 점수를 부여할것.(30점)
3. 프롬프트가 모두 정확히 반영이 되고, 생성된 이미지의 각 객체의 특징에 명확한 오류가 있을 경우 일부 감점할것.(25점)
4. 프롬프트가 일부가 반영되지 않았더라도, 프롬프트가 대부분 반영되어 이미지가 프롬프트에 맞게 생성되었으면 20점 이상의 수준으로 반영해줘.(20점)
5. 프롬프트가 일부만 반영되고, 프롬프트의 전반적인 의미와도 다른 이미지가 생성되었으면 감점하여 15점 수준으로 낮게 평가할것.(15점)
6. 프롬프트가 전혀 반영되지 않았으면 10점으로 낮게 평가할것.(10점)
7. 만일 30점 만점이 아니면, 감점된 이유를 "Reason"열에 적고, 30점 만점이면 "Reason"열에 "만점" 으로만 표기 할것.
{inner_extra_criterions}

# 감정과 이미지의 관계
1. 행복, 기쁨, 사랑 : 꽃, 태양, 웃음, 하트 등의 이미지
2. 슬픔, 눈물 : 물방울 이미지
3. 짜증, 화남 : 눈썹이 올라간 표정, 천둥, 번개, 폭탄, 불 등의 이미지
4. 침울, 절망, 실망, 우울, 기운빠짐, 허탈 ,무너짐 : 축 처지거나 늘어진 모습이나, 전체적으로 회색톤의 어두운 이미지

# 출력양식(예시)
No:[제시된 No를 그대로 적을것]
Score:[주어지는 이미지가 이미지 생성 Prompt를 제대로 반영하여 생성되었는지를 총30점 기준으로 판단할것]
Reason:[위 점수에 대한 평가근거를 반드시 ko_KR으로 표현하고 반영된 프롬프트와 반영되지 않은 프롬프트를 구분하여 적을것]
Caption:[Generated image에 대한 Caption상세설명을 반드시 ko_KR으로 표현할 것]

아래와 같이 Header열이 포함된 MarkDown테이블로만 답변할것.
|No|Score|Reason|Caption|
|---|---|---|---|
|1|30|멋진 오로라가 있는 겨울 밤하늘 풍경을 보여주고, 땅에는 눈이 덮여 있는 모습은 북극을 충분히 반영하고 있습니다.|이 이미지는 멋진 오로라가 있는 겨울 풍경을 보여줍니다. 밤하늘에 푸르스름한 빛이 흐르고, 반짝이는 별들이 보입니다. 하늘은 푸른색과 보라색으로 물들어 있으며, 땅에는 눈이 덮여 있습니다. 강물이 장면을 반사하여 환상적인 분위기를 더합니다. 주위의 침엽수림이 그림에 깊이감을 더해 주며, 자연의 평온함을 느낄 수 있습니다.|

Generated image는 {inner_extra_original_img}Extra Prompt를 반영하여 생성하였다.
전문판정위원으로써 Generated image에 대해서 정확하게 평가해줘.'''

__PROMPT_EXTRA_CRITERIONS : str = '''8. 프롬프트를 모두 정확히 반영하였다면, Original image의 일부가 변경되거나 누락되었더라도 감점하지 말것.
9. 프롬프트를 모두 정확히 반영하였다면, 원본이 크게 변화되지 않았더라도 감점하지 말것.'''

__MAX_IMG_SIZE_IN_KB : int = 1024
__DETAIL_MODE_IMG_THRESHOLD : int = 512

g_my_input_datas_arr : list = []

def do_main(arg_sys = None, __DIR_NAME_RESULT=None):
    global g_my_input_datas_arr

    eval_img_start_time = time.time()

    result_total_eval_arr = []

    EXT_EXCEL = '.xlsx'
    EXT_CSV = '.csv'
    fname_real_body = 'datas_noimg'

    fname_cur_time = get_date_file_name()

    fname_in_csv_file = f'in_{fname_real_body}'
    fname_in_csv_file_with_ext = f'{fname_in_csv_file}{EXT_CSV}'
    print(f'fname_in_csv_file_with_ext : {fname_in_csv_file_with_ext}')

    fname_out_csv_file = f'out_{fname_real_body}'
    fname_out_csv_file_with_ext = f'{fname_out_csv_file}_{fname_cur_time}{EXT_CSV}'
    print(f'fname_out_csv_file_with_ext : {fname_out_csv_file_with_ext}')

    fname_out_excel_file = f'out_{fname_real_body}'
    fname_out_excel_file_with_ext = f'{fname_out_excel_file}_{fname_cur_time}{EXT_EXCEL}'
    print(f'fname_out_excel_file_with_ext : {fname_out_excel_file_with_ext}')

    fname_out_excel_img_file = f'out_{fname_real_body}_img'
    fname_out_excel_img_file_with_ext = f'{fname_out_excel_img_file}_{fname_cur_time}{EXT_EXCEL}'
    print(f'fname_out_excel_img_file_with_ext : {fname_out_excel_img_file_with_ext}')

    out_image_dir = os.path.join(DIR_NAME_RES, DIR_NAME_RES_OutImage)
    in_image_dir = os.path.join(DIR_NAME_RES, DIR_NAME_RES_InImage)

    out_unique_tid_dir_full = os.path.join(DIR_NAME_RESULT, fname_cur_time)
    print(f'out_unique_tid_dir_full : {out_unique_tid_dir_full}')
    if not os.path.exists(out_unique_tid_dir_full):
        os.makedirs(out_unique_tid_dir_full)

    # file open
    input_csv_file = open(os.path.join(DIR_NAME_RES, DIR_NAME_RES_CSV, fname_in_csv_file_with_ext), "r", encoding='utf-8-sig')
    readlines = csv.reader(input_csv_file, delimiter=r'|')

    g_has_in_img = False
    for ___idx, arr_splitted_str_by_row in enumerate(readlines):
        if ___idx == 0:
            g_has_in_img = True if len(arr_splitted_str_by_row) == 5 else False     # 4:No InImage , 5: Has InImage, else : Error
        g_my_input_datas_arr.append(arr_splitted_str_by_row)

    # # # # #  START loop for all input datas  # # # # #
    # 0:A:No , 1:B: Prompt, 2:C:Style, 3:D:OutImage, [4:E:InImage]
    # if g_has_in_img:
    #     count_eval_size_per_1cycle = 4
    # else:
    #     count_eval_size_per_1cycle = 4
    count_eval_size_per_1cycle = 4

    count_all_input_datas = len(g_my_input_datas_arr)

    s_idx = 0
    e_idx = 0
    real_count_eval_size_per_1cycle = 0

    ___idx_per_1cycle = 0
    while e_idx < count_all_input_datas:
        s_idx = e_idx
        e_idx = count_all_input_datas if s_idx + count_eval_size_per_1cycle > count_all_input_datas else s_idx + count_eval_size_per_1cycle
        real_count_eval_size_per_1cycle = e_idx - s_idx

        print(f'================== count_all_input_datas -> split[{___idx_per_1cycle}]: [{s_idx}:{e_idx}] => __{real_count_eval_size_per_1cycle}__==================')

        client = OpenAI()

        ___inner_system_prompt = __PROMPT_IMG_EVAL.format(inner_extra_criterions='' if g_has_in_img == False else __PROMPT_EXTRA_CRITERIONS,
                                                   inner_extra_original_img='' if g_has_in_img == False else "Original image를 바탕으로, ",
                                                   )

        ___result_system_content_arr = []
        ___result_system_content_arr.insert(0,{  # 1st
            "type": "text",
            "text": ___inner_system_prompt
        })

        ___inner_user_prompt = ''
        ___result_user_content_arr = []

        for ___idx in range(real_count_eval_size_per_1cycle):
            ___item = g_my_input_datas_arr[s_idx + ___idx]

            ___inner_prompt_extra_img = PROMPT_EXTRA_IMG_ITEM.format(
                inner_no=___item[0],                                                                            # No
                innerPrompt=___item[1],                                                                         # Prompt
                innerStyle=___item[2],                                                                          # Style
                innerStyleExtra='' if (___item[2] is None or ___item[2] == '') else f'+{___item[2]} Style',     # StyleExtra
                inner_out_img=___item[3],                                                                       # OutImage
                # inner_in_img = ___item[4],                                                                    # InImage
                inner_in_img_extra='' if g_has_in_img == False else f'Original image:{___item[4]}',             # InImageExtra
            )
            ___inner_user_prompt = ___inner_user_prompt + ___inner_prompt_extra_img

            out_image_full_path = os.path.join(out_image_dir, ___item[3])
            # Getting the base64 string for image(jpg/png)
            #___inner_out_base64_image = encode_image(out_image_full_path)
            ___inner_out_base64_image, ___out_max_dim, ___out_img_dim = process_image(out_image_full_path, __MAX_IMG_SIZE_IN_KB)
            print(f'out_base64_image:{___out_max_dim , ___out_img_dim}')
            ___result_user_content_arr.append(create_image_content(___inner_out_base64_image, ___out_max_dim, __DETAIL_MODE_IMG_THRESHOLD))

            if g_has_in_img:
                in_image_full_path = os.path.join(in_image_dir, ___item[4])
                # Getting the base64 string for image(jpg/png)
                #___inner_in_base64_image = encode_image(in_image_full_path)
                ___inner_in_base64_image, ___in_max_dim, ___in_img_dim = process_image(in_image_full_path, __MAX_IMG_SIZE_IN_KB)
                print(f'in_base64_image:{___in_max_dim, ___in_img_dim}')
                ___result_user_content_arr.append(create_image_content(___inner_in_base64_image, ___in_max_dim, __DETAIL_MODE_IMG_THRESHOLD))

        ___result_user_content_arr.insert(0,{  # 1st
            "type": "text",
            "text": ___inner_user_prompt
        })

        print(f'-----------------------------------------')
        print(f'■ ___result_system_content_arr : ')
        print(f'{___result_system_content_arr[0]}')

        print(f'-----------------------------------------')
        print(f'■ ___result_user_content_arr : ')
        print(f'{___result_user_content_arr[0]}')

        result_token = get_tiktoken_count(arg_text=str(___result_user_content_arr[0]))
        print(f"■ String len:{len(str(___result_user_content_arr[0]))}")

        # print(f"result:{result}")
        print(f"■ Token count:{len(result_token)}")
        print(f'-----------------------------------------')


        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": ___result_system_content_arr,
                },
                {
                    "role": "user",
                    "content": ___result_user_content_arr,
                }
            ],
            temperature=1.6,
            top_p=0.8,
        )

        print("■ ___inner_prompt :")
        print(___inner_system_prompt)
        print()

        print(f'===> response : {response}')
        print()

        print(f'===> response[{___idx_per_1cycle}] : {response.choices[0]}')
        print()

        my_pattern = re.compile('^\\|.*$', re.MULTILINE)
        arrSplitedFromResponse = my_pattern.findall(response.choices[0].message.content.strip())

        # Except first 2lines(Header and Devider)
        for inner_idx, oneLineItem in enumerate(arrSplitedFromResponse[2:]):
            itemArr = (oneLineItem.strip()[1:-1].split('|'))  # remove '|' in the one line
            # itemArr[0]:No , itemArr[1]:평가점수 , itemArr[2]: 평가근거 , itemArr[3]:caption상세설명
            result_total_eval_arr.append([itemArr[0], itemArr[1], itemArr[2], itemArr[3]])

        ___idx_per_1cycle =+ 1

    # print(f'===> result_total_eval_arr : {result_total_eval_arr}')

    df_total_arr = []
    my_score_pattern = re.compile('[0-9.]+')
    for ___idx, ___item in enumerate(result_total_eval_arr):
        # print(f'===> result_total_eval_arr[{___idx}] : {result_total_eval_arr[___idx]}')

        digit_score = my_score_pattern.findall(result_total_eval_arr[___idx][1])    # Score
        # print(digit_score)

        df_total_arr.append({
            # Getting from result_total_eval_arr
            __TAG_KEY_NO: result_total_eval_arr[___idx][0],                               # No

            # Getting from g_my_input_datas_arr
            __TAG_KEY_OUT_IMG: g_my_input_datas_arr[___idx][3],                           # OutImage
            __TAG_KEY_IN_IMG : g_my_input_datas_arr[___idx][4] if g_has_in_img else '',   # InImage
            __TAG_KEY_PROMPT: g_my_input_datas_arr[___idx][1],                            # Prompt
            __TAG_KEY_STYLE: g_my_input_datas_arr[___idx][2],                             # Style

            # Getting from result_total_eval_arr
            __TAG_KEY_SCORE: digit_score[0],                                              # Score
            __TAG_KEY_REASON: result_total_eval_arr[___idx][2],                           # Reason
            __TAG_KEY_CAPTION: result_total_eval_arr[___idx][3]                           # Caption
        })

    # 0:A:No , 1:B: Prompt, 2:C:Style, 3:D:OutImage, 4:E:InImage, 5:F:Score, 6:G:Reason, 7:H:Caption
    df_total_results = pd.DataFrame.from_records(df_total_arr,
                                                 columns=[__TAG_KEY_NO,__TAG_KEY_PROMPT,__TAG_KEY_STYLE,__TAG_KEY_OUT_IMG,__TAG_KEY_IN_IMG,__TAG_KEY_SCORE,__TAG_KEY_REASON,__TAG_KEY_CAPTION])

    with pd.ExcelWriter(os.path.join(out_unique_tid_dir_full,fname_out_excel_file_with_ext), engine='xlsxwriter') as excel_writer:
        df_total_results.to_excel(excel_writer, sheet_name="eval_image", na_rep='EMPTY', index=False)
    df_total_results.to_csv(os.path.join(out_unique_tid_dir_full,fname_out_csv_file_with_ext), sep='|', na_rep='EMPTY', encoding='utf-8-sig', index=False)

    # pd.set_option('display.max_rows', None)
    # pd.set_option('display.max_columns', None)
    # pd.set_option('display.width', None)

    # print(df_total_results)
    # print(df_total_results.to_markdown())
    print(tabulate(df_total_results, headers='keys', tablefmt='psql', showindex="never"))

    eval_img_end_time = time.time()
    eval_img_elasped_time = eval_img_end_time - eval_img_start_time
    now = datetime.datetime.now()
    formatted_date = now.strftime("%Y-%m-%d_%H:%M:%S")
    print(f'<<<<<<<<<<<< E N D(Eval Image) : [{eval_img_elasped_time:0.9f} second(s)] , NOW : [{formatted_date}]')
    print()

    # Attach Image files in the Excels
    T_workbook = load_workbook(os.path.join(out_unique_tid_dir_full,fname_out_excel_file_with_ext), data_only=True)
    T_worksheet = T_workbook.active

    for ___idx, ___item in enumerate(result_total_eval_arr):
        ## 이미지 불러오기
        out_image_full_path = os.path.join(out_image_dir, g_my_input_datas_arr[___idx][3])
        out_image = Image(out_image_full_path)
        in_image = None

        if g_has_in_img:
            in_image_full_path = os.path.join(in_image_dir, g_my_input_datas_arr[___idx][4])
            in_image = Image(in_image_full_path)

        out_image.width, out_image.height = 100, 100  # 크기 설정
        if g_has_in_img:
            in_image.width, in_image.height = 100, 100  # 크기 설정

        ## 이미지 픽셀을 셀 폭과 높이로 변환
        if ___idx == 0:
            T_worksheet.column_dimensions[__EXCEL_COL_OUTIMG].width = out_image.width / 5 # set width to image's out_image
            T_worksheet.column_dimensions[__EXCEL_COL_INIMG].width = out_image.width / 5  # set width to image's out_image
            T_worksheet.column_dimensions[__EXCEL_COL_PROMPT].width = 50
            T_worksheet.column_dimensions[__EXCEL_COL_REASON].width = 50
            T_worksheet.column_dimensions[__EXCEL_COL_CAPTION].width = 50
            T_worksheet.sheet_view.zoomScale = 80

        T_worksheet[f'{__EXCEL_COL_REASON}{___idx+2}'].alignment = Alignment(wrap_text=True)
        T_worksheet[f'{__EXCEL_COL_CAPTION}{___idx+2}'].alignment = Alignment(wrap_text=True)

        T_worksheet.row_dimensions[___idx+2].height = out_image.height

        T_worksheet.add_image(out_image, f'{__EXCEL_COL_OUTIMG}{___idx + 2}')
        if g_has_in_img:
            T_worksheet.add_image(in_image, f'{__EXCEL_COL_INIMG}{___idx + 2}')

    T_workbook.save(os.path.join(out_unique_tid_dir_full, fname_out_excel_img_file_with_ext))
    T_workbook.close()

if __name__ == '__main__':
    print(f'===> {__file__} <===')
    do_main(sys.argv)
    pass