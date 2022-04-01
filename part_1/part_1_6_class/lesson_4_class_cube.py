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


        
        