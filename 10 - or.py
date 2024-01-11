# Condicional or
# or(ou)	Retorna True(verdadeiro) se uma das afirmações for verdadeira

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '1234'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
     print('Entrar')
else:
     print('Sair')

senha = input('Digite uma nova Senha: ') or 'Sem senha'
print("Sua nova senha é: ", senha)

