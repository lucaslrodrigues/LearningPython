import re
import sys
# cpf = "746.824.890-70".replace('.', '').replace('-','');

# cpf = re.sub(r'[^0-9]', '',"746.(TEXTO_IGNORADO¨@#$%¨#&)824.890-70"); # Aceita apenas números

entrada = input("CPF [746.824.890-70]: ");
cpf = re.sub(r'[^0-9]', '', entrada);

if cpf == cpf[0] * len(cpf):
    print("Você enviou caracteres repetidos")
    sys.exit()

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
# print(f'O penultimo digito do CPF é {resto1}');

num = 11;
total = 0;
for n in novoCpf:
    total += int(n) * num;
    num -= 1;
resto2 = (total * 10) % 11;
resto2 if resto2 <= 9 else 0;
novoCpf += str(resto2);

# print(f'O último digito do CPF é {resto2}');

# print(f'O CPF é {novoCpf}');

if cpf == novoCpf:
    print(f'{cpf} é válido');
else:
    print('CPF inválido!');