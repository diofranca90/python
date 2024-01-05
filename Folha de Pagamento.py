# Este programa é para simular o sistema da folha de pagamento

# Um subprograma funciona como uma função (funciona como um valor)
def calcularSalarioLiq(sal_min, sal_bruto, descontoPS, descontoDs):
    sal_liquido = sal_bruto
    sal_liquido -= descontoDs    
    sal_liquido -= descontoPS * (50/100)
    sal_liquido += sal_min * (8/100)
    sal_liquido += sal_bruto * (5/100)

    return sal_liquido # retornar um resultado

# Um subprograma funciona como um procediemento
def mensagem_abertura():
    print("**************************************************")
    print(" Bem vindo ao Sistema da folha de pagemento       ")
    print("**************************************************")

# Um subprograma para impresso do resultado
def resultado(nome, sal_liquido, sal_bruto):
    print(f"O salário bruto do {nome} = R$ {sal_bruto:.2f}")
    print(f"O salário liquido do {nome} = R$ {sal_liquido:.2f}")

# *************************************************************************************
# programa principal
# chamada o subprgrama mensagem_abertura()
mensagem_abertura()    

continua = True
while (continua):
    # Entrada de dados
    sal_min = 1045.0

    nome_func =  input("Informe o nome de um funcionário: ")
    horasTrabalhadas = float(input("Informe horas trabalhadas por mês: "))
    valor_hora = float(input("Informe o valor por hora: "))                       

    sal_bruto = horasTrabalhadas * valor_hora

    descontoDs = float(input("Informe descontos diversos: "))
    descontoPS = float(input("Informe valor pago no plano de saude: "))

    # chamada do subprograma calcularSalarioLiq(.....)
    sal_receber = calcularSalarioLiq(sal_min, sal_bruto, descontoPS, descontoDs)

    # chamada do subprograma resultado(...)
    resultado(nome_func, sal_receber, sal_bruto)

    opcao = input("Desejar de continuar ??? (S ou N)")
    if (opcao.upper() == "N"):
        continua = False
        print("Você escolheu para sair!!")
    elif (opcao.upper() == "S"):
        continua = True
    else:
        continua = False
        print("Opção invalido e encerrando o sistema!!!")
    
input("Sistema da folha do pagamento encerrado!!!")

