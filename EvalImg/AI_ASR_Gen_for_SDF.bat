@echo off
rem # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
rem # # # # #    DO NOT USE arg(%1 %2 %3 ... %9). Do use it with custom_arg(_SDF_arr[0] , _SDF_arr[1] , _SDF_arr[2] and _SDF_xxxx ....) # # # # #
rem # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
rem AI_ASR_Gen_for_SDF.bat

pushd "%~dp0"
call _import_vars.bat

set _SDF_MY_TAG=%~n0
echo [%_SDF_MY_TAG%]:###__CheckSTEP__#### # # # # # # # Greeting_ASR_SDF WORLD~ # # # # # # # #
echo.

setlocal enabledelayedexpansion

set _SDF_config_UNIQUETID=
FOR /f "tokens=*" %%F IN ('!__shell_cmd_curmillifilename!') DO (
    set _SDF_config_UNIQUETID=%%F
)
if "!_SDF_config_UNIQUETID!"=="" (
    echo [!_SDF_MY_TAG!]:_SDF_config_UNIQUETID is NULL~~~
    goto :__MY_SDF_EOF
)

set _SDF_config_ETYPE=openai
rem set _SDF_config_EMODEL=gpt-4o
set _SDF_config_EMODEL=gpt-4o-2024-11-20
rem set _SDF_config_SKIPGENSCENINFILE=C:\GptApi_ASRAIVoice_wide\result\20241205_042901000\001\result_~~~.csv
set _SDF_config_SKIPGENSCENINFILE=
set _SDF_config_VOICEID=
rem set _SDF_config_SKIPGENAITTS=--skipgenaitts
set _SDF_config_SKIPGENAITTS=
set _SDF_config_PMT=genasrconversation
set _SDF_config_MLANG=English
set _SDF_config_ODIR=%GEN_ASR_AIvoice_RESULT%\__SDF__
set _SDF_config_IDIR=
set _SDF_config_ICFG=
set _SDF_config_BATCHCSV=

set _SDF_ALL_ARGS=%*
echo [%_SDF_MY_TAG%]:###__CheckSTEP__###_SDF_ALL_ARGS:!_SDF_ALL_ARGS!

if "!_SDF_ALL_ARGS!"=="" (
    echo [%_SDF_MY_TAG%]:# OMG. _SDF_ALL_ARGS is NULL.
    goto :__MY_SDF_EOF
)

set _CONV_Inner_ALL_ARGS=!_SDF_ALL_ARGS:"=!
echo [%_SDF_MY_TAG%]:_CONV_Inner_ALL_ARGS : _____!_CONV_Inner_ALL_ARGS!_____
echo [%_SDF_MY_TAG%]:_CONV_Inner_ALL_ARGS ==^> _____!_CONV_Inner_ALL_ARGS: =" "!_____

set _SDF_arr.length=0
for %%I in ("!_CONV_Inner_ALL_ARGS: =" "!") do (
    set _tmp_val=%%I

    if !_tmp_val!=="" (
        echo.
    ) else (
        echo [%_SDF_MY_TAG%]:_tmp_val:!_tmp_val!
        set _SDF_arr[!_SDF_arr.length!]=!_tmp_val:"=!

        set /a _SDF_arr.length=!_SDF_arr.length! + 1
    )
)
set /a _SDF_arr.Ubound=!_SDF_arr.length! - 1

echo [%_SDF_MY_TAG%]:_SDF_ALL_ARGS:!_SDF_ALL_ARGS!
echo [%_SDF_MY_TAG%]:_SDF_arr.length:!_SDF_arr.length! , _SDF_arr.Ubound:!_SDF_arr.Ubound!

rem # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
rem # # # # # Overwrite _SDF_config_XXXXXXXX variables HERE. # # # # #
rem # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
for /L %%I in (0, 1, !_SDF_arr.Ubound!) do (
    FOR /f "tokens=*" %%o IN ('!__shell_cmd_genargskey! "!_SDF_arr[%%I]!"') DO (
        set __args_key=%%o
    )

    FOR /f "tokens=*" %%o IN ('!__shell_cmd_genargsval! "!_SDF_arr[%%I]!"') DO (
        set __args_val=%%o
    )
    echo [%_SDF_MY_TAG%]:_SDF_arr[%%I]:!__args_key!_____!__args_val!
    set _SDF_config_!__args_key!=!__args_val!
    echo [%_SDF_MY_TAG%]: _SDF_config_!__args_key!:_____!__args_val!_____
)
rem # # # # # DONE Overwrite  # # # # # # # # # # # # # # # # # #
if "!_SDF_config_SKIPGENAITTS!"=="" (
    rem do nothing
) else (
    set _SDF_config_SKIPGENAITTS=-SKIPGENAITTS::!_SDF_config_SKIPGENAITTS!
)

if "!_SDF_config_SKIPGENSCENINFILE!"=="" (
    rem do nothing
) else (
    set _SDF_config_SKIPGENSCENINFILE=-SKIPGENSCENINFILE::!_SDF_config_SKIPGENSCENINFILE!
)

if "!_SDF_config_VOICEID!"=="" (
    rem do nothing
) else (
    set _SDF_config_VOICEID=-VOICEID::!_SDF_config_VOICEID!
)

if "!_SDF_config_IDIR!"=="" (
    rem do nothing
) else (
    set _SDF_config_IDIR=-IDIR::!_SDF_config_IDIR!
)

if "!_SDF_config_ICFG!"=="" (
    rem do nothing
) else (
    set _SDF_config_ICFG=-ICFG::!_SDF_config_ICFG!
)

if "!_SDF_config_BATCHCSV!"=="" (
    rem do nothing
) else (
    set _SDF_config_BATCHCSV=-BATCHCSV::!_SDF_config_BATCHCSV!
)

rem # # # TRUE : IF last char is "\",
if "!_SDF_config_BATCHCSV:~-1!"=="\" (
    rem # # # remove last char("\")
    set _SDF_config_BATCHCSV=!_SDF_config_BATCHCSV:~0,-1!
)

rem _______| "-UNIQUETID::!_SDF_config_UNIQUETID!" | "!_SDF_config_BATCHCSV!" | "-ETYPE::" | "-EMODEL::" | "-PMT::!_SDF_config_PMT!" | "-MLANG::!_SDF_config_MLANG!" | "!_SDF_config_IDIR!" | "!_SDF_config_ICFG!" | !_SDF_config_SKIPGENAITTS! | "-ODIR::!_SDF_config_ODIR!" |
set _SDF_pass_to_args="-UNIQUETID::!_SDF_config_UNIQUETID!" "!_SDF_config_BATCHCSV!"       "-ETYPE::!_SDF_config_ETYPE!" "-EMODEL::!_SDF_config_EMODEL!" "-PMT::!_SDF_config_PMT!" "-MLANG::!_SDF_config_MLANG!" "!_SDF_config_IDIR!" "!_SDF_config_ICFG!" "-ODIR::!_SDF_config_ODIR!" "!_SDF_config_SKIPGENAITTS!" "!_SDF_config_SKIPGENSCENINFILE!" "!_SDF_config_VOICEID!"

echo [%_SDF_MY_TAG%]:###__CheckSTEP__### call __Inner_AI_ASR_Gen.bat !_SDF_pass_to_args!
call __Inner_AI_ASR_Gen.bat !_SDF_pass_to_args!

:__MY_SDF_EOF
echo [%_SDF_MY_TAG%]:###__CheckSTEP__#### # # # # __MY_SDF_EOF # # # # #
endlocal
popd