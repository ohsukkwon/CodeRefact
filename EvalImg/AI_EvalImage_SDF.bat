@echo off
rem # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
rem # # # # #    DO NOT USE arg(%1 %2 %3 ... %9). Do use it with custom_arg(_SDF_arr[0] , _SDF_arr[1] , _SDF_arr[2] and _SDF_xxxx ....) # # # # #
rem # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
rem AI_EvalImage_SDF.bat

pushd "%~dp0"
call _import_vars.bat

set _SDF_MY_TAG=%~n0
echo [%_SDF_MY_TAG%]:###__CheckSTEP__#### # # # # # # # Greeting_ASR_SDF WORLD~ # # # # # # # #
echo.

setlocal enabledelayedexpansion

rem # # # # # # # # # # # # # # # # override config values # # # # # # # # # # # # # # # #
set _SDF_config_UNIQUETID=
FOR /f "tokens=*" %%F IN ('!__shell_cmd_curmillifilename!') DO (
    set _SDF_config_UNIQUETID=%%F
)
if "!_SDF_config_UNIQUETID!"=="" (
    echo [!_SDF_MY_TAG!]:_SDF_config_UNIQUETID is NULL~~~
    goto :__MY_SDF_EOF
)

set _SDF_config_MLANG=Korean
set _SDF_config_SCOUNT=2
set _SDF_config_TNUM=10

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

rem # # # # # DONE Overwrite Routine # # # # # # # # # # # # # # # # # #
if "!_SDF_config_MLANG!"=="" (
    rem do nothing
) else (
    set _SDF_config_MLANG=-MLANG::!_SDF_config_MLANG!
)

if "!_SDF_config_SCOUNT!"=="" (
    rem do nothing
) else (
    set _SDF_config_SCOUNT=-SCOUNT::!_SDF_config_SCOUNT!
)

if "!_SDF_config_TNUM!"=="" (
    rem do nothing
) else (
    set _SDF_config_TNUM=-TNUM::!_SDF_config_TNUM!
)

rem _______| "-UNIQUETID::" | "-ETYPE::" | "-EMODEL::" | "-PMT::" | "-MLANG::" | "-SCOUNT::" | "-TNUM::" | "-IDIR::" | "-ICSV::" | "-IINIMGDIR::" | "-IOUTIMGDIR::" | "-ODIR::" |
set _SDF_pass_to_args="-UNIQUETID::!_SDF_config_UNIQUETID!" "-ETYPE::!_SDF_config_ETYPE!" "-EMODEL::!_SDF_config_EMODEL!" "-PMT::!_SDF_config_PMT!" "!_SDF_config_MLANG!" "!_SDF_config_SCOUNT!" "!_SDF_config_TNUM!" "-IDIR::!_SDF_config_IDIR!" "-ICSV::!_SDF_config_ICSV!" "-IINIMGDIR::!_SDF_config_IINIMGDIR!" "-IOUTIMGDIR::!_SDF_config_IOUTIMGDIR!" "-ODIR::!_SDF_config_ODIR!"

echo [%_SDF_MY_TAG%]:###__CheckSTEP__### call __Inner_AI_EvalImg.bat !_SDF_pass_to_args!
call __Inner_AI_EvalImg.bat !_SDF_pass_to_args!

:__MY_SDF_EOF
echo [%_SDF_MY_TAG%]:###__CheckSTEP__#### # # # # __MY_SDF_EOF # # # # #
endlocal
popd