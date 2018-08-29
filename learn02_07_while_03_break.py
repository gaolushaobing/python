# -*- coding:utf-8 -*-
# learn02_07_while_03_break
# break退出整个循环

prompt = "\nPlease enter the name of city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")