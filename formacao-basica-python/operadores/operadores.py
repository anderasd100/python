#Operadores: Aritméticos, relacional, Lógico e de associação. 

#Aritméticos:

1+2
2+3
lista= ['Anderson'+'Adejair'+'Patricia'+'Neide']
print(lista)
print(len(lista))

lua = 'gata' * 20
print(lua)

estrela = 2 ** 4 #exponenciação
print(estrela)

#divisão simples
marte = 10/5
print(marte)

#Divisão inteira
marte1 = 10 // 5
print(marte1)

# Módulo operador de módulo, que retorna o resto da divisão entre dois números.
teste = 10 % 3
print(teste)

comparacaostg = 'mar' <= 'litoral'
print(comparacaostg)

# ==
#!=
# condição AND se ouver uma condição false irá voltar falso, exemplo:
cond1 = 10 == 10 and 7==6
print(cond1)

# condição OR se ouver uma condição TRUE irá voltar verdadeira, exemplo:
cond2 = 10 == 10 or 7==6
print(cond2)

teste2 = not False
print(teste2)

teste3= not True
print(teste3)

#Operadores associação:

esta = 10 in [4,6,6,87,564]
print(esta)

esta2= 10 not in [100,5,6,7,6,8]
print(esta2)