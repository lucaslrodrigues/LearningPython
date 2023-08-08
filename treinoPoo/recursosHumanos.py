import colaborador

class RecursosHumanos:
    totalPromovidos: 0
    totalReajustes: 0

    def reajustarSalario(self, reajuste: float, colaborador: colaborador.Colaborador):
        valorReajustado = (colaborador.getSalario() * reajuste) + colaborador.salario;
        self.totalReajustes += 1;
        return valorReajustado;

    def promoverColaborador(self, colaborador: colaborador.Colaborador, cargo: str, salario: int):
        if salario > colaborador.getSalario():
            colaborador.setCargo(cargo);
            colaborador.setSalario(salario);
            self.totalPromovidos += 1;
            print("Promovido")
