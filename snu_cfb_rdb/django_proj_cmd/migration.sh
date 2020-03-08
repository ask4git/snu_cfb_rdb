#!/bin/sh
# shellcheck disable=SC2164
cd /Users/ask4git/snu_cfb_rdb/snu_cfb_rdb
python manage.py makemigrations cfb_rdb
python manage.py migrate cfb_rdb