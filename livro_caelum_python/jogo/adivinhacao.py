# -*- coding: utf-8 -*-
def execute() -> str:
    barra: str = "*"
    print(f'%s\n\'    Jogo da adivinhação     \'\n%s' % (barra * 30, barra * 30))

    numero_secreto = 42
    tentativas_restantes = 3

    while (tentativas_restantes > 0):
        response = int(input("Qual é o número secreto: "))
        if response == numero_secreto:
            return f'Você acertou o numero secreto %d' % numero_secreto
        elif response > numero_secreto:
            print("Você errou acima do número secreto")
        else:
             if tentativas_restantes > 0:
                 print("Você errou abaixo do numero secreto")
             else: return "Acabaram as tentativas"
        tentativas_restantes -= 1

def restam(tentativas: str) -> str:
    return f"Você tem %d tentativas" % tentativas if tentativas > 1 else "Está é sua última tentativa"
# def text() -> str:
#     return ("---" * 15) + "Simple text"


if __name__ == "__main__":
    print(execute())
