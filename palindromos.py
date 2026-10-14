palavra = input("Digite uma palavra: ")
p_invertida = palavra[::-1]
if palavra == p_invertida:
    print("A palavra é um palíndromo!")
else:
    print("A palavra não é um palíndromo!")
