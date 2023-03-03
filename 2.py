"""
Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número,
ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
"""

# pede para o usuário informar um número inteiro positivo
n = int(input("Digite um número inteiro positivo: "))

# inicializa as variáveis para os dois primeiros números da sequência
a, b = 0, 1

# inicializa uma variável para armazenar o próximo número da sequência
proximo = a + b

# verifica se o número informado pelo usuário já é um dos primeiros números da sequência
if n == a or n == b:
    print(f"{n} pertence à sequência de Fibonacci.")
else:
    # itera sobre a sequência até encontrar um número maior ou igual ao número informado pelo usuário
    while proximo <= n:
        if proximo == n:
            print(f"{n} pertence à sequência de Fibonacci.")
            break
        a = b
        b = proximo
        proximo = a + b
    else:
        print(f"{n} não pertence à sequência de Fibonacci.")
