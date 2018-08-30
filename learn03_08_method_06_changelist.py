# -*- coding:utf-8 -*-
# 数据存储到一个列表，打印后存才另外一个列表

''' # 首先创建一个列表，包含要打印的东西
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# 模拟打印 转移到完成列表中
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Printing model: " + current_design)
    completed_models.append(current_design)

# 显示打印好的模型
print("\nThe following models have been printed: ")
for completed_model in completed_models:
    print(completed_model) '''

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iPhone 8', 'iPhone 9', 'iPhone 10']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)