"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
try:
    num = (input("Digite um numero inteiro: "))
    num = int(num)

    if num % 2 == 0:
        print("o número par")  
    else:
        print("o número é ímpar")

except:
    print("Este não é um número inteiro")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

print("\n" "____Saudação____")

hora = input("Digite a hora atual: ")
hora = int(hora)

if hora > 00 and hora <= 11:
    print("____Bom dia !____")
elif hora > 11 and hora <= 17:
    print ("____Boa tarde !____")
elif hora > 17 and hora <= 23:
    print("____Boa noite !____")
else:
    print(" Hora inexistene")

print("\n")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

print("____Tamanhdo do nome____")

nome = input("Digite seu nome: ")
nome = str(nome)

if len(nome) <= 4:
    print("Seu nome é curto")
elif len(nome) == 5 or len(nome) == 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande" "\n")
