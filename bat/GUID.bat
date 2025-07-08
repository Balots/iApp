@echo off
setlocal enabledelayedexpansion
set /p input=""

:: Укажите нужный GUID программы
set "GUID=!input!"

:: Проверяем разделы реестра (64-бит и 32-бит)
for %%R in (
    "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\!GUID!"
    "HKLM\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\!GUID!"
) do (
    for /f "tokens=2,*" %%A in (
        'reg query %%~R /v DisplayName 2^>nul ^| find "REG_SZ"'
    ) do (
        echo %%B
    )
)

exit \b