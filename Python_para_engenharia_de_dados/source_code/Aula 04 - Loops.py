# Databricks notebook source
# MAGIC %md
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 0px;  padding-bottom: 0px;">
# MAGIC   <img src="https://yt3.googleusercontent.com/RW6rRKJqeKTCIFFqZ6e1cdPCQ5dCsnQcXr2ejTcUduHMASnF4Q7UYPA_aCvgLquL93bbEAk2cQ=w1060-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj" alt='AD Logo' style="width: 1500px" >
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # Loops ou Estruturas de Repetição
# MAGIC
# MAGIC ### Nessa aula vamos ver sobre:
# MAGIC   * Fluxos de controle com loops
# MAGIC   * Use loops para lidar com listas

# COMMAND ----------

# MAGIC %md
# MAGIC ## For
# MAGIC
# MAGIC Loops são um jeito de criarmos um bloco de repetição quando precisamos iterar ou percorrer uma sequência.
# MAGIC
# MAGIC ```
# MAGIC  for var_name in list:
# MAGIC      code_block
# MAGIC ```
# MAGIC
# MAGIC O Python vai executar o **`code_block`** para cada **`var_name`** em **`list`**

# COMMAND ----------

for i in [0, 1, 2]:
    print(i)

# COMMAND ----------

palavra = "Python"

for letra in palavra:
    print(letra)

# COMMAND ----------

# MAGIC %md
# MAGIC Se você deseja executar um bloco de código várias vezes, mas sem usar uma lista, pode usar a função `range()`.
# MAGIC
# MAGIC A função `range()` recebe um índice de início e um índice de parada (o valor do índice de parada é exclusivo, não inclusivo). Por padrão, ela incrementa de um em um, começando no índice de início e terminando em stop-1. 
# MAGIC
# MAGIC Nessa lógica, `range(0, 4)` iteraria pelos valores: 0, 1, 2, 3.

# COMMAND ----------

for item in range(0, 10):
    print("Olá!")

# COMMAND ----------

for item in range(3):
    print("Olá!")

# COMMAND ----------

# MAGIC %md
# MAGIC Aqui, o item é temporariamente atribuído a cada número nesse intervalo em cada iteração.

# COMMAND ----------

for item in range(0, 10):
    print(item)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Exercício

# COMMAND ----------

# MAGIC %md
# MAGIC Pergunta: Como podemos alterar o código para imprimir de 1 a 10, não de 0 a 9?

# COMMAND ----------

for i in range(5,12):
  print(i)

# COMMAND ----------

# MAGIC %md
# MAGIC Você pode usar loops para filtrar uma lista. Por exemplo, digamos que quiséssemos filtrar uma lista de números para manter apenas os números maiores que 4.
# MAGIC
# MAGIC Podemos fazer isso criando uma nova lista vazia, percorrendo nossa lista de números e adicionando os números à lista vazia se forem maiores que 4.

# COMMAND ----------

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
final_list = []

# COMMAND ----------


for element in numbers_list:
    if element >= 4:
        final_list.append(element)
    else:
        pass # Não faz nada
        
final_list

# COMMAND ----------

# MAGIC %md
# MAGIC Criar uma nova lista filtrando outra com um loop é um problema comum e que o Python fornece um atalho muito útil.
# MAGIC
# MAGIC Esse "atalho" é chamado de **`list comprehension`** e tem a sintaxe: `[nome_variável for nome_variável in lista if (condição booleana)]`
# MAGIC
# MAGIC Vamos usar esse atalho para fazer exatamente a mesma coisa que fizemos na célula anterior.

# COMMAND ----------

final_list = [element for element in numbers_list if element > 4]
final_list

# COMMAND ----------

# MAGIC %md
# MAGIC Você pode ler isso da esquerda para a direita, incluindo o **`element`** na lista final para cada **`element`** em **`numbers`** se o **`element`** for maior que 4.
# MAGIC
# MAGIC Por exemplo, digamos que, em vez de incluir apenas cada **`element`** em **`numbers`** que seja maior que 4, queremos incluir 2 **`element`** para cada **`element`** em **`numbers`** se o **`element`** for maior que 4. 
# MAGIC
# MAGIC Vamos ver o código abaixo.

# COMMAND ----------

lista_dupla = [2 * element for element in numbers_list if element > 4]
lista_dupla

# COMMAND ----------

# MAGIC %md
# MAGIC A expressão booleana é realmente opcional. 
# MAGIC Vamos dobrar cada elemento na lista.

# COMMAND ----------

[2 * element for element in numbers_list]

# COMMAND ----------

nova_lista = []
for element in numbers_list:
    #print(2* element)
    nova_lista.append(2*element)

nova_lista

# COMMAND ----------

