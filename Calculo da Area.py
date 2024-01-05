# Programa simples #
"""
comentário em varias linhas

"""

largura_garagem = float (input("Insira a largura da garagem: "))
profundidade_garagem = float (input("Insira a profundidade da garagem: "))

area_garagem = largura_garagem * profundidade_garagem

largura_terreno = float (input("Insira a largura do terreno: "))
profundidade_terreno = float (input("Insira a profundidade do terreno: "))

area_terreno = largura_terreno * profundidade_terreno
percentual_ocupacao = area_garagem / area_terreno

print("Percentual de ocupacao e: ", percentual_ocupacao)
