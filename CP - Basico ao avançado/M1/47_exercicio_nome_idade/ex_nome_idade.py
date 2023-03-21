nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

invertido = nome[::-1]
espaco = " " in nome
qtdLetras = len(nome)
ultimaLetra = nome[-1]
if espaco:
    espaco = "contem"
else:
    espaco = "não contém"
if nome == "" or idade == "":
    print("Desculpe você deixou campos vazios")
else:
    print(f'Seu nome é {nome}\nSeu nome {espaco} espaços\nSeu nome tem {qtdLetras} letras\nA primeira letra do seu nome é {nome[0]}\nA última letra do seu nome é {ultimaLetra}')