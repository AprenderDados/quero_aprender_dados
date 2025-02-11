# **Guia de Estudos para a Certificação Databricks Data Engineer Associate**

[![Miniatura](https://raw.githubusercontent.com/AprenderDados/quero_aprender_dados/main/Aprendendo_Databricks/img/img_roadmap_certificacao_databricks.jpeg)](https://pay.kiwify.com.br/hP20Upy)

---


## **Como é a prova da certificação?**

O exame está dividido em tópicos de alta relevância para um engenheiro de dados iniciante, com base em cenários práticos e arquiteturas modernas como Lakehouse.

Os principais temas incluem:

1. **Databricks Lakehouse Platform (24%)**
   - Compreender as vantagens e uso da plataforma Lakehouse.
   - Gerenciamento de tabelas Delta e otimizações Delta.

2. **ETL com Spark SQL e Python (29%)**
   - Transformações de dados.
   - Configuração de tabelas e ingestão de dados.

3. **Processamento Incremental de Dados (22%)**
   - Gerenciamento de pipelines de dados em tempo real.
   - Controle incremental de atualizações.

4. **Pipelines de Produção (16%)**
   - Criação e gerenciamento de pipelines resilientes.
   - Melhores práticas de automação de tarefas repetitivas.

5. **Governança de Dados (9%)**
   - Práticas de segurança e controle de acessos.
   - Organização e estrutura de catálogos de dados.

---

## **O que você deveria saber?**

### **1. Fundamentos do Databricks**

#### **1.1 Noções de Notebook**
- Como criar um cluster no Databricks, anexar um notebook a esse cluster.
- Executar diferentes linguagens (%sql, %python, %scala).
- Utilizar dbutils (por exemplo, `dbutils.fs.ls`) para manipular arquivos e recursos auxiliares.
- Comandos mágicos (%) e células Markdown (%md) para anotações dentro dos notebooks.

### **2. Delta Lake**

#### **2.1 Gerenciamento de Tabelas Delta**
- É possível usar CREATE TABLE, INSERT INTO, SELECT FROM, UPDATE, DELETE, DROP TABLE em tabelas Delta.
- A partir do Databricks Runtime 8+, o modo de tabela padrão é o Delta.

#### **2.2 Merge (Upserts)**
- Usado para Upserts (atualizações + inserções).
- `MERGE` requer pelo menos um campo para correspondência na cláusula ON. Cada WHEN MATCHED ou WHEN NOT MATCHED pode ter diversas condições adicionais.

#### **2.3 Opções Avançadas**

##### **2.3.1 OPTIMIZE**
- Compacta os arquivos, substituindo-os por arquivos combinados menores, otimizando leituras.

##### **2.3.2 Z ORDER**
- Indexa/organiza fisicamente os arquivos para consultas eficientes.
- Acelera a recuperação de dados em consultas filtradas pelas colunas envolvidas.

##### **2.3.3 VACUUM**
- Remove dados obsoletos ("stale data").
- Padrão de retenção: 7 dias.
- Pode ser configurado via parâmetros (ex.: `spark.databricks.delta.retentionDurationCheck.enabled`).

#### **2.4 Time Travel – Funções-Chave**

##### **2.4.1 VERSION (HISTORY / TIME TRAVEL)**
- Permite consultar versões anteriores de uma tabela por número de versão ou timestamp.

##### **2.4.2 DRY RUN**
- Exibe os arquivos que seriam excluídos antes de executar a operação efetiva (ex.: VACUUM).

##### **2.4.3 RESTORE**
- Restaura uma versão anterior da tabela (rollback).

### **3. Entidades Relacionais**

#### **3.1 Databases & Tables**
- Diferença entre tabelas externas e gerenciadas.
- Localização (LOCATION) afeta onde os dados serão armazenados.

#### **3.2 Views, Temp Views & Global Temp Views**
- Views: Acessíveis dentro do database.
- Temp Views: Acessíveis somente na sessão atual.
- Global Temp Views: Criadas no database `global_temp` e acessíveis enquanto o cluster estiver ativo.

#### **3.3 CTEs (Common Table Expressions)**
- Utilizadas para subconsultas temporárias dentro de uma query.
- Diferem de tabelas temporárias, que duram a sessão inteira.

### **4. ETL com Spark SQL**

#### **4.1 Consulta Direta a Arquivos**
- Permite consultar arquivos CSV, JSON, PARQUET diretamente.

#### **4.2 Opções para Fontes Externas**
- Registro de tabelas em locais externos.
- Extração de dados via JDBC.

#### **4.3 Criação de Tabelas Delta**
- Usar `CTAS` (Create Table As Select).
- Configurar colunas geradas automaticamente e constraints.

#### **4.4 Escrita em Tabelas**
- Operações de sobrescrita, append, merge e incremental.

#### **4.6 Limpeza de Dados**
- Contagem de valores nulos e manipulação com WHERE, GROUP BY.

#### **4.7 Transformações SQL Avançadas**
- Manipulação de dados JSON, arrays e execução de JOINs.

#### **4.8 SQL UDFs e Fluxo de Controle**
- Criação de funções customizadas e uso de CASE/WHEN.

### **5. Python para Spark SQL (Opcional)**

#### **5.1 Strings e Controle**
- Uso de strings de múltiplas linhas e F-strings.
- Uso de estruturas como `if/elif/else`.

### **6. Processamento de Dados Incremental usando AutoLoader**
- Configurar ingestão incremental automatizada de arquivos.

### **7. Arquitetura Medallion (Bronze, Silver & Gold)**
- Bronze: Dados brutos (raw).
- Silver: Dados filtrados e enriquecidos.
- Gold: Dados prontos para análise e relatórios.

### **8. Delta Live Tables**

#### **8.1 Criação de ETLs**
- Configurar ETLs declarativos com Delta Live Tables.

#### **8.3 Continuous vs Triggered**
- Diferenciar modos contínuos e acionados.

### **9. Orquestração de Tarefas (Jobs)**
- Criar DAGs com dependências entre tarefas.

### **10. DB SQL & Dashboards**
- Criação de dashboards SQL interativos e configuração de alertas.

### **11. Gerenciamento de Permissões com Unity Catalog**

#### **11.1 Data Explorer**
- Configurar permissões em databases e tabelas.
- Funcionamento e detalhes técnicos do Unity Catalog

---

## **Tabela de Checklist com Exemplos de Aplicação**

| **Tópico**              | **Habilidade**                | **Exemplos de Aplicação**                                   | **Referências**                             | **Aula** |
|-------------------------|-------------------------------|--------------------------------------------------------|--------------------------------------------|---------|
| Fundamentos do Databricks | Noções de Notebook            | Criar cluster, anexar notebooks para análises           | [Link](https://docs.databricks.com/clusters/index.html) | 01      |
| Delta Lake              | Gerenciamento de Tabelas Delta | Usar operações CRUD para manipulação de tabelas Delta   | [Link](https://docs.databricks.com/delta/index.html) | 04      |
| Delta Lake              | Merge (Upserts)               | Atualizar dados com MERGE para evitar duplicações       | [Link](https://docs.databricks.com/delta/merge.html) | 04      |
| Delta Lake              | OPTIMIZE                      | Compactar arquivos para melhorar desempenho             | [Link](https://docs.databricks.com/delta/optimize.html) | 04      |
| ETL com Spark SQL       | Consulta Direta a Arquivos    | Consultar arquivos JSON, CSV diretamente com SQL        | [Link](https://docs.databricks.com/data/databricks-file-system.html) | 03      |
| Python para Spark SQL   | Strings                      | Criar strings dinâmicas para configurar caminhos de arquivo | [Link](https://docs.python.org/3/tutorial/introduction.html) | 02      |
| Processamento Incremental | AutoLoader                  | Configurar ingestão contínua para novos arquivos         | [Link](https://docs.databricks.com/spark/latest/structured-streaming/auto-loader.html) | 06      |
| Arquitetura Medallion   | Bronze, Silver & Gold         | Estruturar camadas de dados para pipelines resilientes  | [Link](https://docs.databricks.com/data/metastores/index.html) | 04      |
| Delta Live Tables       | Criação de ETLs               | Criar pipelines declarativos com tabelas Delta          | [Link](https://docs.databricks.com/workflows/delta-live-tables/index.html) | 09      |
| Orquestração de Tarefas | Jobs                          | Criar pipelines dependentes com tarefas automatizadas   | [Link](https://docs.databricks.com/workflows/jobs/index.html) | 08      |
| DB SQL & Dashboards     | Dashboards e Alertas          | Criar dashboards interativos com KPIs                  | [Link](https://docs.databricks.com/sql/index.html) | 05      |
| Gerenciamento de Permissões | Data Explorer            | Configurar e gerenciar permissões em tabelas e databases | [Link](https://docs.databricks.com/security/access-control/workspace-acl.html) | 09      |

---

## **Conheça a preparação para certificação Databricks DataEng Associate**

[**Adquira agora o Treinamento**](https://pay.kiwify.com.br/hP20Upy)

[**Já comprei o curso**](https://alunos.aprenderdados.com/189295-preparatorio-databricks-data-engineering-associate)

Nosso treinamento abrange as principais áreas para a certificação, organizadas em módulos:

1. **Introdução ao Databricks Community + Workspace + PySpark + SQL**
2. **Clusters e Otimização**
3. **Ingestão de Dados com PySpark e SQL**
4. **Delta Lake e Arquitetura Lakehouse (Bronze, Prata e Ouro)**
5. **Ingestão Incremental com AutoLoader**
6. **Automação de Pipelines com Workflows**
7. **Delta Live Tables e Unity Catalog**
8. **Preparação para Certificação**

---

[![Miniatura do Curso](https://raw.githubusercontent.com/AprenderDados/quero_aprender_dados/main/Aprendendo_Databricks/img/img_treinamento_certificacao_databricks_.png)](https://pay.kiwify.com.br/hP20Upy)

@AprenderDados 2025
