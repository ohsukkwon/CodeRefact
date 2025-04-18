rem @echo off

pushd "%~dp0"
call _import_vars.bat

set _Inner_MY_TAG=%~n0
echo.
echo.
echo [!_Inner_MY_TAG!]:###__CheckSTEP__### # # # # # # # # Greeting_INNER WORLD~ # # # # # # # #
echo.
echo.

setlocal EnableDelayedExpansion

rem GET ___start_total_time
echo GET ___start_total_time

for /F "tokens=1-4 delims=:.," %%a in ('!__shell_cmd_curtime2!') do (
    echo "A:" %%a
    echo "B:" %%b
    echo "C:" %%c
    echo "D:" %%d

    set /A "___start_total_time=((((%%a*60)+((100+%%b) %% 100))*60)+((100+%%c) %% 100))"
)

set config_UNIQUETID=
FOR /f "tokens=*" %%F IN ('!__shell_cmd_curmillifilename!') DO (
    set config_UNIQUETID=%%F
)
if "!config_UNIQUETID!"=="" (
    echo [!_Inner_MY_TAG!]:config_UNIQUETID is NULL~~~
    goto :__MY_INNER_EOF
)

set config_ETYPE=openai
set config_EMODEL=gpt-4o-2024-11-20
set config_SKIPGENSCENINFILE=
set config_VOICEID=
set config_SKIPGENAITTS=
set config_PMT=genasrconversation
set config_MLANG=Korean
set config_ODIR=%GEN_ASR_AIvoice_RESULT%
set config_IDIR=
set config_ICFG=
set config_BATCHCSV=

set _Inner_ALL_ARGS=%*
echo [!_Inner_MY_TAG!]:###__CheckSTEP__###_Inner_ALL_ARGS:!_Inner_ALL_ARGS!

if "!_Inner_ALL_ARGS!"=="" (
    set _CONV_Inner_ALL_ARGS=!_Inner_ALL_ARGS!
) else (
    set _CONV_Inner_ALL_ARGS=!_Inner_ALL_ARGS:"=!
)
echo [!_Inner_MY_TAG!]:_CONV_Inner_ALL_ARGS:!_CONV_Inner_ALL_ARGS!

call _import_vars.bat

set _Inner_arr.length=0
if not "!_CONV_Inner_ALL_ARGS!"=="" (
    for %%I in ("!_CONV_Inner_ALL_ARGS: =" "!") do (
        set _tmp_val=%%I

        if !_tmp_val!=="" (
            echo.
        ) else (
            echo [%_Inner_MY_TAG%]:_tmp_val:!_tmp_val!
            set _Inner_arr[!_Inner_arr.length!]=!_tmp_val:"=!

            set /a _Inner_arr.length=!_Inner_arr.length! + 1
        )
    )
)
set /a _Inner_arr.Ubound=!_Inner_arr.length! - 1

echo [%_Inner_MY_TAG%]:_Inner_ALL_ARGS:!_Inner_ALL_ARGS!
echo [%_Inner_MY_TAG%]:_Inner_arr.length:!_Inner_arr.length! , _Inner_arr.Ubound:!_Inner_arr.Ubound!

rem ### for debugging
echo ...
for /L %%I in (0, 1, !_Inner_arr.Ubound!) do (
    echo [!_Inner_MY_TAG!]:_Inner_arr[%%I] = !_Inner_arr[%%I]!
)
echo ...

rem # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
rem # # # # # Overwrite config_XXXXXXXX variables HERE. # # # # #
rem # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
for /L %%I in (0, 1, !_Inner_arr.Ubound!) do (
    FOR /f "tokens=*" %%o IN ('!__shell_cmd_genargskey! "!_Inner_arr[%%I]!"') DO (
        set __args_key=%%o
    )

    FOR /f "tokens=*" %%o IN ('!__shell_cmd_genargsval! "!_Inner_arr[%%I]!"') DO (
        set __args_val=%%o
    )
    echo [!_Inner_MY_TAG!]:_Inner_arr[%%I]:!__args_key!_____!__args_val!
    set config_!__args_key!=!__args_val!
    echo [!_Inner_MY_TAG!]: config_!__args_key!:_____!__args_val!_____
)
rem # # # # # DONE Overwrite  # # # # # # # # # # # # # # # # # #
if "!config_SKIPGENSCENINFILE!"=="" (
    rem do nothing
    set arg_config_SKIPGENSCENINFILE=
) else (
    set arg_config_SKIPGENSCENINFILE=--skipgensceninfile !config_SKIPGENSCENINFILE!
)

if "!config_VOICEID!"=="" (
    rem do nothing
    set arg_config_VOICEID=
) else (
    set arg_config_VOICEID=-Voiceid !config_VOICEID!
)

