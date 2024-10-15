# Databricks notebook source
# MAGIC %md
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 0px;  padding-bottom: 0px;">
# MAGIC   <img src="https://yt3.googleusercontent.com/RW6rRKJqeKTCIFFqZ6e1cdPCQ5dCsnQcXr2ejTcUduHMASnF4Q7UYPA_aCvgLquL93bbEAk2cQ=w1060-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj" alt='AD Logo' style="width: 1500px" >
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # Introdução ao Pandas
# MAGIC
# MAGIC Pandas é uma biblioteca Python popular entre cientistas de dados, com estruturas de dados e ferramentas de análise de dados de alto desempenho e fáceis de usar.
# MAGIC
# MAGIC ### Nessa aula vamos ver sobre:
# MAGIC   * O que pandas é e por que é tão popular
# MAGIC   * Criar e manipular pandas DataFrame e Series
# MAGIC   * Executar operações em pandas objcets
# MAGIC
# MAGIC Primeiro, vamos importar pandas com o alias pd para que possamos consultar a biblioteca sem precisar digitar pandas todas as vezes. pandas está pré-instalado no Databricks.
# MAGIC
# MAGIC Referências:
# MAGIC * <a href="https://pandas.pydata.org/docs/user_guide/index.html" target="_blank">Documentação Pandas</a>
# MAGIC * <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html" target="_blank">Pandas DataFrame</a> 

# COMMAND ----------

# MAGIC %pip install pandas

# COMMAND ----------

import pandas as pd

# COMMAND ----------

# MAGIC %md
# MAGIC ### Por que pandas?
# MAGIC * Cada vez mais, os dados lideram a tomada de decisões.
# MAGIC * Excel é ótimo, mas e se...
# MAGIC   * Você deseja automatizar sua análise para que ela seja executada novamente com novos dados todos os dias?
# MAGIC   * Você deseja construir uma base de código para compartilhar com seus colegas?
# MAGIC   * Você quer análises mais robustas para alimentar uma decisão de negócios?
# MAGIC   * Você quer fazer aprendizado de máquina?
# MAGIC * pandas é uma das principais bibliotecas usadas por analistas e cientistas de dados em Python.

# COMMAND ----------

# MAGIC %md
# MAGIC ## DataFrame
# MAGIC Vimos como diferentes tipos de dados fornecem diferentes tipos de dados e funcionalidades.
# MAGIC
# MAGIC **`pandas` é uma biblioteca que fornece tipos de dados e funções que nos permitem fazer análises de dados programáticas rigorosas.**
# MAGIC
# MAGIC * O tipo de dados principal pandasé chamado de **`DataFrame`**.
# MAGIC Um **`DataFrame`** é uma tabela bidimensional de linhas e colunas nomeadas, semelhante a uma tabela SQL.
# MAGIC
# MAGIC * A **`DataFrame`** classe possui um **`data`** atributo para os dados da tabela que devemos definir quando instanciamos um **`DataFrame`** objeto.
# MAGIC
# MAGIC Digamos que queremos transformar a seguinte tabela em uma **`DataFrame`**:
# MAGIC
# MAGIC | Nome    | Idade | Cargo|
# MAGIC | ----------- | ----------- | ----------- | 
# MAGIC | João   | 30    | Recursos Humanos |
# MAGIC | Ana    | 30       | Desenvolvedor |
# MAGIC | Marcos     | 40       | Líder Técnico |
# MAGIC
# MAGIC
# MAGIC Uma maneira de fazer isso é criar uma lista de listas onde cada lista da lista representa uma linha de dados:

# COMMAND ----------

data = [["João", 30, "Recursos Humanos"], ["Ana", 30, "Desenvolvedor"], ["Marcos", 40, "Líder Técnico"]]

df = pd.DataFrame(data=data)
df

# COMMAND ----------

# MAGIC %md
# MAGIC Lembre-se de que criamos um objeto de uma classe personalizada como  **`object = Class()`**. Como **`DataFrame`** está definido em **`pandas`** usamos **`pd.DataFrame()`**.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Adicionando nomes de colunas
# MAGIC Os nomes das colunas 0, 1, 2 acima são valores padrão. Para especificar os nomes das colunas que queremos, **`DataFrame`** tem outro atributo:columns

# COMMAND ----------

cols = ["Nome", "Idade", "Cargo"]
df = pd.DataFrame(data=data, columns=cols)
df

# COMMAND ----------

# MAGIC %md
# MAGIC ## Series
# MAGIC O outro tipo de dados principal fornecido é o **`Series`** .
# MAGIC
# MAGIC A **`Series`** é apenas uma coluna do arquivo **`DataFrame`**.
# MAGIC
# MAGIC Podemos selecionar a **`Series`** de duas maneiras:
# MAGIC
# MAGIC 1. **`df["column_name"]`**
# MAGIC 2. **`df.column_name`**
# MAGIC
# MAGIC Vamos selecionar a coluna Idade abaixo:

# COMMAND ----------

df['Idade']

# COMMAND ----------

df.Idade

# COMMAND ----------

# MAGIC %md
# MAGIC É preferível usar **`df["column_name"]`** para acessar uma coluna. A **`df.column_name`** notação não funciona bem quando há espaços nos nomes das colunas.

