# -*- coding: utf-8 -*-
import requests

from AWS_AiVoiceUtils import get_client_ai_voice_aws
from GlobalUtil import get_dir_result_without_overlay
from GlobalVars import *
from MyKeyStore import *

requests.packages.urllib3.disable_warnings()

ASR_AWS_SUPPORT_LANGUAGES = [
    ["영어(영국)", "en-GB", "Amy"],           #10
    ["영어(영국)", "en-GB", "Emma"],          #11
    ["영어(영국)", "en-GB", "Brian"],         #12
    ["영어(영국)", "en-GB", "Arthur"],        #13
    ["영어(인도)", "en-IN", "Kajal"],         #14
    ["프랑스어", "fr-FR", "Lea"],             #32
    ["프랑스어", "fr-FR", "Remi"],            #33
    ["프랑스어(벨기에)", "fr-BE", "Isabelle"], #34
    ["프랑스어(캐나다)", "fr-CA", "Gabrielle"],#35
    ["프랑스어(캐나다)", "fr-CA", "Liam"],     #36
    ["스페인어(유럽)", "es-ES", "Lucia"],               #54
    ["스페인어(유럽)", "es-ES", "Sergio"],              #55
    ["표준 중국어", "cmn-CN", "Zhiyu"],       #6
    ["일본어", "ja-JP", "Takumi"],            #44
    ["일본어", "ja-JP", "Kazuha"],            #45
    ["일본어", "ja-JP", "Tomoko"],            #46
]

ASR_AWS_SUPPORT_LANGUAGES2 = [
    ["스페인어(미국)", "es-US", "Lupe"],           #10
    ["스페인어(미국)", "es-US", "Pedro"],          #11
    ["폴란드어", "pl-PL", "Ola"],         #12
    ["네덜란드어", "nl-NL", "Laura"],        #13
    ["스웨덴어", "sv-SE", "Elin"],         #14
    ["영어(호주)", "en-AU", "Olivia"],             #32
    ["중국어(광동어)", "yue-CN", "Hiujin"],            #33
    ["힌디어", "hi-IN", "Kajal"], #34
    ["아랍어", "are", "Hala"],#35
    ["아랍어", "are", "Zayd"],#35
    ["터키어", "tr-TR", "Burcu"],
    ["포르투갈어(브라질)", "pt-BR", "Vitoria"], #51
    ["포르투갈어(유럽)", "pt-PT", "Ines"],
    ["스페인어(멕시코)", "es-MX", "Andrés"],
]

text_en = """
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

text_fr = """
Bonjour, aujourd'hui, je vais parler de l'impact de YouTube sur la société.
YouTube est une plateforme où les individus peuvent créer et partager du contenu.
La génération MZ dirige de nouvelles tendances grâce à YouTube.
Cette plateforme est devenue un nouveau moyen d'éducation et de diffusion d'informations.
Il est facile de trouver des informations diverses, difficiles à obtenir par les médias traditionnels.
YouTube a également eu une grande influence sur le changement des modèles économiques.
Les marques et les particuliers utilisent YouTube pour communiquer avec plus de consommateurs.
Un espace où le public peut participer directement a été créé.
Cela contribue également à la formation de l'opinion politique.
Par exemple, plusieurs campagnes se sont largement propagées via YouTube.
"""

text_es = """
Hola, hoy hablaré sobre el impacto de YouTube en la sociedad.
YouTube es una plataforma en la que los individuos pueden crear y compartir contenido.
La generación MZ está liderando nuevas tendencias a través de YouTube.
Esta plataforma se ha convertido en un nuevo método de educación y transmisión de información.
Es fácil encontrar información diversa que es difícil de obtener en los medios tradicionales.
YouTube también ha tenido un gran impacto en el cambio de los modelos de negocio.
Las marcas y los individuos utilizan YouTube para comunicarse con más consumidores.
Se ha creado un espacio donde el público puede participar directamente.
Esto también está contribuyendo a la formación de la opinión política.
Por ejemplo, muchas campañas se han difundido ampliamente a través de YouTube.
"""

text_cmn = """
大家好，今天我将谈谈YouTube对社会的影响。
YouTube 是一个个人可以制作和分享内容的平台。
MZ 世代正在通过YouTube 引领新的潮流。
这个平台已经成为一种新的教育和信息传播方式。
很容易找到传统媒体中难以获得的各种信息。
YouTube 也对商业模式的变革产生了巨大影响。
品牌和个人利用 YouTube与更多的消费者进行沟通。
一个让公众直接参与的空间已经被创建。
这也为政治舆论的形成做出了贡献。
例如，许多活动通过YouTube 广泛传播。
"""

text_jp = """
こんにちは、今日はYouTubeが社会に与える影響についてお話しします。
YouTubeは、個人がコンテンツを作成し共有できるプラットフォームです。
MZ世代はYouTubeを通じて新しいトレンドをリードしています。
このプラットフォームは、教育や情報伝達の新しい方法になっています。
従来のメディアでは得にくい様々な情報を簡単に見つけることができます。
YouTubeはビジネスモデルの変革にも大きな影響を与えました。
ブランドや個人はYouTubeを活用して、より多くの消費者とコミュニケーションをとっています。
大衆が直接参加できる場が提供されました。
これは政治的な世論形成にも貢献しています。
例えば、多くのキャンペーンがYouTubeを通じて広く拡散されました。
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

