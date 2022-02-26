# Кортеж - неизменяемый, элемент получаем по индексу

dimensions = (200, 50)
print(dimensions[0]) 
print(dimensions[1])

# dimensions[0] = 250 #ничего нельзя добавить или убрать, на то и изменяемый


dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

foods = ('pizza', 'sushi', 'burger')
for food in foods:
    print(food)

foods_list = list(foods)
foods_list[0] = 'pasta'
foods_list[1] = 'pho bo'
print(foods_list)