"""
 Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;

"""

# Definir a string a ser invertida
texto = "Exemplo de string a ser invertida"

# Inverter a string usando slicing
texto_invertido = texto[::-1]

# Imprimir o resultado
print(texto_invertido)

"""
Nessa solução, definimos a string a ser invertida na variável texto. Em seguida, utilizamos o operador de slicing [::-1] 
para inverter a string, atribuindo o resultado a uma nova variável chamada texto_invertido. Por fim, 
imprimimos o resultado usando a função print(). O resultado será a string invertida:

aditrevni res a gnirts ed olpmxE

"""