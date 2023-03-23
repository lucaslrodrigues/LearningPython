x = 99;

def dentroDaFunction():
    x = 11;
    print(x); # INTERNO

dentroDaFunction();
print(x) # EXTERNO


def soma(num1, num2):
    return num1 + num2;

def soma2(num1, num2):
    print(num1 + num2);

soma = soma(2, 3);
soma2 = soma2(2, 3);

print(soma);

print(soma2);