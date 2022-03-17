# Позиционные аргументы

def describe_pet(animal_type, pet_name):
    """Выводит информацию о животном."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
# Многократные вызовы функций
describe_pet('dog', 'willie')

# Именованные аргументы
def describe_pet(animal_type, pet_name):
    """Выводит информацию о животном."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

# Значения по умолчанию
def describe_pet(pet_name, animal_type='dog'):
    """Выводит информацию о животном."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')
describe_pet(pet_name='john')

# ex 1
def make_shirt (text,size='ML'):
    print(f'The size of the t-shirt is {size} and text is "{text}"')

#make_shirt('X', 'I love Vietnam')
#make_shirt(text='I love Dibai', size='XL')
make_shirt(text='I love Cyprus')

# ex 2

def describe_city(city, country='Belarus'):
    print(f'{city} is in {country}')

#describe_city('Minsk', 'Belarus')
describe_city(city='Vitebsk')
describe_city(city='Minsk')
describe_city(city='Gomel')


