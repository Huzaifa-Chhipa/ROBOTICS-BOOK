@echo off
REM Script to start both backend and frontend for the robotics book chatbot
REM Usage: start_chatbot.bat

echo Starting the Physical AI & Humanoid Robotics Book Chatbot...

echo.
echo NOTE: This script will start both the backend and frontend in separate windows.
echo Make sure you have Python and Node.js installed before running this script.
echo.

echo Starting backend server...
start cmd /k "cd backend && python -m src.main"

timeout /t 5 /nobreak >nul

echo Starting frontend server...
start cmd /k "npm start"

echo.
echo Both servers should now be running:
echo - Backend: http://localhost:8000
echo - Frontend: http://localhost:3000
echo.
echo The chatbot will be available on the frontend website!
echo.
pause