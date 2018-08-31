# -*- coding:utf-8 -*-
# learn02_07_while_04_continue.py
# continue英文有继续持续的意思 在语法中是退出当次循环，继续下一次循环
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# 示例偶数退出循环，奇数打印
