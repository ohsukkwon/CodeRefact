# -*- coding: utf-8 -*-

# test 폴더내에만 정의하는 파일
requsted_texts_eng = [
"Saving Private Ryan has a total length of 169 minutes.",
"Lake Baikal in Russia is the deepest freshwater lake in the world, reaching a depth of about 1,642 meters.",
"Not too shabby, thanks for askin'. Say, I'm plannin' on headin' down to that crawfish boil this weekend. Y'all wanna come along?",
"I have to go in to work at 9 am tomorrow, but I highkey don't want to because I'm so tired!",
"Kick the bucket",
" Samsung has made significant contributions to the development of memory chips",
"The Supreme Court won’t hear InfoWars host’s First Amendment challenge to his Jan. 6 conviction, maintaining his misdemeanor charges for efforts to inflame the Capitol crowd.",
"The IMF projects global growth at 3.1% in 2024, slightly higher than the 3.0% forecast in October 2023, driven by resilience in the United States and several large emerging markets.",
"The tomb of Thutmose IV's scribe Nakht in Egypt offers a glimpse into the astronomical knowledge and daily life of a high-ranking official during the New Kingdom.",
"A new study shows that antibodies might help fight Influenza B effectively.",
"The Biden administration's policies aim to dramatically reduce carbon dioxide emissions, aligning with the goal of becoming carbon neutral by 2050.",
"Intellectual humility, the willingness to acknowledge what you don't know, is a crucial trait for effective communication in today's complex world.",
"Open-source AI refers to technology with freely available source code, promoting collaboration and transparency within the AI community.",
"Gun control is such a polarizing issue, especially with the rise in mass shootings this year.",
"The 2024 U.S. presidential candidates ramp up their campaigns as debates intensify over key issues like immigration and healthcare."
    ]

requsted_texts_kor = [
"통계청이 1일 발표한 ‘2024년 6월 온라인쇼핑 동향’ 등의 자료를 보면 지난 6월 온라인쇼핑 전체 거래액은 20조683억 원으로 지난해 같은 달(18조6140억 원)보다 7.8% 늘었다.",
"광주의 대표 축제인 광주비엔날레를 중심으로 광주김치대축제, 광주국제영화제 등 5대 축제를 즐길 수 있다.",
"야는 여 쓰는기고 쟈는 중간에 낑굴때 쓰는기고 저 끄트바리에 있는기는 요로코롬 놔둬가 쓰는기다.",
"와 이게 바로 편리미엄",
"콩 심은데 콩 나고 팥 심은데 팥난다",
"갤럭시 버즈3' 시리즈 또한 버즈 시리즈 사상 최초로 '스템(Stem)'형 디자인, 일명 '콩나물' 디자인을 채택했습니다. '갤럭시 워치 울트라' 역시 기존의 원형 디자인에서 벗어나 둥근 사각형 디자인으로 출시했습니다.",
"여야 잠재적 대권주자 8인에 대한 호감도 조사에서 친윤(親윤석열)계 주류 반대를 압도하며 당선된 한동훈 국민의힘 대표가 5%포인트에 가까이 약진하며, 더불어민주당 대표 연임이 확실시되는 '선두' 이재명 전 대표와의 격차를 한자릿수로 좁혔다.",
"15대 주력 수출 품목 중에서는 자동차 등 일부 품목을 빼고 반도체 등 11개 수출 품목의 수출이 증가했다.",
"컴퓨터도, 소규모 기억장치도 없던 시절에 백업을 정말 철저하게 했다. 고려실록은 궁궐에 1부, 소실을 대비해 해인사에 1부, 총 2부를 만들었는데 조선왕조실록은 항상 4~5부를 만들었다.",
"가정의 혼란은 ADHD 증상을 보이는 10대들의 수면의 질 저하와 관련이 있다.",
"나무는 이산화탄소의 좋은 흡수원이다. 예를 들어, 북유럽과 같이 산림이 우거진 국가는 흡수량이 많아 온실가스 감축에 큰 부담을 느끼지 않는 것이 좋은 예인 것이다.",
"자신과 타인의 감정을 인식하고 관리하는 능력인 감성지능은 개인적, 직업적 성공의 핵심이다.",
"서치GPT'는 사용자가 원하는 내용을 입력하면, 요약된 검색 결과 및 이미지를 소스 링크와 함께 제공한다. 사용자는 검색 내용에 관련된 후속 질문을 할 수 있고 상황에 맞는 응답을 받을 수 있다.",
"그 스타일 마음에 드네요. 나도 안경을 새로 맞춰야 하는데, 그거 어디서 맞춘 거예요?",
"밤낮을 가리지 않는 무더위가 기승을 부리고 있습니다. 강릉은 18일째 열대야가 이어지며 최장 밤더위 기록을 매일 경신하고 있는데요. 서울은 16일째 열대야가, 14일 연속 폭염특보가 발효 중입니다."
    ]

solutions_arr = [
    "NCP_",
    "AWS_",
    "MSA_",
    "OPENAI_",
    "GOOGLE_",
    "ElevenLabs_"
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