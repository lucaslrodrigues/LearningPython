PALAVRA = "tentativa"

plTemp = "*" * len(PALAVRA)

verify = True
while verify:
    l = input("Digite uma letra")
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
        print(plTemp)
    else:
        print("Digite outra letra")

    if plTemp == PALAVRA:
        print("Parabens! Você descobriou a palavra secreta")
        verify = False
