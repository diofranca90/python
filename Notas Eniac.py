# Calcular a média ponderado seguindo avaliação da Faculdade Eniac
# Entrada de dados: 4 notas e saida: A media e o resultado de aprovação

# um subprograma como um procediemento: calcular_media()
def calcular_media():
    nome_aluno = input("Informe o seu nome: ")

    portfolio = float(input("Informe a sua nota do Portfólio: "))
    exer_fix = float(input("Informe a sua nota do exercícos de fixação: "))
    prova_eletr = float(input("Informe a sua nota da prova eletônica: "))
    mom_enade = float(input("Informe a sua nota do momento Enade: "))

    nota_media = portfolio*0.15 + exer_fix*0.30 + prova_eletr*0.45 + mom_enade*0.10
    
    print("A media  = {:.2f}".format(nota_media)) # comando format(..)
    print(f"A media  = {nota_media:.2f}")  # f"....{}.."

    if (nota_media >= 6.0):
        print(f"você {nome_aluno} está aprovado com a media = {nota_media:.2f}") 
        print("Parabéns!!")
    else:
        print("você {} está reprovado com a media = {:.2f}.".format(nome_aluno,nota_media))
        print("Vc precisar estudar mais !!!")

#Programa principal
#chamando subprograma calcular_media() para executar
calcular_media()
input("Fim do programa!") # para parar o resultado na tela quando rodar no prompt

# o que aprendemos hoje:
#comando input()
#comando print() + formatação de texto com variáveis
#utilizar variáveis sem necessário da declaração
#if e else 
#indentação: 4 espaços no minimo
#primeira função sem parametros
#comentários

'''
gshjjsjjkdskjk
jchsdjcsdkkdlka
dhjhjsdk
'''
"""
hsdhjkvjkb  xmn
"""
