def set_union():
    conjunto_a = {1, 2}
    conjunto_b = {3, 4}

    print(conjunto_a.union(conjunto_b))

def set_intersection():
    conjunto_a = {1, 2, 3}
    conjunto_b = {2, 3, 4}

    print(conjunto_a.intersection(conjunto_b))

def set_difference():
    conjunto_a = {1, 2, 3}
    conjunto_b = {2, 3, 4}

    print(conjunto_a.difference(conjunto_b))
    print(conjunto_b.difference(conjunto_a))

def set_symmetric_difference():
    conjunto_a = {1, 2, 3}
    conjunto_b = {2, 3, 4}

    print(conjunto_a.symmetric_difference(conjunto_b))

def set_issubset():
    conjunto_a = {1, 2, 3}
    conjunto_b = {4, 1, 2, 5, 6, 3}

    print(conjunto_a.issubset(conjunto_b))
    print(conjunto_b.issubset(conjunto_a))

def set_issuperset():
    conjunto_a = {1, 2, 3}
    conjunto_b = {4, 1, 2, 5, 6, 3}

    print(conjunto_a.issuperset(conjunto_b))
    print(conjunto_b.issuperset(conjunto_a))

def set_isdisjoint():
    conjunto_a = {1, 2, 3, 4, 5}
    conjunto_b = {6, 7, 8, 9}
    conjunto_c = {1, 0}

    print(conjunto_a.isdisjoint(conjunto_b))
    print(conjunto_a.isdisjoint(conjunto_c))

def set_add():
    sorteio = {1, 23}
    print(sorteio)
    sorteio.add(25)
    sorteio.add(42)
    sorteio.add(25)
    print(sorteio)

def set_clear():
    sorteio = {1, 23}
    print(sorteio)
    sorteio.clear()
    print(sorteio)

def set_copy():
    sorteio = {1, 23}
    print(sorteio)
    sorteio2 = sorteio.copy()
    print(sorteio2)

def set_discard():
    numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
    print(numeros)
    numeros.discard(1)
    numeros.discard(45)
    print(numeros)

# Elimina os valores do começo
def set_pop():
    numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
    print(numeros) 
    numeros.pop()
    numeros.pop()
    print(numeros)

def set_remove():
    numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
    print(numeros)
    numeros.remove(0)
    print(numeros)

def set_len():
    numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
    print(len(numeros))

def set_in():
    numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
    print(1 in numeros)
    print(10 in numeros)

if __name__ == "__main__":
    set_union()
    set_intersection()
    set_difference()
    set_symmetric_difference()
    set_issubset()
    set_issuperset()
    set_isdisjoint()
    set_add()
    set_clear()
    set_copy()
    set_discard()
    set_pop()
    set_remove()
    set_len()
    set_in()
