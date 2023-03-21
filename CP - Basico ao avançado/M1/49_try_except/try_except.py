num = input("Digite um número: ")

if num.isdigit():
    num_float = float(num)
    print('Em float %.2f' % (num_float))
else:
    print("valor invalido")


try:
    print(f'Em string: {num}')
    num_float = float(num)
    print('Em float %.2f' % (num_float))
except:
    print("valor invalido")