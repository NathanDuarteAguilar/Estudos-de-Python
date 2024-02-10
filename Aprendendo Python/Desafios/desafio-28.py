##################################################################################################################################################
print('-------------------------------------------------------------------------------------------------------------------------------------\n\n')
##################################################################################################################################################

# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
# escolhido pelo compudator

# o programa deverá escrever na tela se o usuário venceu ou perdeu

import random

n1 = int(input("O número que o computador pensou foi entre 0 e 5, tente adivinhar, qual o número o computador pensou? "))
n2 = random.randint(0,5)
if n1 == n2:
    print("Parabens! Você acertou")
else:
    print("Você errou, o número escohido pelo computador foi {}, tente novamente".format(n2))

##################################################################################################################################################
print('\n\n-------------------------------------------------------------------------------------------------------------------------------------')
##################################################################################################################################################