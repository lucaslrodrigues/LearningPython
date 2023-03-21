print(True and True and "0" and False)
print(True and True and 0 and False)

print(True or True or "0" or 0)
print(False or False or "0" or 0)

senha = input("senha: ") or "Nenhuma senha digitada" # Deixar vazio
print(senha)
senha = input("senha: ") and "Adicionando senha" # Adicionar valor
print(senha)

# not

teste = not 1
print(teste)
teste = not 0
print(teste)

senha = input("senha: ")

if senha != 123:
    print(f'Senha invalida')
else:
    print('Dale')