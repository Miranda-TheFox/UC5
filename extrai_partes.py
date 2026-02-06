# Programa que extrai partes de um código de produto

codigo = "PROD-2024-XYZ"

# Extraindo o tipo do produto (PROD)
tipo_produto = codigo.split("-")[0]

# Extraindo o ano (2024)
ano = codigo.split("-")[1]

print(f"Tipo do produto: {tipo_produto}")
print(f"Ano: {ano}")