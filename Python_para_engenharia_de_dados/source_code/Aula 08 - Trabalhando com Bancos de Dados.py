# Databricks notebook source
# MAGIC %md
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 0px;  padding-bottom: 0px;">
# MAGIC   <img src="https://yt3.googleusercontent.com/RW6rRKJqeKTCIFFqZ6e1cdPCQ5dCsnQcXr2ejTcUduHMASnF4Q7UYPA_aCvgLquL93bbEAk2cQ=w1060-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj" alt='AD Logo' style="width: 1500px" >
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC # Trabalhando com Bancos de Dados
# MAGIC
# MAGIC ### Nessa aula vamos ver sobre:
# MAGIC * Conexão com banco de dados;
# MAGIC * Manipulações de dados;
# MAGIC * Análises Exploratórias de dados.
# MAGIC
# MAGIC Tudo isso usando um banco de dados **real** disponibilizado **exclusivamente** para os alunos da **Aprender Dados**
# MAGIC
# MAGIC Referências
# MAGIC
# MAGIC * <a href="https://spark.apache.org/docs/latest/sql-data-sources-jdbc.html" target="_blank">Spark - JDBC Data Source</a>
# MAGIC * <a href="https://dataedo.com/samples/html/Data_warehouse/doc/AdventureWorksDW_4/modules/Dimensions_97/module.html" target="_blank">Documentação AdventureWorks</a>

# COMMAND ----------

# MAGIC %md
# MAGIC ## AdventureWorks DW 2022
# MAGIC
# MAGIC - O AdventureWorks é um exemplo de banco de dados de data warehouse fornecido pela Microsoft, geralmente utilizado para inteligência de negócios, análise de dados e relatórios.
# MAGIC
# MAGIC <a href="https://alunos.aprenderdados.com/114693-lakehouse-na-azure-projeto-adventure-works" target="_blank">Lakehouse na Azure | Projeto Adventure Works</a>

# COMMAND ----------

# MAGIC %md
# MAGIC ### Import a Biblioteca Pandas

# COMMAND ----------

import pandas as pd

# COMMAND ----------

# MAGIC %md
# MAGIC ### **Conectando ao Banco de Dados:**
# MAGIC
# MAGIC Aqui estamos usando o pyspark como um atalho para conectar ao Banco de dados

# COMMAND ----------

# Configurações da conexão
jdbc_hostname = "sqldb-study-lakehouse-server.database.windows.net"
jdbc_port = 1433
database_name = "AdventureWorksDW2022"
jdbc_url = f"jdbc:sqlserver://{jdbc_hostname}:{jdbc_port};database={database_name}"
username = 'APRENDER_DADOS_READ' 
password = 'SW4N0FW!D0Xd4W&Rt7'  

# Configurações de autenticação
connection_properties = {
    "user": username,
    "password": password,
    "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver"
}

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Carregando Dados em DataFrames do Pandas

# COMMAND ----------

# Leitura da tabela DimCustomer com o spark

df_customers = (spark.read
    .format("jdbc")
    .option("url", jdbc_url)
    .option("dbtable", "DimCustomer")
    .option("user", username)
    .option("password", password)
    .load())


# COMMAND ----------

# Use .toPandas() para converter o dataframe spark em pandas dataframe

df_customers = df_customers.toPandas() 

# COMMAND ----------

df_customers.display()

# COMMAND ----------

query = "SELECT * FROM INFORMATION_SCHEMA.TABLES"


df = (spark.read
    .format("jdbc")
    .option("url", jdbc_url)
    .option("query", query)
    .option("user", username)
    .option("password", password)
    .load())

df = df.toPandas()

# COMMAND ----------

