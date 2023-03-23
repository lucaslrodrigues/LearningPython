import os

itens = []
verify = True

while verify:
    opicao = input("Selecione uma opição\n[i]nserir \
[a]pagar [l]istar [0]sair: ")
    
    if opicao == "i" or opicao == "I":
        os.system("cls")

        item = input("Digite o item a ser adicionado: ")
        if len(item) > 0: 
            itens.append(item)
            print(item)
        else:
            print("Item não inserido")

    elif opicao == "a" or opicao == "A":
        os.system("cls")
        if len(itens) <= 0:
            print("Nada para ser apagado")
        else:
            i = input("Qual index deseja apagar? ")

            if len(itens) <= i:
                print("Index inválido!")
            else:
                print(f'Item {itens[i]} apagado')
                del itens[i]

    elif opicao == "l" or opicao == "L":
        os.system("cls")
        if len(itens) <= 0:
            print("Nada para ser listado")
        else:
            for index, name in enumerate(itens):
                print(index, name)

    elif opicao == '0':
        verify = False
        print("Até a próxima!")
    
    else:
        os.system("cls")
        print("Digite uma opição válida")