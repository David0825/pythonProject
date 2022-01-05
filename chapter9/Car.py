
class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        """设置随时间变化的属性，用于存储汽车的总里程"""
        self.odometer_reading = 10

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条之处汽车里程的消息"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        将里程表读数设置未指定的值
        禁止将里程表读数往回调
        """
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, mileage):
        """将里程表读数增加指定的量"""
        if mileage < 0:
            self.odometer_reading += 0
        else:
            self.odometer_reading += mileage

    @staticmethod
    def fill_gas_tank():
        print("This car need a gas tank!")

# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())
# # """直接修改属性"""
# # my_new_car.odometer_reading = 23
# """通过方法修改属性的值"""
# my_new_car.update_odometer(8)
# my_new_car.read_odometer()
#
# """通过方法对属性的值进行递增"""
# my_user_car = Car('subaru','outback',2015)
# print(my_user_car.get_descriptive_name())
#
# my_user_car.update_odometer(23500)
# my_user_car.read_odometer()

# my_user_car.increment_odometer(500)
# my_user_car.read_odometer()
