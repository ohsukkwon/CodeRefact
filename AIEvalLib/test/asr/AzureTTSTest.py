# -*- coding: utf-8 -*-
from GlobalVars import *
from GlobalUtil import get_date_file_name, get_dir_result_without_overlay
from MSA_AiVoiceUtils import gen_ai_voice_msa
from MyKeyStore import *

ASR_MSA_SUPPORT_LANGUAGES = [
    'en-US-AvaMultilingualNeural',
    'en-US-AndrewMultilingualNeural',
    'en-US-CoraMultilingualNeural',
    'en-US-ChristopherMultilingualNeural',
    'en-US-BrandonMultilingualNeural',
    'en-US-EmmaMultilingualNeural',
    'en-US-BrianMultilingualNeural',
    'en-US-GuyNeural',
    'en-US-AriaNeural',
    'en-US-JaneNeural',
    'en-US-JasonNeural',
    'en-US-BrandonNeural',
    'en-US-ChristopherNeural',
    'en-US-CoraNeural',
    'en-US-JennyMultilingualNeural',
    'en-US-RyanMultilingualNeural',
    'it-IT-AlessioMultilingualNeural',
    'it-IT-GiuseppeMultilingualNeural',
    'it-IT-IsabellaMultilingualNeural',
    'it-IT-MarcelloMultilingualNeural',
    'it-IT-ElsaNeural',
    'it-IT-IsabellaNeural',
    'it-IT-DiegoNeural',
    'it-IT-GiuseppeNeural',
    'pt-BR-MacerioMultilingualNeural',
    'pt-BR-ThalitaMultilingualNeural',
    'pt-BR-FranciscaNeural',
    'pt-BR-ThalitaNeural',
    'es-MX-DaliaNeural',
    'es-MX-JorgeNeural',
]


