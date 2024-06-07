def tupla_count():
    cores = ("vermelho", "azul", "verde", "azul",)
    print(cores.count("vermelho"))
    print(cores.count("azul"))
    print(cores.count("verde"))

def tupla_index():
    linguagens = ("python", "js", "c", "java", "csharp",)
    print(linguagens.index("java"))
    print(linguagens.index("python"))

def tupla_len():
    linguagens = ("python", "js", "c", "java", "csharp",)
    print(len(linguagens))

if __name__ == '__main__':
    tupla_count()
    tupla_index()
    tupla_len()