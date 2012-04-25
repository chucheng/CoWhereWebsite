#!/bin/sh
git checkout /home/chucheng/project/gituhb/BridgeServer/src/AirBridge.py
git pull
sed -i "s/PRODUCTION_MODE = False/PRODUCTION_MODE = True/g" /home/chucheng/project/gituhb/BridgeServer/src/AirBridge.py
echo "s/PRODUCTION_MODE = False/PRODUCTION_MODE = True/g"
