# Databricks notebook source
# MAGIC %md
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 0px;  padding-bottom: 0px;">
# MAGIC   <img src="https://yt3.googleusercontent.com/RW6rRKJqeKTCIFFqZ6e1cdPCQ5dCsnQcXr2ejTcUduHMASnF4Q7UYPA_aCvgLquL93bbEAk2cQ=w1060-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj" alt='AD Logo' style="width: 1500px" >
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC # Criando seu próprio Ambiente
# MAGIC
# MAGIC ### Nessa aula vamos ver sobre:
# MAGIC * Como criar seu banco de dados no Databricks
# MAGIC
# MAGIC Referências
# MAGIC
# MAGIC * <a href="https://spark.apache.org/docs/latest/sql-data-sources-jdbc.html" target="_blank">Spark - JDBC Data Source</a>
# MAGIC * <a href="https://dataedo.com/samples/html/Data_warehouse/doc/AdventureWorksDW_4/modules/Dimensions_97/module.html" target="_blank">Documentação AdventureWorks</a>
# MAGIC * <a href="https://spark.apache.org/docs/latest/sql-data-sources-load-save-functions.html" target="_blank">Pyspark - Load/Save Functions </a>

# COMMAND ----------

# MAGIC %md
# MAGIC ## Clonando o Adventure Works

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

df_customers = (spark.read
    .format("jdbc")
    .option("url", jdbc_url)
    .option("dbtable", "DimCustomer")
    .option("user", username)
    .option("password", password)
    .load())


# COMMAND ----------

(df_customers.write.format("delta")
 .mode("overwrite")
 .option("mergeSchema", "true")
 .saveAsTable("DIM_COSTUMER")
)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM default.dim_costumer

# COMMAND ----------

# MAGIC %md
# MAGIC ## Criando Tabelas via Arquivo
# MAGIC
# MAGIC   1. Navegue até o seu espaço de trabalho do Databricks e clique no ícone Configurações(Settings) no canto superior direito.
# MAGIC
# MAGIC   2. Vá até a seção **Avançado** e procure por **DBFS**.
# MAGIC
# MAGIC   3. Marque a caixa ao lado de "**Habilitar navegador de arquivos DBFS**". Atualize a página para que a alteração entre em vigor.
# MAGIC
# MAGIC   4. Volte ao Workspace e localize a aba "**DBFS**" na seção **Catálogo**.
# MAGIC
# MAGIC   5. Clique em "**Create Table**" para abrir a área de **Upload File**. Aqui podemos enviar um arquivo local (um csv, por exemplo) para ser usado na criação da nossa tabela

# COMMAND ----------

# MAGIC %md
# MAGIC &copy; 2024 Aprender Dados. Todos os direitos reservados.<br/>
# MAGIC <a href="https://wa.me/31616144014">Contato</a>