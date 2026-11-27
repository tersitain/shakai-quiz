#!/bin/sh
# 問題（q.txt）や画面（tpl.html）を直したあとに実行すると、公開用の index.html と sw.js を作り直す
set -e
cd "$(dirname "$0")"
mkdir -p app && cp ../sw.js app/sw.js
python3 -I build.py
python3 -I mkapp.py
cp app/index.html app/sw.js ..
rm -rf app index.html
