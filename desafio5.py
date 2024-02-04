# Desafio 5: Implemente um jogo Jokenpo (Pedra, papel ou tesoura). Será o jogador contra a máquina. O código tem que gerar as posições aleatoriamente e comparar com o que escolhemos;

import random  # Como lidaremos com decisões aleatórias, importanto mais uma vez a biblioteca random.
def jokenpo():
    lista_escolhas_maquina = ["pedra", "papel", "tesoura"] 
    escolha_maquina = random.choice(lista_escolhas_maquina)
    # print(escolha_maquina)  # Pra facilitar na hora de testar o código.
    escolha_player = input("Pedra, papel ou tesoura? ").lower()  # O lower aqui é só converter o que foi escrito para minúsculo pra evitar possíveis bugs.
    if escolha_player == escolha_maquina:
            print(f"O computador escolheu {escolha_maquina.capitalize()}")
            print("Empate!")
    elif escolha_player == "pedra" and escolha_maquina == "papel" or escolha_player == "papel" and escolha_maquina == "tesoura" or escolha_player == "tesoura" and escolha_maquina == "pedra":
            print(f"O computador escolheu {escolha_maquina.capitalize()}")
            print("A máquina venceu 🤖🏆")
    elif escolha_maquina == "pedra" and escolha_player == "papel" or escolha_maquina == "papel" and escolha_player == "tesoura" or escolha_maquina == "tesoura" and escolha_player == "pedra":
            print(f"O computador escolheu {escolha_maquina.capitalize()}")
            print("Vitória do humano 🙋🏆")
    else:
            print("Caracter inválido. Tente novamente")
jokenpo()