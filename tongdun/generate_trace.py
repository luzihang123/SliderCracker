# -*- coding: utf-8 -*-
# @Time    : 2019/10/17 8:40
# @Author  : Esbiya
# @Email   : 18829040039@163.com
# @File    : generate_trace.py
# @Software: PyCharm

import time
import random


def _generate_trace(distance):
    """
    生成轨迹
    :param distance: 缺口距离
    :return:
    """
    start_x = random.randint(500, 520)
    start_y = random.randint(652, 658)
    # 初速度
    v = 0
    # 位移/轨迹列表，列表内的一个元素代表0.02s的位移
    tracks_list = []
    # 当前的位移
    current = 0
    while current < distance:
        # 加速度越小，单位时间的位移越小,模拟的轨迹就越多越详细
        a = random.randint(10000, 12000)  # 加速运动
        # 初速度
        v0 = v
        t = random.randint(9, 18)
        s = v0 * t / 1000 + 0.5 * a * ((t / 1000) ** 2)
        # 当前的位置
        current += s
        # 速度已经达到v,该速度作为下次的初速度
        v = v0 + a * t / 1000
        # 添加到轨迹列表
        if current < distance:
            tracks_list.append(round(current))
    # 减速慢慢滑
    if round(current) < distance:
        for i in range(round(current) + 1, distance + 1):
            tracks_list.append(i)
    else:
        for i in range(tracks_list[-1] + 1, distance + 1):
            tracks_list.append(i)
    # 生成时间戳列表
    timestamp_list = []
    timestamp = int(time.time() * 1000)
    for i in range(len(tracks_list)):
        t = random.randint(11, 18)
        timestamp += t
        timestamp_list.append(timestamp)
        i += 1
    y_list = []
    zy = 0
    for j in range(len(tracks_list)):
        y = random.choice(
            [0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
             -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, -1, 0, 0])
        zy += y
        y_list.append(zy)
        j += 1
    trace = []
    for index, x in enumerate(tracks_list[:-1]):
        if not index:
            trace.append({
                'type': 1,
                'time': timestamp_list[index],
                'Action': 12,
                'op_x': x + start_x,
                'op_y': y_list[index] + start_y,
            })
        elif index == len(tracks_list) - 1:
            trace.append({
                'type': 3,
                'time': timestamp_list[index],
                'Action': 13,
                'op_x': x + start_x,
                'op_y': y_list[index] + start_y,
            })
        trace.append({
            'type': 1,
            'time': timestamp_list[index],
            'Action': '',
            'op_x': x + start_x,
            'op_y': y_list[index] + start_y,
        })
    return trace


x = _generate_trace(76)
print(x)
