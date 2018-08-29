# -*- coding:utf-8 -*-
# 利用while和remove()来删除多余的重复元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)