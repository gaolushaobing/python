# -*- coding:utf-8 -*-
# 在with外使用文件逐行的内容
with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())