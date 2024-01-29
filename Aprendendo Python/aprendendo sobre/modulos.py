##################################################################################################################################################
print('-------------------------------------------------------------------------------------------------------------------------------------\n\n')
##################################################################################################################################################

###### importando biblioteca  math  inteira ######

import math

num = int(input("Digite um número: "))

raiz = math.sqrt(num)

#arredondando para cima usando ceil

print("A raiz de {} é igual a {}".format(num, math.ceil(raiz)))

#arredondando para baico usando floor
print("A raiz de {} é igual a {}".format(num, math.floor(raiz)))

###### importando funções especificas da biblioteca math ######

from math import sqrt

num = int(input("Digite um número: "))

raiz = sqrt(num)

print("A raiz de {} é igual a {}".format(num, raiz))

###### biblioteca random ######

import random 

num = random.randint(1,10)

print(num)

###### biblioteca emoji ######

import emoji

print(emoji.emojize('Python é :woman:'))

print(emoji.emojize("Olá, mundo :👩‍🍼:"))

##################################################################################################################################################
print('\n\n-------------------------------------------------------------------------------------------------------------------------------------')
##################################################################################################################################################