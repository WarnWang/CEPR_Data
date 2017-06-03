#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Filename: constant
# @Date: 2017/6/3
# @Author: Mark Wang
# @Email: wangyouan@gmial.com

import os


class Constants(object):
    ROOT_PATH = r'D:\CEPR_Data_sort' if not hasattr(os, 'uname') else '/home/zigan/Documents/WangYouan/research/CEPR'
    DATA_PATH = os.path.join(ROOT_PATH, 'data')
    RESULT_PATH = os.path.join(ROOT_PATH, 'result')
    TEMP_PATH = os.path.join(ROOT_PATH, 'temp')


if __name__ == '__main__':
    c = Constants()

    for i in [c.DATA_PATH, c.RESULT_PATH, c.TEMP_PATH]:
        if not os.path.isdir(i):
            os.makedirs(i)
