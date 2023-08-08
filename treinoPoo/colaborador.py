class Colaborador:
    nome: str;
    cargo: str;
    salario: int;

    def getNome(self):
        return self.nome;
    
    def setNome(self, nome):
        self.nome = nome;

    def getSalario(self):
        return self.salario
    
    def setSalario(self, salario):
        self.salario = salario;

    def getCargo(self):
        return self.cargo;

    def setCargo(self, cargo):
        self.cargo = cargo;