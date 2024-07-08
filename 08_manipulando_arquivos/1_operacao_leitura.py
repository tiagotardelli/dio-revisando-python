from pathlib import Path 

caminho = Path(__file__).resolve().parent

def ler_arquivo_read():
    arquivo = open(f"{caminho}/lorem.txt", 'r')
    print("##### Read #####" )
    print(arquivo.read())
    print('#' * 190)
    arquivo.close()

def ler_arquivo_readline():
    arquivo = open(f"{caminho}/lorem.txt", 'r')
    print("##### Readline #####" )
    print(arquivo.readline())
    print(arquivo.readline())
    print(arquivo.readline())
    print(f"{arquivo.readline()} sem linha")
    print('#' * 190)
    arquivo.close()
    
def ler_arquivo_readline_while():
    arquivo = open(f"{caminho}/lorem.txt", 'r')
    print("##### Readline While #####" )
    while len(linha := arquivo.readline()):
        print(linha)
    print('#' * 190)
    arquivo.close()

def ler_arquivo_readlines():
    arquivo = open(f"{caminho}/lorem.txt", 'r')
    print("##### Readlines #####" )
    print(arquivo.readlines())
    print('#' * 190)
    arquivo.close()

if __name__ == "__main__":
    ler_arquivo_read()
    ler_arquivo_readline()
    ler_arquivo_readline_while()
    ler_arquivo_readlines()