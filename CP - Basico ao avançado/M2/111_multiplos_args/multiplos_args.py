x, y, *resto = 1, 2, 3 ,4;
print(x, y, resto);
def soma(*args):
    total = 0;
    for numero in args:
        # print("Total", total, numero);
        total += numero;
        print("Total", total);
    print(total);

soma(1, 2, 3, 4, 5, 6);
num = (1, 2, 3, 4, 5, 6); # TUPLA PARA SUM

print("Com o sum", sum(num)) # SUM SÓ RECEBER NO MÁXIMO 2 ARGS, POR ISSO É NECESSÁRIO UMA TUPLA PARA DESEMPACOTAR
print(*num) # DESEMPACOTADO