##################################################################################################################################################
print('-------------------------------------------------------------------------------------------------------------------------------------\n\n')
##################################################################################################################################################

# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela

x = input("Digite qualquer coisa:")

print("Você escreveu: \'{}\'".format(x))

print("O tipo primitivo é: {}".format(type(x)))
print("É um alfanumérico? {}".format(x.isalnum()))
print("É um caracter alfabético? {}".format(x.isalpha()))
print("É um decimal? {}".format(x.isdecimal()))
print("É um dígito? {}".format(x.isdigit()))
print("É um identificador? {}".format(x.isidentifier()))
print("Todos os caracteres digitados são minúsuculos? {}".format(x.islower()))
print("Todos os caracteres são números inteiros? {}".format(x.isnumeric()))
print("É possível imprimir o que digitou? {}".format(x.isprintable()))
print("Todos os caracteres são espaços? {}".format(x.isspace()))
print("Está capitalizado? {}".format(x.istitle()))
print("Todos os caracteres são maiúsculos? {}".format(x.isupper()))


##################################################################################################################################################
print('\n\n-------------------------------------------------------------------------------------------------------------------------------------')
##################################################################################################################################################