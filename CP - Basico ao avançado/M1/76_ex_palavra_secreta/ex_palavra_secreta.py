import os

PALAVRA = "tentativa"

plTemp = "*" * len(PALAVRA)

verify = True
while verify:
    print(plTemp)
    l = input("Digite uma letra: ")
    os.system('cls')

    plTempTemp = ''
    if l in PALAVRA:
        c=0
        for i in PALAVRA:
            if plTemp[c] != "*":
                plTempTemp += plTemp[c]
            else:
                if i == l:
                    plTempTemp += i
                else:
                    plTempTemp += "*"
            c+=1
            
        plTemp = plTempTemp
    else:
        print("Digite outra letra")

    if plTemp == PALAVRA:
        print("Parabens! Você descobriou a palavra secreta")
        verify = False
