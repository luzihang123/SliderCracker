# -*- coding: utf-8 -*-
# @Time    : 2019/10/18 12:24
# @Author  : Esbiya
# @Email   : 18829040039@163.com
# @File    : get_trace.py
# @Software: PyCharm


import random


def generate_trace(distance):
    """
    生成轨迹
    :param distance: 缺口距离
    :return:
    """
    # 轨迹算法已删除
    return trace


def process_trace(trace):
    """
    处理轨迹
    :param trace: 轨迹
    :return:
    """
    merge = lambda s: ','.join([str(s['p']), str(s['t'])])
    new_trace = '|'.join([merge(i) for i in trace]) + '|'
    return new_trace

