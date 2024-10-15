# Databricks notebook source
# MAGIC %md
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 0px;  padding-bottom: 0px;">
# MAGIC   <img src="https://yt3.googleusercontent.com/RW6rRKJqeKTCIFFqZ6e1cdPCQ5dCsnQcXr2ejTcUduHMASnF4Q7UYPA_aCvgLquL93bbEAk2cQ=w1060-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj" alt='AD Logo' style="width: 1500px" >
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # Condicionais
# MAGIC
# MAGIC ### Nessa aula vamos ver sobre:
# MAGIC   * Usando **`if`** / **`else`** para fluxo de controles

# COMMAND ----------

# MAGIC %md
# MAGIC ## if/else
# MAGIC
# MAGIC
# MAGIC **`if`** / **`else`** são comuns em diversas linguagens de programação e são utilizados como fluxos de controle.
# MAGIC
# MAGIC Com ele conseguimos mapear e lidar com n possibilidades de ocorrências durante a execução do nosso código.
# MAGIC
# MAGIC Veja abaixo lógica e sintaxe por tras do **`if`** / **`else`**:
# MAGIC
# MAGIC
# MAGIC     if bool:
# MAGIC         code_1
# MAGIC     else:
# MAGIC         code_2
# MAGIC
# MAGIC
# MAGIC `bool`:: expressão booleana que pode ser **`True`** ou **`False`**
# MAGIC
# MAGIC No código acima, o Python lê `bool` e caso o valor deste seja **`True`**, então **`code_1`** será executado. 
# MAGIC
# MAGIC Se o valor de `bool` for **`False`**, o comando **`code_1`** será "ignorado" e o **`code_2`** será executado.

# COMMAND ----------

if True:
    print("True")
else:
    print("False")

# COMMAND ----------

if 1!=2:
  print('é diferente')
else:
  print('é igual')

# COMMAND ----------

# MAGIC %md
# MAGIC ## Operadores
# MAGIC
# MAGIC Para usar o **`if`** / **`else`** utilize operadores para auxiliar nas comparações de valores
# MAGIC
# MAGIC | Sintaxe | Operador |
# MAGIC | --- | --- |
# MAGIC | **`==`** | igual |
# MAGIC | **`>`** | maior que |
# MAGIC | **`<`** | menor que |
# MAGIC | **`>=`** | maior ou igual a |
# MAGIC | **`<=`** | menor ou igual a |
# MAGIC | **`!=`** | diferente |

# COMMAND ----------

print(1 == 1)
print(1.5 != 2.5)
print("abc" == "xyz")
print(True == True)

# COMMAND ----------

comida = 'arroz'

if comida == "arroz":
    print(f"Eu amo {comida}")
else:
    print(f"Eu não gosto de {comida}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## elif
# MAGIC
# MAGIC Mas e se eu precisar considerar multiplas expressões??
# MAGIC
# MAGIC Nesse caso podemos usar o  **`elif`** que é uma abreviação de (`else` + `if`).
# MAGIC
# MAGIC
# MAGIC     if bool:
# MAGIC         code_1
# MAGIC     elif bool:
# MAGIC         code_2
# MAGIC     elif bool:
# MAGIC         code_3
# MAGIC     .
# MAGIC     .
# MAGIC     .
# MAGIC     else:
# MAGIC         code_last

# COMMAND ----------

comida = 'carne'

if comida == "arroz":
    print(f"Eu amo {comida}")
elif comida == "batata":
    print(f"Meu vegetal favorito é {comida}")
elif comida == "carne":
    print(f"Você tem alguma receita para {comida}?")
else:
    print(f"Eu nao como {comida}")

# COMMAND ----------

# MAGIC %md
# MAGIC ### Exercícios
# MAGIC
# MAGIC Com o que você aprendeu, construa um código python que reflita a situação abaixo:
# MAGIC
# MAGIC 1. João tem R$ 20 para almoçar e decide ir ao restaurante A perto do trabalho. Se o preço do prato executivo for igual ou menor ao valor que João tem, então ele irá almoçar ali, Se não, João seguirá ao próximo restaurante

# COMMAND ----------

carteira = 20
prato_executivo = 25

if prato_executivo <= carteira:
  print('João vai almoçar aqui')
else:
  print('João não vai almoçar aqui')

# COMMAND ----------

# MAGIC %md
# MAGIC 2. O que pode acontecer caso o preço do restaurante A e o preço do restaurante B forem superiores ao valor total que João tem?

# COMMAND ----------

carteira = 20
restaurante_a = 25
restaurante_b = 60

if restaurante_a < carteira:
  print('João vai almoçar no A')
elif restaurante_b < carteira:
  print("João vai almoçar no B")
else:
  print('João não vai almoçar aqui')

# COMMAND ----------

# MAGIC %md
# MAGIC 3. João decidiu comer no restaurante C pois o preço da refeição era de R$ 15. Após o almoço, João tem ainda R$ 5 na carteira e pode comprar uma sobremesa. Nesse caso, como ficaria nosso código?

# COMMAND ----------

carteira = 20
restaurante_a = 25
restaurante_b = 60
restaurante_c = 16

if restaurante_a <= carteira:
  print('João vai almoçar no A')
elif restaurante_b <= carteira:
  print("João vai almoçar no B")
elif restaurante_c <= carteira:
  print('João vai comer no C')
  troco = carteira - restaurante_c
  if troco >= 5:
    print('João vai comer um doce')
  else:
    print('João nao vai comer doce')
else:
  print('João não vai almoçar aqui')

# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------

prato_executivo = 20

if prato_executivo <= 20:
    print("Vou comer aqui")
else:
    print("Vou procurar outro lugar")

# COMMAND ----------

carteira = 20
rest_a = 25
rest_b = 30
rest_c = 15

if carteira >= rest_a:
    print("Vou comer no restaurante A")
elif carteira >= rest_b:
    print("Vou comer no restaurante B")
elif carteira >= rest_c:
    print("Vou comer no restaurante C")

# COMMAND ----------

carteira = 20
rest_a = 25
rest_b = 30
rest_c = 15
sobremesa = 6

if carteira >= rest_a:
    print("Vou comer no restaurante A!")
elif carteira >= rest_b:
    print("Vou comer no restaurante B!")
elif carteira >= rest_c:
    print("Vou comer no restaurante C!")
    troco = carteira - rest_c
    if troco >= sobremesa:
      print("Vou comer um pudim!")
    else:
      print("Melhor deixar pra outro dia =( ")

# COMMAND ----------

# MAGIC %md
# MAGIC &copy; 2024 Aprender Dados. Todos os direitos reservados.<br/>
# MAGIC <a href="https://wa.me/31616144014">Contato</a>