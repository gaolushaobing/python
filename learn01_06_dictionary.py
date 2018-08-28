# -*- coding:utf-8 -*-
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

print(alien_0)

# 为字典添加信息
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 删除键值对
del alien_0['x_position']
print(alien_0)

del alien_0['y_position']
print(alien_0)

# 类似对象组成的字典
favorite_languages = {
    'kevin': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("Kevin's favorite language is " +
      favorite_languages['kevin'].title() + ".")

# 遍历词典 
for key, value in favorite_languages.items():
    print("key: " + key + " value: " + value)

# 遍历字典中的所有键 keys()
for name in favorite_languages.keys():
    print(name.title())
print("--------------")

# 遍历字典中所有的值values()
for value in favorite_languages.values():
    print(value.title())
