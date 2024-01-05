#Calculadora de IMC

print("\n" "Calculo do IMC" "\n")

nome = input("Insira seu nome: ")
idade = int(input("Insira sua idade: "))
peso = float(input("Insira seu peso: "))
altura = float(input("Insira seu altura: "))
imc = (peso / (altura * altura))

print("\n" "Resultado do IMC" "\n")

if (imc <= 18.5):
    print("Você esta abaixo do peso")
elif (imc > 18.5 and imc <= 24.9):
    print("Você esta com o peso normal")
elif (imc > 24.9 and imc <= 29.9):
    print("Você esta com sobrepeso")
elif (imc > 29.9 and imc <= 34.9):
    print("Você esta com obesidade I")
else: 
    print("Você esta com obesidade II e III")

print("Seu IMC é: ", imc)