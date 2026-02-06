# Programa que analisa uma frase contando caracteres e letras específicas

frase = "Integração é essencial"

# A quantidade total de caracteres
total_caracteres = len(frase)

# Quantas vezes a letra "e" aparece
quantidade_e = frase.lower().count("e")

print(f"Quantidade total de caracteres: {total_caracteres}")
print(f"Quantas vezes a letra 'e' aparece: {quantidade_e}")