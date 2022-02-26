bicycles = ['trek', 'cannondale', 'redline', 'specialized'] #list

print(bicycles)
print(bicycles[0]) #индексы с 0
print(bicycles[0].title())

message = f"My first bicycle was a {bicycles[0].title()}." 
print(message)

names = ['Vlad', 'Stas', 'Kirill', 'Nikita', 'Anton']
print(names[0])
print(names[1])
print(names[-1])
print(f'{names[0]} said :"zdarova, patsany"')
print('my best friend forever is {}'.format(names[-1]))
print('my best friend forever is', names[-1])

names[0] = 'Tolya' #изменение элемента в списке
print(names)

names.append('Andrey') #Добавление элемента в список
print(names)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati') #вставка элемента в список по индексу
print(motorcycles)

del motorcycles[0] #Удаление элемента из списка
print(motorcycles)

popped_motorcycle = motorcycles.pop() #Удаление элемента из списка по индексу
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop() #удаленный элемент в переменной
print(f"The last motorcycle I owned was a {last_owned.title()}.")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('yamaha') #Удаление элементов по значению
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(motorcycles)
too_expensive = 'ducati' #Удаление элементов по значению в переменной
motorcycles.remove(too_expensive) #Удаление элементов по значению в переменной
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")


invited_people = ['Vlad', 'Stas', 'Kirill', 'Nikita', 'Anton']
print(f'Список приглашенных:\n\a{invited_people[0]}\n\a{invited_people[1]}\n\a{invited_people[2]}\n\a{invited_people[3]}\n\a{invited_people[-1]}')
print(f'не может прийти {invited_people[2]}, потому что променял нас на Девочек')
invited_people[2] = 'Ilya'
print(f'Список приглашенных обновленный:\n\a{invited_people[0]}\n\a{invited_people[1]}\n\a{invited_people[2]}\n\a{invited_people[3]}\n\a{invited_people[-1]}')
invited_people.insert(0, 'Lena')
invited_people.insert(3, 'Oksana')
invited_people.insert(5, 'Pasha')
print(f'Список приглашенных обновленный:\n\a{invited_people[0]}\n\a{invited_people[1]}\n\a{invited_people[2]}\n\a{invited_people[3]}\n\a{invited_people[5]}')
print(invited_people.index('Pasha'))

print(invited_people.pop())
print(invited_people.pop())
print(invited_people.pop())
print(invited_people.pop())
print(invited_people.pop())
print(invited_people.pop())
print(invited_people)

del invited_people[0]
del invited_people[0]
print(invited_people)

#Sorted lists
#1
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() #По алфавиту
print(cars)
#2
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True) #В обратную сторону алфавита
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse() #В обратную сторону
print(cars)

print(len(cars)) #длина списка, кол-во элементов

print(sorted(cars)) #В алф. порядке
print(sorted(cars, reverse=True)) #обратный алфавит

