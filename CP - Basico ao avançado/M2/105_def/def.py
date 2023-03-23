# POO EM PYTHON NÃO PRECISA DE SETTER()

class Check:
    def __init__(self, nome):
        self.nome = nome;
    
    # def setNome (self, name):
    #     self.nome = name;

    def getNome (self):
        print("Ola ", self.nome);


obj = Check("Lucas");
obj.getNome();
# obj.setNome()

class Calculo:
    def __init__(self) -> None:
        pass;
    
    def compararMultiplo(self, num1, num2):    
        return True if (num1 % num2 == 0) else False;
    
    def mostrarMultiplo(self, num1, num2):
        res = Calculo.compararMultiplo(self, num1, num2);
        if res:
            print(f'{num1} é multiplo de {num2}!');
        else:
            print(f'{num1} não é multiplo de {num2}!');

    
obj2 = Calculo();
obj2.mostrarMultiplo(16, 8);