if "!config_IDIR!"=="" (
    rem do nothing
    set arg_config_IDIR=
) else (
    set arg_config_IDIR=-IDir !config_IDIR!
)

if "!config_ICFG!"=="" (
    rem do nothing
    set arg_config_ICFG=-
) else (
    set arg_config_ICFG=-Icfg !config_ICFG!
)


rem # # # TRUE : IF last char is "\",
if "!config_BATCHCSV:~-1!"=="\" (
    rem # # # remove last char("\")
    set config_BATCHCSV=!config_BATCHCSV:~0,-1!
)

rem Change the existing BATCH_DIR related path configuration to be based on GEN_ASR_AIvoice_HOME.
set UTILS_DIR=%GEN_ASR_AIvoice_HOME%\utils
set BATCHCFG_DIR=%GEN_ASR_AIvoice_RES%\batchcfg\!config_UNIQUETID::skip=!
for %%I in ("%BATCHCFG_DIR%") do set BATCHCFG_DIR=%%~fI
set PY_MAKE_CFG_SCRIPT=%UTILS_DIR%\MakeCSVtoCFG.py
set AI_SCRIPT=%GEN_ASR_AIvoice_HOME%\AI_ASR_Gen.py
set RESULT_DIR=%config_ODIR%\!config_UNIQUETID::skip=!

rem Initial message output
echo [!_Inner_MY_TAG!]:# # # # # # # # # # # # Starting batch process...
echo [!_Inner_MY_TAG!]:Batch directory: !BATCHCFG_DIR!
echo [!_Inner_MY_TAG!]:Utils directory: %UTILS_DIR%
echo [!_Inner_MY_TAG!]:Result directory: !RESULT_DIR!

if "!config_SKIPGENSCENINFILE!"=="" (
    rem Check for exist BATCHCSV file.
    if not exist "!config_BATCHCSV!" (
        echo [!_Inner_MY_TAG!]:Error: Input CSV file not found: !config_BATCHCSV!
        goto :__MY_INNER_EOF
    )
)

rem MakeDir for UNIQUETID.
if not exist "%BATCHCFG_DIR%" (
    mkdir "%BATCHCFG_DIR%"
)

if not "!config_SKIPGENSCENINFILE!"=="" (
    echo [!_Inner_MY_TAG!]:Script csv is exist: !config_SKIPGENSCENINFILE!
    set ARGS=-Uniquetid !config_UNIQUETID! -Etype !config_ETYPE! -Emodel !config_EMODEL! -Pmt !config_PMT! -Mlang !config_MLANG! !arg_config_IDIR! !arg_config_ICFG! -ODir !config_ODIR! !config_SKIPGENAITTS! !arg_config_SKIPGENSCENINFILE! !arg_config_VOICEID!
    echo [!_Inner_MY_TAG!]:###__CheckSTEP__###And This Arguments is !ARGS!
    set CFG_FILE=!config_IDIR!/!config_ICFG!
    echo # # # # check_CFG_FILE:!CFG_FILE!

    if exist "!CFG_FILE!" (
        echo [!_Inner_MY_TAG!]:Running configuration: %%I
        rem # # # # # # # # # # # # # # # # # # # # # #
        rem # # # # # python.exe(AI_SCRIPT) # # # # # #
        rem # # # # # # # # # # # # # # # # # # # # # #
        echo [!_Inner_MY_TAG!]:###__CheckSTEP__### call python.exe "%AI_SCRIPT%" !ARGS!
        call python.exe "%AI_SCRIPT%" !ARGS!
    ) else (
        echo [!_Inner_MY_TAG!]:Warning: No .cfg file found in folder %%I.
    )
    echo [!_Inner_MY_TAG!]:Process completed.
    goto :__MY_INNER_EOF
)

rem Run the Python script to generate a cfg file.(from ~/batch/xxx.csv in the config_BATCHCSV)
echo [!_Inner_MY_TAG!]:rmdir ...%BATCHCFG_DIR%...
rmdir /s /q %BATCHCFG_DIR%

echo [!_Inner_MY_TAG!]:Generating .cfg files... !config_BATCHCSV! !config_UNIQUETID! !config_PMT!

set ARGS=!config_BATCHCSV! !config_UNIQUETID! !config_PMT!
rem # # # # # # # # # # # # # # # # # # # # # # # # #
rem # # # # # python.exe(PY_MAKE_CFG_SCRIPT) # # # # #
rem # # # # # # # # # # # # # # # # # # # # # # # # #
echo [!_Inner_MY_TAG!]:###__CheckSTEP__### call python.exe "%PY_MAKE_CFG_SCRIPT%" !ARGS!
call python.exe "%PY_MAKE_CFG_SCRIPT%" !ARGS!
if %errorlevel% neq 0 (
    echo [!_Inner_MY_TAG!]:Error: Failed to generate .cfg files.
    goto :__MY_INNER_EOF
)

