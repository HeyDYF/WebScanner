#-*- coding =utf-8 -*-
#@Time:2021/3/4 17:49
#@Author:简简
#@File：iplocating.py
#@software:PyCharm


# -*- coding:utf-8 -*-
import json
from ast import literal_eval
import requests



def get_locating(ip):
    """
    获取ip归属地
    """
    # api_url = 'http://freeapi.ipip.net/'
    api_url = 'http://whois.pconline.com.cn/ip.jsp?ip='
    # api_url = 'http://ip-api.com/json/'
    # print(ip)
    # res = requests.get(api_url + ip + "&action=2")
    # res = requests.get("https://www.ip138.com/iplookup.php?ip=120.46.76.152&action=2")
    # res = requests.get("https://ip.taobao.com/outGetIpInfo?ip=120.46.76.152", timeout=4)

    try:
        res = requests.get(api_url+ip+"&accessKey=alibaba-inc", timeout=4)
        # res = requests.get(api_url+ip, timeout=4)
        print(res.text)
        data = json.loads(res.text)
        # print(data)
        # 提取 city 值
        result_str = data['data']['city']
        # result_str = literal_eval(res.text)
        # result_str = (result[0])
        print(result_str)
        # result_str = '国家({})，省份({})，城市({})'.format(result[0],result[1],result[2])
    except Exception as e:
        result_str = '获取数据失败，请稍后再试'
        print(result_str)
    return result_str


if __name__ == '__main__':
    # ip = "120.46.76.152"
    # get_locating(ip)
    print(get_locating('139.224.112.182'))



