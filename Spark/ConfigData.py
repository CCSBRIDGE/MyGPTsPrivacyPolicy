# -*- coding: utf-8 -*-
# coding=utf-8
# coding: utf-8
# @Time    : 2024/6/24 0:02
# @Author  : Mark Deng
# @Email   : 1114026501@qq.com
# @File    : ConfigData
# @Software: PyCharm

APPId = "e9bd9822"
APIKey = "1cb17ef5f1fd4ffbffc66f2434a654a0"
APISecret = "MmYzZGRjZGFkMGFkMjhhZDM2YTM3YmQx"
VCN = "x4_lingxiaoxuan_oral"
# vcn.x4_lingyuzhao_oral 聆玉昭
# vcn.x4_lingxiaoxuan_oral 聆小璇
# vcn.x4_lingfeizhe_oral 聆飞哲

# 请求数据
request_data = {
    "header": {
        "app_id": APPId,
        "status": 0
    },
    "parameter": {
        "oral": {
            "oral_level": "mid",
            "spark_assist": 1,
            "scenarized": 0
        },
        "tts": {
            "vcn": VCN,
            "volume": 50,
            "speed": 50,
            "pitch": 50,
            "bgs": 0,
            "rhy": 0,
            "audio": {
                "encoding": "lame",
                "sample_rate": 16000,
                "channels": 1,
                "bit_depth": 16,
                "frame_size": 0
            },
            "pybuf": {
                "encoding": "utf8",
                "compress": "raw",
                "format": "plain"
            }
        }
    },
    "payload": {
        "text": {
            "encoding": "utf8",
            "compress": "raw",
            "format": "plain",
            "status": 0,
            "seq": 0,
            "text": "./resource/input/1.txt"
        },
        "user_text": {
            "encoding": "utf8",
            "compress": "raw",
            "format": "plain",
            "status": 0,
            "seq": 0,
            "text": "./resource/input/1.txt"
        }
    }
}

# 请求地址
request_url = "ws://cbm01.cn-huabei-1.xf-yun.com/v1/private/medd90fec"
# "ws(s)://cbm01.cn-huabei-1.xf-yun.com/v1/private/medd90fec"
# ws(s)://cbm01.cn-huabei-1.xf-yun.com/v1/private/medd90fec

# 用于快速定位响应值

response_path_list = ['$..payload.pybuf', '$..payload.audio', ]
