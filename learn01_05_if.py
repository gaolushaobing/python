# -*- coding:utf-8 -*-
# 把bmw大写

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
        
print("\n-------------\n")

#不等于
answer = 17
if answer != 31:
    print("That is not the correct answer. Please try again!")
