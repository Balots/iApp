@echo off
chcp 65001 > nul
setlocal enabledelayedexpansion

:: Ввод имени хоста
set /p "input=Введите имя хоста: "
set "HOST=!input!"

:: Настройка лог-файла
set "logfile=script_ip.log"

:: Получение IP-адреса
set "ip="
for /f "tokens=2 delims=:" %%I in ('psexec \\!HOST! ipconfig ^| findstr "IPv4" 2^>^&1') do (
    set "ip=%%I"
    set "ip=!ip: =!"
)

:: Логирование с универсальным форматом даты
for /f "tokens=1-6 delims=/:. " %%a in ("%date% %time%") do (
    set "datetime=%%c-%%b-%%a %%d:%%e:%%f"
)

echo !datetime!    PC:!HOST!    !ip! >> "!logfile!"
echo Результат записан в !logfile!
exit /b 0