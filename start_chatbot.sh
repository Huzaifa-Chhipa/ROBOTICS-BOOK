#!/bin/bash
# Script to start both backend and frontend for the robotics book chatbot
# Usage: ./start_chatbot.sh

echo "Starting the Physical AI & Humanoid Robotics Book Chatbot..."

echo
echo "NOTE: This script will start both the backend and frontend in separate processes."
echo "Make sure you have Python and Node.js installed before running this script."
echo

# Start the backend server in the background
echo "Starting backend server..."
cd backend
python -m src.main > backend.log 2>&1 &
BACKEND_PID=$!
cd ..

# Wait a few seconds for the backend to start
sleep 5

# Start the frontend server
echo "Starting frontend server..."
npm start

echo
echo "Servers should be running:"
echo "- Backend: http://localhost:8000 (PID: $BACKEND_PID)"
echo "- Frontend: http://localhost:3000"
echo
echo "The chatbot will be available on the frontend website!"
echo

# Clean up: kill backend when script exits
trap "kill $BACKEND_PID 2>/dev/null" EXIT