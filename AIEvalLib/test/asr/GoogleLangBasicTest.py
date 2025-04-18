# -*- coding: utf-8 -*-
from google.cloud import translate_v3 as translate

PROJECT_ID = 'osk1004-helloworld1st'

# Initialize Translation client
def get_supported_languages():
    client = translate.TranslationServiceClient()

    parent = f"projects/{PROJECT_ID}"

    # Supported language codes: https://cloud.google.com/translate/docs/languages
    response = client.get_supported_languages(parent=parent)

    # List language codes of supported languages.
    print("Supported Languages:")
    for language in response.languages:
        print(f"Language Code: {language.language_code}")

    return response

def list_languages():
    """Lists all available languages."""
    from google.cloud import translate_v2 as mytranslate

    translate_client = mytranslate.Client()
    results = translate_client.get_languages()
    return results

if __name__ == '__main__':
    supported_languages = list_languages()
    for __idx_, __item_ in enumerate(supported_languages):
        print(f"{__idx_}:{__item_['language']} ({__item_['name']})")

    # supported_languages = get_supported_languages()
    # print(supported_languages)
    # # List language codes of supported languages.
    # print("Supported Languages:")
    # print()
    # for language in supported_languages.languages:
    #     print(f"Language Code: {language.language_code}")