@echo off
setlocal EnableDelayedExpansion

REM Set the main directories
set MAIN_DIR_PARENT=%GEN_ASR_AIvoice_HOME%\..
IF "%MAIN_DIR_PARENT%"=="\.." set MAIN_DIR_PARENT=%~dp0

set MAIN_DIR=%GEN_ASR_AIvoice_HOME%
IF "%MAIN_DIR%"=="" set MAIN_DIR=%~dp0

set Batch_CFG_DIR=%MAIN_DIR_PARENT%\res\batchcfg
set RES_DIR=%MAIN_DIR_PARENT%\result\output\__ASR__
set PYTHON_SCRIPT=%MAIN_DIR%\AI_ASR_Gen.py
set UTILS_DIR=%MAIN_DIR%\utils

echo MAIN_DIR_PARENT:%MAIN_DIR_PARENT%
echo MAIN_DIR:%MAIN_DIR%
echo Batch_CFG_DIR:%Batch_CFG_DIR%
echo RES_DIR:%RES_DIR%
echo PYTHON_SCRIPT:%PYTHON_SCRIPT%
echo UTILS_DIR:%UTILS_DIR%
      
REM Initialize PYTHONPATH with the main directory and add all subdirectories, including \utils
set PYTHONPATH=%MAIN_DIR%;%UTILS_DIR%
for /r "%MAIN_DIR%" %%d in (.) do (
    set PYTHONPATH=%PYTHONPATH%;%%d
)
echo %PYTHONPATH%

REM Set Python IO encoding to UTF-8 to avoid encoding issues
set PYTHONIOENCODING=utf-8

set /a FolderCount=0
echo dir /a-s-h /b %Batch_CFG_DIR%
for /f %%a in ('dir /a-s-h /b %Batch_CFG_DIR%') do (
	echo count : %%a
	set /a FolderCount+=1
)
echo FolderCount:%FolderCount%
echo ... 

REM Run the Python script for each .cfg file in the Batch_CFG_DIR
for /f %%a in ('dir /a-s-h /b %Batch_CFG_DIR%') do (
	for /f %%b in ('dir /a-s-h /b %Batch_CFG_DIR%\%%a\') do (
		set cfg_file_name=%%b
	)
	echo cfg_file_name:!cfg_file_name!
    echo Processing %Batch_CFG_DIR%\%%a\!cfg_file_name!
	set ARGS=-Etype openai -Emodel gpt-4o -TNum 1 --noresponseinout --skipgenaitts -Pmt genasrconversation -Mlang Korean -IDir %Batch_CFG_DIR%\%%a\ -ODir %RES_DIR%
    cmd /c "set PYTHONPATH=%PYTHONPATH% & python.exe %PYTHON_SCRIPT% !ARGS! -Icfg !cfg_file_name!"
)
echo All scenarios processed.