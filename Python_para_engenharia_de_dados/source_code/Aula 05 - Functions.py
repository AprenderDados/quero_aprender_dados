# Databricks notebook source
# MAGIC %md
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 0px;  padding-bottom: 0px;">
# MAGIC   <img src="https://yt3.googleusercontent.com/RW6rRKJqeKTCIFFqZ6e1cdPCQ5dCsnQcXr2ejTcUduHMASnF4Q7UYPA_aCvgLquL93bbEAk2cQ=w1060-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj" alt='AD Logo' style="width: 1500px" >
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # Functions
# MAGIC
# MAGIC   * Crie e use funções para reutilização de código
# MAGIC   * Função **`help()`**
# MAGIC
# MAGIC Referências:
# MAGIC * <a href="https://docs.python.org/3/tutorial/controlflow.html#defining-functions" target="_blank">Documentação Python</a>

# COMMAND ----------

# MAGIC %md
# MAGIC ## Functions ou Funções
# MAGIC
# MAGIC Nesta lição, veremos como podemos usar funções para tornar o código reutilizável.
# MAGIC
# MAGIC Definimos uma função da seguinte forma:
# MAGIC
# MAGIC       def function_name(parameters):
# MAGIC           function_code
# MAGIC
# MAGIC Observe a palavra-chave **`def`**, seguida pelo nome da função, quaisquer parâmetros entre parênteses e um dois-pontos.
# MAGIC
# MAGIC Na verdade, já estamos usando funções: **`print()`** é uma função pré-definida em Python.

# COMMAND ----------

print(0)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Built-in Functions
# MAGIC
# MAGIC Python fornece algumas funções internas para operações comuns.
# MAGIC
# MAGIC Algumas notáveis incluem **`print()`**, que já vimos, **`max()`**, que retorna o valor máximo da entrada, e **`len()`**, que retorna o comprimento da entrada.

# COMMAND ----------

print(max(1, 2))
print(min(1, 2))

# COMMAND ----------

print(len("abc"))


# COMMAND ----------

# MAGIC %md
# MAGIC Podemos chamar **`help()`** nas funções internas para ver sua documentação.

# COMMAND ----------

help(max)

# COMMAND ----------

# MAGIC %md
# MAGIC À medida que o Python executa o código, quando encontra uma chamada para nossa função, ele pula para o bloco de código dentro da definição da função, executa esse código e, em seguida, volta para onde a função foi chamada e continua de onde parou.
# MAGIC
# MAGIC Vamos escrever um exemplo simples de função sem parâmetros.
# MAGIC
# MAGIC Digamos que temos 10 reais e queremos calcular a conversão para euros. No momento desta aula, 1 real equivale a aproximadamente 0,17 euros.

# COMMAND ----------

def real_to_euro():
    print(20.0 * 0.17)

# COMMAND ----------

real_to_euro()

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Para chamar nossa função, podemos seguir a sintaxe:
# MAGIC
# MAGIC ```
# MAGIC function_name(arg)
# MAGIC ``` 
# MAGIC
# MAGIC Por enquanto, vamos ignorar **arg**.
# MAGIC
# MAGIC Veremos sobre mais a frente.

# COMMAND ----------

print("Antes da Função")

real_to_euro()

print("Depois da função")

# COMMAND ----------

# MAGIC %md
# MAGIC ### Parâmetros
# MAGIC
# MAGIC Frequentemente, queremos que nossa função receba algum tipo de entrada. Os parâmetros são variáveis — espaços reservados para os valores reais que a função precisa.
# MAGIC
# MAGIC Vamos considerar nosso exemplo de conversão de dólar para euro. Em vez de nossa função converter apenas 10 dólares para euros, seria melhor se pudéssemos passar qualquer quantia em dólar e convertê-la para euros.
# MAGIC
# MAGIC Podemos fazer isso tendo um parâmetro que represente o **`real`** que queremos converter.

# COMMAND ----------

def real_to_euro(real):
    print(real * 0.17)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Argumentos
# MAGIC
# MAGIC Se nossa função tiver parâmetros, precisamos especificar quais valores queremos que esses parâmetros tenham. Em nosso exemplo, precisamos fornecer um valor para o parâmetro **`real`**. Fazemos isso incluindo o valor entre parênteses quando chamamos a função, assim como fizemos ao fornecer um valor para **`print()`**.
# MAGIC
# MAGIC O valor que passamos para nossa função é chamado de argumento. Em outras palavras, executar **`real(5)`** atribui o valor 5 ao parâmetro **`real`** e, em seguida, executa o código da função.

