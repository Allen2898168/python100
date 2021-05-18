# coding=utf-8
"""
    python笔记4
    如何遍历查找出某个文件夹内所有的子文件呢？并且找出某个后缀的所有文件
"""

import os
import requests

a = requests.post()

def get_files(path=r'C:\Users\EDZ\PycharmProjects\study', rule=".py"):
    all = []
    for fpathe, dirs, fs in os.walk(path):  # os.walk是获取所有的目录
        for f in fs:
            filename = os.path.join(fpathe, f)
            if filename.endswith(rule):  # 判断是否是"xxx"结尾
                all.append(filename)
    return all


if __name__ == "__main__":
    b = get_files(r"/")
    for i in b:
        print(i)

import note_5

x = note_5.a()
x.succeess = False
