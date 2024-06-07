# Tupla é imutável
# Pode-se criar usando a classe tuple ou colocando valores separados por vírgula e parenteses

def criando_tupla():
    frutas = ("laranja", "pera", "uva",) # boa prática vírgula ao final para não confundir com precedência
    letras = tuple("python")
    numeros = tuple([1, 2, 3, 4])
    pais = ("Brasil",)
    print(f"""
        {frutas}
        {letras}
        {numeros}
        {pais}
    """, end="" )

def acessando_valroes():
    frutas = ("laranja", "pera", "uva",)
    print(frutas[0])
    print(frutas[2])
    print(frutas[-1])
    print(frutas[-3])

def tuplas_aninhadas():
    matriz = (
        (1, "a", 2),
        ("b", 3, 4),
        (6, 5, "c"),
    )
    print(matriz[0])
    print(matriz[0][0])
    print(matriz[0][-1])
    print(matriz[-1][-1])

def tuplas_fatiamento():
    tupla = ("p", "y", "t", "h", "o", "n",)
    print(tupla[2:])
    print(tupla[:2])
    print(tupla[1:3])
    print(tupla[0:3:2])
    print(tupla[::])
    print(tupla[::-1])

def tuplas_iterar():
    carros = ("gol", "celta", "palio",)

    for carro in carros:
        print(carro)
    
    for indice, carro in enumerate(carros):
        print(f"{indice}: {carro}")

if __name__ == '__main__':
    criando_tupla()
    acessando_valroes()
    tuplas_aninhadas()
    tuplas_fatiamento()
    tuplas_iterar()