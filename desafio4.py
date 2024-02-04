# Desafio: Gere 10 números aleatórios entre 0 e 100; mostre todos na tela (em uma única linha); identifique o menor e o maior deles;

import random  # Importanto a biblioteca random para lidar com operações envolvendo números aleatórios em Python.
def definindo_aleatorio():
    numero_aleatorio = range(100) 
    lista_aleatoria = (random.choices(numero_aleatorio, k = 10))  # k é a variável reservada onde é inserido o valor do tamanho da lista que será retornada por random.choices.
    print(f"Valores: {lista_aleatoria}.") # Optei por salvar a lista em uma variável para utilizá-la na próxima função.
    menor_valor = min(lista_aleatoria)
    maior_valor = max(lista_aleatoria)
    print(f"O menor valor é: {menor_valor}. \nO maior valor é: {maior_valor}.")
definindo_aleatorio()