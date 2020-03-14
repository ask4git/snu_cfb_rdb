"""
db_normalization.py
"""
# -*- coding: utf-8 -*-

import os
import csv

from tqdm import tqdm
from os.path import join as pjoin


in_file_name = 'Pathway.csv'
out_file_name = '_Pathway.csv'
path_desktop = '/Users/ask4git/Desktop/'

path_in_file = pjoin(path_desktop, in_file_name)
path_out_file = pjoin(path_desktop, out_file_name)


def csv_to_tsv(csv_fname, tsv_fname):
    with open(csv_fname, encoding='utf-8') as in_csv_file, \
            open(tsv_fname, 'w', encoding='utf-8') as out_csv_file:

        reader = csv.reader(in_csv_file, delimiter=',')
        writer = csv.writer(out_csv_file, delimiter='\t')

        # Doing something ==================================
        for index, row in tqdm(enumerate(reader)):
            writer.writerow(row)
    print(f'Convert finish!: {os.path.basename(csv_fname)} -> {os.path.basename(tsv_fname)}')


def delete_duplicate_item(tgt_list):
    res = set()
    for item in tgt_list:
        res.add(item.strip())
    return list(res)


def sort_dict(tgt_dict):
    tgt_dict = sorted(tgt_dict.items())
    return dict(tgt_dict)


def add_dict_item(tgt_dict, k, v):
    if k in tgt_dict:
        tgt_dict[k].append(v)
    else:
        tgt_dict[k] = [v]


def insert_dict(tgt_dict, k, v):
    if k in tgt_dict:
        if v != tgt_dict[k]:
            print('?')
            # print(k, tgt_dict[k])
            # print(k, v)
    else:
        tgt_dict[k] = v


def check_duplicate(tgt_set, item):
    if item in tgt_set:
        pass
        print(item)
    else:
        tgt_set.add(item)


def convert():
    result_dict = {}
    with open(path_in_file, encoding='utf-8') as in_csv_file,\
            open(path_out_file, 'w', encoding='utf-8') as out_csv_file:

        reader = csv.reader(in_csv_file, delimiter=',')
        writer = csv.writer(out_csv_file, delimiter=',')

        # Doing something ==================================
        for index, row in tqdm(enumerate(reader)):
            if index == 0:
                continue
            try:
                pname, smpdbid, gname = row[0], row[2], row[3]
                key = ';;'.join([pname, smpdbid])
                value = gname
                add_dict_item(result_dict, key, value)
            except IndexError as error:
                print(error, row)

        result_dict = sort_dict(result_dict)

        pnames = set()
        smpdbids = set()

        for k, v in result_dict.items():
            pname, smpdbid = k.strip().split(';;')
            check_duplicate(pnames, pname)
            check_duplicate(smpdbids, smpdbid)
            gname = ';'.join(v)
            writer.writerow([None, pname, None, smpdbid, gname, None])
        # ==================================================


convert()
