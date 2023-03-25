#!/bin/bash
cd //home/a/Desktop/project/dash_board
python3 manage.py runserver &
sleep 10
chromium-browser --app=http://localhost:8000 &
