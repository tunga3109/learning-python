players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) #срезы - последний не выводится


players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")

for player in players[:3]: #до 4 элемента невключительно
    print(player.title())

