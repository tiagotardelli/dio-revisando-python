from pathlib import Path 

ROOT_PATH = Path(__file__).resolve().parent

def arquivo_inexistente():
    try:
        arquivo = open(ROOT_PATH / "arquivo_que_nao_existe.txt", 'r')
        arquivo.close()
    except FileNotFoundError as exc:
        print("Arquivo não encontrado")
        print(exc)

def abrir_diretorio():
    try:
        arquivo = open(ROOT_PATH / "novo-diretorio", 'r')
    except IsADirectoryError as exc:
        print(f"Não foi possível abrir o arquivo: {exc}")
    except Exception as exc:
        print(f"Algum problema ocorreu ao tentar abrir o arquivo: {exc}")
if __name__ == "__main__":
    arquivo_inexistente()
    abrir_diretorio()