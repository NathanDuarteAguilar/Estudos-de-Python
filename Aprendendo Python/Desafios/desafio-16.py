##################################################################################################################################################
print('-------------------------------------------------------------------------------------------------------------------------------------\n\n')
##################################################################################################################################################

# Cria um programa que leia um número Real qualquer pelo teclado e mostre na ela sua porção inteira.
# Ex: Digite um número: 6.127  o número 6.127 tem parte inteira 6.

import math

num = float(input("Digite um valor: "))

print("O valor digitado foi {} e a sua porção inteira é {}".format(num, math.trunc(num)))

#fazendo sem blibioteca 

print("\nO valor digitado foi {} e a sua porção inteira é {}".format(num, int(num)))

##################################################################################################################################################
print('\n\n-------------------------------------------------------------------------------------------------------------------------------------')
##################################################################################################################################################