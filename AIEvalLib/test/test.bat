@echo off

echo Greeting test world~ %~n0

echo ___________________1____________________
echo __Dir_GPTHOME:%__Dir_GPTHOME%
echo __Excelxlsb:%__Excelxlsb%
echo __MagicLampJar:%__MagicLampJar%
echo __shell_cmd_getargscount:%__shell_cmd_getargscount%

setlocal EnableDelayedExpansion
echo ___________________2____________________
echo __Dir_GPTHOME:%__Dir_GPTHOME%
echo __Excelxlsb:%__Excelxlsb%
echo __MagicLampJar:%__MagicLampJar%
echo __shell_cmd_getargscount:%__shell_cmd_getargscount%
call _import_vars.bat

echo ___________________3____________________
echo __Dir_GPTHOME:%__Dir_GPTHOME%
echo __Excelxlsb:%__Excelxlsb%
echo __MagicLampJar:%__MagicLampJar%
echo __shell_cmd_getargscount:%__shell_cmd_getargscount%

set AAA="D:\00_Dev\SvcApp2\SvcApp2_sukkwon.oh_W02\TEAM\SQE\KOR\ServiceApp2\iAutoEvaluation"\result\output\Korean_English\R3CW90EJ80P
set BBB=
echo AAA_1:!AAA!
echo BBB_1:!BBB!
if not "!BBB!"=="" (
    echo BBB_2:!BBB:"=!
) else (
    echo BBB_2:!BBB!
)
echo BBB_3:!BBB:"=!


endlocal

@echo on