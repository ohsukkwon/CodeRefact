# -*- coding: utf-8 -*-
import os

from google.cloud import texttospeech

from GlobalVars import *
from GlobalUtil import get_date_file_name, get_client_ai_voice_ggc, get_dir_result_without_overlay

text_es = """
Hola, hoy voy a hablar sobre el impacto de YouTube en la sociedad.
YouTube es una plataforma donde las personas pueden crear y compartir contenido.
La generación MZ está liderando nuevas tendencias a través de YouTube.
Esta plataforma se ha convertido en un nuevo método para la educación y la difusión de información.
Es fácil encontrar información diversa que es difícil de obtener en los medios tradicionales.
YouTube también ha tenido un gran impacto en el cambio de los modelos de negocio.
Las marcas y las personas están utilizando YouTube para comunicarse con más consumidores.
Se ha creado un espacio donde el público puede participar directamente.
Esto también está contribuyendo a la formación de la opinión política.
Por ejemplo, muchas campañas se han difundido ampliamente a través de YouTube.
"""

text_pl = """
Dzień dobry, dzisiaj omówię wpływ YouTube na społeczeństwo.
YouTube to platforma, na której ludzie mogą tworzyć i udostępniać treści.
Pokolenie MZ wyznacza nowe trendy za pośrednictwem YouTube.
Ta platforma stała się nową metodą edukacji i rozpowszechniania informacji.
Łatwo znaleźć różnorodne informacje, które trudno zdobyć za pomocą tradycyjnych mediów.
YouTube miał również duży wpływ na zmianę modeli biznesowych.
Marki i osoby prywatne wykorzystują YouTube do komunikacji z większą liczbą konsumentów.
Stworzono przestrzeń, w której społeczeństwo może bezpośrednio uczestniczyć.
Przyczynia się to również do kształtowania opinii politycznych.
Na przykład, różne kampanie szeroko się rozprzestrzeniają za pośrednictwem YouTube.
"""

text_nl = """
Hallo, vandaag ga ik het hebben over de impact van YouTube op de samenleving.
YouTube is een platform waar individuen inhoud kunnen creëren en delen.
De MZ-generatie leidt nieuwe trends via YouTube.
Dit platform is een nieuwe methode geworden voor educatie en verspreiding van informatie.
Het is gemakkelijk om diverse informatie te vinden die moeilijk te verkrijgen is via traditionele media.
YouTube heeft ook een grote invloed gehad op de verandering van bedrijfsmodellen.
Merken en individuen gebruiken YouTube om met meer consumenten te communiceren.
Er is een ruimte gecreëerd waar het publiek direct kan deelnemen.
Dit draagt ook bij aan de vorming van politieke meningen.
Zo zijn verschillende campagnes zich wijdverbreid gaan verspreiden via YouTube.
"""

text_sw = """
Hej, idag kommer jag att prata om YouTubes påverkan på samhället.
YouTube är en plattform där individer kan skapa och dela innehåll.
Generation MZ leder nya trender genom YouTube.
Denna plattform har blivit en ny metod för utbildning och informationsspridning.
Det är lätt att hitta mångsidig information som är svår att få från traditionella medier.
YouTube har också starkt påverkat förändringen av affärsmodeller.
Varumärken och individer använder YouTube för att kommunicera med fler konsumenter.
En plats där allmänheten kan delta direkt har skapats.
Detta bidrar också till bildandet av politiska åsikter.
Till exempel har olika kampanjer spridits brett via YouTube.
"""

text_ro = """
Bună ziua, astăzi voi vorbi despre impactul YouTube asupra societății.
YouTube este o platformă unde indivizii pot crea și distribui conținut.
Generația MZ conduce noi tendințe prin intermediul YouTube.
Această platformă a devenit o nouă metodă de educație și diseminare a informațiilor.
Este ușor să găsești informații diverse, care sunt dificil de obținut din media tradiționale.
YouTube a influențat semnificativ schimbarea modelelor de afaceri.
Mărcile și indivizii folosesc YouTube pentru a comunica cu mai mulți consumatori.
A fost creat un spațiu în care publicul poate participa direct.
Aceasta contribuie, de asemenea, la formarea opiniilor politice.
De exemplu, diferite campanii s-au răspândit pe scară largă prin intermediul YouTube.
"""

