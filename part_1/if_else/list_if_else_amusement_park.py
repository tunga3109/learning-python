age = 12

if age < 4: #если
    print("Your admission cost is $0.") 
elif age < 18:  #второе условие если
    print("Your admission cost is $25.")
else: #иначе
    print("Your admission cost is $40.")



age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings: 
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings: 
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings: 
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

alien_color = 'red'
if alien_color == 'green':
    print('Игрок только что заработал 5 очков.')
elif alien_color == 'red':
    print('Игрок только что заработал 0 очков.')

alien_color = 'green'
if alien_color == 'green':
    print('Игрок только что заработал 5 очков.')
elif alien_color == 'yellow':
    print('Игрок только что заработал 10 очков.')
elif alien_color == 'red':
    print('Игрок только что заработал 15 очков.')


age = 34

if age == 2:
    pass
elif age >= 2 and age < 4:
    pass
elif age >=4 and age < 13:
    pass
elif age >= 13 and age < 20:
    pass
elif age >= 20 and age < 65:
    print('ok')
elif age >= 65:
    pass

fruits = ['banana', 'apple', 'berry', 'peach', 'passion fruit']
fav_fruits = ['apple', 'passion fruit', 'banana']
if 'banana' in fruits:  #если есть элемент в списке
    print('we have this fruit')
else:
    print('we do not this one')


for fruit in fruits:
    if fruit in fav_fruits: #если есть элемент во втором списке
        print(f'we have {fruit}') 
    else: 
        print(f'we do not have {fruit}') # те элементы, которых нет в списке
 

