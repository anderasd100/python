#Uma classe em Python é uma ótima maneira de ter coleções de funções e atributos rotulados e organizados.

# Classe =  projeto Arquitetônico de um escritório
# Objeto = O escritório

class Escri:
    def __init__(self): # É uma função especial que estabele o estado inicial do objeto, informando seus atributos.
        self.movel = 4
        self.cor = 'verde'
        self.nome= 'Arq Patricia'

        def material(self):
            print(self.nome + ' é um escritório grande')

meu_escritorio = Escri()

vizinho_escritorio = Escri()