text_esmx = """
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

text_itit = """
Ciao, oggi parlerò dell'impatto di YouTube sulla società.
YouTube è una piattaforma in cui le persone possono creare e condividere contenuti.
La generazione MZ sta guidando nuove tendenze attraverso YouTube.
Questa piattaforma è diventata un nuovo metodo per l'istruzione e la diffusione di informazioni.
È facile trovare informazioni varie che sono difficili da ottenere dai media tradizionali.
YouTube ha avuto un grande impatto anche sul cambiamento dei modelli di business.
I marchi e le persone usano YouTube per comunicare con più consumatori.
È stato creato uno spazio in cui il pubblico può partecipare direttamente.
Questo contribuisce anche alla formazione dell'opinione pubblica politica.
Ad esempio, molte campagne si sono diffuse ampiamente tramite YouTube.
"""

text_ptbr = """
Olá, hoje vou falar sobre o impacto do YouTube na sociedade.
O YouTube é uma plataforma onde as pessoas podem criar e compartilhar conteúdo.
A geração MZ está liderando novas tendências através do YouTube.
Esta plataforma se tornou um novo método para educação e disseminação de informações.
É fácil encontrar informações diversas que são difíceis de obter na mídia tradicional.
O YouTube também teve um grande impacto na mudança dos modelos de negócios.
Marcas e indivíduos estão utilizando o YouTube para se comunicar com mais consumidores.
Foi criado um espaço onde o público pode participar diretamente.
Isso também está contribuindo para a formação da opinião política.
Por exemplo, muitas campanhas se espalharam amplamente através do YouTube.
"""

text_enus = """
Hello, today I will talk about the impact of YouTube on society.
YouTube is a platform where individuals can create and share content.
The MZ generation is leading new trends through YouTube.
This platform has become a new method for education and information dissemination.
It is easy to find diverse information that is difficult to obtain from traditional media.
YouTube has also greatly influenced the change in business models.
Brands and individuals are using YouTube to communicate with more consumers.
A space where the public can directly participate has been created.
This is also contributing to the formation of political opinions.
For example, various campaigns have spread widely through YouTube.
"""

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

ASR_MSA_SUPPORT_LANGUAGES2 = {
    'es-US-PalomaNeural': text_es,
    'es-US-AlonsoNeural': text_es,
    'pl-PL-MarekNeural': text_pl,
    'pl-PL-ZofiaNeural': text_pl,
    'nl-NL-FennaNeural': text_nl,
    'nl-NL-MaartenNeural': text_nl,
    'sv-SE-MattiasNeural': text_sw,
    'sv-SE-HilleviNeural': text_sw,
    'ro-RO-AlinaNeural': text_ro,
    'ro-RO-EmilNeural': text_ro,
    'vi-VN-HoaiMyNeural': text_vi,
    'vi-VN-NamMinhNeural': text_vi,
    'th-TH-NiwatNeural': text_th,
    'th-TH-AcharaNeural': text_th,
    'id-ID-GadisNeural': text_id,
    'id-ID-ArdiNeural': text_id,
    'en-AU-NatashaNeural': text_au,
    'en-AU-WilliamNeural': text_au,
    'zh-HK-HiuMaanNeural': text_hk,
    'zh-HK-WanLungNeural': text_hk,
    'zh-TW-HsiaoChenNeural': text_tw,
    'zh-TW-YunJheNeural': text_tw,
    'hi-IN-AaravNeural': text_hi,
    'hi-IN-AnanyaNeural': text_hi,
    'ru-RU-DmitryNeural': text_ru,
    'ru-RU-DariyaNeural': text_ru,
    'ar-AE-FatimaNeural': text_ar,
    'ar-AE-HamdanNeural': text_ar,
    'tr-TR-EmelNeural': text_tr,
    'tr-TR-AhmetNeural': text_tr,
}

requested_texts = [
    "Which arm of the government has the power to interpret and apply laws?",
    "When was the information published or last updated?",
    "I'm planning a road trip to Perth. What's the best route to take from Sydney?",
    "Can you text me the recipe for that delicious soup? I want to cook it for my friends.",
    "Beware of mechanical moving parts!",
    "Warning! Do not feed the animals!",
    "Treat the environment with respect and leave no trace from your visit.",
    "Step aside on slopes and give way to people going uphill.",
    "A severe weather warning for damaging winds is current across western and central districts of Australia.",
    "One Aussie state has called for an end to terms like 'Boomer' and 'Millennial', claiming it separates generations.",
    "Do you support an Australian republic?",
    "What smell reminds you most of a specific place or time?",
    "I love this place so much, do you think we could stay a little longer? ",
    "How much water have we got left? I'm ever so thirsty. ",
    "We're not going to the beach! It's far too hot!",
    "He told me he never wanted to see me again! I'm devastated! ",
    "Please write whenever you get a chance.",
    "Shut the door quietly so you don't wake the baby.",
    "I'm juggling a busy week at work with the school hols. Will write more soon.",
    "Mum was thrilled to bits when you turned up unexpectedly.",
    "Hey, how's things? Do you fancy a dog walk soon?",
    "What time will you be at Mum's tomorrow?",
    "Can't talk now, busy with work. Speak later? ",
    "Booked table for half 12, couldn't get 12. Hope that's OK?",
    "Congratulations! You have just won the holiday of a lifetime!",
    "We really should keep in touch more often!",
    "New products just arrived. Click here to go to our site and get yours now.",
    "Get fit, get healthy. Shape your perfect body. Join now.",
    "We've had to reschedule your delivery today. We'll now deliver between 10:30 - 11:30 tomorrow.",
    "King Charles to tour Australia in first visit since taking the throne."
]

my_target_dir = get_dir_result_without_overlay()
try:
    if not os.path.exists(my_target_dir):
        os.makedirs(my_target_dir)
except OSError:
    print("Error: Failed to create the directory.")

___tmp_idx = 0
for i, text_item in enumerate(requested_texts):
    my_voice_save_file_name = f'AzureTTS1_{get_date_file_name()}_{i:02d}.{AI_VOICE_SAVE_FILE_EXT}'
    tmp_mp3_path = os.path.join(my_target_dir, my_voice_save_file_name)

    gen_ai_voice_msa(tmp_mp3_path, text_item, 81, argSpeakingSpeed=0.5, argSpeakingPitch='low')
    ___tmp_idx += 1
    if ___tmp_idx >= 1:
        break