# COMMAND ----------

real_to_euro(5.0)
real_to_euro(10)
real_to_euro(20.0)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Múltiplos Parâmetros
# MAGIC
# MAGIC Podemos criar uma função com vários parâmetros definindo-os separados por vírgulas.
# MAGIC
# MAGIC Por exemplo, vamos especificar a **`conversao`** além do **`real`** quando chamarmos a função, caso ela mude no futuro.

# COMMAND ----------

def taxa_real_euro(real, taxa_conversao):
    print(real * taxa_conversao)

# COMMAND ----------

# MAGIC %md
# MAGIC Ao invocar essa nova função, devemos fornecer um valor para cada um dos parâmetros da função, separados por vírgulas.

# COMMAND ----------

taxa_real_euro(10.0, 0.93)
taxa_real_euro(5.0, 1.0)
taxa_real_euro(0.20, 10.0) # Retorna erro

# COMMAND ----------

# MAGIC %md
# MAGIC ### Named Invocation
# MAGIC
# MAGIC Na maioria das vezes, quando passamos argumentos para uma função, fazemos isso como acabamos de fazer acima. Fornecemos uma sequência de argumentos e eles são atribuídos aos parâmetros da função na mesma ordem.
# MAGIC
# MAGIC Na chamada **`taxa_real_euro(10, 0.93)`**, o **`real`** é atribuído como **`10`** porque **`real`** é o primeiro parâmetro e **`10`** é o primeiro argumento. 
# MAGIC
# MAGIC Em seguida, **`taxa_conversao = 0.17`** porque eles são o segundo parâmetro e argumento.
# MAGIC
# MAGIC Também podemos passar argumentos para uma função como mostrado abaixo, fornecendo explicitamente os nomes dos parâmetros. Isso é menos comum, mas se feito dessa maneira, a ordem em que os argumentos são passados não importa.

# COMMAND ----------

taxa_real_euro(real=10.0, taxa_conversao=0.93)
taxa_real_euro(taxa_conversao=0.93, real=10.0)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Valores Padrão dos Parâmetros
# MAGIC
# MAGIC Às vezes, é útil ter valores padrão para os parâmetros.
# MAGIC
# MAGIC Em nosso exemplo de conversão de real para euro, talvez queiramos que **`taxa_conversao`** seja **`0.17`**, a taxa de conversão atual, a menos que seja especificado de outra forma.
# MAGIC
# MAGIC Podemos definir valores padrão para os parâmetros da seguinte forma:
# MAGIC
# MAGIC
# MAGIC ```
# MAGIC def func(params, param=default_value):
# MAGIC       code
# MAGIC ```
# MAGIC
# MAGIC

# COMMAND ----------

def real_to_euro(real=10.0, taxa_conversao=0.93):
    print(real * taxa_conversao)

# COMMAND ----------

# MAGIC %md
# MAGIC Agora, quando chamamos essa função e não especificamos um argumento para **`taxa_conversao`**, ele é definido como **`0.17`**

# COMMAND ----------

real_to_euro(1)
real_to_euro(10.0, 0.5)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Output
# MAGIC
# MAGIC Até agora, todas as funções que definimos apenas imprimem valores. Se as avaliarmos como uma expressão, veremos que elas não produzem um resultado útil.
# MAGIC
# MAGIC

# COMMAND ----------

a = real_to_euro(10.0)
print(a)

# COMMAND ----------

# MAGIC %md
# MAGIC Nossa função é executada e imprime 9.3 enquanto o corpo da função está sendo executado, mas quando tentamos avaliar a função como uma expressão em Python, ela é avaliada como **`None`**. **`None`** é um tipo de dado especial que representa nada.
# MAGIC
# MAGIC Se quisermos que o Python avalie nossa função como uma expressão para o valor que estamos imprimindo atualmente, precisamos usar a palavra-chave return.
# MAGIC
# MAGIC

# COMMAND ----------

def real_to_euro(real, taxa_conversao=0.93):
    calculo = real * taxa_conversao
    return calculo

# COMMAND ----------

a = real_to_euro(10.0)
print(a)

