"""identar Código
Para o Python é por intemédio da identação que o interpretador do código
consegue determinar onde um bloco de comando se inicia e onde ele termina 
"""
def sacar(valor: float) -> None:
    """Validando saldo"""

    saldo = 500

    if saldo >= valor:
        saldo -= valor
        print(f'Valor de {saldo} em sua conta')

def depositar(valor):
    saldo = 500
    saldo += valor

    print(f'Valor atual da conta é {saldo}')

sacar(100)
depositar(100)