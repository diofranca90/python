# Condicionais if elif e else

print("\n" "Incrisção de atleta" "\n")

nome = input("Digite seu nome: ")
posicao = input("Digite seu posição em campo: ")
idade = int(input("Digite sua idade: "))
camisa = int(input("Digite o número da camisa: "))

print("\n" "Jogador camisa:", camisa, "\n" "Posição:", posicao, "\n")

if (idade < 9):
    print("Categoria fraldinha")
elif (idade > 9 and idade < 11):
    print("Categoria dente de leite")
elif (idade > 11 and idade < 12):
    print("Categoria pré-mirim")
elif (idade > 12 and idade < 13):
    print("Categoria mirim")
elif (idade > 13 and idade < 15):
    print("Categoria infantil")
elif (idade > 15 and idade < 16):
    print("Categoria infanto-juvenil")
elif (idade > 16 and idade < 18):
    print("Categoria juvenil")
elif (idade > 18 and idade < 20):
    print("Categoria junior")  
else: 
    print("Categoria profissional")