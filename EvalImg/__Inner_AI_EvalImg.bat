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

rem # # # # # # # # # # # # # # # # override config values # # # # # # # # # # # # # # # #
set config_UNIQUETID=
FOR /f "tokens=*" %%F IN ('!__shell_cmd_curmillifilename!') DO (
    set config_UNIQUETID=%%F
)
if "!config_UNIQUETID!"=="" (
    echo [!_Inner_MY_TAG!]:config_UNIQUETID is NULL~~~
    goto :__MY_INNER_EOF
)

set config_IDIR=

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
if "!config_IDIR!"=="" (
    rem do nothing
    set arg_config_IDIR=
) else (
    set arg_config_IDIR=!config_IDIR!
)

rem Change the existing BATCH_DIR related path configuration to be based on XXX_HOME.
set BATCHCFG_DIR=%AI_EVAL_IMG_RES%\batchcfg\!config_UNIQUETID::skip=!
for %%I in ("%BATCHCFG_DIR%") do set BATCHCFG_DIR=%%~fI
set AI_SCRIPT=%AI_EVAL_IMG_HOME%\AI_Eval_Img.py
set RESULT_DIR=%config_ODIR%\!config_UNIQUETID::skip=!

rem Initial message output
echo [!_Inner_MY_TAG!]:# # # # # # # # # # # # Starting batch process...
echo [!_Inner_MY_TAG!]:Batch directory: !BATCHCFG_DIR!
echo [!_Inner_MY_TAG!]:Result directory: !RESULT_DIR!

rem MakeDir for UNIQUETID.
set ARGS=-Uniquetid !config_UNIQUETID! -Etype !config_ETYPE! -Emodel !config_EMODEL! -Pmt !config_PMT! -Mlang !config_MLANG! -SCount !config_SCOUNT! -TNum !config_TNUM! -IDir !config_IDIR! -Icsv !config_ICSV! -IInImgDir !config_IINIMGDIR! -IOutImgDir !config_IOUTIMGDIR! -ODir !config_ODIR!
echo [!_Inner_MY_TAG!]:###__CheckSTEP__###And This Arguments is !ARGS!

echo [!_Inner_MY_TAG!]:Running configuration: AI_SCRIPT
rem # # # # # # # # # # # # # # # # # # # # # #
rem # # # # # python.exe(AI_SCRIPT) # # # # # #
rem # # # # # # # # # # # # # # # # # # # # # #
echo [!_Inner_MY_TAG!]:###__CheckSTEP__### call python.exe "%AI_SCRIPT%" !ARGS!
call python.exe "%AI_SCRIPT%" !ARGS!

echo [!_Inner_MY_TAG!]:Process completed.
goto :__MY_INNER_EOF

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