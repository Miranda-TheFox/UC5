# Programa que substitui palavras negativas por "***"

frase1 = "Esse sistema é muito ruim"
frase2 = "Eu odeio me exercitar"
frase3 = "Estou péssimo hoje!"

# Lista de palavras negativas a serem substituídas
palavras_negativas = ["ruim", "odeio", "péssimo"]

# Substitui as palavras negativas por "***"
for palavra in palavras_negativas:
    frase1 = frase1.replace(palavra, "***")
    frase2 = frase2.replace(palavra, "***")
    frase3 = frase3.replace(palavra, "***")

print(frase1)
print(frase2)
print(frase3)