name = 'Igor'

print(f'Hello {name}, would you like to learn some Python today?')
print('Hello {}, would you like to learn some Python today?'.format(name))

print(name.title())
print(name.lower())
print(name.upper())

print('Albert Einstein once said, "A person who never made\n\ta mistake never tried anything new."')

famous_person = ' Albert Einstein '
print(f'{famous_person} once said, "A person who never made\n\ta mistake never tried anything new."')
print('{} once said, "A person who never made\n\ta mistake never tried anything new."'.format(famous_person))


print(famous_person.lstrip())
print(famous_person.rstrip())
print(famous_person.strip())