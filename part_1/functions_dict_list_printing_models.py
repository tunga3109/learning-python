from functions_printing_funtions import print_models, show_completed_models
#import functions_dict_person
import functions_dict_person as fdp
#from functions_dict_person import build_person 
#from functions_dict_person import build_person as bp
from functions_user_profile import *


# Изменение списка в функции

# Список моделей, которые необходимо напечатать.
#from email import message
#
#
#unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
#completed_models = []
# Цикл последовательно печатает каждую модель до конца списка.
#  После печати каждая модель перемещается в список completed_models.
#while unprinted_designs:
#    current_design = unprinted_designs.pop()
#    print(f"Printing model: {current_design}")
#    completed_models.append(current_design)
## Вывод всех готовых моделей.
#print("\nThe following models have been printed:")
#for completed_model in completed_models:
#    print(completed_model)
#
#def print_models(unprinted_designs, completed_models): 
#    """Имитирует печать моделей, пока список не станет пустым.
#    Каждая модель после печати перемещается в completed_models."""
#    while unprinted_designs:
#        current_design = unprinted_designs.pop()
#        print(f"Printing model: {current_design}")
#        completed_models.append(current_design)
#
#def show_completed_models(completed_models):
#    """Выводит информацию обо всех напечатанных моделях.""" 
#    print("\nThe following models have been printed:")
#    for completed_model in completed_models:
#        print(completed_model)




# ex 1

#def show_messages(messages):
#    for message in messages:
#        print(message)
#
#message = ['hello', 'world']
#show_messages(message)

#1
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

#2
tunga = fdp.build_person('tunga','chan')
print(tunga)


sandwitch('cheezz', 'fkjkjdf', 'dfdfdf')

artem = build_profile('tunga','chan',age='30',occupation='support agent')
print(artem)

mers = car_model('Mercedes','viano',color='red')
print(mers)