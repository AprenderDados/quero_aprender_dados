
# Python Cheatsheet

## 1. Variáveis e Tipos de Dados

| Tipo de Dado | Descrição                 | Exemplo                      |
|--------------|---------------------------|------------------------------|
| `int`        | Números inteiros           | `idade = 25`                 |
| `float`      | Números de ponto flutuante | `altura = 1.75`              |
| `str`        | Sequência de caracteres    | `nome = "João"`              |
| `bool`       | Valores booleanos          | `ativo = True`               |

### Conversão de Tipos
```python
num_str = "100"
num_int = int(num_str)
print(float(num_int))  # Converte para float
```

---

## 2. Condicionais

| Operador | Descrição               |
|----------|-------------------------|
| `==`     | Igual a                 |
| `!=`     | Diferente de            |
| `>=`     | Maior ou igual a        |
| `<=`     | Menor ou igual a        |

### Estrutura `if`, `elif`, `else`
```python
idade = 18
if idade >= 18:
    print("Maior de idade")
elif idade >= 16:
    print("Pode votar")
else:
    print("Menor de idade")
```

---

## 3. Loops

| Palavra-chave | Descrição                        |
|---------------|----------------------------------|
| `for`         | Itera sobre uma sequência        |
| `while`       | Executa enquanto a condição é `True` |
| `break`       | Sai do loop                      |
| `continue`    | Pula para a próxima iteração     |

### Exemplo de `for` e `while`
```python
for i in range(5):
    print(i)  # Exibe 0, 1, 2, 3, 4

cont = 0
while cont < 5:
    print(cont)
    cont += 1
```

---

## 4. Funções

| Função               | Descrição                                             |
|----------------------|-------------------------------------------------------|
| `def`                | Define uma função                                     |
| `return`             | Retorna um valor de uma função                        |
| Parâmetros Padrão    | Define valores padrão para parâmetros                 |
| Funções com Vários Parâmetros | Aceita múltiplos parâmetros na função          |

### Exemplo de Função com Parâmetros
```python
def somar(a, b):
    return a + b

resultado = somar(5, 3)
print(resultado)  # Exibe: 8
```

---

## 5. Estruturas de Dados

| Estrutura   | Descrição                               | Exemplo                        |
|-------------|-----------------------------------------|--------------------------------|
| **Lista**   | Coleção mutável                         | `frutas = ["maçã", "banana"]`  |
| **Dicionário** | Pares chave-valor                    | `aluno = {"nome": "Ana"}`      |
| **Tupla**   | Coleção imutável                        | `cores = ("vermelho", "azul")` |
| **Conjunto**| Itens únicos e não ordenados            | `numeros = {1, 2, 3}`          |

### Operações com Listas
```python
frutas.append("abacaxi")
print(frutas[1])  # Exibe: banana
```

---

## 6. Exceções

| Exceção              | Descrição                        |
|----------------------|----------------------------------|
| `ZeroDivisionError`   | Erro ao dividir por zero         |
| `TypeError`           | Tipo de dado inválido            |
| `NameError`           | Variável não definida            |

### Exemplo de Exceções
```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Erro: divisão por zero")
```

---

## 7. Pandas

| Operação               | Descrição                                        |
|------------------------|--------------------------------------------------|
| `pd.DataFrame()`        | Cria um DataFrame                               |
| `df["coluna"]`          | Seleciona uma coluna                            |
| `df.describe()`         | Estatísticas básicas do DataFrame               |
| `df[df["coluna"] > 30]` | Filtra o DataFrame com base em uma condição     |

### Criando um DataFrame
```python
import pandas as pd
dados = {"Nome": ["Ana", "João"], "Idade": [28, 34]}
df = pd.DataFrame(dados)
print(df)
```

---

## 8. Conectando com Bancos de Dados

| Função SQLAlchemy      | Descrição                                           |
|------------------------|----------------------------------------------------|
| `create_engine()`       | Cria a conexão com o banco de dados                |
| `pd.read_sql()`         | Executa uma query SQL e retorna um DataFrame       |
| `df.to_sql()`           | Salva um DataFrame em uma tabela do banco de dados |

### Conexão com Banco de Dados
```python
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///meu_banco.db')
df = pd.read_sql('SELECT * FROM minha_tabela', engine)
```

---

## 9. Dicas Gerais

| Operação                  | Descrição                                          |
|---------------------------|----------------------------------------------------|
| Fatiamento de listas       | Seleciona um intervalo de elementos                |
| List comprehensions        | Cria listas usando uma expressão compacta          |
| `zip()`                    | Combina duas listas                                |

### Exemplo de Fatiamento e List Comprehension
```python
lista = [1, 2, 3, 4, 5]
print(lista[1:4])  # Exibe: [2, 3, 4]

quadrados = [x**2 for x in range(5)]
print(quadrados)  # Exibe: [0, 1, 4, 9, 16]
```

---

Essa versão da cheatsheet inclui tabelas para operadores, estruturas e funções, facilitando a leitura e impressão em folha A4.
