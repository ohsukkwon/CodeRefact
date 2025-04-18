# -*- coding: utf-8 -*-
import traceback

from GlobalUtil import is_azure_support_langcode, get_client_ai_language_detection_ggc

__test_sample_arr = [
    ["Afrikaans","EMPTY","af","empty",	"오늘은 진짜 너무 hot한 날씨라서 コンビニ(편의점) 가서 冰淇淋(아이스크림) 하나 사먹어야겠다."],
    ["Albanian","EMPTY","sq","empty",	"Kur shikoj perëndimin e kuq të diellit, ndihem sikur po kthehem në fëmijërinë time, kur luaja pafajësisht. Mora një moment për të reflektuar mbi fëmijërinë time. Ishte e mrekullueshme të kalonim një kohë të mirë së bashku. Jam sinqerisht mirënjohës."],
    ["Amharic","EMPTY","am","empty",	"በቀይ ቀለም የተሞላ የምሽት ፀሐይ መጥለቂያን ስትመለከቱ እንደ ልጅነት ዘመን እንደምትመለሱ አስታውሳለሁ። ልጅነቴን ስላስታወስሁ አንድ ጊዜ ሐሳብ ላይ እቅፍ አልፌ ነበር። በአንድነት ጥሩ ጊዜ ማሳለፍ በጣም ደስ አለኝ። እንባለሁ።"],
    ["Arabic","EMPTY","ar","empty",	"عندما أنظر إلى غروب الشمس الأحمر، أشعر وكأنني أعود إلى طفولتي حين كنت ألعب ببراءة. أخذت لحظة للتفكير في طفولتي. كان من الرائع قضاء وقت جيد معًا. أشكركم بصدق."],
    ["Armenian","EMPTY","hy","empty",	"Երբ ես նայում եմ կարմիր մայրամուտին, թվում է, թե վերադարձնում եմ մանկությանս, երբ անմեղ խաղում էի: Մի պահ վերցրեցի մտածել մանկությանս մասին: Հրաշալի էր միասին լավ ժամանակ անցկացնել: Ես անկեղծորեն շնորհակալ եմ:"],
    ["Assamese","EMPTY","as","empty",	"ৰঙা সন্ধিয়া সূৰ্যাস্ত চাওঁতে, মোৰ শৈশৱৰ দিনবোৰলৈ উভতি যোৱাৰ দৰে অনুভৱ হয়। যেতিয়া মই নিৰ্দোষভাৱে খেলিছিলো। মই মোৰ শৈশৱৰ দিনবোৰৰ বিষয়ে চিন্তা কৰি কিছু সময়ৰ বাবে চিন্তাৰ নিমজ্জিত হৈ পৰিলো। একেলগে ভাল সময় কটাব পাৰি বৰ ভাল লাগিল। আন্তৰিক ধন্যবাদ।"],
    ["Azerbaijani","EMPTY","az","empty",	"Qırmızı rəngə boyanmış gün batımına baxanda, sanki keçmişdəki uşaqlıq illərimə, məsumca oynadığım o günlərə qayıdıram. Uşaqlıq xatirələrimi düşünərək bir anlıq düşüncəyə daldım. Birlikdə yaxşı vaxt keçirmək çox xoş idi. Səmimi təşəkkürlər."],
    ["Bashkir","EMPTY","ba","empty",	"Ҡыҙыл төҫкә буялған киске ҡояш байышына ҡарағанда, бала сағымдағы саф уйнап йөрөгән ваҡыттарыма кире ҡайтҡандай булам. Бала сағымды иҫкә алып, бер аҙ уйға сумдым. Бергә яҡшы ваҡыт үткәреү бик күңелле булды. Ихлас рәхмәттәр."],
    ["Basque","EMPTY","eu","empty",	"Ilunabar gorriari begira, nire haurtzarora itzultzen naizela sentitzen dut, lotsagabe jolasten nuenean. Une bat hartu nuen nire haurtzaroaz hausnartzeko. Oso polita izan zen elkarrekin denbora ona pasatzea. Benetan eskertzen dut."],
    ["Belarusian","EMPTY","be","empty",	"Калі я гляджу на чырвоны захад сонца, адчуваю, быццам вяртаюся ў дзяцінства, калі гуляў без клопатаў. Я на хвіліну задумаўся пра сваё дзяцінства. Было цудоўна правесці час разам. Шчыра дзякую."],
    ["Bengali","EMPTY","bn","empty",	"লাল রঙের সূর্যাস্তের দিকে তাকালে, মনে হয় যেন আমি আমার শৈশবে ফিরে গেছি, যখন আমি নির্দোষভাবে খেলতাম। আমি আমার শৈশবের কথা চিন্তা করে কিছু সময় ধরে চিন্তাভাবনা করেছিলাম। একসাথে ভাল সময় কাটানো খুব ভাল লাগল। আন্তরিক ধন্যবাদ।"],
    ["Bosnian","EMPTY","bs","empty",	"Kada gledam crveni zalazak sunca, osjećam se kao da se vraćam u svoje djetinjstvo, kada sam bezbrižno trčao i igrao se. Uzeo sam trenutak da se prisjetim svog djetinjstva. Bilo je divno provesti lijepo vrijeme zajedno. Iskreno sam zahvalan."],
    ["Bulgarian","EMPTY","bg","empty",	"Когато гледам червения залез, усещам, че се връщам в детството си, когато играех безгрижно. Взех момент да размисля за детството си. Беше чудесно да прекараме хубаво време заедно. Искрено благодаря."],
    ["Burmese","EMPTY","my","empty",	"နေဝင်သောအခါ အနီရောင်ဖြင့်ဆေးဖြန်းသော နေဝင်မြင်ကွင်းကို ကြည့်နေရသည့်အခါ၊ ကလေးဘဝကို ပြန်လည်သွားသလိုခံစားရသည်။ ကလေးဘဝကိုအလေးထားဖို့ တစ်ခဏယူခဲ့သည်။ အတူတူကောင်းမွန်သောအချိန်တွေဖြုန်းခဲ့တာက မိုက်လှခဲ့တယ်။ ကျေးဇူးတင်ပါတယ်။"],
    ["Catalan","EMPTY","ca","empty",	"Quan miro la posta de sol vermella, sento com si tornés a la meva infantesa, quan jugava despreocupadament. He pres un moment per reflexionar sobre la meva infantesa. Ha estat meravellós passar un bon moment junts. Estic sincerament agraït."],
    ["Central Khmer","EMPTY","km","empty",	"នៅពេលដែលខ្ញុំមើលទស្សនវប្បធម៌ក្រហមនៃថ្ងៃលិច ខ្ញុំមានអារម្មណ៍ដូចជាត្រលប់ទៅក្មេងវ័យនៅពេលដែលខ្ញុំលេងដោយសារស្មោះ។ ខ្ញុំបានយកពេលវេលាមួយសម្រាប់ពិចារណាពីអាយុក្មេងរបស់ខ្ញុំ។ វាគឺជាពេលវេលាប្រសើរណាស់ក្នុងការចំណាយពេលល្អជាមួយគ្នា។ ខ្ញុំសូមអរគុណពីចិត្ត។"],
    ["Chinese Simplified","EMPTY","zh_chs","empty",	"当我看到红色的晚霞时，我感觉自己仿佛回到了童年，那时我无忧无虑地玩耍。我花了一点时间回想我的童年。能一起度过美好的时光真的很棒。我由衷地感谢。"],
    ["Chinese Traditional","EMPTY","zh_cht","empty",	"當我看到紅色的晚霞時，我感覺自己仿佛回到了童年，那時我無憂無慮地玩耍。我花了一點時間回想我的童年。能一起度過美好的時光真的很棒。我由衷地感謝。"],
    ["Chuvash","EMPTY","cv","empty",	"Кăвăл сурăхĕн йĕрĕш хăйăн, пирĕн хурчăк çулĕм ятне ятлакан çуралăмлă. Пирĕн хурчăк çулăн хатирĕн эпĕн хатмаланăм. Вăлĕ хышнă шăмахкан вĕрент. Уйĕн паçăлăхта тăрăх."],
    ["Corsican","EMPTY","co","empty",	"Quandu guardu u tramontu rossu, mi sentu cum'è s'ellu mi torna à a mo zitellina, quandu ghjucava spenseratu. Aghju pigliatu un mumentu per riflette nantu à a mo zitellina. Era maravigliosu passà un bellu tempu inseme. Sò sinceramente ringraziatu."],
    ["Croatian","EMPTY","hr","empty",	"Kad gledam crveni zalazak sunca, osjećam se kao da se vraćam u svoje djetinjstvo, kada sam bezbrižno trčao i igrao se. Uzeo sam trenutak da se prisjetim svog djetinjstva. Bilo je divno provesti lijepo vrijeme zajedno. Iskreno sam zahvalan."],
    ["Czech","EMPTY","cs","empty",	"Když se dívám na červený západ slunce, připadám si, jako bych se vrátil do svého dětství, kdy jsem si bezstarostně hrál. Vzal jsem si chvíli na přemýšlení o svém dětství. Bylo úžasné strávit spolu dobrý čas. Upřímně děkuji."],
    ["Danish","EMPTY","da","empty",	"Når jeg ser på den røde solnedgang, føles det som om jeg rejser tilbage til min barndom, hvor jeg legede ubekymret. Jeg tog et øjeblik til at reflektere over min barndom. Det var vidunderligt at have en god tid sammen. Jeg er oprigtigt taknemmelig."],
    ["Dari","EMPTY","prs","empty",	"زمانی که من به غروب آفتاب سرخ نگاه میکنم، احساس میکنم که به دوران کودکیام بازگشتهام، زمانی که معصومانه بازی میکردم. لحظهای وقت گرفتم تا به دوران کودکیام فکر کنم. گذراندن وقت خوب با هم فوقالعاده بود. از صمیم قلب متشکرم."],
    ["Divehi","EMPTY","dv","empty",	"މުސައިގަން އަށްދެއްވި ކޮކުންނެތް ފާހަގަކުރަން އަހަރުންނަކައިފިނަމަކު އެންމެ ފެނުކައިކޮށްދޭނެކޮށްދޭނެކޮށްދޭނެކޮށްދޭނެކޮށްދޭނެކޮށްދޭނެކޮށްދޭނެކޮށްދޭނެކޮށްދޭނެކޮށްދޭނެކޮށްދޭނެ."],
    ["Dutch","EMPTY","nl","empty",	"Als ik naar de rode zonsondergang kijk, voelt het alsof ik terugga naar mijn kindertijd, toen ik onbezorgd speelde. Ik nam een moment om na te denken over mijn kindertijd. Het was geweldig om samen een goede tijd door te brengen. Ik ben oprecht dankbaar."],
    ["English","EMPTY","en","empty",	"When I look at the crimson sunset, it feels like I'm going back to my childhood, when I used to play innocently. I took a moment to reflect on my childhood. It was wonderful to spend a good time together. I am sincerely grateful."],
    ["Esperanto","EMPTY","eo","empty",	"Kiam mi rigardas la ruĝan sunsubiron, mi sentas, kvazaŭ mi revenas al mia infanaĝo, kiam mi ludis senkulpe. Mi prenis momenton por pripensi mian infanaĝon. Estis mirinde pasigi bonan tempon kune. Mi sincere dankas."],
    ["Estonian","EMPTY","et","empty",	"Kui vaatan punast päikeseloojangut, tunnen, justkui läheksin tagasi oma lapsepõlve, kui mängisin muretult. Võtsin hetke, et mõelda oma lapsepõlvele. Oli imeline veeta koos head aega. Olen siiralt tänulik."],
    ["Faroese","EMPTY","fo","empty",	"Tá eg hyggi at reyða sólsetrinum, kennist tað sum um eg fari aftur til mína barnatíð, tá eg spældi ósek. Eg tók eina løtu at hugsa um mína barnatíð. Tað var deiligt at hava ein góðan tíma saman. Eg eri veruliga takksamur."],
    ["Fijian","EMPTY","fj","empty",	"Ni'u rai ki na kavoro ni siga damudamu, e vaka e'u sa lesu tale ki na noqu gauna ni gone, ni'u dau qito sega ni lomaocaoca. Au a taura e dua na gauna me'u vakananuma na noqu gauna ni gone. Sa rui totoka na gauna vinaka eda a vakayagataka vata. Au sa vakavinavinaka vakabibi."],
    ["Finnish","EMPTY","fi","empty",	"Kun katson punaista auringonlaskua, tuntuu siltä kuin palaisin lapsuuteeni, jolloin leikin huolettomasti. Otin hetken miettiäkseni lapsuuttani. Oli ihanaa viettää yhdessä hyvää aikaa. Olen vilpittömästi kiitollinen."],
    ["French","EMPTY","fr","empty",	"En regardant le coucher de soleil rouge, j'ai l'impression de revenir à mon enfance, lorsque je jouais innocemment. J'ai pris un moment pour réfléchir à mon enfance. C'était merveilleux de passer un bon moment ensemble. Je vous suis sincèrement reconnaissant."],
    ["Galician","EMPTY","gl","empty",	"Cando miro o solpor vermello, sinto como se volvese á miña infancia, cando xogaba inocentemente. Tomei un momento para reflexionar sobre a miña infancia. Foi marabilloso pasar un bo momento xuntos. Estou sinceramente agradecido."],
    ["Georgian","EMPTY","ka","empty",	"როდესაც ვუყურებ წითელ მზის ჩასვლას, ვგრძნობ, თითქოს ვბრუნდები ჩემს ბავშვობაში, როდესაც უდანაშაულოდ ვთამაშობდი. მე გავატარე ცოტა დრო, რომ გავიხსენო ჩემი ბავშვობა. მშვენიერი იყო ერთად კარგი დროის გატარება. გულწრფელად მადლობელი ვარ."],
    ["German","EMPTY","de","empty",	"Wenn ich den roten Sonnenuntergang anschaue, fühle ich mich, als ob ich in meine Kindheit zurückkehre, als ich unbeschwert gespielt habe. Ich habe einen Moment innegehalten, um über meine Kindheit nachzudenken. Es war wunderbar, eine schöne Zeit zusammen zu verbringen. Ich bin aufrichtig dankbar."],
    ["Greek","EMPTY","el","empty",	"Όταν κοιτάζω το κόκκινο ηλιοβασίλεμα, αισθάνομαι σαν να επιστρέφω στην παιδική μου ηλικία, όταν έπαιζα ανέμελα. Πήρα μια στιγμή να αναλογιστώ την παιδική μου ηλικία. Ήταν υπέροχο να περνάμε καλά μαζί. Σας ευχαριστώ ειλικρινά."],
    ["Gujarati","EMPTY","gu","empty",	"જ્યારે હું લાલ રંગના સાંજના સુર્યાસ્તને જોઈશ ત્યારે એવું લાગે છે કે હું મારી બાળપણની દિવસોમાં પાછો ફરું છું, જ્યારે હું નિર્દોષ રીતે રમતો હતો. મેં મારી બાળપણ વિશે વિચાર કરવા માટે એક ક્ષણ લીધી. એકસાથે સારો સમય પસાર કરવો અદભૂત હતો. હું હ્રદયપૂર્વક આભારી છું."],
    ["Haitian","EMPTY","ht","empty",	"Lè mwen gade solèy kouche wouj la, mwen santi mwen tankou mwen retounen nan anfans mwen, lè mwen t ap jwe san pwoblèm. Mwen te pran yon moman pou reflechi sou anfans mwen. Li te bèl pase yon bon moman ansanm. Mwen sensèman rekonesan."],
    ["Hausa","EMPTY","ha","empty",	"Lokacin da na kalli ja da duhu na faɗuwar rana, na ji kamar na koma zamanin ƙuruciyata, lokacin da nake wasa cikin rashin damuwa. Na ɗauki lokaci kaɗan don tunanin ƙuruciyata. Ya kasance mai kyau sosai yin lokaci tare. Ina godiya sosai."],
    ["Hebrew","EMPTY","he","empty",	"כאשר אני מביט בשקיעה האדומה, אני מרגיש כאילו אני חוזר לילדותי, כשהייתי משחק בתמימות. לקחתי רגע לחשוב על ילדותי. היה נפלא לבלות זמן טוב ביחד. אני אסיר תודה מעומק הלב."],
    ["Hindi","EMPTY","hi","empty",	"जब मैं लाल रंग के सूर्यास्त को देखता हूं, तो ऐसा लगता है जैसे मैं अपने बचपन में लौट रहा हूं, जब मैं मासूमियत से खेलता था। मैंने अपने बचपन के बारे में सोचने के लिए एक पल लिया। साथ में अच्छा समय बिताना बहुत अच्छा था। मैं दिल से आभारी हूं।"],
    ["Hmong Daw","EMPTY","mww","empty",	"Thaum kuv saib lub hnub poob liab, kuv hnov zoo li kuv rov qab mus rau kuv thaum yau, thaum kuv tau ua si dawb huv. Kuv tau siv ib pliag los xav txog kuv thaum yau. Nws zoo kawg nkaus rau peb ua ke zoo siab. Kuv ua tsaug tiag tiag."],
    ["Hungarian","EMPTY","hu","empty",	"Amikor a vörös naplementére nézek, olyan érzésem van, mintha visszatérnék a gyermekkoromba, amikor gondtalanul játszottam. Vettem egy pillanatot, hogy átgondoljam a gyermekkoromat. Csodálatos volt együtt jó időt tölteni. Őszintén hálás vagyok."],
    ["Icelandic","EMPTY","is","empty",	"Þegar ég horfi á rauða sólarlagið, líður mér eins og ég sé að fara aftur til æsku minnar þegar ég lék mér saklaus. Ég tók augnablik til að íhuga æsku mína. Það var yndislegt að eyða góðum tíma saman. Ég er innilega þakklátur."],
    ["Igbo","EMPTY","ig","empty",	"Mgbe m na-ele anyanwụ mgbede ojii anya, ọ dị m ka m laghachiri n'afọ m dị nwaanyị, mgbe m na-akpọ ezigbo egwu. M were oge tụgharịa uche banyere nwata m. Ọ dị mma ịnọkọ ọnụ n'oge dị mma. Ekele m dịrị gị n’ụbọchị niile."],
    ["Indonesian","EMPTY","id","empty",	"Saat saya melihat matahari terbenam merah, rasanya seperti saya kembali ke masa kecil saya, ketika saya bermain tanpa beban. Saya mengambil waktu sejenak untuk merenungkan masa kecil saya. Sangat menyenangkan menghabiskan waktu yang baik bersama. Saya sungguh berterima kasih."],
    ["Inuktitut","EMPTY","iu","empty",	"ᐊᐅᓪᓚᖅᓯᒪᓂᖅ ᐊᐃᑦᑐᖅ ᓄᓇᓕᓯᖃᑎᒌᓐᓇᖅ, ᐅᑉᐱᒋᔭᕐᓂᕆᓂᕐᒥᒃ ᐃᑯᓕᐅᕈᑕᖅᑐᖅ. ᐅᖃᖅᓯᒪᒋᔭᖏᓐᓇᖅ ᐃᑯᓕᐅᕈᑕᖅᑐᖅ ᓂᕆᓕᓂᕐᒥᒃ. ᐃᓄᖅᓯᒪᒋᔭᖏᓐᓇᖅ ᑐᓂᒋᓪᓗᒋᑦ."],
    ["Irish","EMPTY","ga","empty",	"Nuair a fhéachaim ar an luí gréine dearg, mothaím mar a bheadh mé ag dul ar ais go dtí mo óige, nuair a bhí mé ag imirt go neamhchiontach. Thóg mé nóiméad chun machnamh a dhéanamh ar mo óige. Bhí sé iontach am maith a chaitheamh le chéile. Táim fíorbhuíoch."],
    ["Italian","EMPTY","it","empty",	"Quando guardo il tramonto rosso, mi sembra di tornare alla mia infanzia, quando giocavo spensierato. Ho preso un momento per riflettere sulla mia infanzia. È stato meraviglioso trascorrere un bel tempo insieme. Sono sinceramente grato."],
    ["Japanese","EMPTY","ja","empty",	"赤く染まった夕焼けを見ていると、無邪気に遊んでいた子供の頃に戻ったような気がします。昔の子供時代を思い出しながら、少しの間物思いにふけりました。一緒に良い時間を過ごせて本当に良かったです。心から感謝しています。"],
    ["Javanese","EMPTY","jv","empty",	"Nalika aku ndeleng srengenge surup abang, aku rumangsa kaya aku bali menyang masa cilikku nalika aku dolanan kanthi polos. Aku njupuk wektu saperangan kanggo mikir babagan masa cilikku. Iku apik banget kanggo nglampahi wektu sing apik bareng. Aku bener-bener matur nuwun."],
    ["Kannada","EMPTY","kn","empty",	"ರಕ್ತವರ್ಣದ ಸೂರ್ಯಾಸ್ತವನ್ನು ನೋಡುತ್ತಿದ್ದಾಗ, ನಾನು ನನ್ನ ಬಾಲ್ಯದ ದಿನಗಳಿಗೆ ಹಿಂತಿರುಗುತ್ತಿರುವಂತೆ ಅನುಭವಿಸುತ್ತೇನೆ, ನಾನು ನಿರ್ದೋಷವಾಗಿ ಆಟವಾಡುತ್ತಿದ್ದೆ. ನಾನು ನನ್ನ ಬಾಲ್ಯದ ಬಗ್ಗೆ ಆಲೋಚಿಸಲು ಕ್ಷಣವನ್ನು ತೆಗೆದೆ. ಒಟ್ಟಾಗಿ ಉತ್ತಮ ಸಮಯವನ್ನು ಕಳೆಯುವುದು ಅದ್ಭುತವಾಗಿದೆ. ನಾನು ಹೃತ್ಪೂರ್ವಕವಾಗಿ ಕೃತಜ್ಞನು."],
    ["Kazakh","EMPTY","kk","empty",	"Қызыл түске боялған кешкі күннің батуы көргенде, бала кезімдегі кінәсіз ойнап жүрген кездеріме қайтып оралғандай сезінемін. Мен бала кезім туралы ойлануға біраз уақыт бөлдім. Бірге жақсы уақыт өткізу тамаша болды. Шын жүректен алғыс айтамын."],
    ["Kinyarwanda","EMPTY","rw","empty",	"Iyo ndeba izuba rirenze ritukura, numva meze nk'uwagarutse mu bwana bwanjye, igihe nakinaga nta nkomyi. Nafashe akanya ko gutekereza ku bwana bwanjye. Byari byiza cyane kugira igihe cyiza turi kumwe. Ndabashimira mbikuye ku mutima."],
    ["Kirghiz","EMPTY","ky","empty",	"Кызыл түнкү күндүн батышын карап турганда, менин бала кезимде бейкапар ойноп жүргөн кезиме кайтып келгендей сезим пайда болот. Бала кезим жөнүндө ойлонууга убакыт бөлдүм. Биргелешип жакшы убакыт өткөрүү сонун болду. Чын жүрөктөн ыраазычылыгымды билдирем."],
    ["Korean","EMPTY","ko","empty",	"빨갛게 물든 저녁노을을 바라보고 있으면, 마치 지나간 어린시절 해맑게 뛰어놀던 그때로 돌아간 것처럼 느껴집니다. 옛날 어린시절을 회상하며 잠시 사색에 잠기게 되었습니다. 함께 좋은 시간을 보낼 수 있어서 너무 좋았습니다. 진심으로 감사드립니다."],
    ["Kurdish","EMPTY","ku","empty",	"کاتێک من بینم غروبە سوورەکان، وا دیتم وەکوو بەچووکەکەم کە بە پاکی یاری دەکردم. کاتێکەم گرتبوو بۆ بیرکردنەوەی سەردەمی منداڵیم. خۆش بووە کاتێکی باش لەگەڵ یەکتر بەسەر بەرین. من بەڕاستی سوپاسدارم."],
    ["Lao","EMPTY","lo","empty",	"ຂອບໃຈຫລາຍ ສໍາລັບການຄືນໄປໃນເວລາເວລາເດັກເຊົ່າ ເທື່ອຂ້ອຍຫຼິ້ນອຍ່າງບໍລິສຸດ. ມັນຂອງທີ່ວ່າຂອງດີທີ່ໄດ້ຢູ່ເຊັ່ນນັ້ນ."],
    ["Latin","EMPTY","la","empty",	"Cum solem rubrum occidentem specto, sentio quasi revertar in pueritiam meam, cum innocenter ludebam. Momentum cepi ut de pueritia mea cogitarem. Mirum fuit tempus bonum simul expendere. Ex animo gratias ago."],
    ["Latvian","EMPTY","lv","empty",	"Kad es skatos uz sarkano saulrietu, man šķiet, ka es atgriežos savā bērnībā, kad nevainīgi spēlējos. Es veltīju mirkli, lai pārdomātu savu bērnību. Bija brīnišķīgi pavadīt jauku laiku kopā. Esmu patiesi pateicīgs."],
    ["Lithuanian","EMPTY","lt","empty",	"Žiūrėdamas į raudoną saulėlydį, jaučiuosi tarsi grįžčiau į savo vaikystę, kai nekaltai žaidžiau. Paskyriau akimirką savo vaikystei prisiminti. Buvo nuostabu praleisti gerą laiką kartu. Esu nuoširdžiai dėkingas."],
    ["Luxembourgish","EMPTY","lb","empty",	"Wann ech op de rouden Sonnenënnergang kucken, fillt et sech un, wéi wann ech op meng Kandheet zeréckgoen, wéi ech onsuergfälteg gespillt hunn. Ech hunn eng Moment geholl fir iwwer meng Kandheet nozedenken. Et war wonnerbar eng gutt Zäit zesummen ze verbréngen. Ech si vu ganzem Häerz dankbar."],
    ["Macedonian","EMPTY","mk","empty",	"Кога го гледам црвениот зајдисонце, се чувствувам како да се враќам во моето детство, кога безгрижно играв. Зедов момент да размислам за моето детство. Прекрасно беше да поминеме добро време заедно. Искрено сум благодарен."],
    ["Malagasy","EMPTY","mg","empty",	"Rehefa mijery masoandro mena milentika aho, mahatsapa ho toy ny niverina tany amin'ny fahazazako aho, rehefa nilalao tamim-pahatsorana aho. Nandray fotoana kely aho hieritreretana ny fahazazako. Nahafinaritra ny nanao fotoana tsara niaraka. Misaotra betsaka aho."],
    ["Malay","EMPTY","ms","empty",	"Apabila saya melihat matahari terbenam merah, saya rasa seperti kembali ke zaman kanak-kanak saya, ketika saya bermain tanpa beban. Saya mengambil masa sejenak untuk merenung tentang zaman kanak-kanak saya. Sangat indah menghabiskan masa yang baik bersama. Saya sangat berterima kasih."],
    ["Malayalam","EMPTY","ml","empty",	"ചുവന്ന സൂര്യാസ്തമയത്തെ നോക്കുമ്പോൾ, ഞാൻ എന്റെ ബാല്യത്തിലേക്ക് തിരിച്ചുപോകുന്നതുപോലെ തോന്നുന്നു, ഞാൻ നിർദോഷമായി കളിച്ചപ്പോൾ. എന്റെ ബാല്യത്തെ കുറിച്ച് ചിന്തിക്കാൻ ഞാൻ ഒരു നിമിഷം എടുത്തു. നല്ല സമയം ചിലവഴിക്കാൻ കഴിഞ്ഞതിൽ അത്ഭുതമായി. ഞാൻ ഹൃദയപൂർവം നന്ദിയുണ്ട്."],
    ["Maltese","EMPTY","mt","empty",	"Meta nara x-xemx tħabbat ħamra, inħossni qisni qed nerġa’ lura għall-infanzja tiegħi, meta kont nilgħab bla ħsieb. Ħadt mument biex nirrifletti fuq l-infanzja tiegħi. Kien sabiħ li nqattgħu ħin tajjeb flimkien. Inħossni tassew grat."],
    ["Maori","EMPTY","mi","empty",	"I taku tirohanga ki te ra whiti whero, ka ahua hoki ahau ki taku tamarikitanga, i te wa i purea ai ahau i te takaro. I mau ahau i tetahi wa poto ki te whakaaro mo taku tamarikitanga. He mea whakamiharo te noho tahi me te pai o te wa. Kei te tino mihi ahau."],
    ["Marathi","EMPTY","mr","empty",	"जेव्हा मी लाल सूर्यास्ताकडे पाहतो, तेव्हा असं वाटतं की मी माझ्या बालपणात परत चाललो आहे, जेव्हा मी निरागसपणे खेळत होतो. मी माझ्या बालपणाविषयी विचार करण्यासाठी एक क्षण घेतला. एकत्र चांगला वेळ घालवणे अद्भुत होते. मी मनापासून कृतज्ञ आहे."],
    ["Mongolian","EMPTY","mn","empty",	"Улаан нар жаргахыг хараад, гэнэн цагаахан тоглож байсан бага насандаа эргэн очих мэт санагддаг. Би бага насаа бодоход цаг гаргасан. Хамтдаа сайхан цагийг өнгөрүүлэх нь гайхалтай байсан. Чин сэтгэлээсээ талархаж байна."],
    ["Nepali","EMPTY","ne","empty",	"रातो सूर्यास्तलाई हेर्दा मलाई लाग्छ कि म आफ्नो बाल्यकालमा फर्किएको छु, जब म निर्दोषसँग खेल्थेँ। मैले आफ्नो बाल्यकालको बारेमा सोच्न केही समय लिएँ। सँगै राम्रो समय बिताउन पाउँदा धेरै राम्रो लाग्यो। म हृदयपूर्वक आभारी छु।"],
    ["Norwegian Nynorsk","EMPTY","nn","empty",	"Når eg ser på den raude solnedgangen, kjennest det som om eg går tilbake til barndommen min, då eg leika bekymringslaust. Eg tok eit augeblikk for å reflektere over barndommen min. Det var vidunderleg å ha ei god tid saman. Eg er oppriktig takksam."],
    ["Norwegian","EMPTY","no","empty",	"Når jeg ser på den røde solnedgangen, føles det som om jeg går tilbake til barndommen min, da jeg lekte bekymringsløst. Jeg tok et øyeblikk for å reflektere over barndommen min. Det var fantastisk å ha en god tid sammen. Jeg er oppriktig takknemlig."],
    ["Odia","EMPTY","or","empty",	"ଯେତେବେଳେ ମୁଁ ଲାଲ ସୂର୍ଯ୍ୟାସ୍ତ ଦେଖେ, ମୁଁ ମୋର ଶିଶୁବଯ଼କ ଦିନଗୁଡିକରେ ପଛକୁ ଫେରିଯାଇଥିବା ଭାବଅନୁଭବ କରେ, ଯେତେବେଳେ ମୁଁ ନିର୍ଦୋଷତାର ସହିତ ଖେଳୁଥିଲି। ମୁଁ ମୋର ଶିଶୁବଯ଼କ ଠାରୁ ଏକ ମୁହୂର୍ତ୍ତ ଭାବିବାକୁ ନେଇଥିଲି। ଏକାସଂଗେ ଭଲ ସମୟ ବିତାଇବା ଅତି ଶୁଭକାମନା। ମୁଁ ହୃଦୟପୂର୍ବକ ଧନ୍ୟବାଦ।"],
    ["Pashto","EMPTY","ps","empty",	"کله چې زه د سره ماښام لمر ډوبیدو ته ګورم، داسې احساس کوم لکه د ماشومتوب دورې ته چې بیرته لاړ شم، کله چې زه بې ګناهانه لوبې کولم. ما د خپلې ماشومتوب د وختونو په اړه فکر کولو لپاره یوه شېبه ونیوله. دا ډیر ښه و چې یو ښه وخت سره تیر کړو. زه له زړه نه مننه کوم."],
    ["Persian","EMPTY","fa","empty",	"وقتی به غروب قرمز نگاه می‌کنم، احساس می‌کنم به کودکی‌ام برمی‌گردم، زمانی که معصومانه بازی می‌کردم. لحظه‌ای برای تأمل درباره کودکی‌ام اختصاص دادم. عالی بود که با هم وقت خوبی سپری کردیم. از صمیم قلب متشکرم."],
    ["Polish","EMPTY","pl","empty",	"Patrząc na czerwony zachód słońca, czuję, jakbym wracał do dzieciństwa, kiedy niewinnie się bawiłem. Zatrzymałem się na chwilę, aby pomyśleć o swoim dzieciństwie. Wspaniale było spędzić razem dobry czas. Jestem szczerze wdzięczny."],
    ["Portuguese","EMPTY","pt","empty",	"Ao olhar para o pôr do sol avermelhado, sinto como se estivesse voltando à minha infância, quando brincava inocentemente. Tirei um momento para refletir sobre minha infância. Foi maravilhoso passar bons momentos juntos. Sou sinceramente grato."],
    ["Punjabi","EMPTY","pa","empty",	"ਜਦੋਂ ਮੈਂ ਲਾਲ ਸੂਰਜ ਦੇ ਡੁੱਬਣ ਨੂੰ ਵੇਖਦਾ ਹਾਂ, ਤਾਂ ਮੈਨੂੰ ਮਹਿਸੂਸ ਹੁੰਦਾ ਹੈ ਜਿਵੇਂ ਮੈਂ ਆਪਣੇ ਬਚਪਨ ਵਿੱਚ ਵਾਪਸ ਜਾ ਰਿਹਾ ਹਾਂ, ਜਦੋਂ ਮੈਂ ਮਾਸੂਮੀ ਨਾਲ ਖੇਡਿਆ ਕਰਦਾ ਸੀ। ਮੈਂ ਆਪਣੇ ਬਚਪਨ ਬਾਰੇ ਸੋਚਣ ਲਈ ਇਕ ਪਲ ਲਿਆ। ਸਾਥ ਨਾਲ ਚੰਗਾ ਸਮਾਂ ਬਿਤਾਉਣਾ ਬਹੁਤ ਵਧੀਆ ਸੀ। ਮੈਂ ਦਿਲੋਂ ਧੰਨਵਾਦੀ ਹਾਂ।"],
    ["Queretaro Otomi","EMPTY","otq","empty",	"Närï mïdo ja nt’änthi hñäki, nki ra t’äjä yühni da ga go r’öribye nthäjä. Högi zë ki ho bädo ne nthäjä yühni. Räjü tuäjä räi’ra ho mi pe. Hño thäjä njöhjo."],
    ["Romanian","EMPTY","ro","empty",	"Privind apusul roșu, simt că mă întorc în copilăria mea, când mă jucam inocent. Am luat un moment să reflectez asupra copilăriei mele. A fost minunat să petrecem un timp bun împreună. Sunt sincer recunoscător."],
    ["Russian","EMPTY","ru","empty",	"Когда я смотрю на красный закат, мне кажется, будто я возвращаюсь в свое детство, когда я играл беззаботно. Я взял момент, чтобы задуматься о своем детстве. Было замечательно провести хорошее время вместе. Я искренне благодарен."],
    ["Samoan","EMPTY","sm","empty",	"A o'u va'ai i le goto ifo o le la mumu, ou te lagona e pei ua ou toe foi i lo'u laitiiti, pe a ou ta'alo e aunoa ma ni popolega. Sa ou ave se taimi e mafaufau ai i lo'u laitiiti. Sa manaia tele le fa'atasi ma le manuia."],
    ["Serbian","EMPTY","sr","empty",	"Kada gledam crveni zalazak sunca, osećam se kao da se vraćam u svoje detinjstvo, kada sam igrao bezbrižno. Uzeo sam trenutak da razmislim o svom detinjstvu. Bilo je divno provesti lepo vreme zajedno. Iskreno sam zahvalan."],
    ["Shona","EMPTY","sn","empty",	"Pandinoona kuvira kwezuva kutsvuku, ndinonzwa sekunge ndiri kudzokera muudiki hwangu, pandaitamba ndisina hanya. Ndakatora nguva diki yekufunga nezveudiki hwangu. Zvaifadza zvikuru kupedza nguva yakanaka pamwe chete. Ndiri kutenda zvikuru."],
    ["Sindhi","EMPTY","sd","empty",	"جڏهن مان ڳاڙهين شام جي غروب کي ڏسان ٿو، مون کي محسوس ٿئي ٿو ڄڻ ته مان پنهنجي ٻالڪپڻ جي ڏينهن ۾ واپس اچي رهيو آهيان، جڏهن مان معصوميت سان کيڏي رهيو هوس. مون پنهنجي ٻالڪپڻ بابت سوچڻ لاءِ هڪ پل ورتو. گڏجي سٺو وقت گذارڻ عظيم هو. مان دل سان شڪر گذار آهيان."],
    ["Sinhala","EMPTY","si","empty",	"රතු පාට ගිලුන සන්ධ්‍යා කාලය දැකන විට, මට මගේ ළමා කාලය වැටහෙන ආකාරයට හැඟේ, එවිට මම නිරදෝෂව ක්‍රීඩා කළෙමි. මම මගේ ළමා කාලය ගැන සිතීමට මොහොතක් ගත්තා. එකට හොඳ කාලයක් ගත කිරීම ඉතාමත් සුන්දරය. මම හෘදයාංගමව පරිශුද්ධ වාදනය කරන්නෙමි."],
    ["Slovak","EMPTY","sk","empty",	"Keď sa pozerám na červený západ slnka, cítim sa, akoby som sa vrátil do svojho detstva, keď som sa bezstarostne hral. Vzal som si chvíľu na zamyslenie nad svojím detstvom. Bolo to nádherné tráviť spolu dobrý čas. Som úprimne vďačný."],
    ["Slovenian","EMPTY","sl","empty",	"Ko gledam rdeči sončni zahod, se počutim, kot da bi se vrnil v svoje otroštvo, ko sem se brezskrbno igral. Vzel sem trenutek, da sem razmišljal o svojem otroštvu. Bilo je čudovito preživeti lep čas skupaj. Iskreno sem hvaležen."],
    ["Somali","EMPTY","so","empty",	"Markaan fiiriyo qorraxda gaduudan ee dhacaysa, waxaan dareemayaa sidii inaan ku noqonayo carruurnimadaydii, markaan ciyaar ku faraxsanaa. Waxaan qaatay waqti yar oo aan ka fikirayo carruurnimadayda. Way fiicnayd in aan waqti fiican wada qaadanno. Waxaan si daacad ah ugu mahadcelinayaa."],
    ["Spanish","EMPTY","es","empty",	"Al mirar la puesta de sol roja, siento como si volviera a mi infancia, cuando jugaba despreocupadamente. Me tomé un momento para reflexionar sobre mi infancia. Fue maravilloso pasar un buen rato juntos. Estoy sinceramente agradecido."],
    ["Sundanese","EMPTY","su","empty",	"Nalika kuring ningali panonpoé surup beureum, kuring ngarasa siga kuring balik deui ka budak leutik kuring, nalika kuring maén tanpa pikiran. Kuring nyandak waktos kanggo ngémutan budak leutik kuring. Éta endah pisan nyéépkeun waktos anu saé babarengan."],
    ["Swahili","EMPTY","sw","empty",	"Ninapoangalia machweo mekundu, najihisi kama narudi utotoni mwangu, nilipokuwa nikicheza bila hatia. Nilichukua muda wa kutafakari kuhusu utotoni mwangu. Ilikuwa ya kushangaza kutumia wakati mzuri pamoja. Ninashukuru kwa dhati."],
    ["Swedish","EMPTY","sv","empty",	"När jag tittar på den röda solnedgången känns det som om jag återvänder till min barndom, när jag lekte oskyldigt. Jag tog en stund för att reflektera över min barndom. Det var underbart att spendera en bra tid tillsammans. Jag är uppriktigt tacksam."],
    ["Tagalog","EMPTY","tl","empty",	"Kapag tinitingnan ko ang pulang paglubog ng araw, parang bumabalik ako sa aking kabataan kung saan ako'y masayang naglalaro. Naglaan ako ng sandali upang pag-isipan ang aking kabataan. Napakasarap ng magkasamang masayang oras. Lubos ang aking pasasalamat."],
    ["Tahitian","EMPTY","ty","empty",	"Ia hi'o vau i te mahana reva u'i, ua fana'o vau i te huru e te mea e, ua ho'i au i to'u tamari'i e mea ha'ape'ape ore e mea. Ua faufa'a taime vau e ha'amanao i to'u tamari'i. Ua rahi te oaoa i te fa'aoromai taime maitai na te tahi e te tahi. Mauruuru vau e to'u here e!"],
    ["Tajik","EMPTY","tg","empty",	"Вақте ки ман ғуруби сурхи офтобро тамошо мекунам, худро ба кӯдакии худ баргашта эҳсос мекунам, вақте ки ман бегуноҳ бозӣ мекардам. Як лаҳзаро барои фикр кардан дар бораи кӯдакии худ сарф кардам. Бениҳоят буд, ки якҷоя вақти хубе гузаронем. Ман самимона сипосгузорам."],
    ["Tamil","EMPTY","ta","empty",	"சிவப்பு நிறமான மாலை சூரியன் மறைவைக் காணும்போது, நான் என் சிறு வயதிற்குத் திரும்பிச் சென்றதைப் போல உணருகிறேன், அப்போது நான் மாசில்லாமல் விளையாடினேன். என் சிறு வயதைக் குறித்து சிந்திக்க ஒரு தருணம் எடுத்தேன். ஒன்றாக நல்ல நேரத்தை செலவழிப்பது அற்புதமாக இருந்தது. நான் மனமார்ந்த நன்றியை வெளிப்படுத்துகிறேன்."],
    ["Tatar","EMPTY","tt","empty",	"Кызыл кояш баешына караганда, үземне балачагыма, саф күңел белән уйнаган вакытларыма кайткан кебек хис итәм. Балачак турында уйланыр өчен вакыт алдым. Бергә яхшы вакыт үткәрү искиткеч булды. Чын күңелдән рәхмәтлемен."],
    ["Telugu","EMPTY","te","empty",	"ఎర్రటి సాయంకాలపు సూర్యాస్తమానాన్ని చూస్తున్నప్పుడు, నేను నా బాల్యంలోకి తిరిగి వెళ్లినట్లు అనిపిస్తుంది, నేను అమాయకంగా ఆడుతున్నప్పుడు. నా బాల్యం గురించి ఆలోచించడానికి నేను కాసేపు సమయం తీసుకున్నాను. కలిసి మంచి సమయాన్ని గడపడం అద్భుతంగా అనిపించింది. నేను హృదయపూర్వకంగా కృతజ్ఞతలు తెలుపుతున్నాను."],
    ["Thai","EMPTY","th","empty",	"เมื่อฉันมองพระอาทิตย์ตกสีแดง ฉันรู้สึกเหมือนกลับไปในวัยเด็กที่ฉันเคยเล่นอย่างไร้เดียงสา ฉันใช้เวลาสักครู่เพื่อคิดถึงวัยเด็กของฉัน มันวิเศษมากที่ได้ใช้เวลาที่ดีร่วมกัน ฉันขอขอบคุณจากใจจริง."],
    ["Tibetan","EMPTY","bo","empty",	"དམར་བའི་ཉི་མ་ནུབ་མོ་ལྟ་བའི་སྐབས་ང་ཚོའི་དུས་རབས་སྐྱིད་པོ་དུས་རབས་སྐྱིད་པོ་དུས་དུས་སྐྱིད་པོ་དུས་གཟིགས་པ་འདུག་ལོག་ནོར།"],
    ["Tigrinya","EMPTY","ti","empty",	"ኣብ እትረኽብ ንቁራሕ ቀይሕ መውሊድ ኣብ ዝኾነ ጊዜ፣ ሓድሽ ካብታ ዘሎ ዝግርም ወይ ዘይቀይሕ ስምዒት ስለ ሓግዚኡካብ ምስማዕ ናብ ትክክል ኣብ ዝኾነ ጊዜ ኣብ ምምላእ ኣሎኹ። ዝብልጽዕ ሰናይ ጊዜ ኣብ ምሕላፍን ንስኹም ኣብ ኩብድን ነብስ ኣእትይኩም።"],
    ["Tongan","EMPTY","to","empty",	"ʻI he taimi ʻoku ou vakai ki he māsiva ʻaho kulokula, ʻoku ou ongoʻi hangē ko ʻeku foki ki heʻeku taimi ʻeneʻeneʻaki ʻeku taʻanga taʻetauhi. Naʻaku tānaki ha miniti ke fakakaukau ki heʻeku taimi ʻo e ʻeneʻene. Ne maʻolunga ke fakatau tokoni taimi lelei fakataha. ʻOku ou fakafetaʻi ʻaki ʻeku loto ʻofaʻanga."],
    ["Turkish","EMPTY","tr","empty",	"Kızıl gün batımına baktığımda, kendimi çocukluk yıllarıma, masumca oynadığım günlere geri dönmüş gibi hissediyorum. Çocukluğum hakkında düşünmek için bir an durdum. Birlikte güzel zaman geçirmek harikaydı. İçtenlikle teşekkür ederim."],
    ["Turkmen","EMPTY","tk","empty",	"Gyzyl güneşin batşyna seredip, özüm çagalyk döwrüme, masumlyk bilen oýnan günlerime gaýdyp barýan ýaly duýýaryn. Çagalyk döwrüm hakda oýlanmak üçin biraz wagt aldym. Bilelikde gowy wagt geçirmek ajaýypdy. Çyndan minnetdarlyk bildirýärin."],
    ["Ukrainian","EMPTY","uk","empty",	"Дивлячись на червоний захід сонця, я відчуваю, ніби повертаюся в своє дитинство, коли я безтурботно грався. Я взяв мить, щоб подумати про своє дитинство. Було чудово провести гарний час разом. Щиро дякую."],
    ["Upper Sorbian","EMPTY","hsb","empty",	"Hdyž sej wobhladuju čerwjenu słóncnu sadźu, mam pocyć, jako bych so wróćił do swojeho dźěćiństwa, hdyž sym njewina hrajeł. Sym sej chwilu wzał, zo by sym swoje dźěćiństwo spomjatkował. Było rědna zawěrzać dobry čas zjednocenjo. Zdaśně dźakujom."],
    ["Urdu","EMPTY","ur","empty",	"جب میں سرخ سورج غروب کو دیکھتا ہوں، تو ایسا محسوس ہوتا ہے جیسے میں اپنے بچپن میں واپس جا رہا ہوں، جب میں معصومیت کے ساتھ کھیلتا تھا۔ میں نے اپنے بچپن کے بارے میں سوچنے کے لیے ایک لمحہ لیا۔ ساتھ وقت گزارنا شاندار تھا۔ میں دل سے شکر گزار ہوں۔"],
    ["Uyghur","EMPTY","ug","empty",	"قىزىل شام پەسىلگە قارىغاندا، بالىلىق دەۋرىمگە قايتقاندەك ھېس قىلىمەن، ئۇ چاغلاردا گۇناھسىز ئوينايتتىم. بالىلىق دەۋرىمنى ئەسلەش ئۈچۈن بىر ئانلىق ۋاقىت ئالدىم. بىرلىكتە ياخشى ۋاقىت ئۆتكۈزۈش غايەت ياخشى بولدى. مەن ھەقىقى چىن كۆڭلىمدىن رەھمەت ئېيتىمەن."],
    ["Uzbek","EMPTY","uz","empty",	"Qizil quyosh botishini tomosha qilayotganimda, o‘zimni go‘daklik davrimga, begunoh o‘ynab yurgan kunlarimga qaytganimdek his qilaman. Bolalik davrimni o‘ylash uchun biroz vaqt ajratdim. Birgalikda yaxshi vaqt o‘tkazish ajoyib edi. Chin yurakdan minnatdorman."],
    ["Vietnamese","EMPTY","vi","empty",	"Khi tôi nhìn hoàng hôn đỏ thẫm, tôi cảm thấy như mình đang quay trở lại thời thơ ấu, khi tôi vô tư chơi đùa. Tôi đã dành một chút thời gian để suy ngẫm về tuổi thơ của mình. Thật tuyệt vời khi dành thời gian tuyệt vời cùng nhau. Tôi chân thành cảm ơn."],
    ["Welsh","EMPTY","cy","empty",	"Pan fyddaf yn edrych ar fachlud haul coch, rwy'n teimlo fel petawn yn dychwelyd i fy mhlentyndod pan oeddwn yn chwarae'n ddiniwed. Cymerais eiliad i fyfyrio am fy mhlentyndod. Roedd yn hyfryd cael treulio amser da gyda'n gilydd. Rwy'n wirioneddol ddiolchgar."],
    ["Xhosa","EMPTY","xh","empty",	"Xa ndibukele ukutshona kwelanga okubomvu, ndiziva ngathi ndibuyele ebuntwaneni bam, xa ndandidlala ngaphandle kokuxhalaba. Ndithathe umzuzu wokucinga ngobuntwana bam. Bekumnandi kakhulu ukuchitha ixesha elihle kunye. Ndiyabulela ngokunzulu."],
    ["Yiddish","EMPTY","yi","empty",	"ווען איך קוק אויף דעם רויטן זונ -אונטערגאַנג, פילט עס ווי איך גיי צוריק צו מיין קינדשאַפט, ווען איך האָב שפּילט אומשולדיג. איך האָב גענומען אַ מאָמענט צו פאַרטראַכטן וועגן מיין קינדשאַפט. עס איז געווען אַ מאַרוויינדיקער צייט צוזאַמען. איך בין טאַקע דאַנקבאַר."],
    ["Yoruba","EMPTY","yo","empty",	"Nigbati mo wo oorun pupa ti n ṣubú, o dabi ẹnipe mo pada si igba ewe mi, nigbati mo n ṣere laini ẹbi. Mo gba iṣẹju diẹ lati ronu nipa igba ewe mi. O jẹ iyanu lati lo akoko ti o dara pọ. Mo dupẹ lọwọ ọkan mi gaan."],
    ["Yucatec Maya","EMPTY","yua","empty",	"Ka táan in wáantik le k'áak'náachil k'áak'náal, tuukultik u chíinil in chichan paal k'i'ichkelem, ka táan in wayéetal bey táan in ma'alob sa'amij. Teech ma'alob ba'axil takinil in yaakunaj."],
    ["Zulu","EMPTY","zu","empty",	"Lapho ngibuka ukushona kwelanga okubomvu, ngizizwa sengathi ngibuyela ebuntwaneni bami, lapho ngidlala ngaphandle kokukhathazeka. Ngithathe isikhashana ukuzindla ngobuntwana bami. Kwakumnandi kakhulu ukuchitha isikhathi esihle ndawonye. Ngiyabonga ngobuqotho."],
]


