import random;
import sys;

print(random.randrange(3, 9));

sys.exit();
entrada = input("CPF [746.824.890-70]: ");
cpf = re.sub(r'[^0-9]', '', entrada);

if cpf == cpf[0] * len(cpf):
    print("Você enviou caracteres repetidos")

cpfCortado = cpf[:9];
novoCpf = cpfCortado

num = 10;
total = 0;
for n in cpfCortado:
    total += int(n) * num;
    num -= 1;
resto1 = (total * 10) % 11;
resto1 if resto1 <= 9 else 0;
novoCpf += str(resto1);

num = 11;
total = 0;
for n in novoCpf:
    total += int(n) * num;
    num -= 1;
resto2 = (total * 10) % 11;
resto2 if resto2 <= 9 else 0;
novoCpf += str(resto2);

if cpf == novoCpf:
    print(f'{cpf} é válido');
else:
    print('CPF inválido!');