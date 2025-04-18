Usage : 

1) python
a) in_datas_hasimg
-Uniquetid 250307_054600000 -Etype openai -Emodel gpt-4o           -Pmt evalimg -Mlang korean -SCount 2 -TNum 0 -IDir C:\Users\osk10\PycharmProjects\EvalImg\res\Csv -Icsv in_datas_hasimg.csv -IInImgDir C:\Users\osk10\PycharmProjects\EvalImg\res\InImage -IOutImgDir C:\Users\osk10\PycharmProjects\EvalImg\res\OutImage -ODir C:\Users\osk10\PycharmProjects\EvalImg\result
-Uniquetid 250307_054600000 -Etype azure  -Emodel gpt-4o:SE-SQE-05 -Pmt evalimg -Mlang korean -SCount 2 -TNum 0 -IDir C:\Users\osk10\PycharmProjects\EvalImg\res\Csv -Icsv in_datas_hasimg.csv -IInImgDir C:\Users\osk10\PycharmProjects\EvalImg\res\InImage -IOutImgDir C:\Users\osk10\PycharmProjects\EvalImg\res\OutImage -ODir C:\Users\osk10\PycharmProjects\EvalImg\result
b) in_datas_noimg
-Uniquetid 250307_054600000 -Etype openai -Emodel gpt-4o           -Pmt evalimg -Mlang korean -SCount 2 -TNum 0 -IDir C:\Users\osk10\PycharmProjects\EvalImg\res\Csv -Icsv in_datas_noimg.csv -IInImgDir C:\Users\osk10\PycharmProjects\EvalImg\res\InImage -IOutImgDir C:\Users\osk10\PycharmProjects\EvalImg\res\OutImage -ODir C:\Users\osk10\PycharmProjects\EvalImg\result
-Uniquetid 250307_054600000 -Etype azure  -Emodel gpt-4o:SE-SQE-05 -Pmt evalimg -Mlang korean -SCount 2 -TNum 0 -IDir C:\Users\osk10\PycharmProjects\EvalImg\res\Csv -Icsv in_datas_noimg.csv -IInImgDir C:\Users\osk10\PycharmProjects\EvalImg\res\InImage -IOutImgDir C:\Users\osk10\PycharmProjects\EvalImg\res\OutImage -ODir C:\Users\osk10\PycharmProjects\EvalImg\result

2) batch
a) in_datas_hasimg
AI_EvalImage_SDF.bat "-UNIQUETID::250307_054600000" "-ETYPE::openai" "-EMODEL::gpt-4o" "-PMT::evalimg" "-MLANG::korean" "-IDIR::C:\Users\osk10\PycharmProjects\EvalImg\res\Csv" "-ICSV::in_datas_hasimg.csv" "-IINIMGDIR::C:\Users\osk10\PycharmProjects\EvalImg\res\InImage" "-IOUTIMGDIR::C:\Users\osk10\PycharmProjects\EvalImg\res\OutImage" "-ODIR::C:\Users\osk10\PycharmProjects\EvalImg\result">log_250307_054600000.log 2>&1
b) in_datas_noimg
AI_EvalImage_SDF.bat "-UNIQUETID::250307_054600000" "-ETYPE::openai" "-EMODEL::gpt-4o" "-PMT::evalimg" "-MLANG::korean" "-IDIR::C:\Users\osk10\PycharmProjects\EvalImg\res\Csv" "-ICSV::in_datas_noimg.csv" "-IINIMGDIR::C:\Users\osk10\PycharmProjects\EvalImg\res\InImage" "-IOUTIMGDIR::C:\Users\osk10\PycharmProjects\EvalImg\res\OutImage" "-ODIR::C:\Users\osk10\PycharmProjects\EvalImg\result">log_250307_054600000.log 2>&1

3) 환경변수
AI_EVAL_IMG_HOME=C:\Users\osk10\PycharmProjects\EvalImg
AI_EVAL_IMG_RES=C:\Users\osk10\PycharmProjects\EvalImg\res
AI_EVAL_IMG_RESULT=C:\Users\osk10\PycharmProjects\EvalImg\result