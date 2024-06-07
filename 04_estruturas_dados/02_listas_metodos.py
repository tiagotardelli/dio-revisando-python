def lista_append():
    lista = []

    lista.append(1)
    lista.append("Python")
    lista.append([40, 30, 20])

    print(lista)

def lista_clear():
    lista = [1, "Python", [40, 30, 20]]
    print(lista)
    lista.clear()
    print(lista)

def lista_copy():
    lista = [1, "Python", [40, 30, 20]]
    l2 = lista.copy()
    print(lista)
    l2[0] = 2
    print(l2)

def lista_count():
    cores = ["vermelho", "azul", "verde", "azul"]
    print(f"""
          Vermehlo: {cores.count("vemelho")}
          Azul: {cores.count("azul")}
          Verde: {cores.count("verde")}         
    """)

def lista_extend():
    linguages = ["python", "js", "c"]
    print(linguages)
    linguages.extend(["java", "csharp"])
    print(linguages)

def lista_index(): 
    #encontra a primeira ocorrência
    linguagens = ["python", "js", "c", "java", ]
    print(linguagens.index("java"))
    print(linguagens.index("python"))

def lista_pop():
    # Tira informação por fila da listas
    linguagens = ["python", "js", "c", "java", "csharp"]
    linguagens.pop()
    print(linguagens)
    linguagens.pop()
    print(linguagens)
    linguagens.pop()
    print(linguagens)
    linguagens.pop(0)
    print(linguagens)

def lista_remove():
    # Remove o primeiro que achar
    linguagens = ["python", "js", "c", "java", "csharp"]
    linguagens.remove("c")
    print(linguagens)

def lista_reverse():
    linguagens = ["python", "js", "c", "java", "csharp"]
    linguagens.reverse()
    print(linguagens)

def lista_sort():
    linguagens = ["python", "js", "c", "java", "csharp"]
    linguagens.sort()
    print(linguagens)
    linguagens = ["python", "js", "c", "java", "csharp"]
    linguagens.sort(reverse=True)
    print(linguagens)
    linguagens = ["python", "js", "c", "java", "csharp"]
    linguagens.sort(key=lambda x: len(x))
    print(linguagens)
    linguagens = ["python", "js", "c", "java", "csharp"]
    linguagens.sort(key=lambda x: len(x), reverse=True)
    print(linguagens)

def lista_len():
    linguagens = ["python", "js", "c", "java", "csharp"]
    print(len(linguagens))

def lista_sorted():
    linguagens = ["python", "js", "c", "java", "csharp"]
    print(sorted(linguagens, key=lambda x: len(x)))
    print(sorted(linguagens))
    print(sorted(linguagens, key=lambda x: len(x), reverse=True))

def lista_montando():
    print([n**2 if n > 6 else n for n in range(10) if n % 2 == 0])

if __name__ == '__main__':
    lista_append()
    lista_clear()
    lista_copy()
    lista_count()
    lista_extend()
    lista_index()
    lista_pop()
    lista_remove()
    lista_reverse()
    lista_len()
    lista_sorted()
    lista_montando()