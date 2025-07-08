@echo off
chcp 65001 > nul
setlocal enabledelayedexpansion
set logfile=test.log
psexec \\upr5-temp reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall >> "%logfile%"
psexec \\upr5-temp reg query HKLM\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall >> "%logfile%"