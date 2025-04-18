import base64
# -*- coding: utf-8 -*-
import datetime
import http
import io
import logging
import ssl
import time

import boto3
import google.cloud.texttospeech as tts
import httplib2
import httpx
from PIL import Image, ImageFile
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from botocore.config import Config
from elevenlabs import ElevenLabs
from google.cloud import translate_v2 as translate
from openai import OpenAI, AzureOpenAI
from openpyxl import load_workbook  # Ensure openpyxl is installed via pip: `pip install openpyxl`
from openpyxl.drawing.image import Image as ExcelImage
from openpyxl.styles import Alignment

from MyKeyStore import *
from config.engine_config import *
from env.env_vars import *

CONNECT_TIME_OUT : int = 30
HTTP_PROXY_IP_ADDRESS : str = 'http://10.244.254.254:8080'
HTTPS_PROXY_IP_ADDRESS : str = 'http://10.244.254.254:8080'

ImageFile.LOAD_TRUNCATED_IMAGES = True
# ==================== FOR monitoring(SMS,...) ====================


# ==================== FOR adb shell command ====================


# ==================== FOR script libs ====================
def get_date_file_name():
    now = datetime.datetime.now()
    fname_date = now.strftime('%y%m%d_%H%M%S')
    return fname_date

def get_timedate_now():
    now = datetime.datetime.now()
    fname_date = now.strftime('%Y-%m-%d %H:%M:%S')
    return fname_date

def printMyLog(msg, isDev=False):
    if not isDev:
        return
    now = datetime.datetime.now()
    now = now.strftime('%Y-%m-%d %X(%f)')
    print(f'{now} : {msg}')

def mySleep(seconds):
    idx = 0
    while idx < seconds:
        print('.', end='')
        time.sleep(1)
        idx = idx + 1
        if idx != 0 and (idx % 10 == 0):
            print(idx)
    print()

def is_skip_gen_gpt_scen(argArgs):
    return len(argArgs.getValInGlobalArg(ARG_KEY_NAME_SKIPGENSCENINFILE, argDefValIfNone="")) > 0

def is_azure_support_langcode(argLangCode):
    if argLangCode is None:
        return False

    ret_is_supported_langcode = False
    try:
        ret_is_supported_langcode = True if azure_language_detection_support_dict_langcode_langname[argLangCode] else False
    except KeyError as keyErr:
        ret_is_supported_langcode = False

    return ret_is_supported_langcode

def is_azure_support_langname(argLangName):
    if argLangName is None:
        return False

    ret_is_supported_langname = False
    try:
        ret_is_supported_langname = True if azure_language_detection_support_dict_langname_langcode[argLangName] else False
    except KeyError as keyErr:
        ret_is_supported_langname = False

    return ret_is_supported_langname

# Example method for detecting the language of text
def langname_from_locale(locale, argLog=None):
    DUMMY_LANGNAME = "EMPTY"
    if locale:
        lang_code = locale.split(r'-')[0].lower()
        if lang_code == 'zh':
            country = locale.split(r'-')[1].lower()
            if country == 'hk' or country == 'tw':
                lang_code = 'zh_cht'
            elif country == 'cn':
                lang_code = 'zh_chs'
        if is_azure_support_langcode(lang_code):
            lang_name = azure_language_detection_support_dict_langcode_langname[lang_code]

            dbg_msg = f'# locale[{locale}] => lang_code[{lang_code}] => lang_name[{lang_name}]'
            if argLog:
                argLog.e(dbg_msg, argGoExit=True)
            else:
                print(dbg_msg)

            return lang_name
        else:
            dbg_msg = f'# OMG!! error. NOT supported {locale}'
            if argLog:
                argLog.e(dbg_msg, argGoExit=True)
            else:
                print(dbg_msg)

            return DUMMY_LANGNAME
    else:
        dbg_msg = f'# OMG!! error. locale is None.'
        if argLog:
            argLog.e(dbg_msg, argGoExit=True)
        else:
            print(dbg_msg)

        return DUMMY_LANGNAME

