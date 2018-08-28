# -*- coding:utf-8 -*-
# 多行input
person = "If you tell us who you are, we can personalize the message you see."
person += "\nWhat is your first name? "

name = input(person)
print("\nHello, " + name.title() + "!")

#int() 将数字的字符串转换为数值