text_pt = """
Olá, hoje vou falar sobre o impacto do YouTube na sociedade.
O YouTube é uma plataforma onde as pessoas podem criar e compartilhar conteúdos.
A geração MZ está a impulsionar novas tendências através do YouTube.
Esta plataforma tornou-se uma nova forma de educação e disseminação de informações.
É fácil encontrar uma variedade de informações que muitas vezes são difíceis de obter nos meios de comunicação tradicionais.
O YouTube também teve um grande impacto na mudança dos modelos de negócios.
Marcas e indivíduos estão a usar o YouTube para se conectar com mais consumidores.
Foi criado um espaço onde o público pode participar diretamente.
Isto também está a ajudar a moldar opiniões políticas.
Por exemplo, várias campanhas foram amplamente divulgadas através do YouTube.
"""

requsted_texts = [
    "The C motif looks good, but the lack of LED treatment is surprising!",
    "Allez! Monkeys frolic in French breviary.",
    "Welcome to our restaurant, Chez Attitude!","Zenith gets approval for generic medication.",
    "The Deutsche Bracke is a small hound.",
    "The well bred Bichon Frise is a feisty and affectionate.",
    "The coulomb is a fundamental unit of electrical charge, and is also the SI derived unit of electric charge.",
    "The news agency Reuters belongs to which country?",
    "Which pyrimidine base contains an amino group at carbon four?",
    "Vemula Ramakrishna was born on sixth of September.", # 8
    "What prompted Harley to start local manufacturing in India?",
    "Why Shah commission report on Odisha mining scam will gather dust?",
    "What is your advice for investors to trade in Nifty?",
    "How one should play these stocks ahead of policy?",
    "How long before AAP's propaganda on corruption comes back to haunt it?",
    "Ah, I can smell jealousy in the air!",
    "Tonight we start a new modded Minecraft Skyblock series!",
    "Arguably, that is a nice bit of safety tech to have!",
    "Third gen BMW X five is headed for an India drive soon!",
    "While engineering builds, science breaks up to see what is inside!",
    "In case you are wondering, that is forty percent of the GDP!",
    "Indian pop singer Raageshwari Loomba to tie the knot!",
    "Hey look, subaahu had cheese and crackers!",
    "Alright! What is that you want to tell me about politics?",
    "But of course! How much are you thinking of spending on event tonight?",
    "Holy cow! I never heard of such a thing. How much do they cost?",
    "A hike would be great! Let me pack us a nice picnic lunch, OK?",
    "But it was full of pencils! How could he say it was empty?",
    "What would drive the mobile ad industry in twothousand fourteen?",
    "The C motif looks good, but the lack of LED treatment is surprising!",
    "For the babus, Lunchbox, is a flop all the way!", # 29
    "For the babus, Lunchbox, is a flop all the way!",
    "What would drive the mobile ad industry in twothousand fourteen?",
    "Don't touch the Small puppies!",
    "Gauhar Ahuja, It is better to fail in originality than to succeed in imitation, right!",
    "Am looking for Jane Street which is left to banquat hall?",
    "After I was rested and refreshed, he asked me, What has brought you back so soon?",
    "Ah said the queen who would have thought the sprites were so lovely.",
    "Among teenage fashion that is prevalent in the world today which do you think is the best.",
    "An isotope of hydrogen listed in the sentences down?",
    "Analyze what are the relevance of social sciences in solving contemporary problems?",
    "Analyze which are the ethical issues involved in Social Science research?"
]

