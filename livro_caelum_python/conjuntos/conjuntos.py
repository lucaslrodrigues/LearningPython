"""
Conjuntos eliminam ocorrencias duplicadas
"""


def main():
    a: set = set("abacate")
    b: set = set("abacaxi")

    print(a, b)
    show = [print(l) for l in a]

    funcoes = (
        a - b,  # Diferença
        a | b,  # União
        a & b,  # Inserseção
        a ^ b  # Diferença simétrica
    )
    show = [print(i) for i in funcoes]


if __name__ == "__main__":
    main()
