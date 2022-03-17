# Функции
def greet_user():
    """Выводит простое приветствие."""
    print("Hello!")

greet_user()

# Передача информации функции
def greet_user(username): # username - параметр
    """Выводит простое приветствие."""
    print(f"Hello, {username.title()}!")

greet_user('jesse') # jesse - аргумент

# ex 1
def display_message():
    print('hello, guys! ')

display_message() 

# ex 2
def favorite_book(title):
    print(f'One of my favorite books is {title.title()}')

favorite_book('Don Kihot')