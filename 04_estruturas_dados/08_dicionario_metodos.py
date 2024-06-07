def dicionario_clear():
    contatos = {
        "tiago@gmail.com": {"nome": "Tiago", "idade": 37, "telefone": "33344-1212" },
        "affonso@gmail.com": {"nome": "Affonso", "idade": 17, "telefone": "33344-1212" },
        "guilhermemail.com": {"nome": "Guilherme", "idade": 37, "telefone": "33344-1212" }
    }
    
    contatos.clear()
    print(contatos)

def dicionario_copy():
    contatos = {
        "tiago@gmail.com": {"nome": "Tiago", "idade": 37, "telefone": "33344-1212" },
        "affonso@gmail.com": {"nome": "Affonso", "idade": 17, "telefone": "33344-1212" },
        "guilhermemail.com": {"nome": "Guilherme", "idade": 37, "telefone": "33344-1212" }
    }

    copia = contatos.copy()
    copia["tiago@gmail.com"] = {"nome": "TT"}
    print(contatos["tiago@gmail.com"])
    print(copia["tiago@gmail.com"])

def dicionario_fronkeys():
    print(dict.fromkeys(["nome", "telefone"]))
    print(dict.fromkeys(["nome", "telefone"], "vazio"))

def dicionario_get():
    contatos = {
        "tiago@gmail.com": {"nome": "Tiago", "idade": 37, "telefone": "33344-1212" },
        "affonso@gmail.com": {"nome": "Affonso", "idade": 17, "telefone": "33344-1212" },
        "guilhermemail.com": {"nome": "Guilherme", "idade": 37, "telefone": "33344-1212" }
    }

    # print(contatos["chave"]) -> da erro no código
    print(contatos.get("chave"))
    print(contatos.get("chave", {}))
    print(contatos.get("tiago@gmail.com", {}))

def dicioanrio_items():
    contatos = {
        "tiago@gmail.com": {"nome": "Tiago", "idade": 37, "telefone": "33344-1212" },
        "affonso@gmail.com": {"nome": "Affonso", "idade": 17, "telefone": "33344-1212" },
        "guilhermemail.com": {"nome": "Guilherme", "idade": 37, "telefone": "33344-1212" }
    }
    print(contatos.items())

def dicionario_keys():
    contatos = {
        "tiago@gmail.com": {"nome": "Tiago", "idade": 37, "telefone": "33344-1212" },
        "affonso@gmail.com": {"nome": "Affonso", "idade": 17, "telefone": "33344-1212" },
        "guilhermemail.com": {"nome": "Guilherme", "idade": 37, "telefone": "33344-1212" }
    }
    print(contatos.keys())

def dicionario_pop():
    contatos = {
        "tiago@gmail.com": {"nome": "Tiago", "idade": 37, "telefone": "33344-1212" },
        "affonso@gmail.com": {"nome": "Affonso", "idade": 17, "telefone": "33344-1212" },
        "guilhermemail.com": {"nome": "Guilherme", "idade": 37, "telefone": "33344-1212" }
    }
    print(contatos.pop("affonso@gmail.com"))
    print(contatos.pop("affonso@gmail.com", {}))

def dicionario_popitem():
    contatos = {
        "tiago@gmail.com": {"nome": "Tiago", "idade": 37, "telefone": "33344-1212" },
        "affonso@gmail.com": {"nome": "Affonso", "idade": 17, "telefone": "33344-1212" },
        "guilhermemail.com": {"nome": "Guilherme", "idade": 37, "telefone": "33344-1212" }
    }
    print(contatos.popitem())
    print(contatos.popitem())

def dicionario_setdefault():
    contato = {"nome": "Tiago", "telefone": "33344-1212" }
    contato.setdefault("nome", "Giovana")
    print(contato)
    contato.setdefault("idade", 28)
    print(contato)

def dicionario_update():
     contatos = {
        "tiago@gmail.com": {"nome": "Tiago", "idade": 37, "telefone": "33344-1212" }
     }
     contatos.update({"tiago@gmail.com": {"nome": "TT"}})
     print(contatos)
     contatos.update({"giovana@gmail.com": {"nome": "Giovana", "telefone": "3222-0909"}})
     print(contatos)

def dicionario_values():
    contatos = {
        "tiago@gmail.com": {"nome": "Tiago", "idade": 37, "telefone": "33344-1212" },
        "affonso@gmail.com": {"nome": "Affonso", "idade": 17, "telefone": "33344-1212" },
        "guilhermemail.com": {"nome": "Guilherme", "idade": 37, "telefone": "33344-1212" }
    }
    print(contatos.values())

def dicionario_in():
    contatos = {
        "tiago@gmail.com": {"nome": "Tiago", "idade": 37, "telefone": "33344-1212" },
        "affonso@gmail.com": {"nome": "Affonso", "idade": 17, "telefone": "33344-1212" },
        "guilhermemail.com": {"nome": "Guilherme", "idade": 37, "telefone": "33344-1212" }
    }
    print("tiago@gmail.com" in contatos)
    print("megui@gmail.com" in contatos)
    print("endereco" in contatos["tiago@gmail.com"])
    print("telefone" in contatos["affonso@gmail.com"])

def dicionario_del():
    contatos = {
        "tiago@gmail.com": {"nome": "Tiago", "idade": 37, "telefone": "33344-1212" },
        "affonso@gmail.com": {"nome": "Affonso", "idade": 17, "telefone": "33344-1212" },
        "guilhermemail.com": {"nome": "Guilherme", "idade": 37, "telefone": "33344-1212" }
    }
    del contatos["affonso@gmail.com"]["telefone"]
    del contatos["guilhermemail.com"]
    print(contatos)

if __name__ == "__main__":
    dicionario_clear()
    dicionario_copy()
    dicionario_fronkeys()
    dicionario_get()
    dicioanrio_items()
    dicionario_keys()
    dicionario_pop()
    dicionario_popitem()
    dicionario_setdefault()
    dicionario_update()
    dicionario_values()
    dicionario_in()
    dicionario_del()