# COMMAND ----------

# MAGIC %md
# MAGIC Agora, com a palavra-chave return, o Python avalia **`real_to_euro(10.0)`** como **`0.93`**, assim como avalia **`10.0 * 0.93`** como **`0.93`**. Qualquer coisa que desejamos que uma função produza para uso fora da função deve ser colocada após o **`return`**. Assim que o Python atinge o **`return`** no corpo de uma função, ele sai da função e volta para onde parou.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Output de mais de um valor

# COMMAND ----------

def calculos(numero1, numero2):
    soma = numero1 + numero2
    multiplicacao = numero1 * numero2

    return soma, multiplicacao

# COMMAND ----------

soma, mult = calculos(2, 3)

print(soma)
print(mult)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Tipo de Dados nos Parâmetros
# MAGIC
# MAGIC Observe que podemos passar qualquer tipo que desejarmos como argumento de função, mesmo que a função tenha sido escrita para funcionar apenas com um determinado tipo.
# MAGIC
# MAGIC Por exemplo, o Python nos permitirá chamar **`real_to_euro(True, "abc")`**, mas falhará porque a multiplicação não está definida entre booleanos e strings.
# MAGIC
# MAGIC Podemos adicionar o tipo do dados esperado às nossas funções para ajudar com isso.
# MAGIC
# MAGIC Isso é feito adicionando dois pontos, um espaço opcional e um tipo de dado a um parâmetro, como mostrado abaixo. **`real: float`**. O tipo de retorno é indicado com um hífen, um sinal de maior e o tipo de dado antes dos dois pontos no final da linha de assinatura. **`-> str:`**
# MAGIC
# MAGIC Por exemplo, se quisermos indicar que **`real_to_euro`** deve funcionar apenas com floats e retornar floats, podemos escrevê-lo como mostrado abaixo.

# COMMAND ----------

def real_to_euro(real: float, taxa_conversao: float = 0.93) -> float:
    return real * taxa_conversao

# COMMAND ----------

# MAGIC %md
# MAGIC **É importante observar que essas dicas de tipo não são obrigatórias.** Elas são sugestões que indicam os tipos esperados, mas ainda podemos passar o tipo errado para a função e ela tentará executá-lo.
# MAGIC
# MAGIC O principal benefício das dicas de tipo é melhorar a legibilidade e alguns ambientes de programação podem usá-las para detectar erros mais cedo.

# COMMAND ----------

real_to_euro(1)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Docstrings
# MAGIC
# MAGIC A documentação torna seu código mais organizado e facilmente compreensível por outras pessoas. Uma maneira comum de documentar seu código é usando docstrings.
# MAGIC
# MAGIC Docstrings são comentários especiais que são colocados entre três aspas, como mostrado abaixo. Para usar docstrings para documentar funções, coloque-os no corpo da função antes do código da função.

# COMMAND ----------

def real_to_euro(real: float, taxa_conversao: float = 0.17) -> float:
    """
    Retorna a conversão entre moeda REAL (BRL) para EURO (EUR)
    
    Parametros:
        real (float): Valor em REAL a ser convertido para EURO
        taxa_conversao (float): Taxa de conversão entre REAL e EURO. Default:0.17
    
    Returns:
         euro (float): Valor em EURO equivalente ao valor em REAL
    """
    euro = real * taxa_conversao
    return euro

# COMMAND ----------

# MAGIC %md
# MAGIC Diferentemente dos comentários, as docstrings são salvas como uma propriedade em Python. A função interna help() acessa a docstring e a exibe.

# COMMAND ----------

help(real_to_euro)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Scope
# MAGIC
# MAGIC Em Python, variáveis definidas em determinadas regiões do código são acessíveis apenas dentro da mesma região. Isso é chamado de escopo.
# MAGIC
# MAGIC Vale ressaltar que qualquer variável definida dentro de uma função é acessível dentro da função, mas não fora dela. Em outras palavras, o escopo da variável está limitado à função em que ela é definida.

# COMMAND ----------

def function():
    numero = 1
    return numero

# COMMAND ----------

function()

# COMMAND ----------

numero

# COMMAND ----------

# MAGIC %md
# MAGIC &copy; 2024 Aprender Dados. Todos os direitos reservados.<br/>
# MAGIC <a href="https://wa.me/31616144014">Contato</a>