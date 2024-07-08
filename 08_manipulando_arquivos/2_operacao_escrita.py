from pathlib import Path 

caminho = Path(__file__).resolve().parent

def escrevendo_no_arquivo():
    arquivo = open(f"{caminho}/teste.txt", 'w')
    arquivo.write("Escrevendo dados em um novo arquivo.")
    arquivo.writelines("Python")
    arquivo.writelines(["\n", "escrevendo", "\n", " um", "\n", " novo", "\n", " texto"])
    arquivo.close()

if __name__ == "__main__":
    escrevendo_no_arquivo()