__test_sample_arr2 = [
    ["Bosnian","EMPTY","bs","empty",	"Kada gledam crveni zalazak sunca, osjećam se kao da se vraćam u svoje djetinjstvo, kada sam bezbrižno trčao i igrao se. Uzeo sam trenutak da se prisjetim svog djetinjstva. Bilo je divno provesti lijepo vrijeme zajedno. Iskreno sam zahvalan."],
    ["Dari","EMPTY","prs","empty",	"زمانی که من به غروب آفتاب سرخ نگاه میکنم، احساس میکنم که به دوران کودکیام بازگشتهام، زمانی که معصومانه بازی میکردم. لحظهای وقت گرفتم تا به دوران کودکیام فکر کنم. گذراندن وقت خوب با هم فوقالعاده بود. از صمیم قلب متشکرم."],
    ["Indonesian","EMPTY","id","empty",	"Saat saya melihat matahari terbenam merah, rasanya seperti saya kembali ke masa kecil saya, ketika saya bermain tanpa beban. Saya mengambil waktu sejenak untuk merenungkan masa kecil saya. Sangat menyenangkan menghabiskan waktu yang baik bersama. Saya sungguh berterima kasih."],
    ["Javanese","EMPTY","jv","empty",	"Nalika aku ndeleng srengenge surup abang, aku rumangsa kaya aku bali menyang masa cilikku nalika aku dolanan kanthi polos. Aku njupuk wektu saperangan kanggo mikir babagan masa cilikku. Iku apik banget kanggo nglampahi wektu sing apik bareng. Aku bener-bener matur nuwun."],
    ["Xhosa","EMPTY","xh","empty",	"Xa ndibukele ukutshona kwelanga okubomvu, ndiziva ngathi ndibuyele ebuntwaneni bam, xa ndandidlala ngaphandle kokuxhalaba. Ndithathe umzuzu wokucinga ngobuntwana bam. Bekumnandi kakhulu ukuchitha ixesha elihle kunye. Ndiyabulela ngokunzulu."],
]

