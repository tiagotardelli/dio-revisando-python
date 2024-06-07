# As chaves dos dicionários são imutáveis
def criando_dicionario():
    pessoa = {"nome": "Tiago", "idade": 37}
    pessoa = dict(nome="Tiago", idade=28)
    print(pessoa)
    pessoa["telefone"] = "1234-1231"
    print(pessoa)

def acessando_dicionario():
    dados = {"nome": "Tiago", "idade": 37, "telefone": "1234-1231"}
    print(dados["nome"])
    print(dados["idade"])
    print(dados["telefone"])

    dados["nome"] = "Maria"
    dados["idade"] = 18
    dados["telefone"] = "9090-90988"
    print(dados)

def dicionario_aninhado():
    contatos = {
        "tiago@gmail.com": {"nome": "Tiago", "idade": 37, "telefone": "33344-1212" },
        "affonso@gmail.com": {"nome": "Affonso", "idade": 17, "telefone": "33344-1212" },
        "guilhermemail.com": {"nome": "Guilherme", "idade": 37, "telefone": "33344-1212" }
    }
    print(contatos["tiago@gmail.com"]["telefone"])

def dicionario_iterar():
    contatos = {
        "tiago@gmail.com": {"nome": "Tiago", "idade": 37, "telefone": "33344-1212" },
        "affonso@gmail.com": {"nome": "Affonso", "idade": 17, "telefone": "33344-1212" },
        "guilhermemail.com": {"nome": "Guilherme", "idade": 37, "telefone": "33344-1212" }
     }
    
    for chave in contatos:
        print(chave, contatos[chave])
    
    for chave, valor in contatos.items():
        print(chave, valor)

if __name__ == "__main__":
    criando_dicionario()
    acessando_dicionario()
    dicionario_aninhado()
    dicionario_iterar()