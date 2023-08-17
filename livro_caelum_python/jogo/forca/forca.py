from typing import List


def main():
	palavra_secreta: str = "banana"

	letras_acertadas: List[str] = []
	for letra in palavra_secreta:
		letras_acertadas.append("-")
	terminou: bool = False

	while not terminou:
		print(f'Letras acertadas: {"".join(letras_acertadas)}') # join une a string vazia ás strings presentes na lista
		chute = input("Qual letra: ")
		cont: int = 0
		for letra in palavra_secreta:
			if chute == palavra_secreta[cont]:
				letras_acertadas[cont] = letra
			cont += 1
		if list(palavra_secreta) == letras_acertadas:
			terminou = True
			print("Você acertou a palavra secreta")


if __name__ == "__main__":
	main()
