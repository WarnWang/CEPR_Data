#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Filename: sort_file
# @Date: 2017/6/3
# @Author: Mark Wang
# @Email: wangyouan@gmial.com

import os

import pandas as pd

from .constant import Constants as const

if __name__ == '__main__':

    data_files = os.listdir(const.DATA_PATH)

    data_dfs = []

    for f in data_files:
        print(f)
        if not f.endswith('.dta'):
            continue

        data_dfs.append(
            pd.read_stata(os.path.join(const.DATA_PATH, f), convert_categoricals=False, convert_missing=True))

    df = pd.concat(data_dfs, ignore_index=True)
    df.to_csv(os.path.join(const.RESULT_PATH, '20170603_merged_data.csv'), index=False)
    df.to_pickle(os.path.join(const.RESULT_PATH, '20170603_merged_data.p'))
    df.to_stata(os.path.join(const.RESULT_PATH, '20170603_merged_data.dta'))