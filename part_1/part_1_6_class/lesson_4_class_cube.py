#1
from random import choice, randint

class Die():

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1,self.sides))

#c = Die(20)
#for i in range(10):
#    c.roll_die()
#
#class Loterey():
#
#    def __init__(self, *combination):
#        self.combination = ['1','2','3','4','5','6','7','8','9','a','b','c','d','e']
#        self.winner = []
#
#    def random(self):
#        for i in range(4):
#            a = choice(self.combination)
#            self.winner.append(a)
#
#        b = ''.join(self.winner)
#        if b == 'abc4':
#            print('You are winner')
#        else:
#            print(f'Try again \n comb {b}')
#
#    
#  
#d = Loterey()


# 2

my_ticket = [323,4554,7767,5845,9293]
attempts = 0

while True:
    combination = choice(my_ticket)
    if combination == 4554:
        attempts += 1
        print(f'You are winner {combination}')
        break
    else:
        attempts += 1
        print(f'Try again {combination}')

print(f' Attempts - {attempts}\n {attempts - 1} - Unsuccessfully \n {attempts - (attempts -1)} - Successfully')




    



    
    
    


        
        