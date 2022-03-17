#import lesson_8_functions_pizza
#import lesson_8_functions_pizza as fp
#from lesson_8_functions_pizza import make_pizza
from lesson_8_functions_pizza import make_pizza as mp
from lesson_9_functions_user_profile import *

# 1
#lesson_8_functions_pizza.make_pizza(16,'tomato','pepperoni')
#fp.make_pizza(16,'tomato','pepperoni')
#make_pizza(16,'tomato','pepperoni')
mp(16,'tomato','pepperoni')

# 2
sandwitch('bread','pepperoni','salad')

t_chan = build_profile('tunga','chan',age='23',education='MSLU')
print(t_chan)

mers = car_model('Mercedes', 'Viano', color='red', nice=True)
print(mers)


