# Сохранение информации о заказанной пицце.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Описание заказа.
print(f"You ordered a {pizza['crust']}-crust pizza ""with the following toppings:")

for topping in pizza['toppings']: # список
    print("\t" + topping)
