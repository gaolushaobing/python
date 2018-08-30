# -*- coding:utf-8 -*-
# for 遍历
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("That is nice!")
print("Thank you, everyone. That was a great magic show!")

# 函数range()生成数字
for value in range(1, 5):
    print(value)

# list()可以转换列表
numbers = list(range(1, 6))
print(numbers)

# range可以指定步长
# 2开始 不断加2 达到或者超过11
even_numbers = list(range(2, 11, 2))
print(even_numbers)


# 1~10的平方
squares = []
for value in range(1, 11):
    squares.append(value**2)

print(squares)

print("\n-------------\n")

# 处理数字列表的函数
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 列表解析
squares = [value**2 for value in range(1, 11)]
print(squares)

# 列表切片
letters = ['a', 'b', 'c', 'd', 'e', 'f']
print(letters[0:3])
print(letters[-3:])

# 根据列表切片衍生的复制列表
my_drinks = ['tea', 'coffee', 'beer', 'milk']
friend_drinks = my_drinks[:]
print("My:" + str(my_drinks))
print("Friend:" + str(friend_drinks))


# 元组 · 不可变的列表 可以重新赋值定义

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

print("\n-------------\n")