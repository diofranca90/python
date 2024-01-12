""""
Peça ao usuário para digitar seu nome, sua idade
Se nome e idade forem digitados 
exiba:
    Seu nome é {nome}
    Seu nome invertido {nome}
    Seu nome contém {n} letras
    A primeira letra do seu nome é {letra}
    A ultima letra do seu nome é {letra}
Se não for digitado seu nome ou idade:
exiba:
    Desculpe, você deixou campos vazios

"""

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if nome == "" or idade == "":
    print("Desculpe, você deixou campos vazios ")
else:
    print(f"Seu nome é: {nome}")
    print(f"Seu nome invertido é: {nome[::-1]}")
    print(f"Seu nome contém {len(nome)} letras")
    print(f"A primeira letra do seu nome é: {nome[0]}")
    print(f"A ultima letra do seu nome é: {nome[-1]}")

