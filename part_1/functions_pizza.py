#Передача произвольного набора аргументов

def make_pizza(*toppings):
    """Вывод списка заказанных топпингов."""
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

#Звездочка в имени параметра *toppings приказывает Python создать пустой кортеж с именем toppings и упаковать в него все полученные значения. 
#Результат команды print в теле функции показывает, что Python успешно справляется и с вызовом функции с одним значением, и с вызовом с тремя значениями.


def make_pizza(*toppings):
    """Выводит описание пиццы."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

#Позиционные аргументы с произвольными наборами аргументов


def make_pizza(size, *toppings):
    """Выводит описание пиццы."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')