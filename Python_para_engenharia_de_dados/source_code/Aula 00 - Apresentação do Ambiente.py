# Databricks notebook source
# MAGIC %md
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 0px;  padding-bottom: 0px;">
# MAGIC   <img src="https://yt3.googleusercontent.com/RW6rRKJqeKTCIFFqZ6e1cdPCQ5dCsnQcXr2ejTcUduHMASnF4Q7UYPA_aCvgLquL93bbEAk2cQ=w1060-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj" alt='AD Logo' style="width: 1500px" >
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # Conhecendo o Databricks Community
# MAGIC
# MAGIC   * Criando um cluster
# MAGIC   * Desenvolvendo com notebooks
# MAGIC   * Export notebooks
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Referências:
# MAGIC * <a href="https://docs.databricks.com/" target="_blank">Documentação Databricks</a>
# MAGIC * <a href="https://www.databricks.com/try-databricks#account" target="_blank">Databricks Comnmunity</a>  

# COMMAND ----------

# MAGIC %md
# MAGIC ## Criando um cluster
# MAGIC
# MAGIC Antes de iniciar as nossas aulas, nós precisamos criar e iniciar um cluster (cluster é um conjunto de recursos computacionais que vamos usar para executar os nossos códigos)
# MAGIC
# MAGIC ##### Passo 1:
# MAGIC No menu lateral esquerdo, acesse a opção **Compute (ou Computação)**
# MAGIC <img src="http://files.training.databricks.com/images/ITP/ClickCompute.png" style="width:800px;height:400px;">
# MAGIC
# MAGIC
# MAGIC
# MAGIC
# MAGIC ##### Passo 2:
# MAGIC Clique em **Create Cluster (ou Criar Compute)**
# MAGIC <img src="http://files.training.databricks.com/images/ITP/step2.png" style="width:1100px;height:300px;">
# MAGIC
# MAGIC
# MAGIC
# MAGIC ##### Passo 3:
# MAGIC Aqui você vai conseguir nomear o seu cluster e escolher a versão de execução. 
# MAGIC
# MAGIC Nessa trilha estaremos usando a versão **14.3 LTS**
# MAGIC
# MAGIC
# MAGIC ##### Passo 4:
# MAGIC
# MAGIC Para concluir, clique em **Create Cluster**
# MAGIC
# MAGIC
# MAGIC ##### Step 5:
# MAGIC
# MAGIC Agora você pode vincular o seu cluster no notebook e começar a aula!!
# MAGIC <img src="http://files.training.databricks.com/images/ITP/step5.png" style="width:1000px;height:400px">
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md-sandbox <i18n value="fee29257-b1d9-49e6-a74f-53e1afc5bf29"/>
# MAGIC
# MAGIC
# MAGIC ## Executando o código
# MAGIC
# MAGIC * Cada notebook possui uma linguagem padrão, no nosso curso estaremos utilizando o **Python**
# MAGIC * Execute a célula a seguir usando uma das seguintes opções:
# MAGIC   * **CTRL+ENTER** ou **CMD+RETURN**
# MAGIC   * **SHIFT+ENTER** ou **SHIFT+RETURN** para executar a celula e mover o cursor para a próxima célula
# MAGIC   * Use **Run Cell**, **Run All Above** ou **Run All Below** assim como mostrado abaixo: <br/><img style="box-shadow: 5px 5px 5px 0px rgba(0,0,0,0.25); border: 1px solid rgba(0,0,0,0.25);" src="https://files.training.databricks.com/images/notebook-cell-run-cmd.png"/>

# COMMAND ----------

print("Bem vindo ao nosso curso Python para Engenheiros da Aprender Dados!!!")

# COMMAND ----------

# MAGIC %md <i18n value="58b85c79-1640-47a8-90c2-325a2bd2e265"/>
# MAGIC
# MAGIC
# MAGIC ## Saiba Mais
# MAGIC
# MAGIC Para saber mais sobre o Databricks e como utilizar os notebooks, verifique os links abaixo:
# MAGIC
# MAGIC * <a href="https://docs.databricks.com/user-guide/index.html" target="_blank">User Guide</a>
# MAGIC * <a href="https://docs.databricks.com/user-guide/notebooks/index.html" target="_blank">User Guide / Notebooks</a>

# COMMAND ----------

# MAGIC %md
# MAGIC &copy; 2024 Aprender Dados. Todos os direitos reservados.<br/>
# MAGIC <a href="https://wa.me/31616144014">Contato</a>