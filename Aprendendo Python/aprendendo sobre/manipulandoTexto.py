##################################################################################################################################################
print('-------------------------------------------------------------------------------------------------------------------------------------\n\n')
##################################################################################################################################################

##### Fatiamento #####

frase = str("Curso em Video Python")
print(frase)

print(frase[9])
print(frase[9:14])
print(frase[9:21:2])

print(frase[:5])
print(frase[15:])

print(frase[9::3])

##### Análise #####

#Comprimento da String
print(len(frase))

#conta quantos 'o' existem na frase
print(frase.count('o'))

#conta quantos 'o' existem na frase fatiando a string
print(frase.count('o',0,13))

#Mostra quantas vezes é encontrado 'deo'
print(frase.find('deo'))

#identifica a posição e se existe frase especifica dentro de string
print(frase.find('android'))

#validade a existencia da frase dentro da string
print('Curso' in frase)

##### Transformação #####

#subjstituição

print(frase.replace('Python','Android'))

#transformando todas as letras em maiusculo
print(frase.upper())

#transformando todas as letras em minusculo
print(frase.lower())

#transforma todos os caracteres em minusculo menos o primeiro caracter
print(frase.capitalize())

#transformando apenas as primeiras letras de cada palavra em maiusculo
print(frase.title())

##### Nova Frase #####
frase2 = "   Aprenda Python  "

#removendo espaços inuteis (primeiros e ultimos)
print(frase2.strip())

#removendo apenas espaços da direita
print(frase2.rstrip())

#removendo apenas espaços da esquerda
print(frase2.lstrip())

##### Divisão #####

#criando uma lista com cada conjunto de caracteres
print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[2][3])

##### junção #####

print('-'.join(frase))

##### escrevendo um  texto muito longo #####
print("""Criando um texto longo, quebrando linha 
e mesmo assim continuo escrevendo o mesmo texto com apenas um print
show de bola """)

##### Combinando comandos #####
print(frase.upper().count('O'))
print(len(frase.strip()))
print(frase.lower().find('video'))
##################################################################################################################################################
print('\n\n-------------------------------------------------------------------------------------------------------------------------------------')
##################################################################################################################################################