# -*- coding: utf-8 -*-
import csv
import datetime
import os
import shutil
import sys
import time

import pandas as pd
from tabulate import tabulate

from GlobalVars import *
from env.env_vars import get_my_proj_home
from utils.GlobalUtil import get_date_file_name

__TAG_KEY_NO : str = 'No'
__EXCEL_COL_NO : str = 'A'

__TAG_KEY_PROMPT : str = 'Prompt'
__EXCEL_COL_PROMPT : str = 'B'

__TAG_KEY_STYLE : str = 'Style'
__EXCEL_COL_STYLE : str = 'C'

__TAG_KEY_IN_IMG : str = 'InImage'
__EXCEL_COL_INIMG : str = 'D'

__MAX_IMG_SIZE_IN_KB : int = 1024
__DETAIL_MODE_IMG_THRESHOLD : int = 512

__IMG_CATEGORY_3DEMOJI : str = "3Demoji"
__IMG_CATEGORY_DOODLE : str = "Doodle"
__IMG_CATEGORY_ILLUSTRATION : str = "Illustration"
__IMG_CATEGORY_RETOROLOGO : str = "Retrologo"


g_my_input_datas_arr : list = []

def do_main(arg_sys = None, __DIR_NAME_RESULT=None):
    global g_my_input_datas_arr

    gen_evalimg_csv_start_time = time.time()

    result_total_eval_arr = []

    EXT_CSV = '.csv'
    EXT_TXT = '.txt'
    EXT_JPG = '.jpg'
    fname_real_body = 'datas_noimg'

    fname_cur_time = get_date_file_name()

    fname_in_txt_file = f'script_ko'                                 # File input txt
    fname_in_txt_file_with_ext = f'{fname_in_txt_file}{EXT_TXT}'
    print(f'fname_in_txt_file_with_ext : {fname_in_txt_file_with_ext}')

    fname_out_csv_file = f'out_{fname_real_body}'                               # File output csv
    fname_out_csv_file_with_ext = f'{fname_out_csv_file}_{fname_cur_time}{EXT_CSV}'

    in_image_dir = os.path.join(DIR_NAME_RES, DIR_NAME_RES_InImage)             # Dir all imgs

    out_unique_tid_dir_full = os.path.join(get_my_proj_home(), DIR_NAME_RESULT, fname_cur_time)     # Dir UniqueTid
    if not os.path.exists(out_unique_tid_dir_full):
        os.makedirs(out_unique_tid_dir_full)

    # file open
    input_csv_file = open(os.path.join(get_my_proj_home(), DIR_NAME_SAMPLE_DATAS, fname_in_txt_file_with_ext), "r", encoding='utf-8-sig')
    readlines = csv.reader(input_csv_file)

    for ___idx, arr_splitted_str_by_row in enumerate(readlines):
        g_my_input_datas_arr.append(arr_splitted_str_by_row[0])

    count_my_all_input_datas = len(g_my_input_datas_arr)
    print(f'===> count_my_all_input_datas : {count_my_all_input_datas}')



    img_category_arr = [__IMG_CATEGORY_3DEMOJI, __IMG_CATEGORY_DOODLE, __IMG_CATEGORY_ILLUSTRATION, __IMG_CATEGORY_RETOROLOGO]
    df_total_arr = []
    path_img_dir = os.path.join(get_my_proj_home(), DIR_NAME_SAMPLE_DATAS,DIR_NAME_SAMPLE_DATAS_IMG)
    ___all_idx = 0
    ___start_idx = 550
    path_sample_img_path = os.path.join(get_my_proj_home(), DIR_NAME_SAMPLE_DATAS, DIR_NAME_SAMPLE_DATAS_IMG, "sample.jpg")
    ___new_item = None
    for ___idx, ___item in enumerate(g_my_input_datas_arr):
        if ___idx < ___start_idx:
            continue

        for ___inner_img_category_idx,__img_category in enumerate(img_category_arr):
            img_file_full_path = os.path.join(path_img_dir, f'{___idx+1}_{img_category_arr[___inner_img_category_idx]}{EXT_JPG}')
            img_file_name = os.path.basename(img_file_full_path)
            img_file_dir = os.path.dirname(img_file_full_path)
            if os.path.exists(img_file_full_path):

                pass
            else:
                shutil.copyfile(path_sample_img_path, img_file_full_path)

                print(f'OMG! No img file : {img_file_name}')

            ___new_item = [
                f'{___all_idx+1}',                  # No
                g_my_input_datas_arr[___idx],       # Prompt
                f"{__img_category}",                                 # Style
                f"{img_file_name}",  # img file
            ]
            df_total_arr.append(___new_item)
            ___all_idx += 1

        print(f'===> df_total_arr[{___idx}] : {___new_item}')

    print(f'===> result_total_eval_arr : {result_total_eval_arr}')

    # 0:A:No , 1:B: Prompt, 2:C:Style, 3:D:InImage
    df_total_results = pd.DataFrame.from_records(df_total_arr, columns=[__TAG_KEY_NO,__TAG_KEY_PROMPT,__TAG_KEY_STYLE,__TAG_KEY_IN_IMG])

    df_total_results.to_csv(os.path.join(out_unique_tid_dir_full,fname_out_csv_file_with_ext), sep='|', na_rep='EMPTY', encoding='utf-8-sig', index=False, header=False)

    print(tabulate(df_total_results, headers='keys', tablefmt='psql', showindex="never"))

    gen_evalimg_csv_end_time = time.time()
    gen_evalimg_csv_elasped_time = gen_evalimg_csv_end_time - gen_evalimg_csv_start_time
    now = datetime.datetime.now()
    formatted_date = now.strftime("%Y-%m-%d_%H:%M:%S")

    print(f'fname_out_csv_file_with_ext : {out_unique_tid_dir_full}/{fname_out_csv_file_with_ext}')
    print(f'<<<<<<<<<<<< E N D(Gen EvalIMG CSV) : [{gen_evalimg_csv_elasped_time:0.9f} second(s)] , NOW : [{formatted_date}]')
    print()

if __name__ == '__main__':
    print(f'===> {__file__} <===')
    do_main(sys.argv)
    pass