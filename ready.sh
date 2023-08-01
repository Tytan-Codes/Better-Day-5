#!/bin/bash

echo 'Hello and welcome. Would you:'
echo '(1) Install'
echo '(2) Update'

read choice

if [ "$choice" = "1" ]; then
echo "Performing installation..."
apt-get install git -y && apt-get install python3 -y 
git clone https://github.com/tytan-codes/better-day-5.git
cd better-day-5
pip install -r requirements.txt && python3 main.py
# Insert your installation code here
elif [ "$choice" = "2" ]; then
echo "Performing update..."
rm -rf better-day-5
git clone https://github.com/tytan-codes/better-day-5.git
cd better-day-5
python3 main.py
# Insert your update code here
else
echo "Invalid choice. Exiting..."
fi
