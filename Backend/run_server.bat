@echo off
echo Starting NanoGPT API Server...
cd /d "%~dp0"
uvicorn main:app --reload --host 0.0.0.0 --port 8000
