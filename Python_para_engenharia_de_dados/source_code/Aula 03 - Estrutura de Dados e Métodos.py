# Databricks notebook source
# MAGIC %md
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 0px;  padding-bottom: 0px;">
# MAGIC   <img src="https://yt3.googleusercontent.com/RW6rRKJqeKTCIFFqZ6e1cdPCQ5dCsnQcXr2ejTcUduHMASnF4Q7UYPA_aCvgLquL93bbEAk2cQ=w1060-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj" alt='AD Logo' style="width: 1500px" >
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # Métodos e Estrutura de Dados
# MAGIC
# MAGIC ### Nessa aula vamos ver sobre:
# MAGIC   * Lidando com as estruturas de dados:
# MAGIC     * Listas
# MAGIC     * Dicionários

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Objetos e Métodos
# MAGIC
# MAGIC ### Objetos
# MAGIC
# MAGIC Um objeto é uma instância de um tipo de dado específico. Por exemplo, o número 1 é um objeto do tipo inteiro, e a palavra “Olá” é um objeto do tipo string.
# MAGIC
# MAGIC
# MAGIC ### Métodos
# MAGIC
# MAGIC Os métodos são como funções especiais associadas a um tipo de dado. Eles nos oferecem funcionalidades extras. 
# MAGIC
# MAGIC **`object.method_name(arguments)`**
# MAGIC
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Métodos String

# COMMAND ----------

# MAGIC %md
# MAGIC * **`lower()`**: Converte todos os caracteres maiúsculos de uma string em minúsculos

# COMMAND ----------

saudacao = "OLÁ A TODOS"
print(saudacao)
print(saudacao.lower())

# COMMAND ----------

saudacao


# COMMAND ----------

# MAGIC %md
# MAGIC * **`upper()`**: Converte todos os caracteres minúsculos de uma string em maiúsculos

# COMMAND ----------

saudacao = "olá"
print(saudacao)
print(saudacao.upper())

# COMMAND ----------

# MAGIC %md
# MAGIC * **`capitalize()`**: Converte o primeiro caractere de uma string para maiúsculo

# COMMAND ----------

saudacao = 'ola a todos'
print(saudacao.capitalize())

# COMMAND ----------

# MAGIC %md
# MAGIC * **`replace()`**: Substitui todas as ocorrências de uma substring por outra substring
# MAGIC

# COMMAND ----------

saudacao = 'olá a todos'
print(saudacao.replace('olá', 'oi'))

# COMMAND ----------

# MAGIC %md
# MAGIC * **`rsplit()`**: Divida a string da direita pelo separador especificado

# COMMAND ----------

saudacao = "olá, alunos da aprender dados"
print(saudacao.rsplit(','))

# COMMAND ----------

texto = 'Python na Aprender Dados'
site = 'https://alunos.aprenderdados.com/'

print(texto.rsplit(' '))
print(site.rsplit('.'))

# COMMAND ----------

# MAGIC %md
# MAGIC ### Estrutura de Dados e Métodos
# MAGIC
# MAGIC Em Python, temos várias estruturas de dados que são como ferramentas para organizar e manipular informações. 

# COMMAND ----------

# MAGIC %md
# MAGIC ### 1. Listas
# MAGIC
# MAGIC Listas são definidas por uma sequencia ordenada de itens entre colchetes e separados por vírgula.
# MAGIC
# MAGIC Na prática, você pode criar listas quando os valores (itens) possuem semelhanças entre si, são do mesmo tipo, etc.
# MAGIC
# MAGIC **Exemplos:** **`[item1, item2, item3...]`**
# MAGIC
# MAGIC
# MAGIC **Sintaxe:** Definido usando colchetes **`[]`**.

# COMMAND ----------

frutas = ['maça', 'melancia', 'laranja']
print(frutas)
print(type(frutas))

# COMMAND ----------

# MAGIC %md
# MAGIC As listas são mutáveis, o que significa que você pode modificar seus elementos após a criação da lista. Você pode adicionar, remover ou modificar elementos.

# COMMAND ----------

# MAGIC %md
# MAGIC * **`append()`**: Adiciona um elemento à lista

# COMMAND ----------

frutas.append('limão')
print(frutas)


# COMMAND ----------

frutas = frutas + ['mamão']
frutas

# COMMAND ----------

# MAGIC %md
# MAGIC **DICA:** Você também pode usar o operador **`+=`** para realizar a ação de *append*
# MAGIC
# MAGIC **`frutas += ['mamão']`** é o mesmo que **`frutas = frutas + ['mamão']`** 

# COMMAND ----------

frutas += ['mamão']
frutas

# COMMAND ----------

# MAGIC %md
# MAGIC * **`count(x)`**: Retorna a quantidade de elementos conforme o parâmetro `x`

# COMMAND ----------

frutas.count('mamão')

# COMMAND ----------

# MAGIC %md
# MAGIC * **`remove(x)`**: Remova o primeiro item da lista cujo valor é igual a x 

# COMMAND ----------

print(frutas)
frutas.remove('mamão')
print(frutas)


# COMMAND ----------

# MAGIC %md
# MAGIC * **`pop(x)`**: Remova o item da lista cuja a posição na lista é igual a x

# COMMAND ----------

frutas.pop(2)
print(frutas)


# COMMAND ----------

