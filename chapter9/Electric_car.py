"""电动车继承Car"""
from chapter9.Battery import Battery
from chapter9.Car import Car


class Electric_car(Car):
    """电动车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        # """再初始化电动汽车特有的属性"""
        # self.battery_size = 75
        """再初始化电动汽车特有的属性(实例用作属性)"""
        self.battery = Battery(100)


    # def describe_battery(self):
    #     """打印一条藐视电瓶容量的消息"""
    #     print(f"This car has a {self.battery_size}-kwh battery")

    """重写父类的方法"""
    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")


my_tesla = Electric_car('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
# my_tesla.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()
