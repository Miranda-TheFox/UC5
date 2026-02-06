# Programa que demonstra diferentes formas de fatiar uma string

palavra = "otorrinolaringologista"

# As 3 primeiras letras
print(f"As 3 primeiras letras: {palavra[:3]}")

# As 3 últimas letras
print(f"As 3 últimas letras: {palavra[-3:]}")

# Da primeira até a oitava posição
print(f"Da primeira até a oitava posição: {palavra[:8]}")

# A palavra invertida
print(f"A palavra invertida: {palavra[::-1]}")

# De três em três caracteres
print(f"De três em três caracteres: {palavra[::3]}")