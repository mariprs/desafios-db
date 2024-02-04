# Desafio 1: Leia um número até que o usuário digite 10;
# Comentário pessoal: achei que esse exercício ficou um tanto ambíguo. Fiquei em dúvida se o programa leria o código até o usuário digitar 10 números ou o número 10 em si. Como interpretei literalmente, fiz a segunda opção.

def leitura_numeral():  # Optei por encapsular o código em uma função.
    numero = 0 
    while numero != 10:  # Uma estrutura de repetição para que enquanto o número for diferente de 10, o código repita as próximas ações .
        numero= int(input("Digite um número: ")) 
        print(numero) 
        if numero == 10:  
                break  # Entretanto, se o número for 10, o código será parado.
leitura_numeral()  #Chamando a função.