#!/bin/sh
echo 'this shell script make snu_cfb_rdb local server'
cd /Users/ask4git/snu_cfb_rdb
source venv/bin/activate
python ./snu_cfb_rdb/manage.py runserver