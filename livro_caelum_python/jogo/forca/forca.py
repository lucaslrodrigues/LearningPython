def main():
	palavra_secreta = "banana"

	letras_acertadas = []
	for letra in palavra_secreta:
     		letras_acertadas.append("-")
	terminou = False

	while not terminou:
    		chute = input("Qual letra")
    		cont = 0
    		for letra in palavra_secreta:
         		if letra == palavra_secreta[cont]:
	             		letras_acertadas[cont] = letra
         	if list(palavra_secreta) == letras_acertadas:
             	terminou == True
         	cont += 1
    	terminou = True
    
if __name__ == "__main__":
    main()