def langcode_from_langname(langname, argLog=None):
    DUMMY_LANGCODE = "EMP"
    if langname:
        if is_azure_support_langname(langname):
            lang_code = azure_language_detection_support_dict_langname_langcode[langname]

            dbg_msg = f'# langname[{langname}] => lang_code[{lang_code}]'
            if argLog:
                argLog.e(dbg_msg, argGoExit=True)
            else:
                print(dbg_msg)

            return lang_code
        else:
            dbg_msg = f'# OMG!! error. NOT supported {langname}'
            if argLog:
                argLog.e(dbg_msg, argGoExit=True)
            else:
                print(dbg_msg)

            return DUMMY_LANGCODE
    else:
        dbg_msg = f'# OMG!! error. langname is None.'
        if argLog:
            argLog.e(dbg_msg, argGoExit=True)
        else:
            print(dbg_msg)

        return DUMMY_LANGCODE

# ==================== FOR AI Client ====================

def get_client_ai_gpt_gpt():
    return OpenAI(api_key=keystore_get_key_type(argType=KEYTYPE_IDX_GPTScenario_OpenAI_NONE_NONE),
                  default_headers={"OpenAI-Beta": "assistants=v2"},
                  http_client=None if (current_GPT_PROGRAM_PROXY_MODE==GPT_PROGRAM_PROXY_MODE_HOME) else (
                      httpx.Client(verify=False, proxy=HTTP_PROXY_IP_ADDRESS)),
                  timeout=CONNECT_TIME_OUT
                  )

def get_client_ai_gpt_msa(argEngineName=GPT_ENGINE_NAME_GPT4o, argDeployModel=None):

    if argEngineName == GPT_ENGINE_NAME_GPT4o_mini:
        ___g_inner_api_key = keystore_get_key_type(argType=KEYTYPE_IDX_GPTScenario_Azure_OpenAI_GPT4o_mini)
        ___g_inner_ep = keystore_get_ep_type(argType=EPTYPE_IDX_GPTScenario_Azure_OpenAI_GPT4o_mini)
        ___g_inner_api_version = keystore_get_apiversion_type(argType=APIVERSIONTYPE_IDX_GPTScenario_Azure_OpenAI_GPT4o_mini)
    else:
        ___g_inner_api_key = keystore_get_key_type(argType=KEYTYPE_IDX_GPTScenario_Azure_OpenAI_GPT4o)
        ___g_inner_ep = keystore_get_ep_type(argType=EPTYPE_IDX_GPTScenario_Azure_OpenAI_GPT4o)
        ___g_inner_api_version = keystore_get_apiversion_type(argType=APIVERSIONTYPE_IDX_GPTScenario_Azure_OpenAI_GPT4o)

    return AzureOpenAI(
        api_version=___g_inner_api_version,
        api_key=___g_inner_api_key,
        azure_endpoint=___g_inner_ep,
        http_client=None if (current_GPT_PROGRAM_PROXY_MODE==GPT_PROGRAM_PROXY_MODE_HOME) else (
            httpx.Client(verify=False,proxy=HTTP_PROXY_IP_ADDRESS)),
        timeout=CONNECT_TIME_OUT,
        azure_deployment = argDeployModel
    )

def get_client_ai_voice_msa():
    ___g_inner_api_key = keystore_get_key_type(argType=KEYTYPE_IDX_GPTScenario_Azure_OpenAI_tts_hd)
    ___g_inner_ep = keystore_get_ep_type(argType=EPTYPE_IDX_GPTScenario_Azure_OpenAI_tts_hd)
    ___g_inner_api_version = keystore_get_apiversion_type(argType=APIVERSIONTYPE_IDX_GPTScenario_Azure_OpenAI_tts_hd)
    ___g_inner_deploy_model = keystore_get_deployment_type(argType=DEPLOYMENTTYPE_IDX_GPTScenario_Azure_OpenAI_tts_hd)

    return AzureOpenAI(
        api_version=___g_inner_api_version,
        api_key=___g_inner_api_key,
        azure_endpoint=___g_inner_ep,
        http_client=None if (current_GPT_PROGRAM_PROXY_MODE==GPT_PROGRAM_PROXY_MODE_HOME) else (
            httpx.Client(verify=False,proxy=HTTP_PROXY_IP_ADDRESS)),
        timeout=CONNECT_TIME_OUT,
        azure_deployment = ___g_inner_deploy_model
    )

