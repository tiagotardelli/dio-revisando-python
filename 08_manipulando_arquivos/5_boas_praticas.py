from pathlib import Path 

ROOT_PATH = Path(__file__).resolve().parent

def ler_arquivo():
    with open(ROOT_PATH / "lorem.txt", "r") as arquivo:
        1 / 0
    print(arquivo.read())

def ler_arquivo_erro():
    try:
        with open(ROOT_PATH / "losrem.txt", "r") as arquivo:
            1 / 0
        print(arquivo.read())
    except IOError as exc:
        print(f"Erro ao abrir o arquivo {exc}")

def arquivo_utf8():
    try:
        with open(ROOT_PATH / "arquivo-utf-8.txt", 'w',  encoding='utf-8') as arquivo:
            arquivo.write('Aprendendo a manipular arquivos utilizando Python.')
            print(arquivo.readline())
    except IOError as exc:
        print(f"Erro ao abrir o arquivo {exc}")

def arquivo_ascii():
    try:
        with open(ROOT_PATH / "arquivo-utf-8.txt", 'w',  encoding='ascii') as arquivo:
            print(arquivo.readline())
    except IOError as exc:
        print(f"Erro ao abrir o arquivo {exc}")

if __name__ == "__main__":
    ler_arquivo()
    ler_arquivo_erro()
    arquivo_utf8()
    arquivo_ascii()
