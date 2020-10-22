import time

import requests
import google.protobuf.json_format
#! /usr/bin/env python
# -*- coding: utf-8 -*-


# 为 all_person 填充数据


def Tostring(data):
    data = data.SerializeToString()
    return data

def Fromstring(data):
    data_form = data.ParseFromString(data)
    return data_form



