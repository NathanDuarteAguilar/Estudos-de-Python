##################################################################################################################################################
print('-------------------------------------------------------------------------------------------------------------------------------------\n\n')
##################################################################################################################################################

# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

# conta : cateto oposto = 3, cateto adjacente = 4, resultado = raiz(3² + 4²) / raiz(9 + 16) / raiz(25) / 5

import math

oposto = float(input("Cumprimento do cateto oposto: "))
adjacente = float(input("Cumprimento do cateto adjacente: "))


#print("A hipotenusa vai medir {:.2f}".format(math.sqrt((math.pow(oposto,2))+(math.pow(adjacente,2)))))

print("A hipotenusa vai medir {:.2f}".format(math.hypot(oposto, adjacente)))

##################################################################################################################################################
print('\n\n-------------------------------------------------------------------------------------------------------------------------------------')
##################################################################################################################################################