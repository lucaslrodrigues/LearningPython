from typing import List


def main():
	palavra_secreta: str = "banana"

	letras_acertadas: List[str] = []
	for letra in palavra_secreta:
		letras_acertadas.append("-")
	terminou: bool = False;
	erros: int = 0
	while not terminou:
		cont: int = 0
		print(erros)
		if erros >= 6:
			return print("Você perdeu o jogo")
		print(f'Letras acertadas: {"".join(letras_acertadas)}\n\
Vidas restantes: {7 - cont} ') # join une a string vazia ás strings presentes na lista
		chute = input("Qual letra: ")

		for letra in palavra_secreta:
			if chute.upper() == palavra_secreta[cont].upper():
				letras_acertadas[cont] = letra
				
			cont += 1
		if list(palavra_secreta) == letras_acertadas:
			terminou = True
			print(f'Você acertou a palavra secreta %s' % (palavra_secreta))


if __name__ == "__main__":
	main()