def get_client_ai_voice_aws():
    my_config = Config(
        connect_timeout=30,
        proxies={
            'http': HTTP_PROXY_IP_ADDRESS,
            'https': HTTPS_PROXY_IP_ADDRESS
        }
    )

    return boto3.Session(
        aws_access_key_id=keystore_get_key_type(argType=KEYTYPE_IDX_AIvoice_AWS_NONE_NONE),
        aws_secret_access_key=keystore_get_secret_type(argType=SECRETTYPE_IDX_AIvoice_AWS_NONE_NONE),
        region_name=AI_VOICE_AWS_REGION_NAME
    ).client(service_name=AI_VOICE_AWS_SVC_NAME,
             verify=False,
             config= \
        None if (current_GPT_PROGRAM_PROXY_MODE==GPT_PROGRAM_PROXY_MODE_HOME) else ( my_config ))

def get_client_ai_language_detection_msa():
    # Create a logger for the 'azure' SDK
    logger = logging.getLogger('azure')
    logger.setLevel(logging.DEBUG)

    # Configure a console output
    handler = logging.StreamHandler(stream=sys.stdout)
    logger.addHandler(handler)

    if current_GPT_PROGRAM_PROXY_MODE == GPT_PROGRAM_PROXY_MODE_HOME:
        pass
    else:
        os.environ["HTTP_PROXY"] = HTTP_PROXY_IP_ADDRESS
        os.environ["HTTPS_PROXY"] = HTTP_PROXY_IP_ADDRESS
        os.environ["REQUESTS_CA_BUNDLE"] = r"D:\cer_gumi.pem"

    ta_credential = AzureKeyCredential(keystore_get_key_type(argType=KEYTYPE_IDX_GPTScenario_Azure_AIservicesLanguage_NONE))
    text_analytics_client = TextAnalyticsClient(
        endpoint=keystore_get_ep_type(argType=EPTYPE_IDX_GPTScenario_Azure_AIservicesLanguage_NONE),
        credential=ta_credential,
        logging_enable = True
    )
    return text_analytics_client

def get_client_ai_voice_elv():
    ___api_key = keystore_get_key_type(argType=KEYTYPE_IDX_AIvoice_Elevenlabs_NONE_NONE)

    return ElevenLabs(
        api_key=___api_key,
        timeout=CONNECT_TIME_OUT,
        httpx_client=None if (current_GPT_PROGRAM_PROXY_MODE==GPT_PROGRAM_PROXY_MODE_HOME) else (
            httpx.Client(verify=False,proxy=HTTP_PROXY_IP_ADDRESS)))

def get_client_ai_voice_ggc():
    if current_GPT_PROGRAM_PROXY_MODE == GPT_PROGRAM_PROXY_MODE_HOME :
        return tts.TextToSpeechClient()

    http = httplib2.Http(disable_ssl_certificate_validation=True)

    proxy_cert = "D:\cer_gumi.crt"  # Do do : it should be change to Common variable like Environment(

    # 프록시 설정
    os.environ["HTTP_PROXY"] = HTTP_PROXY_IP_ADDRESS
    os.environ['GRPC_DEFAULT_SSL_ROOTS_FILE_PATH'] = 'D:\cer_gumi.crt'
    os.environ['CURL_CA_BUNDLE'] = 'D:\cer_gumi.crt'

    ssl.create_default_context(cafile=proxy_cert)

    client = tts.TextToSpeechClient()
    return client

def get_client_ai_language_detection_ggc():
    # # # # # In case of GGC's language detection. it doesn't need proxy.

    if current_GPT_PROGRAM_PROXY_MODE == GPT_PROGRAM_PROXY_MODE_HOME:
        return translate.Client()

    os.environ["HTTP_PROXY"] = HTTP_PROXY_IP_ADDRESS
    os.environ["HTTPS_PROXY"] = HTTP_PROXY_IP_ADDRESS
    # os.environ["SSL_CERT_FILE"] = r"D:\cer_gumi.pem"
    os.environ["REQUESTS_CA_BUNDLE"] = r"D:\cer_gumi.pem"

    return translate.Client()

