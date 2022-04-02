# Чтение из файла

file_path = 'part_2/part_2_1_files/pi_digits.txt'
with open(file_path) as file_object:
    content = file_object.read()
    print(content.rstrip())



