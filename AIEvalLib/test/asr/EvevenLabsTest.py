# -*- coding: utf-8 -*-
from elevenlabs import VoiceSettings, save

from GlobalVars import *
from GlobalUtil import get_date_file_name, get_client_ai_voice_elv, get_dir_result_without_overlay
from MyKeyStore import *

___api_key = keystore_get_key_type(argType=KEYTYPE_IDX_AIvoice_Elevenlabs_NONE_NONE)

client = get_client_ai_voice_elv()

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

text_kr = """
안녕하세요, 오늘은 유튜브가 사회에 미치는 영향에 대해 이야기하겠습니다.
유튜브는 개인이 콘텐츠를 제작하고 공유할 수 있는 플랫폼입니다.
MZ세대는 유튜브를 통해 새로운 트렌드를 주도하고 있습니다.
이 플랫폼은 교육, 정보 전달의 새로운 방법이 되고 있습니다.
전통적인 매체에서 얻기 힘든 다양한 정보를 쉽게 찾을 수 있습니다.
유튜브는 비즈니스 모델 변화에도 큰 영향을 미쳤습니다.
브랜드와 개인은 유튜브를 활용하여 더 많은 소비자와 소통하고 있습니다.
대중이 직접 참여할 수 있는 공간이 마련되었습니다.
이는 정치적인 여론 형성에도 기여하고 있습니다.
예를 들어, 여러 캠페인이 유튜브를 통해 널리 퍼졌습니다.
"""


# try:
#     models = client.models.get_all()
#     print(f'Support all models : {models}')
# except elevenlabs.core.api_error.ApiError as e:
#     print(f'Error: {e.body["detail"]["message"]}')
#     print("Please ensure your API key has the required 'models_read' permission.")

# text_list = [text_es, text_pl, text_nl, text_sw, text_ro, text_vi, text_th, text_id, text_hi, text_ru, text_ar, text_hk, text_tw, text_tr, text_au]
# lang_list = ["spanish", "polish", "dutch", "swedish", "romanian", "vietnamese", "thai", "indonesian", "hindi", "russian", "arabic", "hongkong", "taiwan", "turkish", "english_au"]

text_list = [text_au]
lang_list = ["english_au"]

for i in range(0, len(text_list)):
    audio = client.text_to_speech.convert(
        #voice_id="IKne3meq5aSn9XLyUdCD", # Male
        voice_id="Xb7hH8MSUJpSbSDYk0k2", # Female
        optimize_streaming_latency="0",
        output_format="mp3_44100_128",
        text=text_list[i],
        # model_id="eleven_multilingual_v2",
        # language_code="ko",
        model_id="eleven_multilingual_v2",
        voice_settings=VoiceSettings(
            stability=0.1,
            similarity_boost=0.3,
            style=0.2,

        ),
    )

    #print(f'audio:{audio}')

    my_target_dir = get_dir_result_without_overlay()

    try:
        if not os.path.exists(my_target_dir):
            os.makedirs(my_target_dir)
    except OSError:
        print("Error: Failed to create the directory.")

    my_voice_save_file_name = f'ELV_multilingual_v2_{get_date_file_name()}.{AI_VOICE_SAVE_FILE_EXT}'
    tmp_mp3_path = os.path.join(my_target_dir, my_voice_save_file_name)
    print(f'tmp_mp3_path : {tmp_mp3_path}')

    #play(audio)
    save(audio, tmp_mp3_path)

