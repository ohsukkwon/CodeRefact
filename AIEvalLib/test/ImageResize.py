# -*- coding: utf-8 -*-

## supporting functions
import base64
import io
import os
import time

from PIL import Image  # Pillow image library
from openai import OpenAI


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

def __process_image(path, arg_max_size):
    with Image.open(path) as image:
        width, height = image.size
        mimetype = image.get_format_mimetype()
        if mimetype == "image/png" and width <= arg_max_size and height <= arg_max_size:
            with open(path, "rb") as f:
                encoded_image = base64.b64encode(f.read()).decode('utf-8')
                return encoded_image, max(width, height)  # returns a tuple consistently
        else:
            resized_image = __resize_image(image, arg_max_size)
            png_image = __convert_to_png(resized_image)
            return base64.b64encode(png_image).decode('utf-8'),max(width, height)  # same tuple metadata

def __create_image_content(image, maxdim, detail_threshold):
    detail = "low" if maxdim < detail_threshold else "high"
    return {
        "type": "image_url",
        "image_url": {"url": f"data:image/jpeg;base64,{image}", "detail": detail}
    }


def __set_system_message(sysmsg):
    return [{
        "role": "system",
        "content": sysmsg
    }]


## user message with images function
def __set_user_message(user_msg_str,
                     file_path_list=[],      # A list of file paths to images.
                     max_size_px=1024,       # Shrink images for lower expense
                     file_names_list=None,   # You can set original upload names to show AI
                     tiled=False,            # True is the API Reference method
                     detail_threshold=700):  # any images below this get 512px "low" mode

    if not isinstance(file_path_list, list):  # create empty list for weird input
        file_path_list = []

    if not file_path_list:  # no files, no tiles
        tiled = False

    if file_names_list and len(file_names_list) == len(file_path_list):
        file_names = file_names_list
    else:
        file_names = [os.path.basename(path) for path in file_path_list]

    base64_images = [__process_image(path, max_size_px) for path in file_path_list]

    uploaded_images_text = ""
    if file_names:
        uploaded_images_text = "\n\n---\n\nUploaded images:\n" + '\n'.join(file_names)

    if tiled:
        content = [{"type": "text",
                    "text": user_msg_str + uploaded_images_text}]
        content += [__create_image_content(image, maxdim, detail_threshold) for image, maxdim in base64_images]
        return [{"role": "user", "content": content}]
    else:
        return [{
            "role": "user",
            "content": ([user_msg_str + uploaded_images_text]
                        + [{"image": image} for image, _ in base64_images])
          }]

if __name__ == '__main__':
    # -- START -- set up run variables
    system_msg = """당신은 VisionPal로, GPT-4o와 컴퓨터 비전 기능을 기반으로 한 AI 비서입니다.
AI 지식 기준: 2024년 11월
내장된 비전 기능:
이미지에서 텍스트 추출
이미지 설명
이미지 콘텐츠 분석
머신 비전이 필요한 논리적 문제 해결""".strip()

    # The user message
    user_msg = """몇 개의 이미지가 수신되었는지 설명하고, 해당 이미지의 품질을 설명하세요.
    
# 출력양식(예시)
아래와 같이 Header열이 포함된 MarkDown테이블로만 답변할것.
|No|파일명|caption상세설명|
|---|---|---|
|0|[첫번째 이미지 파일명]|[첫번째 이미지에 대한 cation 상세 설명]|
|1|[두번째 이미지 파일명]|[두번째 이미지에 대한 cation 상세 설명]|

""".strip()

    # user images file list, and max dimension limit
    max_size = 1024  # downsizes if any dimension above this
    image_paths = ["../res/o_6.jpg", "../res/o_7.jpg"]  # empty for no images
    # true_files = ["real_file_name_1.png", "real_file_name_2.jpg"]
    true_files = None  # you can give real names if using temp upload locations


    # Assemble the request parameters (all are dictionaries)
    system = __set_system_message(system_msg)
    chat_hist = []  # list of more user/assistant items
    user = __set_user_message(user_msg, image_paths, max_size, file_names_list=true_files)

    params = {  # dictionary format for ** unpacking
        "model": "gpt-4o",
        "temperature": 1.6,
        "top_p": 0.8,
        "stream": True,
        "user": "my_customer",
        "messages": system + chat_hist + user,
    }

    print(f'------------ params ----------------')
    print(params)
    print(f'------------------------------------')

    start = time.perf_counter()
    try:
        client = OpenAI()
        response = client.chat.completions.with_raw_response.create(**params)
        headers_dict = response.headers.items().mapping.copy()
        for key, value in headers_dict.items():  # set a variable for each header
            locals()[f'headers_{key.replace("-", "_")}'] = value
    except Exception as e:
        print(f"Error during API call: {e}")
        response = None

    if response is not None:
        reply = ""
        try:
            print(f"---\nSENT:\n{user[0]['content'][0]}\n---")
            for chunk_no, chunk in enumerate(response.parse()):
                if chunk.choices[0].delta.content:
                    reply += chunk.choices[0].delta.content
                    # print(chunk.choices[0].delta.content, end="")
        except Exception as e:
            print(f"Error during receive/parsing: {e}")

        print(f'reply: {reply}')

    print(f"\n[elapsed: {time.perf_counter()-start:.2f} seconds]")