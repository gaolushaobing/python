# -*- coding:utf-8 -*-
# 作为被导入的模块 制作pizz的方法
def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)
