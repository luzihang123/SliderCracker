# -*- coding: utf-8 -*-
# @Time    : 2019/9/29 18:37
# @Author  : Esbiya
# @Email   : 18829040039@163.com
# @File    : geetest.py
# @Software: PyCharm


import random
import requests
import json
import time
from urllib.parse import urlencode
from yidun.get_trace import _generate_trace
from yidun.img_locate import _get_distance
from yidun.encrypt import _reload_js, _encrypt_data, _get_cb, _get_fp


class YidunCracker:

    def __init__(self, sid, referer):
        self.sid = sid
        self.referer = referer
        self.slider_js, self.fp_js = _reload_js()
        self.fp = _get_fp(self.fp_js)
        self.session = requests.session()
        self.session.headers = {
            'Referer': self.referer,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'
        }

    def _init_captcha(self):
        """
        初始化验证码
        :return:
        """
        url = 'https://c.dun.163yun.com/api/v2/get'
        params = {
            'id': self.sid,
            'fp': self.fp,
            'https': 'true',
            'type': 'undefined',
            'version': '2.12.0',
            'dpr': '1',
            'dev': '1',
            'cb': _get_cb(self.slider_js),
            'ipv6': 'false',
            'runEnv': 10,
            'width': '306',
            'token': 'c8663d6fbc5f4e14bf0f7f7246e7b70c',
            'referer': self.referer,
            'callback': '__JSONP_55xb89m_0'
        }

        resp = self.session.get(url, params=params)
        result = json.loads(resp.text.replace('__JSONP_55xb89m_0(', '').replace(');', ''))
        if result['data']['type'] == 2:
            print('滑块验证初始化成功! ')
            print('初始化数据: ', result)
            token = result['data']['token']
            bg = result['data']['bg']
            front = result['data']['front']
            return {
                'token': token,
                'captcha_url': bg,
                'slider_url': front
            }
        elif result['data']['type'] == 3:
            print('当前验证码为点选验证, 跳过...')
            return None
        raise Exception('未知类型验证码! ')

    def _slider_verify(self, trace, token):
        """
        滑块验证
        :param trace:
        :param token
        :return:
        """
        data = _encrypt_data(self.slider_js, token, trace)
        params = {
            'id': self.sid,
            'token': token,
            'acToken': '',
            'data': data,
            'width': '306',
            'type': '2',
            'version': '2.12.0',
            'cb': _get_cb(self.slider_js),
            'extraData': '',
            'runEnv': 10,
            'referer': self.referer,
            'callback': '__JSONP_bc4jy3y_1'
        }
        cookies = {
            'gdxidpyhxdE': self.fp
        }
        check_url = 'https://c.dun.163yun.com/api/v2/check?' + urlencode(params)
        resp = self.session.get(check_url, cookies=cookies)
        result = json.loads(resp.text.replace('__JSONP_bc4jy3y_1(', '').replace(');', ''))
        print('校验结果: ', result)
        if result['data']['result']:
            return {
                'success': 1,
                'message': '校验通过! ',
                'data': {
                    'validate': result['data']['validate']
                }
            }
        return {
            'success': 0,
            'message': '校验失败! ',
            'data': None
        }

    def run(self):
        while True:
            init_data = self._init_captcha()
            if init_data:
                token = init_data['token']
                bg = init_data['captcha_url']
                fg = init_data['slider_url']
                break
            time.sleep(1)
        distance = int(_get_distance(fg[1], bg[1]) * (306 / 320))
        start_time = int(time.time() * 1000)
        time.sleep(random.uniform(0.01, 0.05))
        trace = _generate_trace(distance, start_time)
        result = self._slider_verify(trace, token)
        return result


if __name__ == '__main__':
    x = YidunCracker('5a0e2d04ffa44caba3f740e6a8b0fa84', 'https://dun.163.com/trial/sense').run()
    print(x)
