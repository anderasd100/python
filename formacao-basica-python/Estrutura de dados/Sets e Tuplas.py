#Sets: São definidos com chaves {} ou pela função set():

#Conjuntos: Se utiliza {} E os elementos não se repetem, são únicos'

conjunto ={'grama','sol', 'cachoeria', 'sol'}
print(conjunto)

#Listas (Sequencias de itens sepados por itens, separado por [])

#converter uma lista em um conjunto utilizando a função set()
lista = ['Masculino', 'Feminino', 'Masculino', 'Outro']
conjunto = set(lista)

#Removendo um elemento do conjunto
conjunto.discard('Masculino')

#Adicionando um elemento no conjunto
conjunto.add('Gay')

print(conjunto)


estar = 'Gay' in conjunto
print(estar)

def estacaodoAno():
    return 'primavera', 'verão', 'outono', 'inverno'

esta= type(estacaodoAno())
print(esta)