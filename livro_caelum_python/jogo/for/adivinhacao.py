# -*- coding: utf-8 -*-
def execute() -> str:
    barra: str = "*"
    print(f'%s\n\'    Jogo da adivinhação     \'\n%s' % (barra * 30, barra * 30))

    numero_secreto = 42
    partida = Partida()
    partida.rodada(3)
    print(partida.tentativas)

    for i in range(1, partida.tentativas + 1):
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

class Partida:
    def __init__(self) -> None:
        self.pontuacao: int = 1000
        self.tentativas: int = 0

    def rodada(self, nivel: int):
        if nivel == 1:
            self.tentativas = 20
        elif nivel == 2:
            self.tentativas = 10
        else:
            self.tentativas = 5
 

if __name__ == "__main__":
    print(execute())
