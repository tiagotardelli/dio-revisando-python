import os
import shutil
from pathlib import Path 

ROOT_PATH = Path(__file__).resolve().parent

os.mkdir(ROOT_PATH / "novo-diretorio")

arquivo = open(ROOT_PATH / "novo.txt", 'w')
arquivo.close()

arquivo = open(ROOT_PATH / "novo2.txt", 'w')
arquivo.close()

os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterado.txt")

os.remove(ROOT_PATH / "alterado.txt")

shutil.move(ROOT_PATH / "novo2.txt", ROOT_PATH / "novo-diretorio" / "novo2.txt")

os.remove(ROOT_PATH  / "novo-diretorio" / "novo2.txt") 

os.rmdir(ROOT_PATH / "novo-diretorio") 