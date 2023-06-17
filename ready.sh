#!/bin/bash

echo 'Hello and welcome. Would you:'
echo '(1) Install'
echo '(2) Update'

read choice

if [ "$choice" = "1" ]; then
echo "Performing installation..."
git clone https://oauth2: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@github.com/tytan-codes/better-day-5.git
# Insert your installation code here
elif [ "$choice" = "2" ]; then
echo "Performing update..."
rm -rf better-day-5
git clone https://oauth2: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@github.com/tytan-codes/better-day-5.git
cd better-day-5
python3 main.py
# Insert your update code here
else
echo "Invalid choice. Exiting..."
fi
