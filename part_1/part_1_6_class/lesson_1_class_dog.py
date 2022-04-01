# Lesson 1

class Dog():
    """Простая модель собаки."""

    def __init__(self, name, age): # фукнция в классе - это метод
        #self — ссылка на экземпляр;
        #она предoставляет конкретному экземпляру доступ к 
        #атрибутам и методам класса.
        self.name = name
        self.age = age

    def sit(self):
        print(f'{self.name} is now sitting.')

    def roll_over(self):
        print(f'{self.name} rolled over!')

my_dog = Dog('willie', 6) # my_dog - это экземпляр класса

# Обращение к атрибутам без скобок ()
print(f"My dog's name is {my_dog.name}.") 
print(f"My dog is {my_dog.age} years old.")

# Вызов методов cо скобками ()
my_dog.sit() 
my_dog.roll_over()

#1

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        print(f'{self.restaurant_name} is {self.cuisine_type} restaurant')
     
    def open_restaurant(self):
        print(f'{self.restaurant_name} is opened')

    def set_number_served(self, num_of_people):
        self.number_served = num_of_people

    def increment_number_served(self, num):
        self.number_served += num

restaurant = Restaurant('Saigon', 'Vietnamese')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

pizza = Restaurant('Pizza Tempo', 'Italian')
sushi = Restaurant('Sushi Vesla', 'Japanese')
burger = Restaurant('McDonalds', 'American')

pizza.describe_restaurant()
sushi.describe_restaurant()
burger.describe_restaurant()

pizza.set_number_served(8)
print(pizza.number_served)
pizza.increment_number_served(10)
print(pizza.number_served)


#2

class User():

    def __init__(self, first_name, last_name, age, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.occupation = occupation
        self.login_attempts = 0

    def describe_user(self):
        print(f'{self.first_name}\n{self.last_name}\n{self.age}\n{self.occupation}')

    def greet_user(self):
        print(f'Welcome to the club, {self.first_name} {self.last_name}')
    
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts -= self.login_attempts

tchan = User('Chan', 'Tunga', 23, 'Customer support')
tchan.describe_user()
tchan.greet_user()    
    
tchan.increment_login_attempts()
tchan.increment_login_attempts()
tchan.increment_login_attempts()
print(tchan.login_attempts)
tchan.reset_login_attempts()
print(tchan.login_attempts)



