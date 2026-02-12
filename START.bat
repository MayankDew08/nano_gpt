@echo off
echo ========================================
echo   Shakespeare's Digital Quill Launcher
echo ========================================
echo.
echo Starting Backend API...
cd /d "%~dp0Backend"
start "NanoGPT Backend" cmd /k "uvicorn main:app --reload"
timeout /t 3 /nobreak > nul

echo.
echo Starting Frontend Server...
cd /d "%~dp0Frontend"
start "Shakespeare Frontend" cmd /k "python -m http.server 8080"
timeout /t 2 /nobreak > nul

echo.
echo ========================================
echo   Both servers are starting!
echo ========================================
echo.
echo Backend API: http://localhost:8000
echo Frontend UI: http://localhost:8080
echo API Docs: http://localhost:8000/docs
echo.
echo Press any key to open the frontend in your browser...
pause > nul
start http://localhost:8080
