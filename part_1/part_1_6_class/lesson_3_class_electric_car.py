# Наследование
from lesson_2_class_car import Car
from lesson_1_class_dog import Restaurant, User

class Battery():
    """Простая модель аккумулятора электромобиля."""
    def __init__(self, battery_size=75): 
        """Инициализирует атрибуты аккумулятора.""" 
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора.""" 
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Выводит приблизительный запас хода для аккумулятора."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
              range = 315
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size <= 100:
            self.battery_size += (100 - self.battery_size)
        else:
            print(f'{self.battery_size} %')



class ElectricCar(Car):

    def __init__(self, make, model, year):
        """инициализирует атрибуты класса-родителя."""
        super().__init__(make, model, year)
        self.battery = Battery() # Экземпляры как атрибуты

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """У электромобилей нет бензобака."""
        print("This car doesn't need a gas tank!")
    
    
my_tesla = ElectricCar('tesla', 'model s', 2019) 
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()


# 1

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ['plobbir', 'strawberry', 'pinapple']

    def describe_flavours(self):
        print(self.flavours)

#gh = IceCreamStand('Ice','Italia')
#gh.describe_flavours()

# 2

class Privileges():

    def __init__(self, *privileges):
        self.privileges = [
            "разрешено добавлять сообщения", 
            "разрешено удалять пользователей", 
            "разрешено банить пользователей"
            ]
    
    def show_privileges(self):
        for privileg in self.privileges:
            print(privileg)
        

class Admin(User):
    
    def __init__(self, first_name, last_name, age, occupation):
        super().__init__(first_name, last_name, age, occupation)
        self.previl = Privileges()
        

ss = Admin('Tung', 'Chan', 23, 'support')
ss.previl.show_privileges()
