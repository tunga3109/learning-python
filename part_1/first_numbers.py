for i in range(1,5): #последнее число не выводится
    print(i)

numbers = list(range(1,6)) #Список из цифр
print(numbers)

even_numbers = list(range(2,11,2)) #Список из цифр с использованием срезов
print(even_numbers)

# 1 способ
squares = []
for value in range(1,11): #От 1 до 10
    square = value**2 #значение в квадрате
    squares.append(square)

print(squares)

# 2 способ - более компактный
squares = []
for value in range(1,11):
    squares.append(value**2)

print(squares)

# Простая статистика с числовыми списками
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(min(digits)) # Минимальный элемент в списке
print(max(digits)) # Максимальный элемент в списке
print(sum(digits)) # Сумма элементов в списке

squares = [value**2 for value in range(1,11)] # Список с использованием цикла
print(squares)

for i in range(1,21):
    print(i)

digits = [digit for digit in range(1,101)]
print(digits)

print(min(digits)) # Минимальный элемент в списке
print(max(digits)) # Максимальный элемент в списке
print(sum(digits)) # Сумма элементов в списке

odds = [odd for odd in range(1,21,2)]
print(odds)

squares = [value*3 for value in range(3,31)]
print(squares)

cub = [value**3 for value in range(1,11)]
print(cub)

for i in range(1,11):
    print(i**3)


