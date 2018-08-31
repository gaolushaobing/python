# -*- coding:utf-8 -*-
# 打卡并读取文件，显示在屏幕上
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)