banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.") # Если элемент не в этом массиве


car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

if car.islower():
    print('ok')


age = 19
if age >= 18: # Если значение переменной age больше или равно 18, то....
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else: #иначе
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")