from typing import List
from open_file import OpenFile

def main():
    file = OpenFile()
    file.create_file()

    
    file.append_text()


    palavra_secreta: str = "banana"
    letras_acertadas: List[str] = []
    terminou: bool = False
    erros: int = 0
    rodada: int = 0

    for letra in palavra_secreta:
        letras_acertadas.append("-")

    while not terminou:
        cont: int = 0
        valida_erro: bool = False

        if erros > 6:
            return print("Você perdeu o jogo")
        print(letras_acertadas)
        print(f'Letras acertadas: {"".join(letras_acertadas)}\n\
Vidas restantes: {7 - rodada} ')  # join une a string vazia ás strings presentes na lista

        chute = input("Qual letra: ")
        for letra in range(1, len(palavra_secreta) + 1):
            if chute.upper() == list(palavra_secreta)[cont].upper():
                letras_acertadas[cont] = list(palavra_secreta)[cont]
                valida_erro = True
            cont += 1

        if not valida_erro:
            erros += 1

        if list(palavra_secreta) == letras_acertadas:
            terminou = True
            print(f'Você acertou a palavra secreta %s' % (palavra_secreta))
        rodada += 1


if __name__ == "__main__":
    main()
