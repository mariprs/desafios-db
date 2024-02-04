# Desafio 3: Construa a tabuada de um número. (ex: 1x1=1, 1x2=2,...,1x10=10);

def tabuada(numero):  # Encapsulando o código para que fique mais fácil de reutilizá-lo.
    for multiplicador in range(11): 
        operacao = numero * multiplicador
        print(f"{numero} x {multiplicador} = {operacao}")
tabuada(5)