type(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## **Visualização dos Dados:**
# MAGIC - Utilizar `.head()`, `.info()` e `.describe()` para explorar a estrutura e o resumo dos dados.
# MAGIC

# COMMAND ----------

df_customers.head(10)

# COMMAND ----------

df_customers.info()

# COMMAND ----------

df_customers.describe()

# COMMAND ----------

# MAGIC %md
# MAGIC ## **Limpeza e Preparação de Dados**
# MAGIC
# MAGIC ### **Tratamento de Dados Ausentes:**
# MAGIC

# COMMAND ----------

df_customers.isnull().sum()

# COMMAND ----------

df_customers.fillna('Desconhecido', inplace=True)

# COMMAND ----------

df_customers['Suffix']

# COMMAND ----------

# MAGIC %md
# MAGIC ### **Conversão de Tipos de Dados**
# MAGIC
# MAGIC Quando recebemos um conjunto de dados é comum lidarmos com a leitura padrão de algumas colunas e posteriormente precisamos ajustar o tipo de dado da coluna para o correto.
# MAGIC Com pandas conseguimos alterar o tipo do dado da coluna conforme a nossa necessidade.
# MAGIC
# MAGIC * `to_datetime`: Converte para datetime.
# MAGIC * `to_timedelta`: Converte para timedelta.
# MAGIC * `to_numeric`: Converte para tipo numerico.
# MAGIC * `.astype(dtype)`: Converte o tipo de dado conforme argumento `dtype`. Exemplo: `df.astype('int32')`

# COMMAND ----------

df_customers['DateFirstPurchase'] = pd.to_datetime(df_customers['DateFirstPurchase'])

# COMMAND ----------

df_customers.info()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Selecionando apenas as colunas desejadas

# COMMAND ----------

df_select = df_customers[['CustomerKey','EmailAddress', 'LastName','DateFirstPurchase']]
df_select.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### **Mesclando DataFrames**
# MAGIC
# MAGIC Para mesclar diferentes dataframes podemos usar o `merge`.
# MAGIC O resultado disso será um movo dataframe com a união entre os conjuntos de dados

# COMMAND ----------

query = "SELECT * FROM FactInternetSales"

df_sales = (spark.read
    .format("jdbc")
    .option("url", jdbc_url)
    .option("query", query)
    .option("user", username)
    .option("password", password)
    .load())

df_sales = df_sales.toPandas()

# COMMAND ----------

query = "SELECT * FROM DimProduct"

df_products = (spark.read
    .format("jdbc")
    .option("url", jdbc_url)
    .option("query", query)
    .option("user", username)
    .option("password", password)
    .load())

df_products = df_products.toPandas()

# COMMAND ----------

df_merged = df_sales.merge(df_customers, on='CustomerKey').merge(df_products, on='ProductKey')
print(df_merged.head())

# COMMAND ----------

# MAGIC %md
# MAGIC ### **Estatísticas Básicas:**

# COMMAND ----------

total_sales = df_sales['SalesAmount'].sum()
print(f'Vendas Totais: {total_sales}')

# COMMAND ----------

avg_sales = df_sales['SalesAmount'].mean()
print(f'Média de Vendas Totais: {avg_sales}')

# COMMAND ----------

# MAGIC %md
# MAGIC ### **Visualização de Dados:**
# MAGIC
# MAGIC Podemos usar juntamente com o pandas algumas bibliotecas para visualização de dados, uma delas é o Matplotlib.
# MAGIC
# MAGIC Matplotlib é uma biblioteca usada para criar visualizações estáticas, animadas e interativas em Python.
# MAGIC
# MAGIC <a href="https://matplotlib.org/" target="_blank">Matplotlib: Visualization with Python</a>
# MAGIC

# COMMAND ----------

df_sales.info()

# COMMAND ----------

df_sales['SalesAmount'] = df_sales['SalesAmount'].astype(float)

# COMMAND ----------

import matplotlib.pyplot as plt

df_sales.groupby('OrderDate')['SalesAmount'].sum().plot()
plt.title('Vendas Totais ao Longo do Tempo')
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ### **Agrupamento e Agregação de Dados:**

# COMMAND ----------

sales_by_product = df_merged.groupby('ProductKey')['SalesAmount'].sum().sort_values(ascending=False)
sales_by_product.head()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Colocando em Prática
# MAGIC
# MAGIC ### Exercício 1: Análise de Vendas por Produto
# MAGIC **Objetivo:** Identificar os 5 produtos mais vendidos em termos de quantidade.

# COMMAND ----------

# Calcular as quantidades vendidas por produto

vendas_produto = df_sales.merge(df_products, on="ProductKey")
vendas_por_produto = vendas_produto.groupby('EnglishProductName')['OrderQuantity'].sum().reset_index()

vendas_por_produto.display()

# COMMAND ----------

# Ordenar e pegar os 5 produtos mais vendidos
top_5 = vendas_por_produto.sort_values(by="OrderQuantity", ascending=False).head(5)

top_5.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Exercício 2: Análise de Produtos por Custo
# MAGIC **Objetivo:** Listar todos os produtos junto com seu respectivo Custo.

# COMMAND ----------

produtos_custo = df_products[['ProductKey','EnglishProductName', 'StandardCost']]
produtos_custo.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Exercício 3: Análise de Vendas por Território de Vendas
# MAGIC **Objetivo:** Calcular o total de vendas e a quantidade de pedidos para cada território de vendas.

# COMMAND ----------

# Carregar as tabelas DimSalesTerritory e FactInternetSales

query = "SELECT * FROM DimSalesTerritory"

df_sales_territory = (spark.read
    .format("jdbc")
    .option("url", jdbc_url)
    .option("query", query)
    .option("user", username)
    .option("password", password)
    .load())

df_sales_territory = df_sales_territory.toPandas()

# COMMAND ----------

# Juntar as tabelas de vendas e territórios

vendas_territorios = df_sales.merge(df_sales_territory, on='SalesTerritoryKey')

# COMMAND ----------

# Calcular total de vendas e quantidade de pedidos por território


vendas_por_territorio = vendas_territorios.groupby('SalesTerritoryCountry').agg({"SalesAmount":"sum", "OrderQuantity":"sum"}).reset_index()

vendas_por_territorio.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### **Exercício 4:**
# MAGIC - Encontrar os 10 principais clientes por valor total de vendas.

# COMMAND ----------

top_customers = df_sales.merge(df_customers, on='CustomerKey')

top10 = top_customers.groupby('LastName')['SalesAmount'].sum().reset_index()
top10 = top10.sort_values(by='SalesAmount', ascending=False).head(10)
top10

# COMMAND ----------

# MAGIC %md
# MAGIC ### Exercício 5: Análise Temporal de Vendas
# MAGIC **Objetivo:** Analisar a tendência de vendas ao longo do tempo (ano e mês) para identificar padrões sazonais.

# COMMAND ----------

# Converter a coluna de data para o tipo datetime
df_sales['OrderDate'] = pd.to_datetime(df_sales['OrderDate'])

# COMMAND ----------

# Criar colunas de ano e mês
df_sales['Ano'] = df_sales['OrderDate'].dt.year

df_sales['Mes'] = df_sales['OrderDate'].dt.month

# COMMAND ----------

# Calcular vendas totais por ano e mês
vendas_totais = df_sales.groupby(['Ano','Mes']).agg({'SalesAmount':'sum'}).reset_index()

vendas_totais.display()

# COMMAND ----------

# MAGIC %md
# MAGIC &copy; 2024 Aprender Dados. Todos os direitos reservados.<br/>
# MAGIC <a href="https://wa.me/31616144014">Contato</a>