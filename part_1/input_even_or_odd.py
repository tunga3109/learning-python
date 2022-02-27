number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")


#exercises
#1

car = input('What car do you want to buy? ')
print(f'Let me see if I can find you a {car}')

#2

table_num = int(input('How many tables do you to reserve?'))
if table_num > 8:
    print(f'We do not have enough {table_num} tables')
else:
    print(f'We have {table_num} tables')

#3

dig = int(input('input the digit: '))
if dig % 10 == 0:
    print('Ok')
else:
    print('Bad')