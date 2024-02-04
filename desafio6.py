# Desafio 6: Para cada produto informado (nome, preço e quantidade), escreva o nome do produto comprado e o valor total a ser pago, considerando que são oferecidos descontos pelo número de unidades compradas, segundo a tabela abaixo: a. Até 10 unidades: valor total b. De 11 a 20 unidades: 10% de desconto c. De 21 a 50 unidades: 20% de desconto d. Acima de 50 unidades: 25% de desconto;

def calcular_desconto(quantidade_tabela):
    if quantidade_tabela <= 10:
        return 0
    elif quantidade_tabela > 10 and quantidade_tabela <= 20:
        return 0.1
    elif quantidade_tabela > 20 and quantidade_tabela <= 50:
        return 0.2
    else:
        return 0.25
    
def compras():
    nome_produto = input(str("Digite o nome do produto: "))

    try:  # Testando se o preço é um valor válido.
        preco_produto = float(input("Digite o preço do produto: "))
    except ValueError as e:
        print(f"Erro: {e}")
        return
    
    try:  # Testando se a quantia é um valor válido.
        quantidade_produto = int(input("Digite a quantidade do produto: "))
    except ValueError as e:
        print(f"Erro: {e}")
        return
        
    desconto_tabela = calcular_desconto(quantidade_produto) # Começando o desconto da tabela com 0 para alterá-lo ao longo da função.
    multiplicacao_desconto = preco_produto * desconto_tabela  # Multiplicação para determinar o valor do desconto.
    valor_cada = preco_produto - multiplicacao_desconto  # Esse valor representa o valor que ficará cada produto.
    valor_total = valor_cada * quantidade_produto  # Esse valor representa o valor total que o usuário irá pagar.

    if quantidade_produto <= 10:
        print(f"O produto {nome_produto} não terá desconto, saindo pelo valor de R${preco_produto:.2f}.")
    else: 
        print(f"O produto {nome_produto.capitalize()} terá desconto de R${multiplicacao_desconto:.2f}, saindo pelo valor de R${valor_cada:.2f} cada, dando no total o valor de R${valor_total:.2f}.")

compras()