# Obter o personagem na posição 1 (Nota: O primeiro caractere tem índice 0.):

a = 'Olá Anderson!'
print(a[1])

#Como as strings são arrays, podemos percorrer os caracteres em uma string, com um for loop
for x in 'Anderson':
    print(x)


#Para obter o comprimento de uma string, use o len() função.
compr = 'Anderson'
print(len(compr))

#Para verificar se uma determinada frase ou caractere está presente em uma string, podemos usar a palavra-chave in.

txt = "Gosto demais de Python. É uma super linguagem!!!!"
print("Python" in txt)

#Imprima somente se "livre" estiver presente:
txt = "Gosto demais de Python. É uma super linguagem!!!!"
if "Python" in txt:
 print("Sim, está presente")

#Verifique se "caro" NÃO está presente no seguinte texto:
txt = "Gosto demais de Python. É uma super linguagem!!!!"
print("Sim, está presente" not in txt)