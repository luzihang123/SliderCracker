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
    start_x = random.randint(10, 40)
    start_y = random.randint(10, 20)
    back = random.randint(2, 6)
    distance += back
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
    # 回退
    for _ in range(back):
        current -= 1
        tracks_list.append(round(current))
    tracks_list.append(round(current) - 1)
    if tracks_list[-1] != distance - back:
        tracks_list.append(distance - back)
    # 生成时间戳列表
    timestamp_list = []
    timestamp = random.randint(20, 60)
    for i in range(len(tracks_list)):
        if i >= len(tracks_list) - 6:
            t = random.randint(80, 180)
        else:
            t = random.randint(11, 18)
        timestamp += t
        timestamp_list.append(timestamp)
        i += 1
    y_list = []
    zy = 0
    for j in range(len(tracks_list)):
        y = random.choice(
            [0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
             -1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, -1, 0, 0])
        zy += y
        y_list.append(zy)
        j += 1
    trace = [{'p': f'{start_x},{start_y}', 't': random.choice([0, 1])}]
    for index, x in enumerate(tracks_list):
        trace.append({
            'p': ','.join([str(x + start_x), str(y_list[index] + start_y)]),
            't': timestamp_list[index]
        })
    trace.append({
        'p': f'{tracks_list[-1] + start_x},{y_list[-1] + start_y}',
        't': timestamp_list[-1] + random.randint(100, 300)
    })
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


def get_track(distance):
    track_path = './trace.txt'
    with open(track_path, 'r+') as fp:
        lines = fp.readlines()
    match_tracks = []
    for line in lines:
        if line.strip() == '':
            continue
        x_pos = int(line.split('=')[0])
        track = line.split('=')[1].strip()

        if distance == x_pos or distance == x_pos + 1 or distance == x_pos - 1:
            match_tracks.append((distance, track))
    try:
        x_pos, track = random.choice(match_tracks)
        return x_pos, track
    except:
        return distance, None


