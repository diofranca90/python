# Condicional and
# and(e)	Todas as condições precisam ser True(verdadeira)

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
altura = input("Digite sua altura: ")

nome = str(nome)
idade = int(idade)
altura = float(altura)

if idade < 18 and altura >= 1.65:
    print("Acesso negado menor de idade")
elif idade >= 18 and altura < 1.65:
    print("Acesso negado, altura abaixo da permitida")
else:
    print("Acesso liberado")