def get_http_language_detection_msa(arg_documents):
    if current_GPT_PROGRAM_PROXY_MODE == GPT_PROGRAM_PROXY_MODE_HOME:
        pass
    else:
        os.environ["HTTP_PROXY"] = HTTP_PROXY_IP_ADDRESS
        os.environ["HTTPS_PROXY"] = HTTP_PROXY_IP_ADDRESS

    # HTTP 요청 헤더
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': keystore_get_key_type(argType=KEYTYPE_IDX_GPTScenario_Azure_AIservicesLanguage_NONE)
    }

    ai_endpoint = keystore_get_ep_type(argType=EPTYPE_IDX_GPTScenario_Azure_AIservicesLanguage_NONE)

    # Make an HTTP request to the REST interface
    uri = ai_endpoint.rstrip('/').replace('https://', '')
    conn = http.client.HTTPSConnection(uri)

    conn.request("POST", "/text/analytics/v3.1/languages?", str(arg_documents).encode('utf-8'), headers)

    response = conn.getresponse()

    # 결과 출력
    if response.status == 200:
        print(f"Ok.")
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

    return response

def is_skip_unique_testid(argArgs):
    return len(argArgs.getValInGlobalArg(ARG_KEY_NAME_SKIPUNIQUETID, argDefValIfNone="")) > 0

def get_response_count(locale):
    if locale:
        if locale == 'th-TH' or locale == 'ar-AE':
            return ASR_RESPONSE_COUNT_PER_RESPONSE_FIXED_LOW
    return ASR_RESPONSE_COUNT_PER_RESPONSE

def do_get_all_assisant_list(argLog, arg_client, do_delete = False):
    client = arg_client

    my_assistants = client.beta.assistants.list(
        order="desc",
        limit=20,
    )

    dbg_msg = f'-------- (OpenAI)BEFORE START:do_delete({do_delete}) ---------'
    if argLog:
        argLog.e(dbg_msg)
    else:
        print(dbg_msg)
    if len(my_assistants.data) > 0:
        if argLog:
            argLog.e(my_assistants.data)
        else:
            print(my_assistants.data)

        if my_assistants.data is not None:
            want_delete_count = 20   # 10
            want_delete_lists = {}

            dbg_msg = f'_____ Total count :{len(my_assistants.data)}'
            if argLog:
                argLog.e(dbg_msg)
            else:
                print(dbg_msg)
            pass

            for _idx, ___item in enumerate(my_assistants.data):
                dbg_msg = f'my_assistants.data[{_idx}]:{___item}'
                if argLog:
                    argLog.e(dbg_msg)
                else:
                    print(dbg_msg)
                pass

                if ___item.name != None and ___item.name != '' and ___item.name.startswith('##'):
                    continue

                if do_delete:   # if you want to delete it, make do_delete to TRUE
                    if _idx < want_delete_count:
                        want_delete_lists[_idx] = ___item

            _idx = 0
            for _idx in want_delete_lists:
                ___item = want_delete_lists[_idx]

                dbg_msg = f'want_delete_lists[{_idx}]:{___item.name}:{___item}'
                if argLog:
                    argLog.e(dbg_msg)
                else:
                    print(dbg_msg)

                response = client.beta.assistants.delete(___item.id)
                print(f'# # # # # assistants(DELETE):{response}')
                pass
    else:
        dbg_msg = 'None/Good!'
        if argLog:
            argLog.e(dbg_msg)
        else:
            print(dbg_msg)

    dbg_msg = '======== (OpenAI)BEFORE END ========='
    if argLog:
        argLog.e(dbg_msg)
    else:
        print(dbg_msg)


    # # # After deleting, check again.
    my_assistants = client.beta.assistants.list(
        order="desc",
        limit=20,
    )

    dbg_msg = f'-------- (OpenAI)AFTER START ---------'
    if argLog:
        argLog.e(dbg_msg)
    else:
        print(dbg_msg)

    if len(my_assistants.data) > 0:
        if argLog:
            argLog.e(my_assistants.data)
        else:
            print(my_assistants.data)
    else:
        dbg_msg = 'None/Good!'
        if argLog:
            argLog.e(dbg_msg)
        else:
            print(dbg_msg)

    dbg_msg = '======== (OpenAI)AFTER END ========='
    if argLog:
        argLog.e(dbg_msg)
    else:
        print(dbg_msg)

