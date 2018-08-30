# -*- coding:utf-8 -*-
# 创建类
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")

# 创建实例
tyke = Dog('tyke', '1')
print("My dog's name is " + tyke.name.title() + ".")
print("My dog is " + str(tyke.age) + " years old.")
tyke.sit()
tyke.roll_over()

spike = Dog('spike', '7')
spike.sit()
spike.roll_over()
