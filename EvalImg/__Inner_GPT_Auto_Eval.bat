@echo off
rem # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
rem # # # # #    DO NOT USE arg(%1 %2 %3 ... %9). Only USE custom_arg(_arr[0] , _arr[1] , _arr[2] and config_xxxx ....)    # # # # #
rem # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

rem __Inner_GPT_Auto_Eval.bat "-DIROUTPUT::D:\00_Dev\SvcApp2\SvcApp2_sukkwon.oh_W02\TEAM\SQE\KOR\ServiceApp2\AiAutoEvaluation\result\__SDF__" "-AUTORESIDUE::TRUE" "-DEVICESN::R3CW90EJ80P" "-TGTAPP::sr" "-MLANG::Korean" "-SLANG::English" "-TLANG::Korean" "-STARTIDX::1" "-ENDIDX::25" "-MERGETORESULT::TRUE" "-INPUTCSVPREFIX::trans_sr_English_Indonesian_"
echo ...
echo Greeting_GPT MAIN WORLD~

rem Get start time:
for /F “tokens=1-4 delims=:.,” %%a in (“%time%”) do (
    set /A “___start_time=(((%%a*60)+1%%b %% 100)*60+1%%c %% 100)*100+1%%d %% 100”
)

setlocal EnableDelayedExpansion
set _MY_TAG=%~n0
set _ALL_ARGS=%*
if "!_ALL_ARGS!"=="" (
    set _CONV_ALL_ARGS=!_ALL_ARGS!
) else (
    set _CONV_ALL_ARGS=!_ALL_ARGS:"=!
)
call _import_vars.bat

set _arr.length=0
if not "!_CONV_ALL_ARGS!"=="" (
    for %%I in ("!_CONV_ALL_ARGS: =" "!") do (
        set val=%%I
        set _arr[!_arr.length!]=!val:"=!

        set /a _arr.length=!_arr.length! + 1
    )
)
set /a _arr.Ubound=!_arr.length! - 1

echo ...
echo [!_MY_TAG!]:_ALL_ARGS:!_ALL_ARGS!
echo [!_MY_TAG!]:_CONV_ALL_ARGS:!_CONV_ALL_ARGS!
echo [!_MY_TAG!]:_arr.length:!_arr.length!
echo ...

for /L %%I in (0, 1, !_arr.Ubound!) do (
    echo [!_MY_TAG!]:_arr[%%I] = !_arr[%%I]!
)
echo ...

set __Split_COUNT=4
set __Specific_LANG=Thai Hindi Chinese Vietnamese
rem set /A __residue_loop_waittime=5
set /A __residue_loop_waittime=!__residue_3rd_waittime!
set __zerobase_top=0000
set /A __residue_loop_count=0
set /A __mode_job=0
set /A __gpt_eval_count=0

echo [!_MY_TAG!]:debug_1:!__shell_cmd_getargscount! "!_CONV_ALL_ARGS!"

FOR /f "tokens=*" %%F IN ('!__shell_cmd_curfilename!') DO (
    SET __JOB_ID_=%%F
)
echo [!_MY_TAG!]:__JOB_ID_:!__JOB_ID_!

set __START_TIME=!__JOB_ID_!

echo [!_MY_TAG!]:~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ [GPT_STORY] START batch !__START_TIME!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo ...
echo ...

rem echo #############################################################################################
rem echo ########################### You ONLY *** CAN *** customize below, ###########################
rem echo ---------------------------------------------------------------------------------------------
rem echo -------------------------------         EXAMPLE CASE          -------------------------------
rem echo ---------------------------------------------------------------------------------------------
rem echo set config_AUTORESIDUE=FALSE                           # whether if doing auto-residue or not.
rem echo set config_DEVICESN=R3CW90EJ80P                        # The SN of device
rem echo set config_TGTAPP=sr                                   # Target Translate app(default:sr)
rem echo set config_Mlang=Korean                                # Mother language(explain language, default:Korean)
rem echo set config_SLANG=Korean                                # Source language(From, default:Korean)
rem echo set config_TLANG=English                               # Target language(To, default:English)
rem echo set /A config_STARTIDX=1                               # The start_idx
rem echo set /A config_ENDIDX=-25                               # The end_idx
rem echo set config_RESIDUELIST=32 34 35 36 38                  # The residue list
rem echo set config_INPUTCSVPREFIX=trans_sr_sentence_Korean_Korean_English_   # The input prefilename
rem echo set config_DIRINPUT=D:\00_Dev\SvcApp2\SvcApp2_sukkwon.oh_W02\TEAM\SQE\KOR\ServiceApp2\AiAutoEvaluation\res\input\Korean_English\R3CW90EJ80P\       # The input dir
rem echo set config_DIROUTPUT=D:\00_Dev\SvcApp2\SvcApp2_sukkwon.oh_W02\TEAM\SQE\KOR\ServiceApp2\AiAutoEvaluation\result\output\Korean_English\R3CW90EJ80P\  # The result dir
rem echo set config_ARGSALL=-d R3CW90EJ80P -td R3CW90EJ80P -Pmt trans -Mlang Korean -Slang Korean -Tlang English -SCount 4 --skipgptjob --skipskbd -IDir %config_DIRINPUT% -ODir %config_DIROUTPUT%
rem echo #############################################################################################
set config_AUTORESIDUE=TRUE
set config_DEVICESN=R3CW90EJ80P
set config_TGTAPP=sr
set config_MLANG=Korean
set config_SLANG=Korean
set config_TLANG=English
set /A config_STARTIDX=1
set /A config_ENDIDX=25
set config_DIRINPUT=
set config_DIROUTPUT=
set config_MERGETORESULT=TRUE
set config_SYSTEMTYPE=api
set config_THREADNUM=0