def get_col_width_row_height(img_width, img_height):
    col_width = img_width*63.2/504.19
    row_height = img_height*225.35/298.96
    return col_width, row_height

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def __resize_image(image, max_dimension):
    width, height = image.size

    # Check if the image has a palette and convert it to true color mode
    if image.mode == "P":
        if "transparency" in image.info:
            image = image.convert("RGBA")
        else:
            image = image.convert("RGB")

    if width > max_dimension or height > max_dimension:
        if width > height:
            new_width = max_dimension
            new_height = int(height * (max_dimension / width))
        else:
            new_height = max_dimension
            new_width = int(width * (max_dimension / height))
        image = image.resize((new_width, new_height), Image.LANCZOS)

    return image

def __convert_to_png(image):
    with io.BytesIO() as output:
        image.save(output, format="PNG")
        return output.getvalue()

def process_image(path, max_size):
    with Image.open(path) as image:
        width, height = image.size
        mimetype = image.get_format_mimetype()
        if mimetype == "image/png" and width <= max_size and height <= max_size:
            with open(path, "rb") as f:
                encoded_image = base64.b64encode(f.read()).decode('utf-8')
                return encoded_image, max(width, height), (width, height)  # returns a tuple consistently
        else:
            resized_image = __resize_image(image, max_size)
            png_image = __convert_to_png(resized_image)
            return base64.b64encode(png_image).decode('utf-8'),max(resized_image.width, resized_image.height), (resized_image.width, resized_image.height)  # same tuple metadata

def create_image_content(image, maxdim, detail_threshold):
    # detail = "low" if maxdim < detail_threshold else "high"
    detail = "high"

    return {
        "type": "image_url",
        "image_url": {"url": f"data:image/jpeg;base64,{image}", "detail": detail}
    }

def get_dir_home(argExtPath=None):
    DIR_PATH_TARGET = get_my_proj_home()
    DIR_PATH_TARGET = os.path.abspath(DIR_PATH_TARGET)
    if not DIR_PATH_TARGET:
        sys.exit("OMG!! NO GEN_ASR_AIvoice_HOME. check it.")

    if argExtPath is not None:
        DIR_PATH_TARGET = os.path.join(DIR_PATH_TARGET, argExtPath)
    return DIR_PATH_TARGET

def get_dir_res(argExtPath=None):
    DIR_PATH_TARGET = get_my_proj_res()
    DIR_PATH_TARGET = os.path.abspath(DIR_PATH_TARGET)
    if argExtPath is not None:
        DIR_PATH_TARGET = os.path.join(DIR_PATH_TARGET, argExtPath)
    return DIR_PATH_TARGET

def get_dir_result_without_overlay(argExtPath=None):
    DIR_PATH_TARGET = get_my_proj_result()
    DIR_PATH_TARGET = os.path.abspath(DIR_PATH_TARGET)

    if argExtPath is not None:
        DIR_PATH_TARGET = os.path.join(DIR_PATH_TARGET, argExtPath)
    return DIR_PATH_TARGET

def get_dir_result(argSysArgs, argLog=None, argExtPath=None):
    if argSysArgs is None:
        dbg_msg = f'### OMG(get_dir_result)!!! exception.'
        if argLog:
            argLog.e(dbg_msg, argGoExit=True)
        else:
            print(dbg_msg)
    else:
        if argSysArgs.getValInGlobalArg(ARG_KEY_NAME_OUTPUTDIR):
            DIR_PATH_TARGET = argSysArgs.getValInGlobalArg(ARG_KEY_NAME_OUTPUTDIR)
        else:
            DIR_PATH_TARGET = get_my_proj_result()

    DIR_PATH_TARGET = os.path.abspath(DIR_PATH_TARGET)

    if argExtPath is not None:
        DIR_PATH_TARGET = os.path.join(DIR_PATH_TARGET, argExtPath)
    return DIR_PATH_TARGET

