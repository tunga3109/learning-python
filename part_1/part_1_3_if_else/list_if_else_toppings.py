requested_topping = 'mushrooms'

if requested_topping != 'anchovies': #неравенство
    print("Hold the anchovies!")

print(requested_topping != 'mushrooms') #неравенство
print(requested_topping == 'mushrooms') #равенство

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")


requested_toppings = ['mushrooms', 'onions', 'pineapple'] 
print('mushrooms' in requested_toppings) #есть ли элемент в массиве

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
       print("Sorry, we are out of green peppers right now.")
    else:
       print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")



available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")


users = ['admin','anton99','stas99','kirill99','vlad99']
for user in users:
    if user == 'admin':
        print(f'Hello {user}, would you like to see a status report?')
    else:
        print(f'Hello {user}, thank you for logging in again')