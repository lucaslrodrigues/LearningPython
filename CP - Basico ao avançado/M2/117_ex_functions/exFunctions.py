import os;

def mult(num, expo):
    return num * expo;

def raiz(num, indice):
    return num ** (1/indice);

bar = '-' * 60
verify = True
while verify:
    opicao = input(f"{bar}\nEscolha uma opição\n[1] Duplicar\n[2] Triplicar\n[3] Quadruplicar\n[4] Raiz\n[0] Sair\n>> ");
    os.system('cls')

    if opicao != "0":
        num = input("Qual número sera o número será utilizado? ")
    else:
        print("Até a próxima :)")
        verify = False;
        break;
    
    if not num.isdigit():
        print("Insira um valor válido!!")
    else:
        num = int(num)
        # calc = calculos(num)
        if opicao == '1':
            print(mult(num, 2))
        
        elif opicao == '2':
            print(mult(num, 3))

        elif opicao == '3':
            print(mult(num, 4))

        elif opicao == '4':
            indice = input("Qual será o indice? ")
            if not indice.isdigit():
                print("Insira um valor válido!!")
            else:
                indice = int(indice)
                val = raiz(num, indice)
                print("%.2f" % val)
        else:
            print("Valor incorreto")