text_vi = """
Xin chào, hôm nay tôi sẽ nói về tác động của YouTube đối với xã hội.
YouTube là một nền tảng nơi các cá nhân có thể tạo và chia sẻ nội dung.
Thế hệ MZ đang dẫn đầu các xu hướng mới thông qua YouTube.
Nền tảng này đã trở thành một phương thức mới cho giáo dục và truyền tải thông tin.
Dễ dàng tìm thấy thông tin đa dạng mà khó có thể có được từ các phương tiện truyền thông truyền thống.
YouTube cũng đã ảnh hưởng lớn đến sự thay đổi trong các mô hình kinh doanh.
Các thương hiệu và cá nhân đang sử dụng YouTube để giao tiếp với nhiều người tiêu dùng hơn.
Một không gian nơi công chúng có thể tham gia trực tiếp đã được tạo ra.
Điều này cũng đang góp phần vào việc hình thành các quan điểm chính trị.
Ví dụ, nhiều chiến dịch khác nhau đã lan rộng thông qua YouTube.
"""

text_th = """
สวัสดีค่ะ วันนี้ฉันจะมาพูดถึงผลกระทบของ YouTube ต่อสังคม
YouTube เป็นแพลตฟอร์มที่บุคคลสามารถสร้างและแชร์เนื้อหาได้
คนรุ่น MZ กำลังนำเทรนด์ใหม่ๆ ผ่าน YouTube
แพลตฟอร์มนี้ได้กลายเป็นวิธีใหม่สำหรับการศึกษาและการเผยแพร่ข้อมูล
ง่ายต่อการค้นหาข้อมูลที่หลากหลาย ซึ่งหายากจากสื่อดั้งเดิม
YouTube ยังมีอิทธิพลอย่างมากต่อการเปลี่ยนแปลงรูปแบบธุรกิจ
แบรนด์และบุคคลต่างๆ ใช้ YouTube ในการสื่อสารกับผู้บริโภคมากขึ้น
มีพื้นที่ที่สาธารณชนสามารถเข้าร่วมได้โดยตรง
สิ่งนี้ยังส่งผลต่อการก่อตัวของความคิดเห็นทางการเมืองอีกด้วย
เช่น แคมเปญต่างๆ ได้รับการเผยแพร่อย่างกว้างขวางผ่าน YouTube
"""

text_id = """
Halo, hari ini saya akan berbicara tentang dampak YouTube pada masyarakat.
YouTube adalah platform di mana individu dapat membuat dan berbagi konten.
Generasi MZ memimpin tren baru melalui YouTube.
Platform ini telah menjadi metode baru untuk pendidikan dan penyebaran informasi.
Mudah untuk menemukan informasi yang beragam yang sulit diperoleh dari media tradisional.
YouTube juga sangat mempengaruhi perubahan dalam model bisnis.
Merek dan individu menggunakan YouTube untuk berkomunikasi dengan lebih banyak konsumen.
Telah tercipta ruang di mana publik dapat berpartisipasi secara langsung.
Hal ini juga berkontribusi pada pembentukan opini politik.
Misalnya, berbagai kampanye telah tersebar luas melalui YouTube.
"""

text_hi = """
नमस्ते, आज मैं समाज पर YouTube के प्रभाव के बारे में बात करूंगा।
YouTube एक ऐसा मंच है जहाँ व्यक्ति सामग्री बना और साझा कर सकते हैं।
MZ पीढ़ी YouTube के माध्यम से नए रुझानों का नेतृत्व कर रही है।
यह मंच शिक्षा और जानकारी के प्रसार के लिए एक नई विधि बन गया है।
यहाँ विभिन्न प्रकार की जानकारी आसानी से उपलब्ध होती है जो पारंपरिक मीडिया से प्राप्त करना कठिन है।
YouTube ने व्यवसाय मॉडल में परिवर्तन को भी बड़ी मात्रा में प्रभावित किया है।
ब्रांड और व्यक्ति YouTube का उपयोग अधिक उपभोक्ताओं से संवाद करने के लिए कर रहे हैं।
एक ऐसा स्थान बनाया गया है जहाँ जनता सीधे भाग ले सकती है।
यह राजनीतिक राय के निर्माण में भी योगदान दे रहा है।
उदाहरण के लिए, विभिन्न अभियानों ने YouTube के माध्यम से व्यापक रूप से प्रसार पाया है।
"""

