# -*- coding: utf-8 -*-
# @Time    : 2019/10/11 0:03
# @Author  : Esbiya
# @Email   : 18829040039@163.com
# @File    : geetest.py
# @Software: PyCharm

import re
import json
import requests
import execjs
from luosimao import img_locate
from luosimao.lsm_crypt import aes_encrypt, md5_encrypt
from luosimao.chaojiying import image_to_text

headers = {
    'Content-type': 'application/x-www-form-urlencoded',
    'Origin': 'https://captcha.luosimao.com',
    'Referer': 'https://captcha.luosimao.com/api/widget?k=e7b4d20489b69bab25771f9236e2c4be&l=zh-cn&s=normal&i=_x0lu27ots',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}


def _init_slider():
    """
    初始化验证码
    :return:
    """
    url = 'https://captcha.luosimao.com/api/request?k=e7b4d20489b69bab25771f9236e2c4be&l=zh-cn'
    data = {
        'bg': 'g2heqaxX6YkuuSgnaqY2ArxuBS8dZmrn9ObmF26IbGDJE/UhMPONsbnkY4Ktxp66n7FtT0DeWQmV7Fjj3v6cguu LTTnrhbiAZmmMOWiMTalzoEBCAwa5beDmHTW/TF0T9M0RI9229Igfen7WZCUHQGiIgaDb1tYjIl2 e4Di1uBZNci8 f3rkyzfHi9jHoJjrrBOb7Afs1Bv6xCBy2oTBGk/Z12DaccOjQe3NYSZj0=',
        'b': 'ZqglyXxk9fDSFKOsuJAYZWsS0dmPffwJh3XlW6BlyOfp7gaje58uZU9E8ry9xLAZ'
    }

    resp = requests.post(url, headers=headers, data=data).json()
    return resp


def get_captcha(s):
    """
    获取乱序验证码图片和还原数组
    :param s:
    :return:
    """
    url = 'https://captcha.luosimao.com/api/frame'
    params = {
        's': s,
        'i': '_nv0uo1kzr',
        'l': 'zh-cn'
    }
    resp = requests.get(url, params=params, headers=headers)
    captcha_data = re.search('var captchaImage = ({.*?})', resp.text, re.S).group(1)
    captcha_url = re.search(r"p:\['(.*?)',", captcha_data, re.S).group(1)
    merge_array = json.loads(re.search(r'l:(.*?)}', captcha_data).group(1))
    return captcha_url, merge_array


def encrypt_data(init_data, position):
    """
    js 加密
    :param init_data:
    :param position:
    :return:
    """
    with open('lsm_encrypt.js', 'rb') as f:
        js = f.read().decode()
    ctx = execjs.compile(js)
    return ctx.call('encrypt', init_data, position)


def _slider_verify(init_data, position):
    """
    最终验证
    :param init_data: 初始化数据
    :param position: 点选位置
    :return:
    """
    url = 'https://captcha.luosimao.com/api/user_verify'

    # 参数说明: h: 哈希签名, 给服务器确定使用的验证码图片和密钥;
    #          v: 点选位置加密, 固定偏移量
    #          s: 哈希验签
    # data = {
    #     'h': init_data['h'],
    #     'v': aes_encrypt(init_data['i'], "2801003954373300", position).replace('=', ''),
    #     's': md5_encrypt(position)
    # }
    data = encrypt_data(init_data, position)
    print(data)
    result = requests.post(url, data=data, headers=headers).json()
    print(result)
    if result['res'] == 'success':
        return result['resp']
    else:
        if 'reload' in set(result.keys()):
            init_data = result['request']
            return init_data
        return None


def crack(init_data):
    # 获取乱序验证码图片和还原位置数组
    captcha_url, merge_array = get_captcha(init_data['s'])
    # 还原验证码图片
    captcha_path = img_locate.reduce_image(merge_array, captcha_url)
    # 制作描述图片
    word_path = img_locate.make_word(init_data['w'])
    # 合并
    img_path = img_locate.merge_word(captcha_path, word_path)
    # 提交给打码平台识别
    with open(img_path, 'rb') as f:
        img_data = f.read()
    ok, position = image_to_text(img_data, img_kind=9004)
    if ok:
        # 最终验证
        result = _slider_verify(init_data, position)
        if isinstance(result, str):
            return {
                'success': 1,
                'message': '校验成功! ',
                'data': {
                    'resp': result
                }
            }
        elif isinstance(result, dict):
            print('重新加载验证! ')
            crack(result)
        return {
            'success': 0,
            'message': '校验失败! ',
            'data': None
        }
    else:
        return {
            'success': 0,
            'message': '验证码识别失败! ',
            'data': None
        }


if __name__ == '__main__':
    x = _init_slider()
    y = crack(x)
    print(y)