# MAGIC %md
# MAGIC #### `break`
# MAGIC
# MAGIC Se você quiser sair de um loop antes que ele termine de iterar sobre sua sequência, pode usar o comando **`break`**.
# MAGIC
# MAGIC O **`break`** é escrito em sua própria linha dentro do bloco de código do loop, e quando o Python executa essa linha, ele sai do bloco de código do loop e para de iterar sobre a lista.
# MAGIC
# MAGIC Vamos usar isso para parar de iterar sobre a lista  **`numbers_list`** assim que chegarmos ao número 4.

# COMMAND ----------

for element in numbers_list:
    if element == 4:
        break
    print(element)

# COMMAND ----------

# MAGIC %md
# MAGIC #### `continue`
# MAGIC
# MAGIC O **`break`** sai do bloco de código do loop quando é executado e interrompe a iteração sobre a lista. Se, em vez disso, você quisesse sair do bloco de código do loop mais cedo, mas ainda continuar executando a sequência, poderia usar o comando **`continue`**.
# MAGIC
# MAGIC O **`continue`** também é escrito em sua própria linha e, quando é executado, o Python interrompe a execução do bloco de código do loop e depois continua a iterar sobre a sequência.

# COMMAND ----------

for element in numbers_list:
    if element == 4:
        continue # 4 is not printed, but the numbers after are
    print(element)

# COMMAND ----------

# MAGIC %md
# MAGIC ### For com Dicionários
# MAGIC
# MAGIC Quando se itera sobre um dicionário, você pode iterar pelas chaves, pelos valores ou por ambos (chaves e valores).
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Percorrendo as chaves

# COMMAND ----------

dicionario = {'a': 1, 'b': 2, 'c': 3}

for chave in dicionario:
    print(chave)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Percorrendo os valores

# COMMAND ----------

dicionario.values()

# COMMAND ----------

for valor in dicionario.values():
    print(valor)


# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Percorrendo por chaves e valores

# COMMAND ----------

dicionario.items()

# COMMAND ----------

for chave, valor in dicionario.items():
    print(chave, valor)


# COMMAND ----------

# MAGIC %md
# MAGIC ### `zip`
# MAGIC
# MAGIC A função **`zip()`** é usada para iterar sobre várias sequências ao mesmo tempo. Ela emparelha elementos das sequências em tuplas.

# COMMAND ----------

nomes = ['João', 'Maria', 'Pedro','Ketlen']
idades = [28, 34, 22, 55]

for a, b in zip(nomes, idades):
    print(a, b)


# COMMAND ----------

# MAGIC %md
# MAGIC ## While

# COMMAND ----------

# MAGIC %md
# MAGIC Além dos loops **for**, existe outro tipo de loop chamado **while**.
# MAGIC
# MAGIC Escrevemos um loop while assim:
# MAGIC
# MAGIC ```
# MAGIC  while boolean expression:
# MAGIC      code_block
# MAGIC ```
# MAGIC
# MAGIC O Python executará o **`code_block`** de código repetidamente enquanto a expressão booleana for avaliada como **`True`**. A cada iteração, ele reavaliará a expressão booleana e, se for verdadeira, executará o código novamente; caso contrário, sairá do loop.
# MAGIC
# MAGIC NOTA: Tome cuidado para não criar loops infinitos. Se a expressão booleana nunca se tornar **`False`**, esse código continuará executando indefinidamente.

# COMMAND ----------

count = 10

while count > 0:
    print(count)
    count = count - 1

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Assim como acontece com os comandos **`if/else`**, o Python permite adicionar novos loops dentro um do outro

# COMMAND ----------

for a in range(0,10):
    for b in range(0,10):
        for c in range(0,10):
            print(str(a) +  str(b) + str(c))

# COMMAND ----------

# MAGIC %md
# MAGIC Podemos usar `else` junto com `while`. 
# MAGIC Nesse caso, a cláusula `else` será executada quando o loop terminar (ele não interrompe o loop)

# COMMAND ----------

contador = 0
while contador < 5:
    print(contador)
    contador += 1
else:
    print("Loop terminou normalmente.")


# COMMAND ----------

# MAGIC %md
# MAGIC ### `break`

# COMMAND ----------

contador = 0
while contador < 100:
    print(contador)
    if contador == 10:
        break
    contador += 1


# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Lembre-se:** Um loop permite que você processe grandes quantidades de dados com uma quantidade mínima de código
# MAGIC
# MAGIC * Você pode processar uma lista ou um intervalo de 50.000.000 de elementos com o mesmo código necessário para processar uma lista ou um intervalo de 5 elementos.

# COMMAND ----------

# MAGIC %md
# MAGIC **DICA:**  
# MAGIC * Use for quando souber o número de iterações antecipadamente ou estiver iterando sobre uma sequência conhecida.
# MAGIC
# MAGIC * Use while quando o número de iterações depender de uma condição que pode mudar dinamicamente ou quando a lógica do loop é baseada em eventos.

# COMMAND ----------

# MAGIC %md
# MAGIC &copy; 2024 Aprender Dados. Todos os direitos reservados.<br/>
# MAGIC <a href="https://wa.me/31616144014">Contato</a>