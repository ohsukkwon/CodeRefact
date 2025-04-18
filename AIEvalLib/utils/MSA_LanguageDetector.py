# -*- coding: utf-8 -*-
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from azure.core.pipeline.transport._requests_basic import RequestsTransport

from GlobalUtil import is_azure_support_langcode, get_client_ai_language_detection_msa

text_tw = """
你好，今天我要談談 YouTube 對社會的影響。
YouTube 是一個讓人們可以創作和分享內容的平台。
MZ 世代透過 YouTube 引領新潮流。
這個平台已經成為教育和資訊傳播的新方法。
在這裡很容易找到在傳統媒體中難以獲得的多元資訊。
YouTube 也對商業模式的改變產生了重大影響。
品牌和個人利用 YouTube 與更多消費者溝通。
已經創造出一個讓公眾可以直接參與的空間。
這也有助於政治觀點的形成。
例如，各種活動透過 YouTube 廣泛傳播。
"""

text_hk = """
你好，今日我會講述 YouTube 對社會的影響。
YouTube 係一個平台，俾人可以創作同分享內容。
MZ 世代正通過 YouTube 帶領新嘅潮流。
呢個平台已經成為教育同資訊傳播嘅新方法。
喺傳統媒體難以獲得嘅多樣化資訊可以好容易咁喺 YouTube 搵到。
YouTube 亦都對商業模式嘅轉變產生咗重大影響。
品牌同個人用 YouTube 與更多嘅消費者溝通。
一個讓公眾可以直接參與嘅空間已經被創造出嚟。
呢個亦都有助於政治觀點嘅形成。
例如，各種活動通過 YouTube 廣泛傳播。
"""

text_cn = """
大家好，今天我将讨论YouTube对社会的影响。
YouTube是一个人们可以创作和分享内容的平台。
MZ一代通过YouTube引领了新的潮流。这个平台已经成为教育和信息传播的新方式。
在这里可以轻松找到传统媒体难以获取的多样化信息。
YouTube还极大地影响了商业模式的变革。
品牌和个人正在利用YouTube与更多消费者进行沟通。
这为公众直接参与创造了一个空间。
这也有助于政治意见的形成。
例如，各种活动通过YouTube广泛传播。
"""

text_ar = """
مرحباً، اليوم سأتحدث عن تأثير YouTube على المجتمع.
يُعد YouTube منصة يمكن للأفراد من خلالها إنشاء المحتوى ومشاركته.
يقود جيل MZ الاتجاهات الجديدة عبر YouTube.
لقد أصبحت هذه المنصة وسيلة جديدة للتعليم ونشر المعلومات.
من السهل العثور على معلومات متنوعة يصعب الحصول عليها من وسائل الإعلام التقليدية.
كما أن YouTube قد أثر بشكل كبير على تغيير نماذج الأعمال.
تستخدم العلامات التجارية والأفراد YouTube للتواصل مع المزيد من المستهلكين.
تم إنشاء مساحة يمكن للجمهور المشاركة فيها مباشرة.
هذا يسهم أيضاً في تكوين الآراء السياسية.
على سبيل المثال، انتشرت حملات مختلفة بشكل واسع عبر YouTube.
"""

text_de = """
Hallo, heute werde ich über den Einfluss von YouTube auf die Gesellschaft sprechen.
YouTube ist eine Plattform, auf der Einzelpersonen Inhalte erstellen und teilen können.
Die MZ-Generation führt durch YouTube neue Trends an.
Diese Plattform ist zu einer neuen Methode für Bildung und Informationsvermittlung geworden.
Es ist einfach, vielfältige Informationen zu finden, die in traditionellen Medien schwer zugänglich sind.
YouTube hat auch einen großen Einfluss auf die Veränderung von Geschäftsmodellen gehabt.
Marken und Einzelpersonen nutzen YouTube, um mit mehr Verbrauchern zu kommunizieren.
Ein Raum, in dem die Öffentlichkeit direkt teilnehmen kann, wurde geschaffen.
Dies trägt auch zur Meinungsbildung in der Politik bei.
Zum Beispiel haben sich viele Kampagnen über YouTube weit verbreitet.
"""

########################### Example method for detecting the language of text
def language_detector(text):
    client = get_client_ai_language_detection_msa()
    try:
        response_arr_total = client.detect_language(documents=[text], country_hint='us')
        print(f"{len(response_arr_total)} , response_arr_total: {response_arr_total}")
        print()

        for _inner_idx, one_item in enumerate(response_arr_total):
            response = one_item
            print(f"response: {response}")
            print(f"Language: {response.primary_language.name}")
            print(f"iso6391_name: {response.primary_language.iso6391_name}")
            print(f"warnings: {response.warnings}")
            print(f"is_error: {response.is_error}")

    except Exception as err:
        print("Encountered exception3. {}".format(err))

def language_detector2(text):
    client = get_client_ai_language_detection_msa()
    try:
        response = client.detect_language(documents=[text], country_hint='us')[0]

        if is_azure_support_langcode(response.primary_language.iso6391_name):

            print("yes")
        else:
            print("OMG! NOT supported!!")
    except Exception as err:
        print("Encountered exception4. {}".format(err))
