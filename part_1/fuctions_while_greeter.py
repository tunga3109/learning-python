# Использование функции в цикле while
#def get_formatted_name(first_name, last_name):
#    """Возвращает аккуратно отформатированное полное имя."""
#    full_name = f"{first_name} {last_name}"
#    return full_name.title()

# Бесконечный цикл!

#while True:
#    print("\nPlease tell me your name:")
#    print("(enter 'q' at any time to quit)")
#    f_name = input("First name: ")
#    if f_name == 'q':
#        break
#
#    l_name = input("Last name: ")
#    if l_name == 'q':
#        break
#
#    formatted_name = get_formatted_name(f_name, l_name)
#    print(f"\nHello, {formatted_name}!")

#ex 1

def city_country(city, country):
    full = f'{city}, {country}'
    return full.title()

minsk = city_country('Minsk','Belarus')
moscow = city_country('Moscow', 'Russia')
riga = city_country('Riga', 'Latvia')
print(minsk)
print(moscow)
print(riga)

#ex 2

def make_album(singer, album):
    singer_dict ={
        'singer': singer,
        'album': album
    }
    return singer_dict

rammstein = make_album('Rammstein', 'Rosenrot')
l_park = make_album('Linkin Park', 'New Devide')
the_weekend = make_album('The weekend', 'Save your tears')
print(rammstein)
print(l_park)
print(the_weekend)

while True:
    singer = input('Singer: ')
    if singer == 'q':
        break
    album = input('Album: ')
    if album == 'q':
        break
    full_1 = make_album(singer, album)
    print(full_1) 