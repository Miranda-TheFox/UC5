# Programa que substitui um código de erro por outro na mensagem

mensagem = "Erro 401 - acesso negado"

# Substitui o código 401 por 403
mensagem_atualizada = mensagem.replace("403", "401")

print(mensagem_atualizada)