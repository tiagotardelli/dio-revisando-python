## Gerenciamento de Pacotes, Convenções e Boas Práticas Python

### Ambiente Virtual
Ambientes virtuais, como os criados por venvs, nos permitem manter as dependêcias de diferentes projetos. Isso é
importante para evitar conflitos entre versões de pacotes.
```python
python3 -m venv myenv
source myenv/bin/active

# fecha o ambiente virtual
deactivate
```

### O que são pacotes em Python?
São módulos que podem ser instalados e utilizados em seus programas Python. Eles permitem que você utilize código que
foi escrito por outras pessoas, economizando tempo e esforço.

#### O pepel do pip
Pip é o gerenciador de pacotes do Python. Ele nos permite instalar, atualizar e remover pacotes facilmente. Ele se
comunica com o PyPI (Python Package Index), que é onde a maioria dos pacotes Python são armazenados.

[Link do PyPI](https://pypi.org)
```python
pip install numpy
pip uninstall numpy
pip list
```
```python
# instalar um pacote
pip install nome_do_pacote

# desinstalar um pacote 
pip uninstall nome_do_pacote

# listar pacotes instalados
pip list

# atualizar um pacote
pip install --upgrade nome_do_pacote

```

#### pipenv
É uma ferramnenta de gerenciamento de pacotes que combina a gestão de dependências com a criação de ambiente virtual 
para seus projetos e adiciona/remove pacotes automaticamente do arquivo Pipfile conforme você instala e desinstala 
pacotes.
```python
# instalação é grobal para cada versão do python
pip install pipenv

# instala o pacote e já inicia um ambiente virtual e cria o arquivo Pipfile
pipenv install numpy
pipenv uninstall numpy

# gera o arquivo de lock
pipenv lock

# traz o que está instalado e as dependências da instalação
pipenv graph

# limpa os pacotes de dependência
pipenv clean
```

#### poetry
É uma ferramenta de gerenciamento de dependências para Python que permite declarar as bibliotecas de que
seu projeto depende e gerencia (instala/atualiza/remove) essas bibliotecas para você. Ela também suporta
o empacotamento e a publicação de projetos no PyPI.

```python
pip install poetry

# para novos projetos
poetry new myproject
cd myproject

# na pasta do projeto já criado
poetry init

# instalar as dependências e cria o ambiente virtual
poetry install

poetry add numpy
poetry remove numpy

# traz os pacotes instalados
poetry show

# traz os pacotes com as dependências
poetry show -t
```

### Boas Práticas

#### PEP
Python tem uma série de convenções e melhores práticas codificadas em PEPs (Popostas de Melhoria do Python).
A mais conhecida destas é provavelmente a PEP 8, que cobre o estilo de codificação.

#### PEP 8
É o guia de estilo para codificação em Python. Ele inclui convenções sobre nomes de variáveis, uso de espaços
em branco, comprimento da linha e muitas outras coisas que ajudam a manter o código Python consistente e legível.

[Link PEP 8](https://peps.python.org/pep-0008/)

Principais recomendações:
Algumas das principais recomendações da PEP 8 incluem usar 4 espaços para a identação, limitar as linhas a 79 caracteres
, usar nomes de variáveis em snake_case para funções e variáveis, e CamelCase para classes.

```python
def somar(argumento_1, argumento_2):
    # Essa é uma função de exemplo seguindo a PEP 8
    pass

class ContaBancaria:
    # Essa é uma classe de exemplo seguindo a PEP 8
    pass
```

#### Uso de ferramentas de checagem de estilo (linter)
Para nos auxiliar a seguir as recomendações da PEP 8, podemos usar ferramentas de checagem de estilo como flake8.
Essas ferramentas verificam nosso código e nos informam onde estamos desviando do guia de estilo.

```python
pip install flake8

flake8 meu_script.py
flake8 --max--length=120 meu_script.py
```

### Formatação automática de código (formaters)
Black é uma ferramenta de formatação de código Python que segue a filosofia "formato único". Balck reformata todo
o seu arquivo em um estilo consistente, simplificando a tarefa de manter o código em conformidade com a PEP 8.

```python
pip install black

black meu_script.py
```

#### Organização de imports com isort
Isort é uma ferramenta Python para classificar importaçÕes alfabeticamente e separá-las automaticamente em seções.
Ele proporciona uma maneira rápida e fácil de ordenar e categorizar suas importações.

```
pip install isort

isort meu_script.py
```

#### Utilizando as ferramentas no VSCode
* Black Formatter -> extensão da Microsoft
* isort -> extensão da Microsoft