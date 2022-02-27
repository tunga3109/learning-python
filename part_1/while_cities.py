prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True: # бесконечный цикл
    city = input(prompt)
    if city == 'quit':
        break # остановка бесконечного цикла c помощью break
    else:
        print(f"I'd love to go to {city.title()}!")

#Команда break может использоваться в любых циклах Python . 
#Например, ее можно включить в цикл for для перебора элементов словаря .