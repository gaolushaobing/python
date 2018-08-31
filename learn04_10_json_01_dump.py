# -*- coding:utf-8 -*-
# 导包

import json
numbers = [2, 5, 2, 5, 52, 6, 2, 6, 24, 6, 62, 62, 6, 2, 62, 4]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
