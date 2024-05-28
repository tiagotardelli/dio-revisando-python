def repeticao_for():
    texto = input("informe um texto: ")
    VOGAIS = "AEIOU"


    for letra in texto:
        if letra.upper() in VOGAIS:
            print(letra, end="")
    else:
        print() # Adiciona uma quebra de linha
        print("Fim")

def usando_range():
    print(f'{list(range(4))}')

def range_com_for():
    for numero in range(0, 51, 5):
        print(numero, end=" ")

def repeticao_while():
    opcao = -1

    while opcao != 0:
        opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

        if opcao == 1:
            print("Sacando...")
        elif opcao == 2:
            print("Exibindo o extrato...")
    else:
        print("Obrigado por usar nosso sistema bancário, até logo!")

def usando_break_continue():
    while True:
        numero = int(input("Informe um núemro: "))

        if numero == 10:
            break;
        
        if numero % 2 == 0:
            continue

        print(numero)

#repeticao_for()
#usando_range()
#range_com_for()
#repeticao_while()
usando_break_continue()
