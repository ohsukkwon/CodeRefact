# -*- coding: utf-8 -*-

import azure.cognitiveservices.speech as speechsdk
from pydub import AudioSegment

from MyKeyStore import *
from config.engine_config import *

# https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts#supported-languages
ASR_MSA_SUPPORT_LANGUAGES = [
    "af-ZA-AdriNeural",	                    	#000
    "af-ZA-WillemNeural",	                    #001
    "am-ET-MekdesNeural",	                    #002
    "am-ET-AmehaNeural",	                    #003
    "ar-AE-FatimaNeural",	                    #004
    "ar-AE-HamdanNeural",	                    #005
    "ar-BH-LailaNeural",	                    #006
    "ar-BH-AliNeural",	                    	#007
    "ar-DZ-AminaNeural",	                    #008
    "ar-DZ-IsmaelNeural",	                    #009
    "ar-EG-SalmaNeural",	                    #010
    "ar-EG-ShakirNeural",	                    #011
    "ar-IQ-RanaNeural",	                    	#012
    "ar-IQ-BasselNeural",	                    #013
    "ar-JO-SanaNeural",	                    	#014
    "ar-JO-TaimNeural",	                    	#015
    "ar-KW-NouraNeural",	                    #016
    "ar-KW-FahedNeural",	                    #017
    "ar-LB-LaylaNeural",	                    #018
    "ar-LB-RamiNeural",	                    	#019
    "ar-LY-ImanNeural",	                    	#020
    "ar-LY-OmarNeural",	                    	#021
    "ar-MA-MounaNeural",	                    #022
    "ar-MA-JamalNeural",	                    #023
    "ar-OM-AyshaNeural",	                    #024
    "ar-OM-AbdullahNeural",	                    #025
    "ar-QA-AmalNeural",	                    	#026
    "ar-QA-MoazNeural",	                    	#027
    "ar-SA-ZariyahNeural",	                    #028
    "ar-SA-HamedNeural",	                    #029
    "ar-SY-AmanyNeural",	                    #030
    "ar-SY-LaithNeural",	                    #031
    "ar-TN-ReemNeural",	                    	#032
    "ar-TN-HediNeural",	                    	#033
    "ar-YE-MaryamNeural",	                    #034
    "ar-YE-SalehNeural",	                    #035
    "as-IN-YashicaNeural",	                    #036
    "as-IN-PriyomNeural",	                    #037
    "az-AZ-BanuNeural",	                    	#038
    "az-AZ-BabekNeural",	                    #039
    "bg-BG-KalinaNeural",	                    #040
    "bg-BG-BorislavNeural",	                    #041
    "bn-BD-NabanitaNeural",	                    #042
    "bn-BD-PradeepNeural",	                    #043
    "bn-IN-TanishaaNeural",	                    #044
    "bn-IN-BashkarNeural",	                    #045
    "bs-BA-VesnaNeural",	                    #046
    "bs-BA-GoranNeural",	                    #047
    "ca-ES-JoanaNeural",	                    #048
    "ca-ES-EnricNeural",	                    #049
    "ca-ES-AlbaNeural",	                    	#050
    "cs-CZ-VlastaNeural",	                    #051
    "cs-CZ-AntoninNeural",	                    #052
    "cy-GB-NiaNeural",	                    	#053
    "cy-GB-AledNeural",	                    	#054
    "da-DK-ChristelNeural",	                    #055
    "da-DK-JeppeNeural",	                    #056
    "de-AT-IngridNeural",	                    #057
    "de-AT-JonasNeural",	                    #058
    "de-CH-LeniNeural",	                    	#059
    "de-CH-JanNeural",	                    	#060
    "de-DE-KatjaNeural",	                    #061
    "de-DE-ConradNeural",	                    #062
    "de-DE-AmalaNeural",	                    #063
    "de-DE-BerndNeural",	                    #064
    "de-DE-ChristophNeural",	                #065
    "de-DE-ElkeNeural",	                    	#066
    "de-DE-FlorianMultilingualNeural",	        #067
    "de-DE-GiselaNeural",	                    #068
    "de-DE-KasperNeural",	                    #069
    "de-DE-KillianNeural",	                    #070
    "de-DE-KlarissaNeural",	                    #071
    "de-DE-KlausNeural",	                    #072
    "de-DE-LouisaNeural",	                    #073
    "de-DE-MajaNeural",	                    	#074
    "de-DE-RalfNeural",	                    	#075
    "de-DE-SeraphinaMultilingualNeural",	    #076
    "de-DE-TanjaNeural",	                    #077
    "el-GR-AthinaNeural",	                    #078
    "el-GR-NestorasNeural",	                    #079
    "en-AU-NatashaNeural",	                    #080
    "en-AU-WilliamNeural",	                    #081
    "en-AU-AnnetteNeural",	                    #082
    "en-AU-CarlyNeural",	                    #083
    "en-AU-DarrenNeural",	                    #084
    "en-AU-DuncanNeural",	                    #085
    "en-AU-ElsieNeural",	                    #086
    "en-AU-FreyaNeural",	                    #087
    "en-AU-JoanneNeural",	                    #088
    "en-AU-KenNeural",	                    	#089
    "en-AU-KimNeural",	                    	#090
    "en-AU-NeilNeural",	                    	#091
    "en-AU-TimNeural",	                    	#092
    "en-AU-TinaNeural",	                    	#093
    "en-CA-ClaraNeural",	                    #094
    "en-CA-LiamNeural",	                    	#095
    "en-GB-SoniaNeural",	                    #096
    "en-GB-RyanNeural",	                    	#097
    "en-GB-LibbyNeural",	                    #098
    "en-GB-AbbiNeural",	                    	#099
    "en-GB-AlfieNeural",	                    #100
    "en-GB-BellaNeural",	                    #101
    "en-GB-ElliotNeural",	                    #102
    "en-GB-EthanNeural",	                    #103
    "en-GB-HollieNeural",	                    #104
    "en-GB-MaisieNeural",	                    #105
    "en-GB-NoahNeural",	                    	#106
    "en-GB-OliverNeural",	                    #107
    "en-GB-OliviaNeural",	                    #108
    "en-GB-ThomasNeural",	                    #109
    "en-GB-AdaMultilingualNeural",	            #110
    "en-GB-OllieMultilingualNeural",	        #111
    "en-HK-YanNeural",	                    	#112
    "en-HK-SamNeural",	                    	#113
    "en-IE-EmilyNeural",	                    #114
    "en-IE-ConnorNeural",	                    #115
    "en-IN-AaravNeural",	                    #116
    "en-IN-AashiNeural",	                    #117
    "en-IN-AnanyaNeural",	                    #118
    "en-IN-KavyaNeural",	                    #119
    "en-IN-KunalNeural",	                    #120
    "en-IN-NeerjaNeural",	                    #121
    "en-IN-PrabhatNeural",	                    #122
    "en-IN-RehaanNeural",	                    #123
    "en-KE-AsiliaNeural",	                    #124
    "en-KE-ChilembaNeural",	                    #125
    "en-NG-EzinneNeural",	                    #126
    "en-NG-AbeoNeural",	                    	#127
    "en-NZ-MollyNeural",	                    #128
    "en-NZ-MitchellNeural",	                    #129
    "en-PH-RosaNeural",	                    	#130
    "en-PH-JamesNeural",	                    #131
    "en-SG-LunaNeural",	                    	#132
    "en-SG-WayneNeural",	                    #133
    "en-TZ-ImaniNeural",	                    #134
    "en-TZ-ElimuNeural",	                    #135
    "en-US-AvaMultilingualNeural",	            #136
    "en-US-AndrewMultilingualNeural",	        #137
    "en-US-EmmaMultilingualNeural",	            #138
    "en-US-BrianMultilingualNeural",	        #139
    "en-US-AvaNeural",	                    	#140
    "en-US-AndrewNeural",	                    #141
    "en-US-EmmaNeural",	                    	#142
    "en-US-BrianNeural",	                    #143
    "en-US-JennyNeural",	                    #144
    "en-US-GuyNeural",	                    	#145
    "en-US-AriaNeural",	                    	#146
    "en-US-DavisNeural",	                    #147
    "en-US-JaneNeural",	                    	#148
    "en-US-JasonNeural",	                    #149
    "en-US-SaraNeural",	                    	#150
    "en-US-TonyNeural",	                    	#151
    "en-US-NancyNeural",	                    #152
    "en-US-AmberNeural",	                    #153
    "en-US-AnaNeural",	                    	#154
    "en-US-AshleyNeural",	                    #155
    "en-US-BrandonNeural",	                    #156
    "en-US-ChristopherNeural",	                #157
    "en-US-CoraNeural",	                    	#158
    "en-US-ElizabethNeural",	                #159
    "en-US-EricNeural",	                    	#160
    "en-US-JacobNeural",	                    #161
    "en-US-JennyMultilingualNeural",	        #162
    "en-US-MichelleNeural",	                    #163
    "en-US-MonicaNeural",	                    #164
    "en-US-RogerNeural",	                    #165
    "en-US-RyanMultilingualNeural",	            #166
    "en-US-SteffanNeural",	                    #167
    "en-US-AdamMultilingualNeural",	            #168
    "en-US-AIGenerate1Neural",	                #169
    "en-US-AIGenerate2Neural1",	                #170
    "en-US-AlloyTurboMultilingualNeural",	    #171
    "en-US-AmandaMultilingualNeural",	        #172
    "en-US-BlueNeural1",	                    #173
    "en-US-BrandonMultilingualNeural",	        #174
    "en-US-ChristopherMultilingualNeural",	    #175
    "en-US-CoraMultilingualNeural",	            #176
    "en-US-DavisMultilingualNeural",	        #177
    "en-US-DerekMultilingualNeural",	        #178
    "en-US-DustinMultilingualNeural",	        #179
    "en-US-EchoTurboMultilingualNeural",	    #180
    "en-US-EvelynMultilingualNeural",	        #181
    "en-US-FableTurboMultilingualNeural",	    #182
    "en-US-KaiNeural",	                    	#183
    "en-US-LewisMultilingualNeural",	        #184
    "en-US-LolaMultilingualNeural",	            #185
    "en-US-LunaNeural1",	                    #186
    "en-US-NancyMultilingualNeural",	        #187
    "en-US-NovaTurboMultilingualNeural",	    #188
    "en-US-OnyxTurboMultilingualNeural",	    #189
    "en-US-PhoebeMultilingualNeural",	        #190
    "en-US-SamuelMultilingualNeural",	        #191
    "en-US-SerenaMultilingualNeural",	        #192
    "en-US-ShimmerTurboMultilingualNeural",	    #193
    "en-US-SteffanMultilingualNeural",	        #194
    "en-US-AlloyMultilingualNeural",	        #195
    "en-US-EchoMultilingualNeural",	            #196
    "en-US-FableMultilingualNeural(Neutral)",	#197
    "en-US-OnyxMultilingualNeural",	            #198
    "en-US-NovaMultilingualNeural",	            #199
    "en-US-ShimmerMultilingualNeural",	        #200
    "en-US-AlloyMultilingualNeuralHD",	        #201
    "en-US-EchoMultilingualNeuralHD",	        #202
    "en-US-FableMultilingualNeuralHD(Neutral)",	#203
    "en-US-OnyxMultilingualNeuralHD",	        #204
    "en-US-NovaMultilingualNeuralHD",	        #205
    "en-US-ShimmerMultilingualNeuralHD",	    #206
    "en-ZA-LeahNeural",	                    	#207
    "en-ZA-LukeNeural",	                    	#208
    "es-AR-ElenaNeural",	                    #209
    "es-AR-TomasNeural",	                    #210
    "es-BO-SofiaNeural",	                    #211
    "es-BO-MarceloNeural",	                    #212
    "es-CL-CatalinaNeural",	                    #213
    "es-CL-LorenzoNeural",	                    #214
    "es-CO-SalomeNeural",	                    #215
    "es-CO-GonzaloNeural",	                    #216
    "es-CR-MariaNeural",	                    #217
    "es-CR-JuanNeural",	                    	#218
    "es-CU-BelkysNeural",	                    #219
    "es-CU-ManuelNeural",	                    #220
    "es-DO-RamonaNeural",	                    #221
    "es-DO-EmilioNeural",	                    #222
    "es-EC-AndreaNeural",	                    #223
    "es-EC-LuisNeural",	                    	#224
    "es-ES-ElviraNeural",	                    #225
    "es-ES-AlvaroNeural",	                    #226
    "es-ES-AbrilNeural",	                    #227
    "es-ES-ArnauNeural",	                    #228
    "es-ES-DarioNeural",	                    #229
    "es-ES-EliasNeural",	                    #230
    "es-ES-EstrellaNeural",	                    #231
    "es-ES-IreneNeural",	                    #232
    "es-ES-LaiaNeural",	                    	#233
    "es-ES-LiaNeural",	                    	#234
    "es-ES-NilNeural",	                    	#235
    "es-ES-SaulNeural",	                    	#236
    "es-ES-TeoNeural",	                    	#237
    "es-ES-TrianaNeural",	                    #238
    "es-ES-VeraNeural",	                    	#239
    "es-ES-XimenaNeural",	                    #240
    "es-ES-ArabellaMultilingualNeural",	        #241
    "es-ES-IsidoraMultilingualNeural",	        #242
    "es-ES-TristanMultilingualNeural",	        #243
    "es-ES-XimenaMultilingualNeural",	        #244
    "es-GQ-TeresaNeural",	                    #245
    "es-GQ-JavierNeural",	                    #246
    "es-GT-MartaNeural",	                    #247
    "es-GT-AndresNeural",	                    #248
    "es-HN-KarlaNeural",	                    #249
    "es-HN-CarlosNeural",	                    #250
    "es-MX-DaliaNeural",	                    #251
    "es-MX-JorgeNeural",	                    #252
    "es-MX-BeatrizNeural",	                    #253
    "es-MX-CandelaNeural",	                    #254
    "es-MX-CarlotaNeural",	                    #255
    "es-MX-CecilioNeural",	                    #256
    "es-MX-GerardoNeural",	                    #257
    "es-MX-LarissaNeural",	                    #258
    "es-MX-LibertoNeural",	                    #259
    "es-MX-LucianoNeural",	                    #260
    "es-MX-MarinaNeural",	                    #261
    "es-MX-NuriaNeural",	                    #262
    "es-MX-PelayoNeural",	                    #263
    "es-MX-RenataNeural",	                    #264
    "es-MX-YagoNeural",	                    	#265
    "es-NI-YolandaNeural",	                    #266
    "es-NI-FedericoNeural",	                    #267
    "es-PA-MargaritaNeural",	                #268
    "es-PA-RobertoNeural",	                    #269
    "es-PE-CamilaNeural",	                    #270
    "es-PE-AlexNeural",	                    	#271
    "es-PR-KarinaNeural",	                    #272
    "es-PR-VictorNeural",	                    #273
    "es-PY-TaniaNeural",	                    #274
    "es-PY-MarioNeural",	                    #275
    "es-SV-LorenaNeural",	                    #276
    "es-SV-RodrigoNeural",	                    #277
    "es-US-PalomaNeural",	                    #278
    "es-US-AlonsoNeural",	                    #279
    "es-UY-ValentinaNeural",	                #280
    "es-UY-MateoNeural",	                    #281
    "es-VE-PaolaNeural",	                    #282
    "es-VE-SebastianNeural",	                #283
    "et-EE-AnuNeural",	                    	#284
    "et-EE-KertNeural",	                    	#285
    "eu-ES-AinhoaNeural",	                    #286
    "eu-ES-AnderNeural",	                    #287
    "fa-IR-DilaraNeural",	                    #288
    "fa-IR-FaridNeural",	                    #289
    "fi-FI-SelmaNeural",	                    #290
    "fi-FI-HarriNeural",	                    #291
    "fi-FI-NooraNeural",	                    #292
    "fil-PH-BlessicaNeural",	                #293
    "fil-PH-AngeloNeural",	                    #294
    "fr-BE-CharlineNeural",	                    #295
    "fr-BE-GerardNeural",	                    #296
    "fr-CA-SylvieNeural",	                    #297
    "fr-CA-JeanNeural",	                    	#298
    "fr-CA-AntoineNeural",	                    #299
    "fr-CA-ThierryNeural",	                    #300
    "fr-CH-ArianeNeural",	                    #301
    "fr-CH-FabriceNeural",	                    #302
    "fr-FR-DeniseNeural",	                    #303
    "fr-FR-HenriNeural",	                    #304
    "fr-FR-AlainNeural",	                    #305
    "fr-FR-BrigitteNeural",	                    #306
    "fr-FR-CelesteNeural",	                    #307
    "fr-FR-ClaudeNeural",	                    #308
    "fr-FR-CoralieNeural",	                    #309
    "fr-FR-EloiseNeural",	                    #310
    "fr-FR-JacquelineNeural",	                #311
    "fr-FR-JeromeNeural",	                    #312
    "fr-FR-JosephineNeural",	                #313
    "fr-FR-MauriceNeural",	                    #314
    "fr-FR-RemyMultilingualNeural",	            #315
    "fr-FR-VivienneMultilingualNeural",	        #316
    "fr-FR-YvesNeural",	                    	#317
    "fr-FR-YvetteNeural",	                    #318
    "fr-FR-LucienMultilingualNeural",	        #319
    "ga-IE-OrlaNeural",	                    	#320
    "ga-IE-ColmNeural",	                    	#321
    "gl-ES-SabelaNeural",	                    #322
    "gl-ES-RoiNeural",	                    	#323
    "gu-IN-DhwaniNeural",	                    #324
    "gu-IN-NiranjanNeural",	                    #325
    "he-IL-HilaNeural",	                    	#326
    "he-IL-AvriNeural",	                    	#327
    "hi-IN-AaravNeural",	                    #328
    "hi-IN-AnanyaNeural",	                    #329
    "hi-IN-KavyaNeural",	                    #330
    "hi-IN-KunalNeural",	                    #331
    "hi-IN-RehaanNeural",	                    #332
    "hi-IN-SwaraNeural",	                    #333
    "hi-IN-MadhurNeural",	                    #334
    "hr-HR-GabrijelaNeural",	                #335
    "hr-HR-SreckoNeural",	                    #336
    "hu-HU-NoemiNeural",	                    #337
    "hu-HU-TamasNeural",	                    #338
    "hy-AM-AnahitNeural",	                    #339
    "hy-AM-HaykNeural",	                    	#340
    "id-ID-GadisNeural",	                    #341
    "id-ID-ArdiNeural",	                    	#342
    "is-IS-GudrunNeural",	                    #343
    "is-IS-GunnarNeural",	                    #344
    "it-IT-ElsaNeural",	                    	#345
    "it-IT-IsabellaNeural",	                    #346
    "it-IT-DiegoNeural",	                    #347
    "it-IT-BenignoNeural",	                    #348
    "it-IT-CalimeroNeural",	                    #349
    "it-IT-CataldoNeural",	                    #350
    "it-IT-FabiolaNeural",	                    #351
    "it-IT-FiammaNeural",	                    #352
    "it-IT-GianniNeural",	                    #353
    "it-IT-GiuseppeNeural",	                    #354
    "it-IT-ImeldaNeural",	                    #355
    "it-IT-IrmaNeural",	                    	#356
    "it-IT-LisandroNeural",	                    #357
    "it-IT-PalmiraNeural",	                    #358
    "it-IT-PierinaNeural",	                    #359
    "it-IT-RinaldoNeural",	                    #360
    "it-IT-AlessioMultilingualNeural",	        #361
    "it-IT-GiuseppeMultilingualNeural",	        #362
    "it-IT-IsabellaMultilingualNeural",	        #363
    "it-IT-MarcelloMultilingualNeural",	        #364
    "iu-Cans-CA-SiqiniqNeural",	                #365
    "iu-Cans-CA-TaqqiqNeural",	                #366
    "iu-Latn-CA-SiqiniqNeural",	                #367
    "iu-Latn-CA-TaqqiqNeural",	                #368
    "ja-JP-NanamiNeural",	                    #369
    "ja-JP-KeitaNeural",	                    #370
    "ja-JP-AoiNeural",	                    	#371
    "ja-JP-DaichiNeural",	                    #372
    "ja-JP-MayuNeural",	                    	#373
    "ja-JP-NaokiNeural",	                    #374
    "ja-JP-ShioriNeural",	                    #375
    "ja-JP-MasaruMultilingualNeural",	        #376
    "jv-ID-SitiNeural",	                    	#377
    "jv-ID-DimasNeural",	                    #378
    "ka-GE-EkaNeural",	                    	#379
    "ka-GE-GiorgiNeural",	                    #380
    "kk-KZ-AigulNeural",	                    #381
    "kk-KZ-DauletNeural",	                    #382
    "km-KH-SreymomNeural",	                    #383
    "km-KH-PisethNeural",	                    #384
    "kn-IN-SapnaNeural",	                    #385
    "kn-IN-GaganNeural",	                    #386
    "ko-KR-SunHiNeural",	                    #387
    "ko-KR-InJoonNeural",	                    #388
    "ko-KR-BongJinNeural",	                    #389
    "ko-KR-GookMinNeural",	                    #390
    "ko-KR-HyunsuNeural",	                    #391
    "ko-KR-JiMinNeural",	                    #392
    "ko-KR-SeoHyeonNeural",	                    #393
    "ko-KR-SoonBokNeural",	                    #394
    "ko-KR-YuJinNeural",	                    #395
    "ko-KR-HyunsuMultilingualNeural",	        #396
    "lo-LA-KeomanyNeural",	                    #397
    "lo-LA-ChanthavongNeural",	                #398
    "lt-LT-OnaNeural",	                    	#399
    "lt-LT-LeonasNeural",	                    #400
    "lv-LV-EveritaNeural",	                    #401
    "lv-LV-NilsNeural",	                    	#402
    "mk-MK-MarijaNeural",	                    #403
    "mk-MK-AleksandarNeural",	                #404
    "ml-IN-SobhanaNeural",	                    #405
    "ml-IN-MidhunNeural",	                    #406
    "mn-MN-YesuiNeural",	                    #407
    "mn-MN-BataaNeural",	                    #408
    "mr-IN-AarohiNeural",	                    #409
    "mr-IN-ManoharNeural",	                    #410
    "ms-MY-YasminNeural",	                    #411
    "ms-MY-OsmanNeural",	                    #412
    "mt-MT-GraceNeural",	                    #413
    "mt-MT-JosephNeural",	                    #414
    "my-MM-NilarNeural",	                    #415
    "my-MM-ThihaNeural",	                    #416
    "nb-NO-PernilleNeural",	                    #417
    "nb-NO-FinnNeural",	                    	#418
    "nb-NO-IselinNeural",	                    #419
    "ne-NP-HemkalaNeural",	                    #420
    "ne-NP-SagarNeural",	                    #421
    "nl-BE-DenaNeural",	                    	#422
    "nl-BE-ArnaudNeural",	                    #423
    "nl-NL-FennaNeural",	                    #424
    "nl-NL-MaartenNeural",	                    #425
    "nl-NL-ColetteNeural",	                    #426
    "or-IN-SubhasiniNeural",	                #427
    "or-IN-SukantNeural",	                    #428
    "pa-IN-OjasNeural",	                    	#429
    "pa-IN-VaaniNeural",	                    #430
    "pl-PL-AgnieszkaNeural",	                #431
    "pl-PL-MarekNeural",	                    #432
    "pl-PL-ZofiaNeural",	                    #433
    "ps-AF-LatifaNeural",	                    #434
    "ps-AF-GulNawazNeural",	                    #435
    "pt-BR-FranciscaNeural",	                #436
    "pt-BR-AntonioNeural",	                    #437
    "pt-BR-BrendaNeural",	                    #438
    "pt-BR-DonatoNeural",	                    #439
    "pt-BR-ElzaNeural",	                    	#440
    "pt-BR-FabioNeural",	                    #441
    "pt-BR-GiovannaNeural",	                    #442
    "pt-BR-HumbertoNeural",	                    #443
    "pt-BR-JulioNeural",	                    #444
    "pt-BR-LeilaNeural",	                    #445
    "pt-BR-LeticiaNeural",	                    #446
    "pt-BR-ManuelaNeural",	                    #447
    "pt-BR-NicolauNeural",	                    #448
    "pt-BR-ThalitaNeural",	                    #449
    "pt-BR-ValerioNeural",	                    #450
    "pt-BR-YaraNeural",	                    	#451
    "pt-BR-MacerioMultilingualNeural",	        #452
    "pt-BR-ThalitaMultilingualNeural",	        #453
    "pt-PT-RaquelNeural",	                    #454
    "pt-PT-DuarteNeural",	                    #455
    "pt-PT-FernandaNeural",	                    #456
    "ro-RO-AlinaNeural",	                    #457
    "ro-RO-EmilNeural",	                    	#458
    "ru-RU-SvetlanaNeural",	                    #459
    "ru-RU-DmitryNeural",	                    #460
    "ru-RU-DariyaNeural",	                    #461
    "si-LK-ThiliniNeural",	                    #462
    "si-LK-SameeraNeural",	                    #463
    "sk-SK-ViktoriaNeural",	                    #464
    "sk-SK-LukasNeural",	                    #465
    "sl-SI-PetraNeural",	                    #466
    "sl-SI-RokNeural",	                    	#467
    "so-SO-UbaxNeural",	                    	#468
    "so-SO-MuuseNeural",	                    #469
    "sq-AL-AnilaNeural",	                    #470
    "sq-AL-IlirNeural",	                    	#471
    "sr-Latn-RS-NicholasNeural",	            #472
    "sr-Latn-RS-SophieNeural",	                #473
    "sr-RS-SophieNeural",	                    #474
    "sr-RS-NicholasNeural",	                    #475
    "su-ID-TutiNeural",	                    	#476
    "su-ID-JajangNeural",	                    #477
    "sv-SE-SofieNeural",	                    #478
    "sv-SE-MattiasNeural",	                    #479
    "sv-SE-HilleviNeural",	                    #480
    "sw-KE-ZuriNeural",	                    	#481
    "sw-KE-RafikiNeural",	                    #482
    "sw-TZ-RehemaNeural",	                    #483
    "sw-TZ-DaudiNeural",	                    #484
    "ta-IN-PallaviNeural",	                    #485
    "ta-IN-ValluvarNeural",	                    #486
    "ta-LK-SaranyaNeural",	                    #487
    "ta-LK-KumarNeural",	                    #488
    "ta-MY-KaniNeural",	                    	#489
    "ta-MY-SuryaNeural",	                    #490
    "ta-SG-VenbaNeural",	                    #491
    "ta-SG-AnbuNeural",	                    	#492
    "te-IN-ShrutiNeural",	                    #493
    "te-IN-MohanNeural",	                    #494
    "th-TH-PremwadeeNeural",	                #495
    "th-TH-NiwatNeural",	                    #496
    "th-TH-AcharaNeural",	                    #497
    "tr-TR-EmelNeural",	                    	#498
    "tr-TR-AhmetNeural",	                    #499
    "uk-UA-PolinaNeural",	                    #500
    "uk-UA-OstapNeural",	                    #501
    "ur-IN-GulNeural",	                    	#502
    "ur-IN-SalmanNeural",	                    #503
    "ur-PK-UzmaNeural",	                    	#504
    "ur-PK-AsadNeural",	                    	#505
    "uz-UZ-MadinaNeural",	                    #506
    "uz-UZ-SardorNeural",	                    #507
    "vi-VN-HoaiMyNeural",	                    #508
    "vi-VN-NamMinhNeural",	                    #509
    "wuu-CN-XiaotongNeural",	                #510
    "wuu-CN-YunzheNeural",	                    #511
    "yue-CN-XiaoMinNeural",	                    #512
    "yue-CN-YunSongNeural",	                    #513
    "zh-CN-XiaoxiaoNeural",	                    #514
    "zh-CN-YunxiNeural",	                    #515
    "zh-CN-YunjianNeural",	                    #516
    "zh-CN-XiaoyiNeural",	                    #517
    "zh-CN-YunyangNeural",	                    #518
    "zh-CN-XiaochenNeural",	                    #519
    "zh-CN-XiaochenMultilingualNeural",	        #520
    "zh-CN-XiaohanNeural",	                    #521
    "zh-CN-XiaomengNeural",	                    #522
    "zh-CN-XiaomoNeural",	                    #523
    "zh-CN-XiaoqiuNeural",	                    #524
    "zh-CN-XiaorouNeural",	                    #525
    "zh-CN-XiaoruiNeural",	                    #526
    "zh-CN-XiaoshuangNeural",	                #527
    "zh-CN-XiaoxiaoDialectsNeural",	            #528
    "zh-CN-XiaoxiaoMultilingualNeural",	        #529
    "zh-CN-XiaoyanNeural",	                    #530
    "zh-CN-XiaoyouNeural",	                    #531
    "zh-CN-XiaoyuMultilingualNeural",	        #532
    "zh-CN-XiaozhenNeural",	                    #533
    "zh-CN-YunfengNeural",	                    #534
    "zh-CN-YunhaoNeural",	                    #535
    "zh-CN-YunjieNeural",	                    #536
    "zh-CN-YunxiaNeural",	                    #537
    "zh-CN-YunyeNeural",	                    #538
    "zh-CN-YunyiMultilingualNeural",	        #539
    "zh-CN-YunzeNeural",	                    #540
    "zh-CN-YunfanMultilingualNeural",	        #541
    "zh-CN-YunxiaoMultilingualNeural",	        #542
    "zh-CN-guangxi-YunqiNeural",	            #543
    "zh-CN-henan-YundengNeural",	            #544
    "zh-CN-liaoning-XiaobeiNeural",	            #545
    "zh-CN-liaoning-YunbiaoNeural",	            #546
    "zh-CN-shaanxi-XiaoniNeural",	            #547
    "zh-CN-shandong-YunxiangNeural",	        #548
    "zh-CN-sichuan-YunxiNeural",	            #549
    "zh-HK-HiuMaanNeural",	                    #550
    "zh-HK-WanLungNeural",	                    #551
    "zh-HK-HiuGaaiNeural",	                    #552
    "zh-TW-HsiaoChenNeural",	                #553
    "zh-TW-YunJheNeural",	                    #554
    "zh-TW-HsiaoYuNeural",	                    #555
    "zu-ZA-ThandoNeural",	                    #556
    "zu-ZA-ThembaNeural",	                    #557
]

