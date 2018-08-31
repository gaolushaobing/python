# -*- coding:utf-8 -*-
# 在末尾添加

filename = 'programing.txt'

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets. \n")
    file_object.write("I love creating apps that can run in a browswer.\n")
