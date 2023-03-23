class Calculo():
    def __init__(self) -> None:
        pass
    
    def mult(self, *args):
        tot = 1;
        for n in args:
            tot *= n;
        return tot;

    def isParOuImpar(self, n):
        return n % 2 == 0;

    def showIsParOuImpar(self, n):
        pi = Calculo.isParOuImpar(self, n);
        if pi:
            return f"O número {n} é par!";
        return f'O número {n} é impar!';

calc = Calculo();
print(calc.mult(1, 2, 3, 4, 5));
print(calc.showIsParOuImpar(4))
print(calc.showIsParOuImpar(5))