___client_id = keystore_get_key_type(argType=KEYTYPE_IDX_AIvoice_Azure_SpeechService_NONE)
___client_region = keystore_get_region_type(argType=REGIONTYPE_IDX_AIvoice_Azure_SpeechServices_NONE)

def get_speed_value(speed):
    if speed > 2.0:
        speed = 2.0
    elif speed < 0.5:
        speed = 0.5
    return speed

def get_pitch_value(pitch):
    if pitch == 'high':
        return '50%'
    elif pitch == 'low':
        return '-50%'
    else:
        return '0%'

def gen_ai_voice_msa(argFilePath, argText, argIdxVoiceId, argSpeakingSpeed=1, argSpeakingPitch='middle', argLog=None):
    #For debugging
    #if '20250130_171100888_2P_msa_144_0005_dummy_1-0_middle_genasrconversation.mp3' in argFilePath:
    #    return

    __item_voiceId = ASR_MSA_SUPPORT_LANGUAGES[argIdxVoiceId]

    dbg_msg = f'▶ [msa]argFilePath[Vid:{argIdxVoiceId}:{__item_voiceId}]:{___client_region}] : {argFilePath} : {argText}'
    if argLog:
        argLog.e(dbg_msg)
    else:
        print(dbg_msg)

    speech_config = speechsdk.SpeechConfig(subscription=___client_id, region=___client_region)
    speech_config.speech_synthesis_voice_name = ASR_MSA_SUPPORT_LANGUAGES[argIdxVoiceId]

    if current_GPT_PROGRAM_PROXY_MODE == GPT_PROGRAM_PROXY_MODE_OFFICE:
        speech_config.set_proxy(hostname=r'10.244.254.254', port=8080)

    ___text = '''<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-GB"><voice name="{innerIdxVoiceId}"><prosody rate="{innerSpeakingSpeed}" pitch="{innerSpeakingPitch}">{innerText}</prosody></voice></speak>'''\
        .format(innerIdxVoiceId=__item_voiceId,
                innerSpeakingSpeed=get_speed_value(argSpeakingSpeed),
                innerSpeakingPitch=get_pitch_value(argSpeakingPitch),
                innerText=argText)
    # ___text = f'<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-GB"><voice name="{argIdxVoiceId}"><prosody rate={get_speed_value(argSpeakingSpeed)}">{argText}</prosody></voice></speak>'
    # print(___text)

    mp3_dir_name, mp3_base_name = os.path.split(argFilePath)
    mp3_base_name_no_ext, mp3_only_ext = os.path.splitext(mp3_base_name)
    wav_full_path = f'{os.path.join(mp3_dir_name,mp3_base_name_no_ext)}.wav'


    # Synthesize the text to speech.
    audio_config = speechsdk.audio.AudioOutputConfig(filename=wav_full_path)
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    # response = speech_synthesizer.speak_text_async(argText).get()
    response = speech_synthesizer.speak_ssml_async(___text).get()

    if response.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        # print("Speech synthesized for text [{}]".format(argText))
        if os.path.exists(wav_full_path):
            file_size = os.path.getsize(wav_full_path)
            if file_size > 10:       # Check FileSize of wav. If it's over 10bytes, make mp3 from wav or not.
                sound = AudioSegment.from_wav(wav_full_path)
                sound.export(argFilePath, format="mp3")
            else:
                dbg_msg = f'◆ OMG [msa]argFilePath[Vid:{argIdxVoiceId}:{__item_voiceId}]:{___client_region}] : {argFilePath} : {file_size} '
                if argLog:
                    argLog.e(dbg_msg)
                else:
                    print(dbg_msg)
        pass
    elif response.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = response.cancellation_details
        # print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            # print("Error details: {}".format(cancellation_details.error_details))
            pass