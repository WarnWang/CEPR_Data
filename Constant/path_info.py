#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Filename: path_info
# @Date: 2017/6/3
# @Author: Mark Wang
# @Email: wangyouan@gmial.com

import os

class PathInfo(object):
    ROOT_PATH = r'D:\CEPR_Data_sort' if not hasattr(os, 'uname') else '/home/zigan/Documents/WangYouan/research/CEPR'
    DATA_PATH = os.path.join(ROOT_PATH, 'data')
    RESULT_PATH = os.path.join(ROOT_PATH, 'result')
    TEMP_PATH = os.path.join(ROOT_PATH, 'temp')