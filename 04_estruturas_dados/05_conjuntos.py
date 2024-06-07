# Traz valores unicos. Elimina valores duplicados
# Os dados voltam não ordenados
def criando_set():
    print(set([1, 2, 3, 1, 3, 4]))
    print(set("abacaxi"))
    print(set(["palio", "gol", "celta", "palio"]))

    # pouco usado como {}
    linguagens = {"python", "java", "python"}
    print(linguagens)

# Deve-se converter para uma lista antes de acessar os dados
def acessando_dados():
    numeros = {1, 2, 3, 2}
    numeros = list(numeros)
    print(numeros[0])

def set_iterar():
    carros = {"palio", "gol", "celta", "palio"}

    for carro in carros:
        print(carro)
    
    for indice, carro in enumerate(carros):
        print(f"{indice}: {carro}")

if __name__ == "__main__":
    criando_set()
    acessando_dados()
    set_iterar()