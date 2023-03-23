def criarMultiplicador(mult):
    def multiplicar(num):
        return num * mult;
    return multiplicar

duplicar = criarMultiplicador(2);
triplicar = criarMultiplicador(3);

print(duplicar(2));
print(triplicar(2));