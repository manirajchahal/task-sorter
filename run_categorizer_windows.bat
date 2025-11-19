@echo off
REM Run the task categorizer from the folder this script is in
cd /d "%~dp0"
python categorize_tasks.py
pause
