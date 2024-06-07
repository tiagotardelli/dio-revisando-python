def declarando():
    frutas = ["laranja", "maca", "uva"]
    print(frutas)
    frutas = []
    print(frutas)
    letras = list("python")
    print(letras)
    numero = list(range(10))
    print(numero)
    carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
    print(carro)

def acessar_valores():
    frutas = ["maça", "laranja", "uva", "pera"]
    print(f" Posição 0 - {frutas[0]} | Posição 2 - {frutas[2]}")
    print(f" Posição 0 - {frutas[-1]} | Posição 2 - {frutas[-3]}")

def lista_aninhadas():
    matriz = [
        [1, "a",2],
        ["b", 3, 4],
        [6, 5, "c"]
    ]
    print(matriz[0])
    print(matriz[0][0])
    print(matriz[0][-1])
    print(matriz[-1][-1])

def fatiamento():
    lista = ["p", "y", "t", "h", "o", "n"]
    print(lista[2:])
    print(lista[:2])
    print(lista[1:3])
    print(lista[0:3:2])
    print(lista[::])
    print(lista[::-1])

def iterar_lista():
    carros = ["gol", "celta", "palio"]

    for carro in carros:
        print(carro)
    
    for indice, carro in enumerate(carros):
        print(f"{indice}: {carro}")

def compreensao_listas():
    # versao sem compreension
    numeros = [1, 30, 21, 2, 9, 65, 34]
    pares = []

    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
    print(pares)

    # versao com compreension
    numeros2 = [1, 30, 21, 2, 9, 65, 34]
    pares2 = [numero for numero in numeros2 if numero % 2 == 0]
    print(pares2)

if __name__ == '__main__':
    declarando()
    acessar_valores()
    lista_aninhadas()
    fatiamento()
    compreensao_listas()
