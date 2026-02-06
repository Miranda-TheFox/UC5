# Programa que formata um CPF ocultando os dígitos do meio

cpf = "12345678900"

# Extrai as partes do CPF usando slicing
primeira_parte = cpf[:3]
ultima_parte = cpf[-2:]

# Formata o CPF com asteriscos
cpf_formatado = f"{primeira_parte}.***.***.{ultima_parte}"

print(cpf_formatado)