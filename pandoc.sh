#!/bin/bash

sudo add-apt-repository -y ppa:ubuntu-toolchain-r/test
  # Update
sudo apt-get update -qq
sudo apt install -y pandoc

pandoc README.md -f markdown -t html -s -o main_page/home_page_files/readme.html --email-obfuscation=javascript
mv main_page/* ./
