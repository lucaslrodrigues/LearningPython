def saudacao (msg, nome):
    return f'{msg} {nome}';

def executar(f, msg, nome):
    return f(msg, nome);

def executar(f, *args): # HIGH ORDER FUNCTION
    return f(*args);

print(executar(saudacao, 'bom dia', 'Lucas'));

print(type(int('1'))) # FIRST-CLASS FUNCTIONS (funções de retorno)