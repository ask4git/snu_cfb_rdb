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
        from cfb_rdb.models import Kegg, Pathway, PathwaySub

        bulk_data = []
        path_csv_file = '/Users/ask4git/Desktop/snu_csv_files/kegg_pathway/pathway_sub.tsv'

        with open(path_csv_file, encoding='utf-8') as in_csv_file:
            rdr = csv.reader(in_csv_file, delimiter='\t')   # tsv

            for row in rdr:
                _id, _name, _sid = row
                # _id, _name, _ps, _p = row[0], row[1], None, None
                # if len(row) == 4:
                #     _ps = PathwaySub(pathway_sub_id=int(row[2]))
                #     print(_ps)
                #     _p = Pathway(pathway_id=int(row[3]))

                # print(_id, _name, _ps, _p)
                bulk_data.append(
                    PathwaySub(pathway_sub_id=_id,
                            pathway_sub_name=_name,
                            pathway_name=Pathway(pathway_id=_sid)
                            ))

        PathwaySub.objects.bulk_create(bulk_data)

    except ImportError as exc:
        raise ImportError(
            "Couldn't import module. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc


bulk()
