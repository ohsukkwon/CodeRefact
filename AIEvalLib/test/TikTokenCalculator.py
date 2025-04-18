# -*- coding: utf-8 -*-

import tiktoken

___env_llm_model_name = "gpt-4o"
___env_target_text = \
'''|No|Score|Reason|Caption|\n|---|---|---|---|\n|1|30|만점|이 이미지는 팝아트 스타일로 딸기가 그려진 우유팩을 보여줍니다. 배경은 밝고 다채로운 색상으로 구성되어 있으며, 시각적으로 매우 강렬합니다. 딸기 그림이 우유팩에 생생하게 표현되어 있어 전체적으로 팝아트의 느낌을 잘 살리고 있습니다.|\n|2|15|빨간색 자동차가 여전히 남아 있어 프롬프트가 일부만 반영되었습니다.|이 이미지는 수채화 스타일로 표현된 자동차들을 보여줍니다. 현대적인 건물을 배경으로 두 대의 차가 주차되어 있습니다. 차 중 하나는 빨간색으로, 다른 하나는 은색으로 칠해져 있으며, 배경의 건물과 어우러져 세련된 느낌을 줍니다.|\n|3|30|만점|이 이미지는 원본의 과일 형태를 유지하면서 스케치 스타일로 표현된 과일 접시를 보여줍니다. 세밀한 연필 스케치로 그려진 이 과일들은 섬세한 질감과 명암을 통해 깊이감이 돋보입니다. 과일의 윤곽과 그림자 처리가 섬세하게 묘사되어 있어 사실적인 느낌을 줍니다.|'''

def get_tiktoken_count(arg_model_name='gpt-4o', arg_text=''):
    if arg_text is None or arg_text == '':
        return 0

    # 토크나이저 이름을 이용하는 방법
    # encoder = tiktoken.get_encoding("cl100k_base")

    # LLM 이름을 이용하는 방법
    encoder = tiktoken.encoding_for_model(arg_model_name)
    my_result = encoder.encode(arg_text)

    return my_result

if __name__ == "__main__":
    __result = get_tiktoken_count(___env_llm_model_name, ___env_target_text)
    print(f"■ String len:{len(___env_target_text)}")

    # print(f"__result:{__result}")
    print(f"■ Token count:{len(__result)}")

    #encoder = tiktoken.encoding_for_model(___env_llm_model_name)
    # print(f"__result_str:{''.join(encoder.decode(__result))}")
    #print(f"■ String len:{len(''.join(encoder.decode(__result)))}")