"""
Introdução ao empacotamento e desempacotamento
"""
nome1, *resto = ["Diorgenes", "Lorenzo", "Palmeiras"]

print(nome1, resto)

_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome)