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


# 年龄筛选
age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")


# in 是否含有 披萨加料 
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")

print("\nFinished making your pizza!")

print("\n-------------\n")

# for表示披萨加料
requested_toppings = ['mushrooms', 'extra cheese', 'green peppers']

for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")


