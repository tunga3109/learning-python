print('hello world')

message = 'hello world'
print(message)

name = "ada lovelace"
print(name.title()) #Capitalize
print(name.upper()) #верхний регистр
print(name.lower()) #нижний регистр

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}" 
print(full_name)
print(f"Hello, {full_name.title()}!")
print("{} {}".format(first_name, last_name))

print("\tPython") #табуляция
print("Languages:\nPython\nC\nJavaScript") #разрывы строк

favorite_language = '   python  '
print(favorite_language.rstrip()) #удаление лишних пропусков с правой строны
print(favorite_language.lstrip()) #удаление лишних пропусков с левой стороны
print(favorite_language.strip()) #удаление лишних пропусков с обеих сторон


