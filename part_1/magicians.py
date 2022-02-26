magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: #цикл for проходит по каждому элементу в списке
    print(magician)

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

dishes = ['pizza', 'sushi', 'burger']
for dish in dishes:
    print(f'I really love {dish}')
print('I really love pizza!')