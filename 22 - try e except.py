# Tratamento de erro try e except

try:
    num = (input("Digite um numero inteiro: "))
    num = int(num)

    if num % 2 == 0:
        print("o número par")  
    else:
        print("o número é ímpar")

except:
    print("Este não é um número inteiro")