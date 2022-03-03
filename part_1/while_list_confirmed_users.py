# Перемещение элементов между списками
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")  
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# ex 1
sandwich_orders = ['tuna', 'beaf', 'pork', 'sweet']
finished_sandwiches = []
while sandwich_orders:
    finishing_sandwiches = sandwich_orders.pop()

    print(f'i made {finishing_sandwiches.title()} sandwich')
    finished_sandwiches.append(finishing_sandwiches)

print(finished_sandwiches)
# ex 2
sandwich_orders = ['tuna','pastrami', 'beaf','pastrami', 'pork','pastrami', 'sweet']
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)

# ex 3

responses = {}
polling_active = True
while polling_active:
    name = input('name: ')
    answer = input('Where would you like to pass your vacation?: ')

    responses[name] = answer
    repeat = input('Anyone wants to answer(yse/no): ')
    if repeat == 'no':
        polling_active = False
print('--------- Responses --------')
for name, answer in responses.items():
    print(f'{name} want to pass his vacation in {answer}')