# MAGIC %md
# MAGIC #### Index ou Indexação
# MAGIC
# MAGIC Frequentemente vamos precisar fazer referencia a algum elemento ou elementos da nossa lista.
# MAGIC Para acessar um elemento específico usamos a sintaxe:
# MAGIC
# MAGIC **`list_name[index]`**
# MAGIC
# MAGIC **IMPORTANTE:** Os índices começam em 0, ou seja, a primeira posição de uma lista é 0, a segunda posição é 1 e assim por diante.

# COMMAND ----------

print(frutas)
frutas[0]

# COMMAND ----------

# MAGIC %md
# MAGIC Para acessar o último ou os últimos elementos da lista, podemos usar números negativos
# MAGIC
# MAGIC Para o último item usamos -1, para o penúltimo -2, e assim por diante.

# COMMAND ----------

frutas[-1]

# COMMAND ----------

# MAGIC %md
# MAGIC Também conseguimos acessar um intervalo da nossa lista usando a sintaxe:
# MAGIC
# MAGIC **`list_name[inicio:fim]`**
# MAGIC
# MAGIC Esse código vai retornar uma lista com todos os elementos dentro do intervalo que passamos como **`inicio`** e **`fim`**
# MAGIC
# MAGIC **`IMPORTANTE:`** O index **`fim`** não será retornado

# COMMAND ----------

frutas.append("laranja")

# COMMAND ----------

print(frutas)
frutas[1:4]

# COMMAND ----------

# Usando a sintaxe abaixo, o Python irá considerar como valor inicial o primeiro elemento da lista, ou seja 0

frutas[:2]

# COMMAND ----------

# Usando a sintaxe abaixo, o Python irá considerar como fim, o utimo elemento da lista

frutas[2:]

# COMMAND ----------

# MAGIC %md
# MAGIC Também conseguimos alterar o valor do item a partir do index:

# COMMAND ----------

print(frutas)
frutas[0] = "pera"

print(frutas)

# COMMAND ----------

# MAGIC %md
# MAGIC Para verificar se o valor está contido na lista use **`in`**. Isso retornará uma expressão booleana

# COMMAND ----------

'melancia' in frutas

# COMMAND ----------

# MAGIC %md
# MAGIC Para descobrir qual a posição de um elemento conhecido, use:
# MAGIC **`index(x)`**

# COMMAND ----------

frutas.index('melancia')

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2. Dicionários
# MAGIC
# MAGIC Dicionários são uma sequencia de pares de chave-valor.
# MAGIC
# MAGIC **Exemplos:** **`{chave: valor1, chave: valor2, chave: valor3, ...}`**
# MAGIC
# MAGIC
# MAGIC **Sintaxe:** Definido usando chaves **`{}`**.
# MAGIC
# MAGIC
# MAGIC **IMPORTANTE:** Cada chave corresponde a um valor, então precisamos que cada chave seja única

# COMMAND ----------

# MAGIC %md
# MAGIC Vamos criar um dicionário de frutas, onde cada chave corresponde a uma fruta e o valor é a quantidade que temos em nossa mesa 

# COMMAND ----------

frutas = {'maça': 1, 'melancia': 2, 'banana': 3}
print(frutas)
print(type(frutas))

# COMMAND ----------

# MAGIC %md
# MAGIC #### Métodos
# MAGIC
# MAGIC Em dicionários temos o método **`get(x)`** que podemos usar para acessarmos o valor de `x`que será nossa chave:

# COMMAND ----------

frutas.get('melancia')

# COMMAND ----------

# MAGIC %md
# MAGIC Para termos o mesmo resultado acima, também podemos usar a sintaxe: **`dicionario[chave]`**

# COMMAND ----------

frutas['melancia']

# COMMAND ----------

# MAGIC %md
# MAGIC Podemos atualizar um dicionário da mesma forma que fazemos com listas.
# MAGIC
# MAGIC Se a chave já existir no nosso dicionário, o valor será atualizado.
# MAGIC
# MAGIC Senão, será criado um novo par de chave-valor.

# COMMAND ----------

print(frutas)
frutas["banana"] = 1
frutas["abacate"] = 0
print(frutas)

# COMMAND ----------

# MAGIC %md
# MAGIC Para saber quais chaves temos em nosso dicionário, podemos usar o método **`dicionario.keys()`**

# COMMAND ----------

frutas.keys()

# COMMAND ----------

# MAGIC %md
# MAGIC Assim como fazemos com listas, para descobrir se uma chave existe no nosso dicionário

# COMMAND ----------

print("maça" in frutas.keys())

# COMMAND ----------

# MAGIC %md
# MAGIC **`values()`**: Retorna uma visão dos valores do dicionário.

# COMMAND ----------

valores = frutas.values()
print(valores)  

# COMMAND ----------

# MAGIC %md
# MAGIC Para remover itens de um dicionário, podemos seguir conforme abaixo:

# COMMAND ----------

# MAGIC %md
# MAGIC **`pop(x)`**: Remove o item com a chave especificada e retorna o valor removido.

# COMMAND ----------

frutas.pop("maça")

# COMMAND ----------

print(frutas)

# COMMAND ----------

# MAGIC %md
# MAGIC **Para saber mais sobre Listas e Dicionários:**
# MAGIC <a href="https://docs.python.org/3/tutorial/datastructures.html">Aqui</a>
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC &copy; 2024 Aprender Dados. Todos os direitos reservados.<br/>
# MAGIC <a href="https://wa.me/31616144014">Contato</a>