from pathlib import Path 

import csv

ROOT_PATH = Path(__file__).resolve().parent

def criar_csv():
    try:
        with open(ROOT_PATH / "usuario.csv", 'w',  newline='', encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(["id", "nome"])
            escritor.writerow(["1", "Maria"])
            escritor.writerow(["2", "João"])
    except IOError as exc:
        print(f'Erro ao criar o arquivo: {exc}')

def ler_csv():
    try:
        with open(ROOT_PATH / "usuario.csv", 'r',newline= '', encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            for row in leitor:
                print(row)
    except IOError as exc:
        print(f'Erro ao criar o arquivo: {exc}')

def ler_csv_dif():
    try:
        with open(ROOT_PATH / "usuario.csv", newline= '') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row["id"], row["nome"])
    except IOError as exc:
        print(f'Erro ao criar o arquivo: {exc}')

if __name__ == "__main__":
    # criar_csv()
    ler_csv()
    ler_csv_dif()