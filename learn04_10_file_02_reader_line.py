# -*- coding:utf-8 -*-
# 打卡并读取文件，逐行在屏幕上
with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip())