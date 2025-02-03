#Dois tipos de Estrutura de controle:

#Seleção, exemplo:

#Indentação (representando por quatro espaço vazios)
a = 'internet'
lista = ['internett', 'rede', 'wifi', 'cabeada']

if a in lista:
     print('Tem internet')
else:
     print('Não tem internet')


#interação:

for palavra in lista:
     print(palavra)


b = 2
while b < 10:
        print(b, 'é menor do que 10')
        b += 1