def detect_language(text: str) -> dict:
    """Detects the text's language."""
    translate_client = get_client_ai_language_detection_ggc()

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.detect_language(text)

    return result

if __name__ == '__main__':
    try:
        documents_failed = []
        __idx = 0
        ___tmp_idx = 0
        for item_inner in __test_sample_arr:
            print()
            print(f'item_inner[{__idx}] BEFORE:{item_inner}')
            ___response = detect_language(item_inner[4])
            tmp_res_langcode = ___response["language"]
            tmp_res_confidence = ___response["confidence"]
            print(f'tmp_res_langcode: {tmp_res_langcode}')
            print(f'tmp_res_confidence: {tmp_res_confidence}')

            if is_azure_support_langcode(tmp_res_langcode):
                print(f"♥♥♥ iso6391_name[{tmp_res_langcode}] is SUPPORT♥♥♥")
            else:
                print(f"!!! OMG! iso6391_name[{tmp_res_langcode}] is not supported!!!{item_inner}")

            __test_sample_arr[__idx][3] = tmp_res_langcode
            if __test_sample_arr[__idx][2] == __test_sample_arr[__idx][3]:
                pass
            else:
                documents_failed.append(__test_sample_arr[__idx])
                pass

            __idx += 1

            ___tmp_idx += 1
            if ___tmp_idx >= 1:
                break

        print(f"------------- raw ALL({len(__test_sample_arr)}) ----------------")
        # for item_inner in __test_sample_arr:
        #     print(item_inner)

        print(f"-------------- FAILED({len(documents_failed)})---------------")
        for item_inner in documents_failed:
            print(item_inner)

    except Exception as err:
        print("Encountered exception1. {}".format(err))
        print(f"{traceback.print_exc()}")

