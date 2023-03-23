cpf = '74682489070';

iterator = iter(cpf[:9]);
num = range(-10, 0, 1);

sum = 0;

for n in num:
    try:
        nextNum = next(iterator);
        sum = sum + (abs(n) * int(nextNum));
    except:
        break;

resto = (sum * 10) % 11;
res = 0

if (resto <= 9):
    res = resto;

print(f'O primeiro digito do CPF é {res}')