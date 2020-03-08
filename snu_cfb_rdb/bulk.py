"""
bulk.py
"""
# -*- coding: utf-8 -*-

import os
import django
import csv


def bulk():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'snu_cfb_rdb.settings')
    django.setup()
    try:
        from cfb_rdb.models import Kegg, PathwayType, PathwaySub

        bulk_data = []
        path_csv_file = '/Users/ask4git/Desktop/snu_csv_files/kegg_pathway/kegg.tsv'

        with open(path_csv_file, encoding='utf-8') as in_csv_file:
            rdr = csv.reader(in_csv_file, delimiter='\t')   # tsv

            for row in rdr:

                if len(row) == 2:
                    _uid, _name = row
                    bulk_data.append(Kegg(
                        uid=str(_uid),
                        name=str(_name),
                        pathway_type=None,
                        pathway_sub=None
                    ))
                else:

                    _uid, _name, _sid, _tid = row
                    print(type(_tid), type(_sid))
                    bulk_data.append(Kegg(
                        uid=str(_uid),
                        name=str(_name),

                        pathway_sub=PathwaySub(uid=_sid),
                        pathway_type=PathwayType(uid=_tid)
                    ))

        Kegg.objects.bulk_create(bulk_data)

    except ImportError as exc:
        raise ImportError(
            "Couldn't import module. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc


bulk()
