#-*- coding:utf-8 -*- 

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# addend()添加元素到列表最后
motorcycles.append('honda')
print(motorcycles)

# insert(位置，元素）插入元素到列表指定位置
motorcycles.insert(1, 'hello')
print(motorcycles)

# del语句删除指定位置的元素
del motorcycles[1]
print(motorcycles)

# pop() 删除末尾或者指定索引的元素，并返回该元素
print(motorcycles.pop())
print(motorcycles)

#remove() 删除第一个出现的指定的值
motorcycles.remove('yamaha')
print(motorcycles)