rem Retrieve the list of cfg files.
set CFG_FILES_arr=
set /a CFG_COUNT=0
set /a CFG_FILES_arr.Ubound=0

for /R "%BATCHCFG_DIR%" %%f in (*.cfg) do (
    rem ===> "C:\PycharmProjects\GptApi_ASRAIVoice_wide\res\batchcfg\20241208_171600000\006\"
    set CFG_FILES_arr[!CFG_COUNT!]=%%~dpf
    set /a CFG_COUNT+=1
)

if !CFG_COUNT! LEQ 0 (
    echo [!_Inner_MY_TAG!]:OMG...# # # No .cfg files found in %BATCHCFG_DIR%.
    goto :__MY_INNER_EOF
) else (
    set /a CFG_FILES_arr.Ubound=!CFG_COUNT!-1
)

rem ### for debugging
echo ...
for /L %%I in (0, 1, !CFG_FILES_arr.Ubound!) do (
    echo [!_Inner_MY_TAG!]CFG_FILES_arr[%%I] = !CFG_FILES_arr[%%I]!
)
echo ...
echo [!_Inner_MY_TAG!]:Running .cfg files with AI_ASR_Gen.py... CFG file count is [!CFG_COUNT!]

set /a MISSING_CFG_LIST.length=0
for /L %%I in (0,1,%CFG_FILES_arr.Ubound%) do (
    set CFG_SUBFOLDER=!CFG_FILES_arr[%%I]:~0,-1!
    echo # # # CFG_SUBFOLDER[%%I]:!CFG_SUBFOLDER!

    echo # # BATCHCFG_DIR:!BATCHCFG_DIR!
    echo # # RESULT_DIR[%%I]:!RESULT_DIR!

    for /F "tokens=*" %%a in ('!__shell_cmd_replacestr! !CFG_SUBFOLDER! !BATCHCFG_DIR! !RESULT_DIR!') do (
        set RESULT_SUBFOLDER=%%a
    )
    echo # # # RESULT_SUBFOLDER[%%I]:!RESULT_SUBFOLDER!

    echo [!_Inner_MY_TAG!]:###__CheckSTEP__###CFG Folder is !CFG_SUBFOLDER!
    set ARGS=-Uniquetid !config_UNIQUETID! -Etype !config_ETYPE! -Emodel !config_EMODEL! -Pmt !config_PMT! -Mlang !config_MLANG! -IDir !CFG_SUBFOLDER! !arg_config_ICFG! -ODir !config_ODIR! !config_SKIPGENAITTS! !arg_config_SKIPGENSCENINFILE!
    echo [!_Inner_MY_TAG!]:###__CheckSTEP__### [%%I] And This Arguments is !ARGS!

    set CFG_FILE_FULLPATH=!CFG_SUBFOLDER!\!config_ICFG!
    echo CFG_FILE_FULLPATH:_!CFG_FILE_FULLPATH!_

    if exist "!CFG_FILE_FULLPATH!" (
        echo [!_Inner_MY_TAG!]:###__CheckSTEP__###Running configuration: %%I

        rem GET ___start_each_time
        echo GET ___start_total_time

        for /F "tokens=1-4 delims=:.," %%a in ('!__shell_cmd_curtime2!') do (
            echo "A:" %%a
            echo "B:" %%b
            echo "C:" %%c
            echo "D:" %%d

            set /A "___start_each_time=((((%%a*60)+((100+%%b) %% 100))*60)+((100+%%c) %% 100))"
        )

        rem # # # # # # # # # # # # # # # # # # # # #
        rem # # # # # python.exe(AI_SCRIPT) # # # # #
        rem # # # # # # # # # # # # # # # # # # # # #
        echo [!_Inner_MY_TAG!]:###__CheckSTEP__### [%%I] call python.exe "%AI_SCRIPT%" !ARGS!
        call python.exe "%AI_SCRIPT%" !ARGS!

        rem GET ___end_each_time
        echo GET ___end_each_time

        for /F "tokens=1-4 delims=:.," %%a in ('!__shell_cmd_curtime2!') do (
            echo "A:" %%a
            echo "B:" %%b
            echo "C:" %%c
            echo "D:" %%d

            set /A "___end_each_time=((((%%a*60)+((100+%%b) %% 100))*60)+((100+%%c) %% 100))"
        )

        rem Get ___elapsed_each_time
        set /A ___elapsed_each_time="!___end_each_time! - !___start_each_time!"
        echo "each duration[%%I]:" !___elapsed_each_time!       

        echo [!_Inner_MY_TAG!]:###__CheckSTEP__###_Running [%%I] EACH_TIME : Duration=^> !___elapsed_each_time!
    ) else (
        echo [!_Inner_MY_TAG!]:Warning[%%I]: No .cfg file found in folder.
        goto :__MY_INNER_EOF
    )

    rem Check if the item requires a retry.
    if not exist "!RESULT_SUBFOLDER!" (
        echo [!_Inner_MY_TAG!]:###__CheckSTEP__### [%%I] Folder "!RESULT_SUBFOLDER!" not created. Marking for retry.
        set MISSING_CFG_FOLDER_LIST[!MISSING_CFG_LIST.length!]=!CFG_FOLDER!
        set /a MISSING_CFG_LIST.length=!MISSING_CFG_LIST.length!+1
    )
)

