#!/usr/bin/env sh

sudo apt-get update
sudo apt-get install python3-pip git
sudo /usr/bin/git clone --depth 1 https://github.com/shabane/gitlynx.git ~/gitlynx
/usr/bin/pip install -r ~/gitlynx/requirements.txt
/usr/bin/python3 -m streamlit run main.py
