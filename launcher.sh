#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python scripts, then back home

cd /
cd /home/pi/Smart-Mirror-With-Halloween-Jump-Scare
sudo python smartmirror.py &
sleep 10
sudo python jumpscare.py &
cd /

