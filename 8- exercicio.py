# Exercicio condicional 

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

nome = str(nome)
idade = int(idade)

if idade >= 18:
    print("Acesso liberado")
else:
    print("Acesso negado menor de idade")
