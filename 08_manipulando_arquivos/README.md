## Por que precisamos manipular arquivos?
Os arquivos são essenciais para qualquer tipo de programação, pois fornecem um meio
de armazenar e recuperar dados.Através da manipulação de arquivos, podemos persistir
os dados além da vida útil de um programa específico.

## Conceito de arquivo em informática
Um arquivo é um container no computador onde as informações são armazenadas em formato
digital. Existem dois tipos de arquivos que podemos manipular em Python:
arquivos de texto e arquivos binários.

## Como manipular arquivos em Python?
Para manipular arquivos em Python, primeiro precisamos abri-los. Usamos a função 'open()'
para isso. Quando terminamos de trabalhar com o arquivo, usamos a função 'close()' para
liberar recursos.
```python
file = open("exemplo.txt", "r")
# .. fazemos algo com o arquivo
file.close()
```
## Modos de abertura de arquivo
Existem diferentes modos para abrir um arquivo, como somente leitura('r'), gravação ('w')
e anexar ('a'). O modo de abertura deve ser escolhido de acordo com a operação que iremos 
realizar no mesmo.
```python
# Para ler um arquivo
file = open("exemplo.txt", "r")

# Para escrever em um arquivo
file = open("exemplo.txt", "w")

# Para anexar conteúdo a um arquivo
file = open("exemplo.txt", "r")

```

## Lendo de um arquivo
Python fornece várias maneiras de ler um arquivo. Podemos usar 'read()', 'readline()' ou
'readlines()' dependendo de nossas necessidades

* read -> lê todo o documento
```python
# Ler todo o conteúdo de um arquivo
file = open("exemplo.txt", "r")
print(file.read())
file.close()
```
* readline -> lê uma linha por vez
* readlines -> retorna uma lista onde cadas elemento é uma linha do arquivo
```python
# Ler todo o conteúdo de um arquivo
file = open("exemplo.txt", "r")
print(file.readline())
print(file.readlines())
file.close()
```
## Escrevendo em um arquivo
Podemos usar 'write()' ou 'writlones()' para escrever em um arquivo. Lembre-se,
no entanto, de abrir o arquivo no modo correto.
```python
# Ler todo o conteúdo de um arquivo
file = open("exemplo.txt", "w")
file.write("Olá, mundo!")
file.close()
```

## Gerenciando arquivos e diretorios
Python também oferece funções para gerenciar arquivos e diretórios. Podemos
criar, renomear e excluir arquivos e diretórios usando o módulo 'os' e 'shutil'.
```python
import os
import shutil

# Criar um diretório
os.mkdir("exemplo")

# Renomear um arquivo
os.rename("old.txt", "new.txt")

# Remover um arquivo
os.remove("unwanted.txt")

# Mover um arquivo
shutil.move("source.txt", "destination.txt")
```

## Tratamento de exceções em manipulaçãp de arquivos
Tratar erros é uma parte importante da manipulação de arquivos. Python oferece uma
variedade de exceções que nos permitem lidar com erros comuns.
### Exceções mais comuns:
* FileNotFoundError: Lançada quando o arquivo está sendo aberto não pode ser 
encontrado no diretório especificado.
* PermissionError: Lançada quando ocorre uma tentativa de abrir um arquivo sem as
permissões adequadas para leitura ou gravação.
* IOError: Lançado quando ocorre um erro geral de E/S (entrada/saída) ao trabalhar
com o arquivo, como problemas de permissão, falta de espaço em disco, entre outros.
* UnicodeDecodeError: Lançada quando ocorre um erro ao tentar decodificar os dados
de um arquivo de texto usando uma codificação inadequada.
* UnicodeEncodeError: Lançado quando ocorre um erro ao tentar codificar dados em uma
determinada codificação ao gravar em um arquivo de texto.
* IsADirectoryError: Lançada quando é feita uma tentativa de abrir um diretório em
vez de um arquivo de texto.

```python
try:
    file = open('non_existent_file.txt', 'r')
except FileNotFoundError:
    print("Arquivo não encontrado.")
```

## Boas Práticas
Ao manipular arquivos em Python existem algumas boas práticas que podemos seguir.
### Bloco with
Use o gerenciamento de contexto (context manager) com a declaração 'with'/ O gerenciador
de contexto permite trabalhsar com arquivos de forma segura, garantindo que eles sejam 
fechados corretamente, mesmo em caso de exceções.
```python
with open('arquivo.txt')
```
### Verificar se o arquivo foi aberto com sucesso
É recomendado verificar se o arquivo foi aberto corretamente antes de executar operações
de leitura ou gravação nele.
```python
try:
    with open('arquivo.txt', 'r') as arquivo
except IOError:
    print('Não foi possível abrir o arquivo.')
```
### Use a codificação correta
Certifique-se de usar a codificação correta ao ler ou gravar arquivos de texto. O argumento
'encoding' da função 'open()' permite especificar a codificação.
```python
with open('arquivo.txt', 'r', encoding='utf-8') as arquivo
    # Operações de leitura com codificação UTF-8
with open('arquivo.txt', 'w', encoding='utf-8') as arquivo
    # Operações de escrita com codificação UTF-8
```

## Trabalhando com CSV
CSV é um formato de arquivo amplamente utilizado para armazenar dados tabulares. CSV é
a sigla comum para 'Comma Separated Values'.
### Lendo Arquivos CSV
Pyhton fornece um módulo chamado 'csv' para lidar facilmente com arquivos CSV.
```python
import csv

with open('exemplo.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```
### Escrevendo em arquivos CSV
Da mesma forma podemos utilizar o módulo 'csv' para escrever em arquivos CSV.
```python
import csv

with open('exemplo.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["nome", "idade"])
    writer.writerow(["Ana", 30]
    writer.writerow(["João", 25]
```

### Prátivas recomendadas
* Usar csv.reader e csv.writter para manipular arquivos CSV.
* Fazer o tratamento correto das exceções.
* Ao gravar arquivos csv definir o argumento newline='' no método 'open'.

[Documentação do módulo CSV](https://docs.python.org/3/library/csv.html)