polly_client = get_client_ai_voice_aws()

___tmp_idx = 0
for i, text in enumerate(requsted_texts):
    my_target_dir = get_dir_result_without_overlay()
    try:
        if not os.path.exists(my_target_dir):
            os.makedirs(my_target_dir)
    except OSError:
        print("Error: Failed to create the directory.")

    if i < 9:
        my_voice_save_file_name = f'{i:02d}_en_IN_Intelligibility.mp3'
    elif 9 <= i < 29:
        my_voice_save_file_name = f'{i:02d}_en_IN_Naturalness.mp3'
    else:
        my_voice_save_file_name = f'{i:02d}_en_IN_Appropriateness.mp3'

    tmp_mp3_path = os.path.join(my_target_dir, my_voice_save_file_name)
    print(f'tmp_mp3_path : {tmp_mp3_path}')

    response = polly_client.synthesize_speech(VoiceId="Kajal", OutputFormat=AI_VOICE_SAVE_FILE_EXT, Text=text, Engine=AI_VOICE_AWS_ENGINE)

    file = open(tmp_mp3_path, 'wb')
    file.write(response['AudioStream'].read())
    file.close()
    ___tmp_idx += 1
    if ___tmp_idx >= 1:
        break

# for i in range(0, len(ASR_AWS_SUPPORT_LANGUAGES2)):
#
#     my_target_dir = get_dir_result()
#     try:
#         if not os.path.exists(my_target_dir):
#             os.makedirs(my_target_dir)
#     except OSError:
#         print("Error: Failed to create the directory.")
#
#     if len(ASR_AWS_SUPPORT_LANGUAGES2[i][1].split(r'-')) == 1:
#         my_voice_save_file_name = f'{i:02d}_{ASR_AWS_SUPPORT_LANGUAGES2[i][1]}_{ASR_AWS_SUPPORT_LANGUAGES2[i][2]}.mp3'
#     else:
#         my_voice_save_file_name = f'{i:02d}_{ASR_AWS_SUPPORT_LANGUAGES2[i][1].split(r"-")[1]}_{ASR_AWS_SUPPORT_LANGUAGES2[i][2]}.mp3'
#     tmp_mp3_path = os.path.join(my_target_dir, my_voice_save_file_name)
#     if "en" in ASR_AWS_SUPPORT_LANGUAGES2[i][1]:
#         argText = text_au
#     elif "fr" in ASR_AWS_SUPPORT_LANGUAGES2[i][1]:
#         argText = text_fr
#     elif "es" in ASR_AWS_SUPPORT_LANGUAGES2[i][1]:
#         argText = text_es
#     elif "cmn" in ASR_AWS_SUPPORT_LANGUAGES2[i][1]:
#         argText = text_cmn
#     elif "ja" in ASR_AWS_SUPPORT_LANGUAGES2[i][1]:
#         argText = text_jp
#     elif "pl" in ASR_AWS_SUPPORT_LANGUAGES2[i][1]:
#         argText = text_pl
#     elif "nl" in ASR_AWS_SUPPORT_LANGUAGES2[i][1]:
#         argText = text_nl
#     elif "sv" in ASR_AWS_SUPPORT_LANGUAGES2[i][1]:
#         argText = text_sw
#     elif "yue" in ASR_AWS_SUPPORT_LANGUAGES2[i][1]:
#         argText = text_hk
#     elif "hi" in ASR_AWS_SUPPORT_LANGUAGES2[i][1]:
#         argText = text_hi
#     elif "tr" in ASR_AWS_SUPPORT_LANGUAGES2[i][1]:
#         argText = text_tr
#     elif "are" in ASR_AWS_SUPPORT_LANGUAGES2[i][1]:
#         argText = text_ar
#     elif "pt" in ASR_AWS_SUPPORT_LANGUAGES2[i][1]:
#         argText = text_pt
#     else:
#         argText = ""
#
#     response = polly_client.synthesize_speech(VoiceId=ASR_AWS_SUPPORT_LANGUAGES2[i][2], OutputFormat=AI_VOICE_SAVE_FILE_EXT, Text=argText, Engine=AI_VOICE_AWS_ENGINE)
#
#     print(f'tmp_mp3_path : {tmp_mp3_path}')
#     file = open(tmp_mp3_path, 'wb')
#     file.write(response['AudioStream'].read())
#     file.close()