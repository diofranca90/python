# Exercicio condicional
# Descubra qual valor digitado Ã© maior o primeiro ou o segundo

numero_1 = input("Digite um valor: ")
numero_2 = input("Digite um valor: ")

if numero_1 > numero_2:
    print("O valor 1: ", numero_1, "Ã© maior que o valor 2: ", numero_2)
elif numero_1 == numero_2:
        print("O valor 1: ", numero_1, "Ã© igual ao valor 2: ", numero_2)
else:
    print("O valor 2:",numero_2, "Ã© maior que o valor 1:",numero_1)

# condicional com f-string
if numero_1 > numero_2:
    print(
        f"{numero_1} Ã© maior "
        f"que {numero_2}"
    )
elif numero_1 == numero_2:
    print(
         f"{numero_1} Ã© igual "
         f"a {numero_2}"
    )
else:
    print(
        f"{numero_2} Ã© maior "
        f"do que {numero_1}"
    )