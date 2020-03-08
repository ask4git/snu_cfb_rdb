#!/bin/sh
# shellcheck disable=SC2164
cd /Users/ask4git/snu_cfb_rdb/snu_cfb_rdb
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete