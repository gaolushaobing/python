# -*- coding:utf-8 -*-
# 把bmw大写

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
        

#不等于
answer = 17
if answer != 31:
    print("That is not the correct answer. Please try again!")


# and 和  or
age0 = 23
age1 = 18
print(age0 >= 20 and age1 >= 20)
print(age0 >= 20 or age1 >= 20)

# in 是否在之内
print('bmw' in cars)
print('bmw' not in cars)


# if 语句
age = 8
if age >= 18:
    print("You are old enough to vote!")
else:
    print("You age is small~")


print("\n-------------\n")



