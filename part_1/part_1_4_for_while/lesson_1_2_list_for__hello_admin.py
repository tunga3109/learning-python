users = ['admin','anton99','stas99','kirill99','vlad99']
for user in users:
    if user == 'admin':
        print(f'Hello {user}, would you like to see a status report?')
    else:
        print(f'Hello {user}, thank you for logging in again')

us = []
if us:
    for user in users: 
        print(f'{user} has been added') # если есть элементы в списке
else:
    print('empty list') # если нет элементов в списке


digits = list(range(1,10))
for digit in digits:
    if digit == 1:
        print(f'{digit}st')
    elif digit == 2:
        print(f'{digit}nd')
    elif digit == 3:
        print(f'{digit}rd')
    else:
        print(f'{digit}th')

current_users = ['Anton', 'Katya', 'Lena', 'Edgar', 'Tonya']
new_users = ['Katya', 'ANTON', 'Andrew', 'Vlad', 'Vasya']

for new_user in new_users:
    if new_user in current_users:
        print(f'{new_user} is already exist')
    else:
        print(f'{new_user} has never been used')
