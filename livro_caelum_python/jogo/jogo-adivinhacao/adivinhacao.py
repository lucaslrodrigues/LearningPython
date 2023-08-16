# -*- coding: utf-8 -*-
def execute() -> str:
    barra: str = "*"
    print(f'%s\n\'    Jogo da adivinhação     \'\n%s' % (barra * 30, barra * 30))

    numero_secreto = 42
    partida = Partida()
    partida.validaPartida()

    for i in range(1, partida.getTentativas() + 1):
        print(f'Tentativa %d de %d' % (partida.getRodada(), partida.getTentativas()))
        response = int(input("Qual é o número secreto: "))

        if response == numero_secreto:
            return f'Você acertou o numero secreto %d' % numero_secreto
        elif response > numero_secreto and partida.getRodada() < 3:
            print("Você errou acima do número secreto")
        elif response < numero_secreto and partida.getRodada() < 3:
                 print("Você errou abaixo do numero secreto")
        else:
            return "Acabaram as tentativas"
        partida.passarRodada()

# def restam(tentativas: str) -> str:
#     return f"Você tem %d tentativas" % tentativas if tentativas > 1 else "Está é sua última tentativa"
# def text() -> str:
#     return ("---" * 15) + "Simple text"

class Partida:
    def __init__(self) -> None:
        self.__pontuacao: int = 1000
        self.__tentativas: int = 0
        self.__rodada: int = 0

    def getPontuacao(self) -> int:
        return self.__pontuacao

    def getTentativas(self) -> int:
        return self.__tentativas

    def getRodada(self) -> int:
        return self.__rodada

    def rodadas(self, nivel: int):
        if nivel == 1:
            self.__tentativas = 20
        elif nivel == 2:
            self.__tentativas = 10
        else:
            self.__tentativas = 5

    def passarRodada(self):
        self.__rodada += 1

    def isNumber(self, nivel):
        if nivel.isdigit():
            return False if not int(nivel) >= 1 or not int(nivel) <= 3 else True
        else:
            return False

    def validaPartida(self):
        valida = False
        while not valida:
            nivel = input("Qual nível jogar?\n" \
                  "1 - 20 tentativas\n" \
                  "2 - 10 tentativas\n" \
                  "3 - 5 tentativas\n" \
                  "4 - sair\n: ")
            valida = self.isNumber(nivel)
            print("Digite um numero válido") if not valida else self.rodadas(int(nivel))




if __name__ == "__main__":
    print(execute())
