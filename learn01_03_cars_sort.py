#-*- coding:utf-8 -*- 
cars = ['bmw', 'audi', 'toyota', 'subaru']

# sort()永久性对列表数组排序
cars.sort()
print(cars)

# sort(reverse = True) 相反顺序
cars.sort(reverse = True)
print(cars)

print("---------------")

# sorted() sorted(reverse = Ture)临时排序

# reverse() 反转顺序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

# 函数len() 得到列表的长度
print(len(cars))