text_ru = """
Здравствуйте, сегодня я расскажу о влиянии YouTube на общество.
YouTube — это платформа, на которой люди могут создавать и делиться контентом.
Поколение MZ задает новые тренды через YouTube.
Эта платформа стала новым способом для образования и распространения информации.
Здесь легко найти разнообразную информацию, которую сложно получить из традиционных СМИ.
YouTube также значительно повлиял на изменение бизнес-моделей.
Бренды и частные лица используют YouTube для общения с большим числом потребителей.
Создано пространство, где общественность может участвовать напрямую.
Это также способствует формированию политических мнений.
Например, различные кампании широко распространились через YouTube.
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

text_tr = """
Merhaba, bugün YouTube'un toplum üzerindeki etkisinden bahsedeceğim.
YouTube, bireylerin içerik oluşturup paylaşabildiği bir platformdur.
MZ nesli, YouTube aracılığıyla yeni trendleri belirliyor.
Bu platform, eğitim ve bilgi yayma için yeni bir yöntem haline geldi.
Geleneksel medyadan elde edilmesi zor olan çeşitli bilgilere ulaşmak kolaydır.
YouTube, iş modellerindeki değişimi de büyük ölçüde etkiledi.
Markalar ve bireyler, daha fazla tüketiciyle iletişim kurmak için YouTube'u kullanıyor.
Kamuoyunun doğrudan katılım sağlayabileceği bir alan oluşturuldu.
Bu durum, siyasi görüşlerin oluşumuna da katkıda bulunuyor.
Örneğin, çeşitli kampanyalar YouTube aracılığıyla geniş bir şekilde yayıldı.
"""

text_au = """
G’day, today I’ll be talking about the impact of YouTube on society.
YouTube is a platform where people can create and share content.
The MZ generation is driving new trends through YouTube.
This platform has become a fresh way for education and spreading information.
It’s easy to find a range of information that’s often hard to come by in traditional media.
YouTube has also had a major impact on changing business models.
Brands and individuals are using YouTube to connect with more consumers.
A space where the public can directly participate has been created.
This is also helping to shape political views.
For instance, various campaigns have spread widely across YouTube.
"""


text_nor = """The C motif looks good, but the lack of LED treatment is surprising!"""
text_speed = """<speak><prosody rate="200%">The C motif looks good, but the lack of LED treatment is surprising!</prosody></speak>"""
text_pitch = """<speak><prosody pitch="-5st">The C motif looks good, but the lack of LED treatment is surprising!</prosody></speak>"""

ASR_GGC_SUPPORT_LANGUAGES = {
    # 'es-US-Neural2-A': text_es,
    # 'es-US-Neural2-B': text_es,
    # 'es-US-Neural2-C': text_es,
    # 'es-US-News-D': text_es,
    # 'es-US-News-E': text_es,
    # 'es-US-News-F': text_es,
    # 'es-US-News-G': text_es,
    # 'es-US-Polyglot-1': text_es,
    # 'es-US-Wavenet-A': text_es,
    # 'es-US-Wavenet-B': text_es,
    # 'es-US-Wavenet-C': text_es,
    # 'pl-PL-Wavenet-A': text_pl,
    # 'pl-PL-Wavenet-B': text_pl,
    # 'pl-PL-Wavenet-C': text_pl,
    # 'pl-PL-Wavenet-D': text_pl,
    # 'pl-PL-Wavenet-E': text_pl,
    # 'nl-NL-Wavenet-A': text_nl,
    # 'nl-NL-Wavenet-B': text_nl,
    # 'nl-NL-Wavenet-C': text_nl,
    # 'nl-NL-Wavenet-D': text_nl,
    # 'nl-NL-Wavenet-E': text_nl,
    # 'sv-SE-Wavenet-A': text_sw,
    # 'sv-SE-Wavenet-B': text_sw,
    # 'sv-SE-Wavenet-C': text_sw,
    # 'sv-SE-Wavenet-D': text_sw,
    # 'sv-SE-Wavenet-E': text_sw,
    # 'en-AU-Neural2-A': text_au,
    # 'en-AU-Neural2-B': text_au,
    # 'en-AU-Neural2-C': text_au,
    # 'en-AU-Neural2-D': text_au,
    # 'en-AU-News-E': text_au,
    # 'en-AU-News-F': text_au,
    # 'en-AU-News-G': text_au,
    # 'en-AU-Polyglot-1': text_au,
    # 'en-AU-Wavenet-A': text_au,
    # 'en-AU-Wavenet-B': text_au,
    # 'en-AU-Wavenet-C': text_au,
    # 'en-AU-Wavenet-D': text_au,
    # 'ro-RO-Wavenet-A': text_ro,
    # 'vi-VN-Neural2-A': text_vi,
    # 'vi-VN-Neural2-D': text_vi,
    # 'vi-VN-Wavenet-A': text_vi,
    # 'vi-VN-Wavenet-B': text_vi,
    # 'vi-VN-Wavenet-C': text_vi,
    # 'vi-VN-Wavenet-D': text_vi,
    # 'th-TH-Neural2-C': text_th,
    # 'id-ID-Wavenet-A': text_id,
    # 'id-ID-Wavenet-B': text_id,
    # 'id-ID-Wavenet-C': text_id,
    # 'id-ID-Wavenet-D': text_id,
    # 'yue-HK-Standard-A': text_hk,
    # 'yue-HK-Standard-B': text_hk,
    # 'yue-HK-Standard-C': text_hk,
    # 'yue-HK-Standard-D': text_hk,
    # 'hi-IN-Neural2-A': text_hi,
    # 'hi-IN-Neural2-B': text_hi,
    # 'hi-IN-Neural2-C': text_hi,
    # 'hi-IN-Neural2-D': text_hi,
    # 'hi-IN-Wavenet-A': text_hi,
    # 'hi-IN-Wavenet-B': text_hi,
    # 'hi-IN-Wavenet-C': text_hi,
    # 'hi-IN-Wavenet-D': text_hi,
    # 'ru-RU-Wavenet-A': text_ru,
    # 'ru-RU-Wavenet-B': text_ru,
    # 'ru-RU-Wavenet-C': text_ru,
    # 'ru-RU-Wavenet-D': text_ru,
    # 'ru-RU-Wavenet-E': text_ru,
    # 'ar-XA-Wavenet-A': text_ar,
    # 'ar-XA-Wavenet-B': text_ar,
    # 'ar-XA-Wavenet-C': text_ar,
    # 'ar-XA-Wavenet-D': text_ar,
    # 'tr-TR-Wavenet-A': text_tr,
    # 'tr-TR-Wavenet-B': text_tr,
    # 'tr-TR-Wavenet-C': text_tr,
    # 'tr-TR-Wavenet-D': text_tr,
    # 'tr-TR-Wavenet-E': text_tr,
    # 'en-AU-Neural2-A': text_nor
    # 'en-AU-Neural2-A': text_speed
    'en-AU-Neural2-A': text_pitch
}


idx = 0
def synthesize_text(argText, argLanguageCode, argVoiceName):
    client = get_client_ai_voice_ggc()

    # input_text = texttospeech.SynthesisInput(text=argText)
    input_text = texttospeech.SynthesisInput(ssml=argText)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice_config = texttospeech.VoiceSelectionParams(
        language_code=argLanguageCode,
        name=argVoiceName,
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        request={"input": input_text, "voice": voice_config, "audio_config": audio_config}
    )

    # The response's audio_content is binary.
    my_target_dir = get_dir_result_without_overlay()

    try:
        if not os.path.exists(my_target_dir):
            os.makedirs(my_target_dir)
    except OSError:
        print("Error: Failed to create the directory.")

    #my_voice_save_file_name = os.path.join(my_target_dir, f"GoogleTTS_{date_str}_{argLanguageCode}_{argVoiceName}_{argVoiceGender}_{get_date_file_name()}.{AI_VOICE_SAVE_FILE_EXT}")
    my_voice_save_file_name = os.path.join(my_target_dir, f"GoogleTTS_{idx:02d}_{argLanguageCode}_{argVoiceName[6:]}_{get_date_file_name()}.{AI_VOICE_SAVE_FILE_EXT}")
    print(f'my_voice_save_file_name : {my_voice_save_file_name}')

    with open(my_voice_save_file_name, "wb") as out:
        out.write(response.audio_content)
        print(f'Audio content written to file "{my_voice_save_file_name}"')

def list_voices():
    client = texttospeech.TextToSpeechClient()

    # Performs the list voices request
    voices = client.list_voices()

    for voice in voices.voices:
        # Display the voice's name. Example: tpc-vocoded
        print(f"Name: {voice.name}")

        # Display the supported language codes for this voice. Example: "en-US"
        for language_code in voice.language_codes:
            print(f"Supported language: {language_code}")

        ssml_gender = texttospeech.SsmlVoiceGender(voice.ssml_gender)

        # Display the SSML Voice Gender
        print(f"SSML Voice Gender: {ssml_gender.name}")

        # Display the natural sample rate hertz for this voice. Example: 24000
        print(f"Natural Sample Rate Hertz: {voice.natural_sample_rate_hertz}\n")

    print(f'## voices : {voices}')
    print(f'## All Support voice list : {len(voices.voices)}')


if __name__ == "__main__":
#     list_voices()
#     text = '''안녕하세요, 오늘 발표할 주제는 Youtube가 사회변화에 미치는 영향입니다.
# Youtube는 다양한 콘텐츠 제공으로 개인의 의견 표현의 자유를 확장했습니다.
# 그렇지만 이러한 정보의 과잉으로 인해 잘못된 정보가 확산되는 문제도 존재합니다.'''

    for key, value in ASR_GGC_SUPPORT_LANGUAGES.items():
        print(key[:5])
        print(key)
        print(value)
        print(texttospeech.SsmlVoiceGender.NEUTRAL)
        print(idx)
        synthesize_text(argText=value, argLanguageCode=key[:5], argVoiceName=key)
        idx = idx + 1