def get_dir_result_output(argSysArgs, argLog, argExtPath=None):
    if argSysArgs is None:
        argLog.e(msg=f'### OMG(get_dir_result_output)!!! exception.', argGoExit=True)
    else:
        if argSysArgs.getValInGlobalArg(ARG_KEY_NAME_OUTPUTDIR):
            DIR_PATH_TARGET = argSysArgs.getValInGlobalArg(ARG_KEY_NAME_OUTPUTDIR)
        else:
            DIR_PATH_TARGET = get_my_proj_result()

    DIR_PATH_TARGET = os.path.join(DIR_PATH_TARGET ,'output')
    DIR_PATH_TARGET = os.path.abspath(DIR_PATH_TARGET)

    if argExtPath is not None:
        DIR_PATH_TARGET = os.path.join(DIR_PATH_TARGET, argExtPath)
    return DIR_PATH_TARGET

def attach_img_to_excel(argPath_excel_file, arg_result_total_eval_arr, argPath_outimg_dir, argPath_inimg_dir, arg_has_in_img):
    __TAG_KEY_NO: str = 'No'
    __EXCEL_COL_NO: str = 'A'

    __TAG_KEY_PROMPT: str = 'Prompt'
    __EXCEL_COL_PROMPT: str = 'B'

    __TAG_KEY_STYLE: str = 'Style'
    __EXCEL_COL_STYLE: str = 'C'

    __TAG_KEY_OUT_IMG: str = 'OutImage'
    __EXCEL_COL_OUTIMG: str = 'D'

    __TAG_KEY_IN_IMG: str = 'InImage'
    __EXCEL_COL_INIMG: str = 'E'

    __TAG_KEY_SCORE: str = 'Score'
    __EXCEL_COL_SCORE: str = 'F'

    __TAG_KEY_REASON: str = 'Reason'
    __EXCEL_COL_REASON: str = 'G'

    __TAG_KEY_CAPTION: str = 'Caption'
    __EXCEL_COL_CAPTION: str = 'H'

    T_workbook = load_workbook(argPath_excel_file, data_only=True)
    T_worksheet = T_workbook.active

    for ___idx, ___item in enumerate(arg_result_total_eval_arr):
        ## 이미지 불러오기
        if ___item.getOutImg() == 'FAKE':
            continue

        out_image_full_path = os.path.join(argPath_outimg_dir, ___item.getOutImg())
        out_image = ExcelImage(out_image_full_path)
        in_image = None

        if arg_has_in_img:
            in_image_full_path = os.path.join(argPath_inimg_dir, ___item.getInImg())
            in_image = ExcelImage(in_image_full_path)

        out_image.width, out_image.height = 100, 100  # 크기 설정
        if arg_has_in_img:
            in_image.width, in_image.height = 100, 100  # 크기 설정

        ## 이미지 픽셀을 셀 폭과 높이로 변환
        if ___idx == 0:
            T_worksheet.column_dimensions[__EXCEL_COL_OUTIMG].width = out_image.width / 5  # set width to image's out_image
            T_worksheet.column_dimensions[__EXCEL_COL_INIMG].width = out_image.width / 5  # set width to image's out_image
            T_worksheet.column_dimensions[__EXCEL_COL_PROMPT].width = 50
            T_worksheet.column_dimensions[__EXCEL_COL_REASON].width = 50
            T_worksheet.column_dimensions[__EXCEL_COL_CAPTION].width = 50
            T_worksheet.sheet_view.zoomScale = 80

        T_worksheet[f'{__EXCEL_COL_REASON}{___idx + 2}'].alignment = Alignment(wrap_text=True)
        T_worksheet[f'{__EXCEL_COL_CAPTION}{___idx + 2}'].alignment = Alignment(wrap_text=True)

        T_worksheet.row_dimensions[___idx + 2].height = out_image.height

        T_worksheet.add_image(out_image, f'{__EXCEL_COL_OUTIMG}{___idx + 2}')
        if arg_has_in_img:
            T_worksheet.add_image(in_image, f'{__EXCEL_COL_INIMG}{___idx + 2}')

    excel_dirname, excel_basename = os.path.split(argPath_excel_file)
    excel_name, excel_ext = os.path.splitext(excel_basename)
    excel_name = f'{excel_name}_img'

    new_img_excel_file = os.path.join(excel_dirname, excel_name + excel_ext)

    T_workbook.save(new_img_excel_file)
    T_workbook.close()