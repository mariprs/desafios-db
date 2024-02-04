# Desafio 2: Definir a idade de uma pessoa e verificar se ela é maior de idade ou não;

def definir_maioridade(idade):
    # idade = 0
    # idade = int(input("Digite a idade: ")) # Caso essas duas linhas sejam "descomentadas", o código criará um input ao usuário.
    if idade >= 18: 
        print("Maior de idade")
    elif idade < 18:
        print("Menor de idade")
    else:
        print("Caracter inválido")  # Optei por adicionar caso o usuário digite um caracter inválido ao digitar a idade.
definir_maioridade(18)  # Neste caso, a idade já está definida e a função é executada com base nela.