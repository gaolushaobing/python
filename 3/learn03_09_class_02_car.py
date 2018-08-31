# -*- coding:utf-8 -*-

# 模拟一个汽车类
class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    #修改里程的方法
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    #增加的里程
    def increment_odometer(self, miles):
        self.odometer_reading += miles

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# 修改属性的值
#直接修改
my_new_car.odometer_reading = 50
my_new_car.read_odometer()

#方法来修改
my_new_car.update_odometer(60)
my_new_car.read_odometer()

#方法递增
my_new_car.increment_odometer(200)
my_new_car.read_odometer()