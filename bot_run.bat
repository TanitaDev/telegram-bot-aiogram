@echo off

call %~dp0telegram_bot\venv\Scripts\activate

cd %~dp0telegram_bot

set TOKEN=5815856150:AAGVN1VpgKJpj1233Ady9gNTLjPAYvw378A

python bot_telegram.py

pause