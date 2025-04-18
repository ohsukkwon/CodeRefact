# -*- coding: utf-8 -*-

import csv
import json
import os
import sys
import traceback

from GlobalUtil import get_dir_res
from GlobalVars import *

__MY_TAG : str = os.path.basename(__file__).split('.', 1)[0]

# 중복된 열 이름을 변경하는 함수
def rename_duplicate_headers(headers):
    header_count = {}
    new_headers = []
    for header in headers:
        if header in header_count:
            header_count[header] += 1
            new_headers.append(f"{header}.{header_count[header]}")
        else:
            header_count[header] = 1
            new_headers.append(header)
    return new_headers

# 파일명 생성 함수
def generate_filename(id_, no, mode_):
    folder_name = os.path.join(get_dir_res(), "batchcfg", id_, str('{0:03d}'.format(int(no))))
    file_name = f"{mode_}.cfg"
    os.makedirs(folder_name, exist_ok=True)

    return os.path.join(folder_name, file_name)

# CSV 파일을 JSON으로 변환하는 함수
def csv_to_json(csv_filepath, unique_id, mode_):
    # 다양한 인코딩 시도
    #encodings = ['utf-8-sig', 'utf-8', 'cp949', 'euc-kr']
    encodings = ['utf-8-sig']

    for encoding in encodings:
        try:
            with open(csv_filepath, mode='r', encoding=encoding) as file:
                csv_reader = csv.reader(file, delimiter='|')
                headers = next(csv_reader)  # 헤더만 읽음
                headers = rename_duplicate_headers(headers)  # 중복된 헤더 이름 수정
                csv_dict_reader = csv.DictReader(file, delimiter='|', fieldnames=headers)  # DictReader에 수정된 헤더 적용
                # 각 행을 처리하여 JSON 형식으로 변환
                for row in csv_dict_reader:
                    if mode_ == CONFIG_NAME_VALUE_LISTEN:
                        json_data = {
                            "mode": mode_,
                            "subject": row["Subject"],
                            "extraprompt": row["ExtraPrompt"],
                            "cfgmotherlanguage": row["CfgMotherLanguage"],
                            "wordscountof1line": "40",
                            "totalcountofsentences": row["TotalCountOfSentences"],
                            "personas": [
                                {
                                    "aivoiceengine": row["AiVoiceEngine"],
                                    "aivoiceid": row["AiVoiceId"],
                                    "name": row["Name"],
                                    "gender": row["Gender"],
                                    "age": row["Age"],
                                    "occupation": row["Occupation"],
                                    "countryoforigin": row["CountryOfOrigin"],
                                    "mylanguage": row["MyLanguage"],
                                    "hobby": row["Hobby"],
                                    "personality": row["Personality"],
                                    "annualsalary": row["Annualsalary"],
                                    "speakingspeed": row["Speakingspeed"],
                                    "speakingpitch": row["Speakingpitch"],
                                    "extraprompt": row["ExtraPrompt.2"]
                                }
                            ]
                        }
                    else:
                        json_data = {
                            "mode": mode_,
                            "subject": row["Subject"],
                            "extraprompt": row["ExtraPrompt"],
                            "cfgmotherlanguage": row["CfgMotherLanguage"],
                            "wordscountof1line": "40",
                            "totalcountofsentences": row["TotalCountOfSentences"],
                            "personas": [
                                {
                                    "aivoiceengine": row["AiVoiceEngine"],
                                    "aivoiceid": row["AiVoiceId"],
                                    "name": row["Name"],
                                    "gender": row["Gender"],
                                    "age": row["Age"],
                                    "occupation": row["Occupation"],
                                    "countryoforigin": row["CountryOfOrigin"],
                                    "mylanguage": row["MyLanguage"],
                                    "hobby": row["Hobby"],
                                    "personality": row["Personality"],
                                    "annualsalary": row["Annualsalary"],
                                    "speakingspeed": row["Speakingspeed"],
                                    "speakingpitch": row["Speakingpitch"],
                                    "extraprompt": row["ExtraPrompt.2"]
                                },
                                {
                                    "aivoiceengine": row["AiVoiceEngine.2"],
                                    "aivoiceid": row["AiVoiceId.2"],
                                    "name": row["Name.2"],
                                    "gender": row["Gender.2"],
                                    "age": row["Age.2"],
                                    "occupation": row["Occupation.2"],
                                    "countryoforigin": row["CountryOfOrigin.2"],
                                    "mylanguage": row["MyLanguage.2"],
                                    "hobby": row["Hobby.2"],
                                    "personality": row["Personality.2"],
                                    "annualsalary": row["Annualsalary.2"],
                                    "speakingspeed": row["Speakingspeed.2"],
                                    "speakingpitch": row["Speakingpitch.2"],
                                    "extraprompt": row["ExtraPrompt.3"]
                                }
                            ]
                        }

                    # 파일명 생성 및 저장
                    filename = generate_filename(unique_id, row["No(FileName)"], mode_)
                    with open(filename, 'w', encoding='utf-8-sig') as json_file:
                        json.dump(json_data, json_file, ensure_ascii=False, indent=4)
            break  # 인코딩 성공 시 루프 종료
        except UnicodeDecodeError:
            print(f'{__MY_TAG} : FAIL({encoding}/UnicodeDecodeError) {traceback.format_exc()}')
            continue  # 다음 인코딩 시도

if __name__ == '__main__':
    print(f'# # # # # {__MY_TAG} : {sys.argv}')

    # CSV 파일 경로

    my_target_dir = get_dir_res()

    tmp_my_batch_csv = None
    cfg_unique_id = None
    cfg_mode = None
    if len(sys.argv) < 3:
        # my_batch_csv = f'cfg_batch_conversation.{FILE_EXTENSION_WITHOUT_DOT_CSV}'
        # tmp_my_batch_csv = os.path.join(my_target_dir, "batchcsv", my_batch_csv)
        print(f'{__MY_TAG} : FAIL(cannot find arguments)')
        print('cannot find arguments')
        sys.exit(0)
    else:
        tmp_my_batch_csv = sys.argv[ARG_KEY_CSV_PATH]
        cfg_unique_id = sys.argv[ARG_KEY_CFG_UNIQUE_ID]
        cfg_mode = sys.argv[ARG_KEY_CFG_MODE]

    print(f'{__MY_TAG} : my_batch_csv : {tmp_my_batch_csv}')
    print(f'{__MY_TAG} : cfg_unique_id : {cfg_unique_id}')
    print(f'{__MY_TAG} : cfg_mode : {cfg_mode}')

    csv_to_json(tmp_my_batch_csv, cfg_unique_id, cfg_mode)