# цикл while
current_number = 1
while current_number <= 5: # пока число меньше 5
    print(current_number)
    current_number += 1


#В первой строке отсчет начинается с 1, для чего current_number присваивается зна- чение 1.
# Далее запускается цикл while, который продолжает работать, пока значе- ние current_number остается меньшим или равным 5. 
# Код в цикле выводит значение current_number и увеличивает его на 1 командой current_number += 1. (Оператор += является сокращенной формой записи для current_number = current_number + 1.)
#Цикл повторяется, пока условие current_number <= 5 остается истинным. Так как 1 меньше 5, Python выводит 1, а затем увеличивает значение на 1, отчего current_ number становится равным 2. 
# Так как 2 меньше 5, Python выводит 2 и снова при- бавляет 1, и т. д. Как только значение current_number превысит 5, цикл останавли- вается, 

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue # пропускает все числа кратные 2 с помощью continue
    print(current_number)


while True:
    topping = input('Enter topping:')
    if topping == 'quit':
        break
    else:
        print(f'{topping} has been added')
    