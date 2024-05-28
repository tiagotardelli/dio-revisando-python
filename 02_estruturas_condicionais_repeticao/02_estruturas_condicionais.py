""""estrutura condicional

Permitem o desvio de fluxo de controle, quando determinadas expressões
lógicas são atendidas
"""

import sys

MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

def if_simlpes(saldo):
    """"If simples"""
    saque = float(input("Informe o valod do saque: "))

    if saldo >= saque:
        print("Realizado saque!")

    if saldo < saque:
        print("Saldo insuficiente!")

def if_com_else(saldo):
    """If com else"""
    saque = float(input("Informe o valod do saque: "))

    if saldo >= saque:
        print("Realizado saque!")
    else:
        print("Saldo insuficiente!")

def if_com_elif(saldo):
    """If com elif"""
    opcao = int(input("Informe uma opcção: [1] Sacar \n[2] Extrato: "))

    if opcao == 1:
        valor = float(input("Informe a quantia para saque: "))
        if saldo < valor:
            print(f'Valor de {valor} sacadao com sucesso')
        else:
            print("Você não tem saldo suficiente")
    elif opcao == 2:
        print("Exibindo o extrato ...")
    else:
        sys.exit('Opção inválida')

def validacoes_idade():
    idade = int(input("Informe sua idade: "))

    if idade >= MAIOR_IDADE:
        print("Maior de idade, pode tirar a CNH.")
    
    if idade < MAIOR_IDADE:
        print("Ainda não pode tirar a CNH.")
    
    if idade >= MAIOR_IDADE:
        print("Maior de idade, pode tirar a CNH.")
    else:
        print("Anda não pode tiara a CNH.")

    if idade >= MAIOR_IDADE:
        print("Maior de idade, pode tirar CNH")
    elif idade == IDADE_ESPECIAL:
        print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas")
    else:
        print("Ainda não pode tirar a CNH.")

def if_aninhado():
    conta_normal = True
    conta_universitaria = False

    saldo = 10000
    saque = 200
    cheque_especial = 100

    if conta_normal:
        if saldo >= saque:
            print("Saque realizado com sucesso!!!")
        elif saque <= (saldo + cheque_especial):
            print("Saque realizado com uso do cheque especial")
        else:
            print("Não foi possível realizar o saque, saldo insuficiente")
    elif conta_universitaria:
        if saldo >= saque:
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente")
    else:
        print("Sistema não reconheceu o tipo de conta, entre em contato com o seu gerente.")

def if_ternario():
    saldo = float(input("Digite o saldo: "))
    saque = float(input("Digite o saque: "))
    print(f'{"Sucesso" if saldo >= saque else "Falha"}') 

#if_simlpes(2000.0)
#if_com_else(2000.0)
#if_com_elif(2000.0)
#validacoes_idade()
#if_aninhado()
if_ternario()
