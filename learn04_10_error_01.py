# print(5/0) 
# ZeroDivisionError: division by zero

try: 
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")