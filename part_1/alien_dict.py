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

print("The following languages have been mentioned:")
for language in favorite_languages.values(): # перебор значении словаря
    print(language.title())

glossary = {
    'termin_1':'definition_1',
    'termin_2':'definition_2',
    'termin_3':'definition_3',
    'termin_4':'definition-_4',
}

for term, defin in glossary.items():
    print(f'{term}:{defin}')

# объединение словарей
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2] 
for alien in aliens:
    print(alien)

# Создание пустого списка для хранения пришельцев.
aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Вывод первых 5 пришельцев:
for alien in aliens[:5]:
    print(alien)
print("...")


# Вывод количества созданных пришельцев.
print(f"Total number of aliens: {len(aliens)}")