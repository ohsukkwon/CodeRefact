@echo off

pushd "%~dp0"

if "%__MagicLampJar%"=="" (
    set _import_MY_TAG=%~n0
)
echo.

setlocal enabledelayedexpansion

echo [!_import_MY_TAG!]:GEN_ASR_AIvoice_HOME:"%GEN_ASR_AIvoice_HOME%"
if "%GEN_ASR_AIvoice_HOME%"=="" (
	echo [!_import_MY_TAG!]:# OMG. GEN_ASR_AIvoice_HOME is NULL.
	goto __MY_import_EOF
)

echo [!_import_MY_TAG!]:GEN_ASR_AIvoice_RES:"%GEN_ASR_AIvoice_RES%"
if "%GEN_ASR_AIvoice_RES%"=="" (
	echo [!_import_MY_TAG!]:# OMG. GEN_ASR_AIvoice_RES is NULL.
	goto __MY_import_EOF
)

echo [!_import_MY_TAG!]:GEN_ASR_AIvoice_RESULT:"%GEN_ASR_AIvoice_RESULT%"
if "%GEN_ASR_AIvoice_RESULT%"=="" (
	echo [!_import_MY_TAG!]:# OMG. GEN_ASR_AIvoice_RESULT is NULL.
	goto __MY_import_EOF
)
endlocal

if "%__MagicLampJar%"=="" (
    set __MagicLampJar=.\MagicLamp\MagicLamp.jar
)

if "%__shell_cmd_genargskey%"=="" (
    set __shell_cmd_genargskey=java -jar %__MagicLampJar% FAKESN genargskey
)

if "%__shell_cmd_genargsval%"=="" (
    set __shell_cmd_genargsval=java -jar %__MagicLampJar% FAKESN genargsval
)

if "%__shell_cmd_curmillifilename%"=="" (
    set __shell_cmd_curmillifilename=java -jar %__MagicLampJar% FAKESN curmillifilename
)

if "%__shell_cmd_curtime2%"=="" (
    set __shell_cmd_curtime2=java -jar %__MagicLampJar% FAKESN curtime2
)

if "%__shell_cmd_replacestr%"=="" (
    set __shell_cmd_replacestr=java -jar %__MagicLampJar% FAKESN replacestr
)

:__MY_import_EOF
endlocal
popd