for /L %%I in (0, 1, !_arr.Ubound!) do (
    FOR /f "tokens=*" %%o IN ('!__shell_cmd_genargskey! "!_arr[%%I]!"') DO (
        set __args_key=%%o
    )

    FOR /f "tokens=*" %%o IN ('!__shell_cmd_genargsval! "!_arr[%%I]!"') DO (
        set __args_val=%%o
    )
    echo [!_MY_TAG!]:__arg[%%I]: [!__args_key!] === [!__args_val!]
    set config_!__args_key!=!__args_val!
)

set config_RESIDUELIST=
if /I "!config_INPUTCSVPREFIX!"=="" (
    set config_INPUTCSVPREFIX=trans_!config_TGTAPP!_!config_SLANG!_!config_TLANG!_
)

if /I "!config_DIRINPUT!"=="" (
    set config_DIRINPUT=!__Dir_GPTHOME!\res\input\!config_SLANG!_!config_TLANG!\!config_DEVICESN!
)

if /I "!config_DIROUTPUT!"=="" (
    set config_DIROUTPUT=!__Dir_GPTHOME!\result\output\!config_SLANG!_!config_TLANG!\!config_DEVICESN!
)

if "!config_SYSTEMTYPE!"=="api" (
    set __python_fname=AI_Eval_GPT_api.py
    set __Split_COUNT=4
) else (
    echo [!_MY_TAG!]:_____ OMG!!! Error! stop here! _____
    pause
    goto :MYEOF
)

set config_ARGSALL=-Pmt trans -Mlang !config_MLANG! -Slang !config_SLANG! -Tlang !config_TLANG! -SCount !__Split_COUNT! --skipgptjob -IDir %config_DIRINPUT% -ODir %config_DIROUTPUT% -TNum %config_THREADNUM% -Etype azure
rem echo #############################################################################################

if /I "%1"=="" (
    rem do nothing.
) else (
    if /I "%1"=="-ar" (
        rem MODE_residue_auto_gen_do_empty_result_only
        set /A __mode_job=1
    ) else if /I "%1"=="-autoresidue" (
        rem MODE_residue_auto_gen_do_empty_result_only
        set /A __mode_job=1
    ) else if /I "%1"=="true" (
        rem MODE_residue_auto_gen_do_empty_result_only
        set /A __mode_job=1
    ) else (
        FOR /f "tokens=*" %%o IN ('!__shell_cmd_genargskey! "!_arr[0]!"') DO (
            set __args_1_key=%%o
        )

        FOR /f "tokens=*" %%o IN ('!__shell_cmd_genargsval! "!_arr[0]!"') DO (
            set __args_1_val=%%o
        )

        echo [!_MY_TAG!]:__args_1: [!__args_key!] === [!__args_1_val!]

        if /I "!__args_1_key!"=="autoresidue" (
            if /I "!__args_1_val!"=="TRUE" (
                rem MODE_residue_auto_gen_do_empty_result_only
                set /A __mode_job=1
            )
        ) else if /I "!__args_1_key!"=="ar" (
            if /I "!__args_1_val!"=="TRUE" (
                rem MODE_residue_auto_gen_do_empty_result_only
                set /A __mode_job=1
            )
        ) else (
            rem NONE=0
            set /A __mode_job=0
        )
    )
)

if !__mode_job! EQU 1 (
    set config_AUTORESIDUE=TRUE
) else (
    rem __mode_job : 0
    rem do nothing here!
)
echo [!_MY_TAG!]:__mode_job:!__mode_job!
echo ...

