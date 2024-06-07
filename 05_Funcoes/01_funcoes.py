def exibir_mensagem():
    print("Olá mundo!")

def exibir_menagem_2(nome):
    print(f"Seja bem vido {nome}")

def exibir_menagem_3(nome="Anônimo"):
    print(f"Seja bem vido {nome}")

def calcualar_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

def funcao_teste():
    print('olá mundo')

def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

# *args -> tupla
# **kwargs -> dicionário
def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

# Positional only
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

# Keyword only
def criar_carro_2(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

# Keyword and Positional only
def criar_carro_3(modelo, ano, placa, /, *,marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é = {resultado}")

salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

if __name__ == "__main__":
    exibir_mensagem()
    exibir_menagem_2("Tiago")
    exibir_menagem_3()
    exibir_menagem_3("Tiago")
    print(calcualar_total([10, 20, 34]))
    print(retorna_antecessor_e_sucessor(10))
    print(funcao_teste())
    salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
    salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
    salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})
    exibir_poema("Zen of Python", "Beautiful is better than ugly.", autor="Tim Peters", ano=1999)
    criar_carro("Palio", 1999, "ABC-1231", marca="Fiat", motor="1.0", combustivel="gasolina")
    # Inválido
    # criar_carro(modelo="Palio", ano=1999, placa="ABC-1231", marca="Fiat", motor="1.0", combustivel="gasolina")
    criar_carro_2(modelo="Palio", ano=1999, placa="ABC-1231", marca="Fiat", motor="1.0", combustivel="gasolina")
    criar_carro_3("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="gasolina")
    exibir_resultado(10, 10, somar)
    exibir_resultado(10, 10, subtrair)
    print(salario_bonus(500))