# while estrutura de repetição

# while sem condicional

condicao = 0

while condicao < 10:
    condicao = condicao + 1
    print("Seu número é: ", condicao)


# while com condicional
x = int(input("Digite um numero: "))
while x <= 10:
    print(x)
    x += 1
    if x == 10:
        print("x é igual a 10")
        break
else:
    print("fim while")






    