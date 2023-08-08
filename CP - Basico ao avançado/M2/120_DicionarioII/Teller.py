from DicionarioII import Dicionario

dicio = Dicionario();
dicio.newPerson(('Ana', [{'rua' : 'Vila maria', 'estado' : 'São Paulo', 'numero' : '1056'}]),
                ('Lucas', 'Jardin Santa Lucrecia'),
                ('Maria Helena',[{'rua' : 'Rondonopolis', 'estado' : 'Mato Grosso do sul', 'numero' : '25'}]));

pessoas = dicio.getPerson()

for i in pessoas:
    print(i)