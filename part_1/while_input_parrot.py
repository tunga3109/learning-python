message = input("Tell me something, and I will repeat it back to you: ")
print(message)

prompt = "\nTell me something, and I will repeat it back to you:" 
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit': # пока мы не напишем quit, программа не выйдет
    message = input(prompt)
    print(message)

prompt = "\nTell me something, and I will repeat it back to you:" 
prompt += "\nEnter 'quit' to end the program. "
active = True 
while active: # бесконечный цикл
    message = input(prompt)
    if message == 'quit': 
        active = False # остановка бесконечного цикла
    else: print(message)