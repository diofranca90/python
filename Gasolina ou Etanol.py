# Programa para saber se é melhor usar alcool ou gasolina

print("\n""______ Gasolina ou Etanol______""\n")

gasolina = float(input("Digite o valor do litro da gasolina R$: "))
etanol = float(input("Digite o valor do litro do etanol R$: "))
economia = float(0.7)

if (gasolina * economia) >= etanol:
    print("É melhor colocar etanol por estar equivalente a 70% ou menos do que o valor da gasolina")
else:
    print("É melhor colocar gasolina")