"""Escreva um programa que leia um numero inteiro maior do que zero e devolva, na tela, a
 soma de todos os seus algarismos. Por exemplo, ao numero 251 correspondera o valor
 8 (2 + 5 + 1). Se o numero lido nao for maior do que zero, o programa terminara com a
 mensagem “Numero invalido”."""

def maiorzero():
    numero = int(input("Informe um número: "))
    soma = 0
    while numero > 0:
        algor = numero % 10
        soma += algor
        numero //= 10
        print(f"A soma dos algorismo é: {soma}")


        maiorzero()