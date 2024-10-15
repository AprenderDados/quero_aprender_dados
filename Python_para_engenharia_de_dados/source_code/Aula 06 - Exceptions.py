# Databricks notebook source
# MAGIC %md
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 0px;  padding-bottom: 0px;">
# MAGIC   <img src="https://yt3.googleusercontent.com/RW6rRKJqeKTCIFFqZ6e1cdPCQ5dCsnQcXr2ejTcUduHMASnF4Q7UYPA_aCvgLquL93bbEAk2cQ=w1060-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj" alt='AD Logo' style="width: 1500px" >
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # Erros e Exceções
# MAGIC
# MAGIC   * Lidando com erros
# MAGIC   * Use **`try-catch`** para tratamento de exceções
# MAGIC   * Assertion Error
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Referências:
# MAGIC * <a href="https://docs.python.org/3/library/exceptions.html#exception-context" target="_blank">Built-in Exceptions</a>

# COMMAND ----------

# MAGIC %md
# MAGIC ### Syntax Errors
# MAGIC
# MAGIC Em Python, existem principalmente dois tipos diferentes de erros: Erros de Sintaxe e Exceções. Os Erros de Sintaxe ocorrem quando o código é digitado incorretamente e o Python não consegue interpretá-lo.
# MAGIC
# MAGIC O exemplo abaixo ilustra um Erro de Sintaxe:

# COMMAND ----------

if True
print("Olá")

# COMMAND ----------

# MAGIC %md
# MAGIC ### Exceptions
# MAGIC
# MAGIC As Exceções, por outro lado, ocorrem mesmo quando o código está formatado corretamente e o Python sabe como executá-lo. Elas indicam que, embora o Python tenha entendido o que estávamos tentando fazer, há um problema.
# MAGIC
# MAGIC O exemplo a seguir ilustra uma Exceção:

# COMMAND ----------

print('antes')
1 / 0
print('cod')

# COMMAND ----------

# MAGIC %md
# MAGIC Nesse caso, observamos uma exceção do tipo **`ZeroDivisionError`**, indicando que tentamos dividir por zero, o que não é possível. Existem diferentes exceções fornecidas pelo Python que indicam problemas específicos. 
# MAGIC
# MAGIC **`NOTA:`** Verifique o link de referencia no início da aula para uma lista completa das exceções internas.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Lidando com Exceções
# MAGIC
# MAGIC Os Erros de Sintaxe sempre fazem com que nossos programas falhem, mas podemos lidar com exceções em Python. Isso nos permite programar o que acontece quando o Python encontra uma exceção ou exceções específicas ao tentar executar um bloco de código. Para lidar com exceções em Python, usamos uma declaração **`try`**.
# MAGIC
# MAGIC Escrevemos uma declaração **`try`** da seguinte maneira:
# MAGIC
# MAGIC ```
# MAGIC try:
# MAGIC     # code_block
# MAGIC except:
# MAGIC     # code_block
# MAGIC ```
# MAGIC Quando o Python encontra uma declaração **`try`**, ele primeiro tenta executar o código no bloco **`try`**. Se encontrar uma exceção, em vez de sair e gerar um erro, ele executará o code_block dentro do **`except`**.

# COMMAND ----------

try:
    print('antes')
    1/0
    print("depois")
except:
    print("Exception")

# COMMAND ----------

# MAGIC %md
# MAGIC No exemplo anterior, executamos o bloco **`except`** se encontrarmos qualquer exceção no bloco **`try`**. Se quisermos lidar apenas com uma exceção específica, podemos escrever o nome da exceção após a palavra-chave **`except`**

# COMMAND ----------

try:
    name # ZeroDivisionError
except ZeroDivisionError:
    print("Exception")

# COMMAND ----------

try:
    print(variavelx) 
except ZeroDivisionError:
    print("ZeroDivisionError")

# COMMAND ----------

# MAGIC %md
# MAGIC Se quisermos lidar com múltiplas exceções específicas, podemos escrever uma sequência de exceções separadas por vírgulas entre parênteses.
# MAGIC
# MAGIC Tente comentar uma das linhas de lançamento de exceção abaixo de cada vez e observe que ambas as exceções são tratadas.

# COMMAND ----------

try:
   if print('a')
except (ZeroDivisionError, NameError):
    print("Exception")

# COMMAND ----------

try:
   name
except (ZeroDivisionError):
    print("ZeroDivisionError")
except (NameError):
    print("ação qualquer")


# COMMAND ----------

try:
   name
except Exception as e:
    print(type(e))

# COMMAND ----------

# MAGIC %md
# MAGIC Isso agora lida com as exceções ZeroDivisionError e NameError.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Assertion Error
# MAGIC
# MAGIC Outra exceção útil é chamada de **`AssertionError`**. Podemos gerar **`AssertionErrors`** usando declarações **`assert`**. Essas declarações são frequentemente usadas para verificar o código em laboratórios e exercícios. A sintaxe é a seguinte:
# MAGIC
# MAGIC `assert expressao_booleana, mensagem_opcional`
# MAGIC
# MAGIC Quando o Python executa essa declaração, ele avalia primeiro a expressão booleana. Se for **`True`**, o Python não faz nada e continua. Se for **`False`**, ele gera um **`AssertionError`** com a mensagem opcional, se fornecida.

# COMMAND ----------

#assert 1 == 0
assert 1 == 0, "Primeiro Arg não é igual ao Segundo Arg"

# COMMAND ----------

# MAGIC %md
# MAGIC &copy; 2024 Aprender Dados. Todos os direitos reservados.<br/>
# MAGIC <a href="https://wa.me/31616144014">Contato</a>