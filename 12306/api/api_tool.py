#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2021-02-2021/2/4
@author: xdong
@site:
@email: 12919662@qq.com
@file:  api_tool
@description: $描述$
"""

import requests
from PyQt5.Qt import *


class API(object):

    # 下载验证码
    GET_CAPTCHA_URL = 'https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand'

    # 校验验证码 POST
    # answer: 11, 5
    # login_site: E
    # rand: sjrand
    CHECK_CAPTCHA_URL = "https://kyfw.12306.cn/passport/captcha/captcha-check"

class ApiTool(QObject):

    session = requests.session()

    def __init__(self, parent=None, *args, **kwargs):
        super(ApiTool, self).__init__(parent, *args, **kwargs)

    @classmethod
    def download_captcha(cls):
        response = cls.session.get(API.GET_CAPTCHA_URL)
        print(response.content)
        with open('api/captcha.jpg', 'wb') as f:
            f.write(response.content)
        return "api/captcha.jpg"

    @classmethod
    def check_captcha(cls, result):
        data_dic = {
            "answer": result,
            "login_site": 'E',
            "rand": "sjrand"
        }
        response = cls.session.post(API.CHECK_CAPTCHA_URL, data=data_dic)
        dic = response.json()
        print(dic)
        if dic['result_code'] == '4':
            return True
        else:
            return False



if __name__ == '__main__':

    ApiTool.download_captcha()