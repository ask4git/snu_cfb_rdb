#!/bin/sh
# shellcheck disable=SC2164
cd /Users/ask4git/snu_cfb_rdb/snu_cfb_rdb
python manage.py graph_models -a > graph_model.dot
dot -Tpng graph_model.dot -o graph_model.png