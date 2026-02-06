# Programa que gera um nome de usuário a partir do nome completo

nome_completo = "Carlos Eduardo Silva"

# Divide o nome completo em partes
partes = nome_completo.split()

# Pega o primeiro nome e o último sobrenome
primeiro_nome = partes[0].lower()
ultimo_sobrenome = partes[-1].lower()

# Gera o nome de usuário
nome_usuario = f"{primeiro_nome}.{ultimo_sobrenome}"

print(nome_usuario)