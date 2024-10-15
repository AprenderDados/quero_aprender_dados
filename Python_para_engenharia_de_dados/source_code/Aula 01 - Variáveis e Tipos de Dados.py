# Databricks notebook source
# MAGIC %md
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 0px;  padding-bottom: 0px;">
# MAGIC   <img src="https://yt3.googleusercontent.com/RW6rRKJqeKTCIFFqZ6e1cdPCQ5dCsnQcXr2ejTcUduHMASnF4Q7UYPA_aCvgLquL93bbEAk2cQ=w1060-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj" alt='AD Logo' style="width: 1500px" >
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # Variáveis e Tipos de Dados
# MAGIC ### Nessa aula vamos ver sobre:
# MAGIC   * Tipos de Dados
# MAGIC   * Variáveis
# MAGIC   * Recebendo Valores de Usuários 
# MAGIC
# MAGIC Referências:
# MAGIC * <a href="https://docs.python.org/3/tutorial/" target="_blank">The Python Tutorial</a>
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ## Tipos de Dados
# MAGIC
# MAGIC O Python fornece alguns **tipos de dados** básicos. Sendo cada um deles com suas respectivas finalidades e operações.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### 1. Integers
# MAGIC Integers (ou int, ou Inteiros) são numeros não decimais.
# MAGIC
# MAGIC **Exemplos:** 3, 2, 1, 0, -1, -2 
# MAGIC
# MAGIC **Operações Permitidas**: +, -, *, /

# COMMAND ----------

2 * 3 + 6 - 10

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### 2. Float
# MAGIC
# MAGIC Float (ou floating point) é uma representação de número decimal.
# MAGIC
# MAGIC
# MAGIC **Exemplos:** 3.545, 2.76, 0.54, -1.08, -2.2 
# MAGIC
# MAGIC **Operações Permitidas**: +, -, *, /

# COMMAND ----------

5.2 * 2.3 + 5.5456

# COMMAND ----------

# MAGIC %md
# MAGIC **DICA:** Caso você esteja com dúvidas sobre qual o tipo de dado, você pode usar **`type(x)`**.

# COMMAND ----------

type(1.0)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### 3. String
# MAGIC String (ou str) é uma sequência de caracteres entre aspas (`""` ou `''`). Uma **string** pode ser considerada como um texto, podendo conter números e pontuações ou caracteres especiais.
# MAGIC
# MAGIC **Exemplo:** "Hello", "Python na Aprender Dados", '123abc4.56'
# MAGIC
# MAGIC **Operações Permitidas**: +
# MAGIC
# MAGIC **IMPORTANTE:** No caso de **Strings**, a operação de `+` serve como concatenação entre uma ou mais strings

# COMMAND ----------

"Hello" + "123"

# COMMAND ----------

"Hello"+ " 123"

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### 4.Boolean
# MAGIC Boolean (ou bool) é um dado binário que pode conter dois valores: `True` ou `False`
# MAGIC
# MAGIC **IMPORTANTE:** Python é *case-sentitive*, ou seja, diferencia letras maiúsculas de letras minúsculas. Sendo assim, o Python retornará com erros caso os valores sejam escritos como `true` ou `FALSE`
# MAGIC
# MAGIC **Exemplo:** True, False
# MAGIC
# MAGIC **Operações Permitidas**: operadores lógicos (or, and, not)

# COMMAND ----------

type(False)

# COMMAND ----------

type(true)

# COMMAND ----------

True or False

# COMMAND ----------

False and False

# COMMAND ----------

not True

# COMMAND ----------

1 == 2

# COMMAND ----------

1 == 1

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC ### Trabalhando com Variáveis
# MAGIC
# MAGIC Variáveis são identificadores que armazenam valores na memória da computação.
# MAGIC Nós podemos atribuir qualquer tipo de valor a uma variável, como números, strings, booleanose outros...
# MAGIC
# MAGIC Variáveis são úteis quando precisamos referenciar um mesmo valor várias vezes ao longo do nosso código
# MAGIC
# MAGIC **`nome_variavel = valor`**
# MAGIC
# MAGIC **Algumas convenções importantes a serem seguidas ao trabalhar com variáveis:**
# MAGIC * O nome de uma variável deve começar com letras ou `_`
# MAGIC * O nome de uma variável não pode começar com numeral
# MAGIC * O nome de uma variável deve conter apenas caracteres alfanuméricos (*alpha-numeric*) e *underscores* ( _ )  
# MAGIC * Nomes de variáveis são case-sensitive (**`var`**, **`Var`** and **`VAR`** são 3 variáveis diferentes)
# MAGIC * Opte por nomear suas variáveis com letras minúsculas e substitua o uso de espaços por *underscores* (Use **`minha_variavel`** ao invés de **`Minha_variavel**)
# MAGIC * Não use nomes muito grandes (**primeira_variavel_do_curso_python**)
# MAGIC * Escolha nomes que façam uma referência intuitiva e única ao valor armazenado. Assim você evita confusões e dificuldades desnecessárias enquanto desenvolve

# COMMAND ----------

a = 3
b = 2
c = a*b

c

# COMMAND ----------

b = 4
c = c+1
c

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Você também pode alterar o valor da variável a qualquer momento, não importando qual seja o valor original dela:

# COMMAND ----------

b = "Hello World"
print(b)

b = 2
print(b)

type(b)

# COMMAND ----------

b = 10
type(b)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Print Statements
# MAGIC
# MAGIC Com os notebooks do Databricks, o resultado da **última linha** de cada célula é mostrado automaticamente quando executado.
# MAGIC
# MAGIC Se você quiser acompanhar mais do que apenas a úlima linha, você precisará usar a declaração **`print(x)`** 

# COMMAND ----------

a = 3
b = 2

a
b

# COMMAND ----------

print(a)
print(b)

# COMMAND ----------

print("""
String
com
quebra 
de
linha
""")

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Com o print também conseguimos reproduzir uma concatenação entre strings usando `+`
# MAGIC
# MAGIC Isso é útil quando queremos retornar alguma informação específica com base o valor atribuído à variável.

# COMMAND ----------

aluno = 'Bernardo'
print("O nome do aluno é:" + aluno)

# COMMAND ----------

# MAGIC %md
# MAGIC Por padrão, quando passado diversos argumentos ao print, ele retorna na saída a impressão desses valores com separação por espaços

# COMMAND ----------

print(1, 2, 3)

print('O próximo número é',4)

print("O nome do aluno é:", aluno)

# COMMAND ----------

# MAGIC %md
# MAGIC ## F-strings
# MAGIC
# MAGIC Uma outra forma para lidar com variáveis string ou facilitar o seu print é adicionando a letra **`f`** antes de uma string e inserindo a variável entre chaves (**`{}`**).
# MAGIC
# MAGIC Essa alternativa nos permite também combinar os tipos de dados como string e numéricos em uma mesma mensagem

# COMMAND ----------

f"Atenção {aluno} sua nota está disponível!"

# COMMAND ----------

matricula = 123456
nota = (10 + 8 + 9)/3

print(f"O aluno {aluno} com a matricula: {matricula} recebeu nota final de: {nota}")

# COMMAND ----------

# MAGIC %md
# MAGIC &copy; 2024 Aprender Dados. Todos os direitos reservados.<br/>
# MAGIC <a href="https://wa.me/31616144014">Contato</a>