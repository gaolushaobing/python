# -*- coding:utf-8 -*-
# 定义简单函数
def greet_user():
    print("Hello easy method!")
greet_user()

# 一个参数的函数
def greet_user2(username):
    print("Hello, " + username.title() + "!")
greet_user2('kevin')

# 形参
def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster', 'Jerry')
describe_pet('cat', 'tom')