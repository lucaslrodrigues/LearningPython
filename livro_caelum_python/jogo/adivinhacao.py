# -*- coding: utf-8 -*-
def execute() -> str:
    barra: str = "*"
    print(f'%s\n\'    Jogo da adivinhação     \'\n%s' % (barra * 30, barra * 30))

    numero_secreto = 42
    tentativas_restantes = 3
    rodada = 1

    for i in range(1, tentativas_restantes + 1):
        print(f'Tentativa %d de %d' % (rodada, tentativas_restantes))
        response = int(input("Qual é o número secreto: "))
        if response == numero_secreto:
            return f'Você acertou o numero secreto %d' % numero_secreto
        elif response > numero_secreto and rodada < 3:
            print("Você errou acima do número secreto")
        elif response < numero_secreto and rodada < 3:
                 print("Você errou abaixo do numero secreto")
        else:
            return "Acabaram as tentativas"
        rodada+=1

def restam(tentativas: str) -> str:
    return f"Você tem %d tentativas" % tentativas if tentativas > 1 else "Está é sua última tentativa"
# def text() -> str:
#     return ("---" * 15) + "Simple text"


if __name__ == "__main__":
    print(execute())
