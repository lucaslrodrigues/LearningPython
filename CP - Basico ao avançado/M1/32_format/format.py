a = "A"
b = "B"
c = 1.1

# string = "a={} b={} c={}"
# formato = string.format(a,b,c)

# formato = 'a={} b={} c={:.2f}'.format(a,b,c)
formato = 'a={0} a={0} a={0} b={nome2} c={nome3:.2f}'.format(
    a, nome2 = b, nome3 = c)

"""
a = Argumento
b, c = Parametro

TUDO DEPOIS DE PARAMETRO É UM PARAMETRO
"""

print(formato)