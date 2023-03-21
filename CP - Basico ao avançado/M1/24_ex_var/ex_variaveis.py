from datetime import date

now = date.today()
nowYear = '{}'.format(now.year)

nome = "lucas"
sobrenome = "lima"
anoNascimento = 2003
idade = int(nowYear) - anoNascimento
maiorIdade = idade >= 18
altura = (185 /100)

print(
    "Nome: " , nome,
    "\nSobrenome: ", sobrenome,
    "\nIdade: ", idade,
    "\nAno de nascimento: ", anoNascimento,
    "\nÉ maior de idade? ", maiorIdade,
    "\nAltura: ",altura
)