# -*- coding: utf-8 -*-
# @Time    : 2019/11/1 21:58
# @Author  : Esbiya
# @Email   : 18829040039@163.com
# @File    : encrypt.py
# @Software: PyCharm

import execjs


def _reload_js():
    """
    加载 js
    :return:
    """
    with open('yd_slider.js', 'rb') as f:
        slider_js = f.read().decode()
    with open('generate_fp.js', 'rb') as f:
        fp_js = f.read().decode()
    return slider_js, fp_js


def _get_cb(js):
    """
    生成 cp 参数
    :param js:
    :return:
    """
    ctx = execjs.compile(js)
    return ctx.call('get_cb')[:64]


def _get_fp(js):
    """
    生成指纹 fp
    :param js:
    :return:
    """
    ctx_ = execjs.compile(js)
    return ctx_.call('generateFingerprint')


def _encrypt_data(js, token, trace):
    """
    加密轨迹
    :param token:
    :param trace:
    :return:
    """
    ctx = execjs.compile(js)
    return ctx.call('encrypt', token, trace)
