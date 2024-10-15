
# Ebook de Introdução à Programação com Python

Este ebook fornece uma introdução detalhada à programação com Python, com base nas aulas práticas que abordam desde conceitos básicos de variáveis e tipos de dados até o uso de bibliotecas como Pandas para análise de dados e manipulação de bancos de dados. Cada seção inclui exemplos práticos e explicações detalhadas.

---

## Aula 01 - Variáveis e Tipos de Dados

### O que são variáveis?
Variáveis em Python são usadas para armazenar dados que podem ser reutilizados em diferentes partes do código. Uma variável é criada ao atribuir um valor a ela.

#### Exemplo:
```python
nome = "João"
idade = 25
```

### Tipos de Dados
Em Python, temos os seguintes tipos de dados básicos:
- **int**: números inteiros (ex: 10, -5)
- **float**: números de ponto flutuante (ex: 3.14, -0.5)
- **str**: sequência de caracteres, ou strings (ex: "Olá", "Python")
- **bool**: valores booleanos (True, False)

#### Exemplo:
```python
altura = 1.75  # float
ativo = True   # bool
```

### Conversão de Tipos
Para converter entre diferentes tipos de dados, podemos usar funções como `int()`, `float()`, e `str()`.

#### Exemplo:
```python
num_str = "100"
num_int = int(num_str)
print(num_int + 50)  # Exibe: 150
```

---

## Aula 02 - Condicionais

### Estrutura `if`
Usamos a estrutura condicional `if` para executar blocos de código apenas se uma condição for verdadeira.

#### Exemplo:
```python
idade = 18
if idade >= 18:
    print("Maior de idade")
```

### Estrutura `else`
O bloco `else` é executado quando a condição `if` é falsa.

#### Exemplo:
```python
idade = 17
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```

### Estrutura `elif`
Para múltiplas condições, usamos `elif`:

#### Exemplo:
```python
nota = 85
if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
else:
    print("C")
```

---

## Aula 03 - Estruturas de Dados e Métodos

### Listas
Uma lista é uma coleção de itens mutáveis que podem ser modificados.

#### Exemplo:
```python
frutas = ["maçã", "banana", "laranja"]
print(frutas[0])  # Exibe: maçã
```

Métodos comuns em listas:
- `append()`: adiciona um item à lista.
- `remove()`: remove o primeiro item correspondente.

#### Exemplo:
```python
frutas.append("abacaxi")
print(frutas)  # Exibe: ['maçã', 'banana', 'laranja', 'abacaxi']
```

### Dicionários
Dicionários são coleções de pares chave-valor.

#### Exemplo:
```python
aluno = {"nome": "Ana", "idade": 20}
print(aluno["nome"])  # Exibe: Ana
```

---

## Aula 04 - Loops

### Loop `for`
Usamos loops para executar um bloco de código repetidamente.

#### Exemplo:
```python
for i in range(5):
    print(i)  # Exibe: 0, 1, 2, 3, 4
```

### Loop `while`
O loop `while` continua a execução enquanto a condição for verdadeira.

#### Exemplo:
```python
cont = 0
while cont < 5:
    print(cont)
    cont += 1
```

---

## Aula 05 - Funções

Funções são blocos de código que executam uma tarefa específica e podem ser reutilizados.

### Definindo uma Função
Para definir uma função, usamos a palavra-chave `def`.

#### Exemplo:
```python
def saudacao():
    print("Olá! Bem-vindo ao curso!")
```

### Funções com Parâmetros
Podemos passar informações para uma função usando parâmetros.

#### Exemplo:
```python
def somar(a, b):
    return a + b

resultado = somar(5, 3)
print(resultado)  # Exibe: 8
```

---

## Aula 06 - Exceções

### Lidando com Exceções
Usamos o bloco `try` para capturar exceções e evitar que o programa seja interrompido.

#### Exemplo:
```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Erro: divisão por zero")
```

### Exceções Comuns
- **ZeroDivisionError**: erro ao tentar dividir por zero.
- **TypeError**: tipo de dado inválido.

---

## Aula 07 - Introdução ao Pandas

O Pandas é uma biblioteca poderosa para manipulação e análise de dados em Python.

### Criando um DataFrame
Um `DataFrame` é uma tabela bidimensional usada para armazenar e manipular dados tabulares.

#### Exemplo:
```python
import pandas as pd

dados = {"Nome": ["Ana", "João"], "Idade": [28, 34]}
df = pd.DataFrame(dados)
print(df)
```

### Selecionando Dados
Podemos acessar colunas específicas de um `DataFrame` usando o nome da coluna.

#### Exemplo:
```python
print(df["Nome"])  # Exibe a coluna 'Nome'
```

---

## Aula 08 - Trabalhando com Bancos de Dados

Nesta aula, aprenderemos a conectar e manipular dados de bancos de dados usando Pandas e bibliotecas como `sqlalchemy`.

### Conectando a um Banco de Dados
Para se conectar a um banco de dados SQL, utilizamos o SQLAlchemy junto com o Pandas.

#### Exemplo:
```python
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///meu_banco.db')
df = pd.read_sql('SELECT * FROM minha_tabela', engine)
print(df)
```

### Salvando um DataFrame no Banco de Dados
Também podemos salvar um `DataFrame` de volta no banco de dados.

#### Exemplo:
```python
df.to_sql('minha_tabela', engine, if_exists='replace')
```

---

Este ebook cobre as principais funcionalidades do Python, desde conceitos básicos até o uso avançado de bibliotecas como Pandas para análise e manipulação de dados.
