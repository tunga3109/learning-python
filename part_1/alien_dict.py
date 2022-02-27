from turtle import speed


alien_0 = {'color': 'green', 'points': 5, 'speed': 'medium'} # словарь

print(alien_0['color']) #получить значение через ключ
print(alien_0['points'])

new_points = alien_0['points'] # получить значение через переменную
print(f"You just earned {new_points} points!")

alien_0['x_position'] = 0 # добавление ключ-значение
alien_0['y_position'] = 25 # добавление ключ-значение
print(alien_0)

print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # Пришелец двигается быстро.
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

del alien_0['points'] # Удаление пар «ключ-значение»
print(alien_0)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

language = favorite_languages['sarah'].title() 
print(f"Sarah's favorite language is {language}.")

alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.') # get()
print(point_value)

alien_0 = {
    'color': 'green', 
    'points': 5, 
    'speed': 'medium'} 

print(f'{ alien_0["color"]}\n{alien_0["points"]}\n{alien_0["speed"]}')

for name in favorite_languages.keys(): # перебор ключей словаря
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

