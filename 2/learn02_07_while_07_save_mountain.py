# -*- coding:utf-8 -*-
# 用词典存储用户的输入
# 先建立一个空的词典
responses = {}

# 设置输入是否继续的标志
polling_active = True
while polling_active:
    # 收集用户的名字和回答
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday?")

    # 存储到字典里
    responses[name] = response

    # 结束提示
    repeat = input("Would you like to let another person respond? (yes / no)")
    if repeat == 'no':
        polling_active = False

# 结果输出
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