echo [!_MY_TAG!]:_____________________ DUMP all vars ________________________
echo [!_MY_TAG!]:1)config_AUTORESIDUE:!config_AUTORESIDUE!
echo [!_MY_TAG!]:2)config_DEVICESN:!config_DEVICESN!
echo [!_MY_TAG!]:3)config_TGTAPP:!config_TGTAPP!
echo [!_MY_TAG!]:4)config_MLANG:!config_MLANG!
echo [!_MY_TAG!]:5)config_SLANG:!config_SLANG!
echo [!_MY_TAG!]:6)config_TLANG:!config_TLANG!
echo [!_MY_TAG!]:7)config_STARTIDX:!config_STARTIDX!
echo [!_MY_TAG!]:8)config_ENDIDX:!config_ENDIDX!
echo [!_MY_TAG!]:9)config_DIROUTPUT:!config_DIROUTPUT!
echo [!_MY_TAG!]:10)config_MERGETORESULT:!config_MERGETORESULT!
echo [!_MY_TAG!]:11)config_THREADNUM:!config_THREADNUM!

echo ____________________________________________________________
echo ...

echo [!_MY_TAG!]:____ [GPT_STORY] !config_STARTIDX! : !config_ENDIDX! : !config_RESIDUELIST!

IF !config_STARTIDX! LSS 0 (
    echo [!_MY_TAG!]:_____ skip loop 1_____
    GOTO residue_list_loop__
) else if !config_ENDIDX! LSS 0 (
    echo [!_MY_TAG!]:_____ skip loop 2_____
    GOTO residue_list_loop__
)

for /L %%i in (!config_STARTIDX!,1,!config_ENDIDX!) do (
	if /I "!config_RESIDUELIST!"=="" (
		set config_RESIDUELIST=%%i
	) else (
		set config_RESIDUELIST=!config_RESIDUELIST! %%i
	)
)

echo [!_MY_TAG!]:____ [GPT_STORY] #Adjusted_before_removedup# config_RESIDUELIST : !config_RESIDUELIST!

FOR /f "tokens=*" %%F IN ('%__shell_cmd_removedupitem% "!config_RESIDUELIST!"') DO (
    SET config_RESIDUELIST=%%F
    echo ...
)

echo [!_MY_TAG!]:____ [GPT_STORY] #Adjusted_after_removedup# config_RESIDUELIST : !config_RESIDUELIST!
echo ...
echo ...

:residue_list_loop__
FOR /f "tokens=*" %%F IN ('%__shell_cmd_removedupitem% "!config_RESIDUELIST!"') DO (
    SET config_RESIDUELIST=%%F
)

echo ...
echo [!_MY_TAG!]:--------------_____________________ [GPT_STORY] [!__residue_loop_count!] config_RESIDUELIST : !config_RESIDUELIST!

set __missed_list=
for %%a in (!config_RESIDUELIST!) do (
    set _tmp_index=%%a
    set _zerobase_modify=!__zerobase_top!!_tmp_index!
    set _zerobase=!_zerobase_modify:~-3!
    set _filename=!config_INPUTCSVPREFIX!!_zerobase!
    set /A _do_skip_evaluation=0

    echo [!_MY_TAG!]:--__ _tmp_index:!_tmp_index!
    echo [!_MY_TAG!]:--__ [GPT_STORY] _filename:!_filename!

    if /I "!config_AUTORESIDUE!"=="TRUE" (
        for /F "delims=" %%f in ('dir /b /s "%config_DIROUTPUT%" 2^>^&1^|find /C "!_filename!"') do (
            set /A _made_file_count=%%f
            echo ...
        )
        echo [!_MY_TAG!]:____ [GPT_STORY] _made_file_count_1 === !_made_file_count!

        if !_made_file_count! GEQ 1 (
            set /A _do_skip_evaluation=1
        )
    )

    if !_do_skip_evaluation! EQU 0 (
        rem # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        rem !__Dir_GPTHOME!/AI_Eval_ChatGPT_app.py !config_ARGSALL! -Icsv !_filename!.csv
        rem # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        echo python.exe !__Dir_GPTHOME!\!__python_fname! !config_ARGSALL! -Icsv !_filename!.csv
        python.exe !__Dir_GPTHOME!\!__python_fname! !config_ARGSALL! -Icsv !_filename!.csv

        rem # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        set /A __gpt_eval_count=!__gpt_eval_count! + 1
        timeout 5 > NUL

        for /F "delims=" %%f in ('dir /b /s "%config_DIROUTPUT%" 2^>^&1^|find /C "!_filename!"') do (
            set /A _made_file_count=%%f
            echo ...
        )
        echo [!_MY_TAG!]:____ [GPT_STORY] _made_file_count_2 === !_made_file_count!

        if !_made_file_count! LSS 1 (
            echo [!_MY_TAG!]:____ [GPT_STORY][FAIL] Result file create failed : !config_DIROUTPUT!\!_filename!
            if /I "!__missed_list!" == "" (
                set __missed_list=!_tmp_index!
                echo [!_MY_TAG!]:----replace_____ __missed_list : !__missed_list!
            ) else (
                set __missed_list=!__missed_list! !_tmp_index!
                echo [!_MY_TAG!]:----append_____ __missed_list : !__missed_list!
            )
        ) else (
            echo [!_MY_TAG!]:----_____ Result file create success : !_filename!
        )

        echo ...
        echo [!_MY_TAG!]:____=====____=====____=====____=====____=====____=====____=====____=====____=====
        echo ...
    )
)

