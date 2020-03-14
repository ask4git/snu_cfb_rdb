"""
bulk.py
"""
# -*- coding: utf-8 -*-

import os
import django
import csv


def foo(lst):
    re = []
    for item in lst:
        if item != '':
            re.append(item)
    return re


def bulk():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'snu_cfb_rdb.settings')
    django.setup()
    try:
        from cfb_rdb.models import Kegg, KeggMaster

        bulk_data = []
        path_csv_file = '/Users/ask4git/Desktop/snu_csv_files/kegg_pathway/kegg_master.tsv'

        # kegg master ========================
        #
        # with open(path_csv_file, encoding='utf-8') as in_csv_file:
        #     rdr = csv.reader(in_csv_file, delimiter='\t')  # tsv
        #
        #     for row in rdr:
        #         _kid, _dis, _rel, _gen = row
        #
        #         # kegg_name
        #         _id = Kegg.objects.filter(uid=_kid)[0].id
        #         print(_id)
        #         print(_kid, _rel, _dis, _gen )
        #
        #         res = KeggMaster(
        #             kegg_name=Kegg(id=_id),
        #             related_pathway=foo(_rel.strip().split(';')),
        #             disease_list=foo(_dis.strip().split(';')),
        #             gene_list=foo(_gen.strip().split(';'))
        #         )
        #
        #         bulk_data.append(res)
        #
        #     KeggMaster.objects.bulk_create(bulk_data)

        # ====================================

        # kegg ========================
        # bulk_data = []
        # path_csv_file = '/Users/ask4git/Desktop/snu_csv_files/kegg_pathway/kegg.tsv'
        #
        # with open(path_csv_file, encoding='utf-8') as in_csv_file:
        #     rdr = csv.reader(in_csv_file, delimiter='\t')   # tsv
        #
        #     for row in rdr:
        #
        #         if len(row) == 2:
        #             _uid, _name = row
        #             bulk_data.append(Kegg(
        #                 uid=str("hsa" + _uid),
        #                 name=str(_name),
        #                 pathway_sub=None,
        #                 pathway_type = None
        #             ))
        #         else:
        #             _uid, _name, _sid, _tid = row
        #             print(type(_tid), type(_sid))
        #             bulk_data.append(Kegg(
        #                 uid=str("hsa" + _uid),
        #                 name=str(_name),
        #                 pathway_sub=PathwaySub(uid=_sid),
        #                 pathway_type=PathwayType(uid=_tid)
        #             ))
        #
        # Kegg.objects.bulk_create(bulk_data)
        # =============================

    except ImportError as exc:
        raise ImportError(
            "Couldn't import module. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc


bulk()
