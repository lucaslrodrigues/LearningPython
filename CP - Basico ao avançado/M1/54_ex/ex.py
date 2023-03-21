num = input("Digite um número: ")

if num.isdigit():
    if num % 2 == 0:
        print("Número par")
    else:
        print("Número impar")
else:
    print("Isto não é um número inteiro")


horas = input("Que horas são")

if horas >= 0 and horas < 11:
    print("Bom dia")
elif horas > 10 and horas < 18:
    print("Boa tarde")
else:
    print("Bom dia")

    