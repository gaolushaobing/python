# -*- coding:utf-8 -*-
# 给函数传递列表当做参数，让函数for循环

def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['tom', 'jerry', 'mike', 'kevin']
greet_users(usernames)