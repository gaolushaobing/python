# -*- coding:utf-8 -*-
# for 遍历
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("That is nice!")
print("Thank you, everyone. That was a great magic show!")
print("\n-------------\n")

# 函数range()生成数字
for value in range(1, 5):
    print(value)
print("\n-------------\n")

# list()可以转换列表
numbers = list(range(1, 6))
print(numbers)

print("\n-------------\n")

# range可以指定步长
# 2开始 不断加2 达到或者超过11
even_numbers = list(range(2, 11, 2))
print(even_numbers)

print("\n-------------\n")


# 1~10的平方
squares = []
for value in range(1, 11):
    squares.append(value**2)

print(squares)