if /I "!__missed_list!"=="" (
    echo [!_MY_TAG!]:--------____ [GPT_STORY][PASS] total __missed_list is EMPTY. so stop it. !__residue_loop_count! : !__Excelxlsb:"=! : !config_DIROUTPUT:"=!

    if !__gpt_eval_count! GEQ 1 (
        if  /I "!config_MERGETORESULT!"=="TRUE" (
            python.exe !__Dir_GPTHOME!/AI_Eval_VBA_MergeToResult.py !__Excelxlsb:"=! !config_DIROUTPUT:"=!
            timeout 5 > NUL
        )
    )
) else (
    if !__residue_loop_count! LSS 3 (
    	set config_RESIDUELIST=!__missed_list!
    	if !__residue_loop_count! EQU 0 (
    	    set /A __residue_loop_waittime=!__residue_1st_waittime!
    	) else if !__residue_loop_count! EQU 1 (
    	    set /A __residue_loop_waittime=!__residue_2nd_waittime!
    	) else (
            set /A __residue_loop_waittime=!__residue_3rd_waittime!
			for %%l in (!__Specific_LANG!) do (
				if "%%l"=="!config_SLANG!" (
					set __Split_COUNT=1
					echo [!_MY_TAG!]:----__Split_COUNT=!__Split_COUNT!_____ config_SLANG : !config_SLANG!
					set config_ARGSALL=-d !config_DEVICESN! -td !config_DEVICESN! -Pmt trans -Mlang !config_MLANG! -Slang !config_SLANG! -Tlang !config_TLANG! -SCount !__Split_COUNT! --skipgptjob --skipskbd -IDir %config_DIRINPUT% -ODir %config_DIROUTPUT%
				) else if "%%l"=="!config_TLANG!" (
					set __Split_COUNT=1
					echo [!_MY_TAG!]:----__Split_COUNT=!__Split_COUNT!_____ config_TLANG : !config_TLANG!
					set config_ARGSALL=-d !config_DEVICESN! -td !config_DEVICESN! -Pmt trans -Mlang !config_MLANG! -Slang !config_SLANG! -Tlang !config_TLANG! -SCount !__Split_COUNT! --skipgptjob --skipskbd -IDir %config_DIRINPUT% -ODir %config_DIROUTPUT%
				)
			)
		)

	    echo [!_MY_TAG!]:--------____ [GPT_STORY] total __missed_list : !config_RESIDUELIST!
	    echo [!_MY_TAG!]:--------____ sleep !__residue_loop_waittime! second.


	    timeout !__residue_loop_waittime! > NUL

        set /A __residue_loop_count=!__residue_loop_count!+1
        goto residue_list_loop__
    ) else (
        echo [!_MY_TAG!]:--------____ [GPT_STORY] OMG, It takes too longtime.so stop here. __residue_loop_count:[!__residue_loop_count!]
    )
)

echo ...
echo ...

FOR /f "tokens=*" %%F IN ('!__shell_cmd_curfilename!') DO (
    SET __END_TIME=%%F
)

echo [!_MY_TAG!]:______________________________ [GPT_STORY] End batch [!__START_TIME! : !__END_TIME!]______________________________

:MYEOF

rem Get end time:
for /F “tokens=1-4 delims=:.,” %%a in (“%time%”) do (
    set /A “end=(((%%a*60)+1%%b %% 100)*60+1%%c %% 100)*100+1%%d %% 100”
)

rem Get elapsed time:
set /A elapsed=end-start
rem Show elapsed time:
set /A hh=elapsed/(60*60*100), rest=elapsed%%(60*60*100), mm=rest/(60*100), rest%%=60*100, ss=rest/100, cc=rest%%100
if %mm% lss 10 (
    set mm=0%mm%
)
if %ss% lss 10 (
    set ss=0%ss%
)
if %cc% lss 10 (
    set cc=0%cc%
)

echo ### Running time : dur_!hh!:!mm!:!ss!_!cc!

endlocal