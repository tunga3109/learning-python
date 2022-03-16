def build_profile(first, last, **user_info):
    """Строит словарь с информацией о пользователе."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
    
user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)

#1

def sandwitch(*components):
    print('components: ')
    for component in components:
        print(f'- {component}')
        
sandwitch('cheezz', 'fkjkjdf', 'dfdfdf')

#2

def build_profile(name, last_name, **user_info):
    user_info['name'] = name
    user_info['last_name'] = last_name
    return user_info

artem = build_profile('Artem', 'Ivanov', age='20', occupation='programmer')
print(artem)

#3

def car_model(logo, model, **car_info):
    car_info['logo'] = logo
    car_info['model'] = model
    return car_info

mercedes = car_model('Mercedes', 'Viano', color='Black',tow_package=True)
print(mercedes)