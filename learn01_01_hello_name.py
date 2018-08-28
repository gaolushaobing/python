#-*- coding:utf-8 -*- 
name = "Kevin"
# 字符串拼接
print("Hello " + name + ", would you like to learn some Python today?")

myself_name = "Kevin Zhang"
# 字符串首字母大写
print(myself_name.title())

# 字符串小写
print(myself_name.lower())

# 字符串大写
print(myself_name.upper())

# 引号运用
famous_saying_01 = 'Albert Einstein once said, "A person who never made a mistake never tried anything new."'
print(famous_saying_01)

# 数字要先str()后在与字符串拼接
age = 23
msg = "Happy " + str(age) + "rd Birthday!"
print(msg)

# 列表 数组 著名自行车品牌 -1就是最后一个类似length-1
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[3])
print(bicycles[3].title())
print(bicycles[-1].title())
print(bicycles[-2].title())