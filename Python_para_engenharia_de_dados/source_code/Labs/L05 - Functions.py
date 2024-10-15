# Databricks notebook source
# MAGIC %md
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 0px;  padding-bottom: 0px;">
# MAGIC   <img src="https://yt3.googleusercontent.com/RW6rRKJqeKTCIFFqZ6e1cdPCQ5dCsnQcXr2ejTcUduHMASnF4Q7UYPA_aCvgLquL93bbEAk2cQ=w1060-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj" alt='AD Logo' style="width: 1500px" >
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # Lab 05 - Functions
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Um operador inteiro que é muito útil e que ainda não vimos é o módulo, que usa o símbolo %. O módulo retorna o restante da divisão de dois inteiros.
# MAGIC
# MAGIC Por exemplo, 12 % 7 é 5, porque 12 dividido por 7 é 1 com o resto 5.
# MAGIC
# MAGIC Usando o módulo, escreva uma função chamada **`par_impar(num)`** que aceita um número inteiro **num** e retorna **"par"** se for par, ou **ímpar** caso contrário. 
# MAGIC
# MAGIC Lembre-se, todos os números pares terão módulo 0 porque são divisíveis por 2.
# MAGIC
# MAGIC
# MAGIC **Dica:** Certifique-se de usar **return** em vez de **print** na função, para que ela passe nos casos de teste abaixo.

# COMMAND ----------

12 % 7

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Agora que você construiu as bases básicas para identificar números pares e ímpares, você está pronto para estender essa ideia e enfrentar uma das perguntas mais comuns em entrevistas de programação: **`Fizz Buzz`**.
# MAGIC
# MAGIC Escreva uma função chamada **`fizz_buzz`** que receba um número inteiro e realize o seguinte:
# MAGIC
# MAGIC * Se a entrada não for um número inteiro (lembre-se de que podemos passar o tipo errado, mesmo quando não deveríamos), retorne **`"Wrong type"`** (Tipo errado).
# MAGIC * Para uma entrada de número inteiro, se for divisível por 5, mas não por 3, retorne **`"Fizz"`**.
# MAGIC * Se for divisível por 3, mas não por 5, retorne **`"Buzz"`**.
# MAGIC * Se for divisível por ambos, 3 e 5, retorne **`"FizzBuzz"`**.
# MAGIC * Se não for divisível nem por 3 nem por 5, retorne o próprio número.
# MAGIC
# MAGIC **Dica:** Você vai querer usar uma declaração **`elif`** e **`%`**.
# MAGIC
# MAGIC Tome cuidado com a ordem em que você verifica cada uma dessas condições. Por exemplo, você deve verificar se a entrada é um número inteiro antes de verificar se ela é divisível por algo.

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC &copy; 2024 Aprender Dados. Todos os direitos reservados.<br/>
# MAGIC <a href="https://wa.me/31616144014">Contato</a>