texto = "Estou estudando python"

texto_minus = texto.lower() #minuscula

print(texto_minus)

texto_mais = texto.upper() #Maiscula

print(texto_mais)

texto_primais = texto.title() #Retorna a primeira Letra em Maiscula

print(texto_primais)

texto_priletramais = texto.capitalize() #Retorna a primeira Letra em Maiscula e as demais minuscula

print(texto_priletramais)

from datetime import datetime

print(f'Data e horário atual: {datetime.now()}')
