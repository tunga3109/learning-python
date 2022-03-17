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