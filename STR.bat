@echo off
call %userprofile%\anaconda3\Scripts\activate.bat speech-to-rag
python talk3.py
rem python xtalk.py
cmd /k