# COMMAND ----------

# MAGIC %md
# MAGIC ## dtypes
# MAGIC Se você olhar para o **`Series`** objeto acima, poderá ver **`dtype: int64`**.
# MAGIC
# MAGIC Em pandas, **`dtypes`** é uma abreviatura de tipos de dados, refere-se ao tipo dos valores na coluna.
# MAGIC
# MAGIC A seguir, veremos alguns dos métodos e funcionalidades que **`DataFrame`** ele **`Series`** fornece, mas assim como os tipos de objetos determinam o que você pode fazer com eles, o **`dtype`** de uma coluna determina quais funcionalidades podemos fazer com ela.
# MAGIC
# MAGIC Por exemplo, podemos calcular a média de uma coluna numérica, mas não de uma coluna não numérica.
# MAGIC
# MAGIC As **`dtypes`** colunas of são específicas do pandas, mas as mais comuns são muito semelhantes aos built-in do Python:
# MAGIC
# MAGIC 1. **`object`** é apenas texto, que é semelhante a strings
# MAGIC 2. **`int64`** são inteiros
# MAGIC 3. **`float64`** são flutuantes
# MAGIC 4. **`bool`** são booleanos
# MAGIC
# MAGIC Podemos visualizar o **`dtypes`** valor de cada coluna **`DataFrame`** acessando seu **`dtypes`** atributo:

# COMMAND ----------

df.info()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Series Operations
# MAGIC
# MAGIC Podemos usar operações em **`Series`** um determinado dtype que são semelhantes às operações que podemos fazer com a contraparte integrada semelhante do dtype.
# MAGIC
# MAGIC Essas operações atuam elemento a elemento.
# MAGIC
# MAGIC Por exemplo, podemos adicionar **`Series`** **`int64`** de forma semelhante à forma como podemos adicionar valores inteiros em Python.

# COMMAND ----------

df["Idade"] + df["Idade"]

# COMMAND ----------

# MAGIC %md
# MAGIC Podemos usar todas as operações básicas com números inteiros aqui:

# COMMAND ----------

df["Idade"] * 3 - 1 

# COMMAND ----------

# MAGIC %md
# MAGIC ### Selecionando um valor de um Series
# MAGIC
# MAGIC Às vezes, desejaremos extrair um valor em a **`Series`**. Podemos indexar de forma **`Series`** semelhante à forma como indexamos em uma lista para extrair valores:

# COMMAND ----------

df["Nome"][1]

# COMMAND ----------

# MAGIC %md
# MAGIC ## Selecionando um subconjunto de colunas
# MAGIC
# MAGIC Vimos como selecionar uma determinada coluna como um arquivo **`Series`**.
# MAGIC
# MAGIC Também podemos selecionar um subconjunto de colunas como um arquivo **`DataFrame`**.
# MAGIC
# MAGIC Podemos selecionar um subconjunto de colunas como este:
# MAGIC
# MAGIC **`df[[col_1, col_2, col_3, ...]]`**
# MAGIC
# MAGIC Vamos selecionar apenas as colunas Nome e Idade:

# COMMAND ----------

df[["Nome", "Idade"]]

# COMMAND ----------

# MAGIC %md
# MAGIC ## Limpeza dos Dados
# MAGIC
# MAGIC Por vezes recebemos um conjunto de dados com alguns dados incorretos e precisamos fazer alguns tratamentos iniciais para lidar com isso.
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Dados Duplicados
# MAGIC
# MAGIC Podemos usar o método **`drop_duplicates()`** para remover do nosso dataframe as linhas duplicadas

# COMMAND ----------

cols = ["Nome", "Idade", "Cargo"]
data = [["João", 30, "Recursos Humanos"], ["Ana", 30, "Desenvolvedor"], ["Marcos", 40, "Líder Técnico"], ["Ana", 30, "Desenvolvedor"], ["Marcos", 40, "Líder Técnico"]]

df = pd.DataFrame(data=data, columns=cols)
df

# COMMAND ----------

df_clean = df.drop_duplicates()
df_clean

# COMMAND ----------

# MAGIC %md
# MAGIC ### Colunas Indesejadas
# MAGIC
# MAGIC Também é comum recebermos colunas que não são relevantes para o nosso projeto.
# MAGIC
# MAGIC Podemos usar o método **`drop()`** para remover do nosso dataframe essas colunas.

# COMMAND ----------

cols = ["Nome", "Idade", "Cargo", "Endereco", "Telefone"]

data = [["João", 30, "Recursos Humanos","Rua Leblon, São Paulo, SP", "11974189635"], ["Ana", 30, "Desenvolvedor","Rua Itaquera, Rio de Janeiro, RJ", "21986359741"], ["Marcos", 40, "Líder Técnico","Rua Leblon, Goias, GO", "62918967435"], ["Ana", 30, "Desenvolvedor"]]

df = pd.DataFrame(data=data, columns=cols)
df

# COMMAND ----------

df_drop = df.drop(columns="Endereco")
df_drop

# COMMAND ----------

# MAGIC %md
# MAGIC &copy; 2024 Aprender Dados. Todos os direitos reservados.<br/>
# MAGIC <a href="https://wa.me/31616144014">Contato</a>