REM Retry missing folders through a loop.
if !MISSING_CFG_LIST.length! equ 0 (
    echo [!_Inner_MY_TAG!]:All configurations processed successfully. No retries needed.
) else (
    echo [!_Inner_MY_TAG!]:Retrying missing Configurations: !MISSING_CFG_LIST.length!
    for %%I in (0,1,!MISSING_CFG_LIST.length!) do (
        set RETRY_CFG_FOLDER=!MISSING_CFG_FOLDER_LIST[%%I]!
        set RETRY_CFG_FILE=!RETRY_CFG_FOLDER!\!config_ICFG!
        set RETRY_COUNT=0
        set RETRY_LIMIT=5

        REM Retry loop up to 5 times.
        call :process_retry
    )
)

echo [!_Inner_MY_TAG!]:Process completed.
goto :__MY_INNER_EOF

:process_retry
if !RETRY_COUNT! geq !RETRY_LIMIT! (
    echo [!_Inner_MY_TAG!]:Maximum retry attempts reached for: !RETRY_CFG_FOLDER!
    exit /b
)

set /a RETRY_COUNT+=1
echo [!_Inner_MY_TAG!]:Attempting retry: !RETRY_CFG_FOLDER! (Attempt !RETRY_COUNT! of !RETRY_LIMIT!)
echo [!_Inner_MY_TAG!]:This is !RETRY_CFG_FILE!
set ARGS=-Uniquetid !config_UNIQUETID! -Etype !config_ETYPE! -Emodel !config_EMODEL! -Pmt !config_PMT! -Mlang !config_MLANG! !RETRY_CFG_FOLDER! !arg_config_ICFG! -ODir !config_ODIR! !config_SKIPGENAITTS! !arg_config_SKIPGENSCENINFILE!
echo [!_Inner_MY_TAG!]:And This Arguments is !ARGS!

if exist "!RETRY_CFG_FILE!" (
    echo [!_Inner_MY_TAG!]:Running configuration: !RETRY_CFG_FILE!
    rem # # # # # # # # # # # # # # # # # # # # #
    rem # # # # # python.exe(AI_SCRIPT) # # # # #
    rem # # # # # # # # # # # # # # # # # # # # #
    echo [!_Inner_MY_TAG!]:###__CheckSTEP__### call python.exe "%AI_SCRIPT%" !ARGS!
    call python.exe "%AI_SCRIPT%" !ARGS!
) else (
    echo [!_Inner_MY_TAG!]:Warning: No .cfg file found in folder !RETRY_CFG_FOLDER!.
)

REM Check if the item requires retry.
for /F "tokens=*" %%a in ('!__shell_cmd_replacestr! !RETRY_CFG_FOLDER! !BATCHCFG_DIR! !RESULT_DIR!') do (
    set RESULT_SUBFOLDER=%%a
)

if exist "!RESULT_SUBFOLDER!" (
    echo [!_Inner_MY_TAG!]:Make All Files for !RETRY_CFG_FILE!, Skipping...
    exit /b
) else (
    REM Reinvoke the loop to retry.
    call :process_retry
    exit /b
)

:__MY_INNER_EOF
echo [%_SDF_MY_TAG%]:###__CheckSTEP__#### # # # # __MY_INNER_EOF # # # # #

rem GET ___end_total_time
echo GET ___end_total_time

for /F "tokens=1-4 delims=:.," %%a in ('!__shell_cmd_curtime2!') do (
    echo "A:" %%a
    echo "B:" %%b
    echo "C:" %%c
    echo "D:" %%d

    set /A "___end_total_time=((((%%a*60)+((100+%%b) %% 100))*60)+((100+%%c) %% 100))"
)

rem Get ___elapsed_total_time
set /A ___elapsed_total_time="!___end_total_time!-!___start_total_time!"

echo "total duration:" !___elapsed_total_time!

echo [!_Inner_MY_TAG!]:###__CheckSTEP__###_Running TOTAL_TIME : Duration=^> !___elapsed_total_time!

endlocal
popd