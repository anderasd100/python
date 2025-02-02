#Listas, Dicionários, Tuplas e conjuntos

#Listas (Sequencias de itens sepados por itens, separado por [])

lista = []
lista_numeros = [1,2,3]
lista_mista = [13, 'lista', [4,7,8,9], True, lista_numeros]

#sabendo o tamanho de uma lista, utilize a função LEN:
len(lista_mista)
print(len(lista_mista))

#Tupla se declara utilizando ():

tupla = (2,3,4) #não é possível anexar ou adicionar novos elementos
#Não podemos excluir elementos na Tupla, pois, uma vez declarada ela não pode ser modificada.
#Podemos utilizar para agilizar o processamento.

#Conjuntos: Se utiliza {} E os elementos não se repetem, são únicos'

conjunto_numero = {77,55,44,77,44}

print(len(conjunto_numero)) # Exemplo irá imprimir somente uma única vez o numeral: 77 e 44

#Dicionário: É uma sequência de itens no modelo chave-valor. São representados por uma chave correspondente e os valores são únicos.

dicionario = {'gata': 'Nina', 'legenda':32, 'Cidade': 'Cuiabá', 'Residente': True}

print(dicionario['Cidade'])