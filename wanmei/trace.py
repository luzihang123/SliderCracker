# -*- coding: utf-8 -*-
# @Time    : 2019/10/10 17:29
# @Author  : Esbiya
# @Email   : 18829040039@163.com
# @File    : trace.py
# @Software: PyCharm

import time
import random


def _generate_trace(distance, start_time):
    """
    生成轨迹
    :param distance:
    :return:
    """
    back = random.randint(2, 6)
    distance += back

    base_x = random.randint(35, 50)
    base_y = random.randint(260, 280)

    # 初速度
    v = 0
    # 位移/轨迹列表，列表内的一个元素代表0.02s的位移
    tracks_list = []
    # 当前的位移
    current = 0
    while current < distance - 13:
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
    # 回退
    for _ in range(back):
        current -= 1
        tracks_list.append(round(current))
    tracks_list.append(round(current) - 1)
    if tracks_list[-1] != distance - back:
        tracks_list.append(distance - back)
    # 生成时间戳列表
    timestamp = int(time.time() * 1000)
    timestamp_list = [timestamp]
    for i in range(len(tracks_list)):
        t = random.randint(11, 18)
        timestamp += t
        timestamp_list.append(timestamp)
        i += 1
    y_list = []
    zy = 0
    for j in range(len(tracks_list)):
        y = random.choice(
            [0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
             0, -1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, -1, 0, 0])
        zy += y
        y_list.append(zy)
        j += 1
    trace = [[base_x, base_y, 1, 0]]
    for index, x in enumerate(tracks_list):
        trace.append([base_x + x, base_y + y_list[index], 3, timestamp_list[index] - start_time])
    return trace[:-1]



# x = [[58, 277, 1, 0], [59, 277, 3, 284], [67, 277, 6, 333], [67, 277, 5, 333], [95, 277, 3, 438], [109, 277, 6, 487],
#      [109, 277, 5, 487], [140, 277, 3, 589], [167, 277, 3, 691], [183, 277, 3, 794], [199, 277, 3, 925],
#      [210, 277, 3, 1050], [211, 277, 3, 1160], [213, 277, 3, 1284], [218, 277, 3, 1394], [223, 277, 3, 1504],
#      [226, 277, 3, 1607], [228, 278, 3, 1752]]
# y = {"length": 168, "validateTimeMilSec": 24038}
