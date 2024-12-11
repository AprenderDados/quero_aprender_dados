# Criando um Produto de Análise de Vendas na Internet Utilizando um Lakehouse na Azure com Databricks

## Cenário

Imagine a Adventure Works, uma empresa de artigos esportivos que principalmente vende bicicletas.

A empresa coleta grandes volumes de dados de transações de vendas em seu banco de dados OLTP (Online Transaction Processing).

Este banco de dados é excelente para operações diárias, como inserção e atualização de registros, mas não é ideal para análises complexas e relatórios históricos.

Para obter insights valiosos e melhorar a tomada de decisões, a Adventure Works decide transformar seus dados OLTP em um Data Warehouse (DW) utilizando uma arquitetura de Lakehouse com Databricks na Azure.

## Arquitetura Lakehouse na Azure com Databricks

A arquitetura de Lakehouse combina os melhores aspectos dos Data Lakes e Data Warehouses.

No Azure, isso pode ser alcançado utilizando o Azure Data Lake Storage (ADLS) para armazenar grandes volumes de dados em seu formato bruto e o Databricks para transformar e analisar esses dados.

### Componentes Principais

1. **Azure Data Lake Storage (ADLS)**: Armazena dados brutos, semi-estruturados e estruturados.
2. **Azure Databricks**: Processa grandes volumes de dados, executa transformações complexas e armazena dados estruturados no formato Delta Lake.
3. **Azure Data Factory**: Orquestra a movimentação e transformação de dados entre diferentes serviços.
4. **Power BI**: Cria relatórios e dashboards interativos.

## Processo de Transformação

### 1. Extração de Dados do OLTP

Utilizamos o Azure Data Factory para extrair dados das tabelas do banco OLTP. As tabelas de interesse incluem:

- `Sales.SalesOrderHeader`
- `Sales.SalesOrderDetail`
- `Production.Product`
- `Production.ProductSubcategory`
- `Production.ProductModel`
- `Production.ProductDescription`
- `Sales.Customer`
- `Sales.SpecialOffer`
- `Sales.Currency`
- `Sales.SalesTerritory`
- `Sales.SalesReason`
- `Person.Address`
- `Person.Person`
- `Person.EmailAddress`
- `Person.PersonPhone`
- `Person.StateProvince`
- `Person.CountryRegion`

### 2. Armazenamento no Data Lake

Os dados extraídos são armazenados no Azure Data Lake Storage em seu formato bruto. Isso garante que os dados originais estejam disponíveis para qualquer necessidade futura.

### 3. Transformação dos Dados com Databricks

Usamos o Databricks para transformar os dados brutos em informações estruturadas e otimizadas para análise. Aplicamos regras de limpeza, transformação e agregação para preparar os dados para o Data Warehouse, utilizando o Delta Lake para armazenamento eficiente.

#### Camadas de Dados

##### Camada Bronze

A camada Bronze é a primeira camada no Data Lakehouse.

- **Propósito**: Armazenar uma cópia dos dados brutos.
- **Formato**: Convertido para o formato Delta para facilitar a leitura e a eficiência.
- **Conteúdo**: Dados exatamente como foram extraídos da fonte, sem qualquer processamento ou limpeza.

##### Camada Prata

A camada Prata é onde começamos a processar e limpar os dados.

- **Propósito**: Aplicar regras de qualidade e limpeza aos dados.
- **Transformações**:
  - **Validação de Schema**: Garantir que os dados estejam no formato esperado.
  - **Checks de Qualidade**: Verificar inconsistências e valores ausentes.
  - **Deduplicação**: Remover registros duplicados para garantir a singularidade dos dados.
- **Resultado**: Dados limpos e validados prontos para análise mais profunda e criação de modelos.

##### Camada Ouro

A camada Ouro é onde criamos nosso produto final para análise.

- **Propósito**: Recriar as tabelas do Data Warehouse (DW) com dados prontos para consumo analítico.
- **Transformações**:
  - **Agregações**: Resumir dados conforme necessário para análises.
  - **Modelagem de Dados**: Estruturar os dados em tabelas dimensionais e de fatos.
  - **Enriquecimento de Dados**: Combinar dados de diferentes fontes e camadas para criar uma visão completa e rica.
- **Resultado**: Tabelas otimizadas para consultas analíticas, prontas para serem consumidas pelo Power BI e outras ferramentas de BI.

### 4. Carregamento no Data Warehouse com Delta Lake

Os dados transformados são armazenados no Delta Lake no Azure Databricks. Criamos as tabelas dimensionais e de fatos conforme a necessidade analítica da empresa.

### 5. Criação de Relatórios e Dashboards

Com os dados estruturados no Data Warehouse, utilizamos o Power BI para criar relatórios e dashboards interativos que fornecem insights valiosos sobre as vendas pela internet.

## Produto de Análise de Vendas pela Internet

### Objetivo

Desenvolver um produto de análise de vendas pela internet que permite à empresa entender melhor o comportamento dos clientes, desempenho dos produtos e efetividade das promoções.

### Tabelas Chave

1. **FactInternetSales**: Contém informações detalhadas sobre cada venda realizada pela internet.
2. **FactInternetSalesReason**: Contém informações sobre as razões das vendas realizadas pela internet.
3. **DimCustomer**: Contém informações detalhadas sobre os clientes.
4. **DimProduct**: Contém informações detalhadas sobre os produtos.
5. **DimPromotion**: Contém informações detalhadas sobre as promoções.
6. **DimSalesTerritory**: Contém informações sobre os territórios de vendas.
7. **DimCurrency**: Contém informações sobre as moedas.
8. **DimDate**: Contém informações sobre as datas.
9. **DimSalesReason**: Contém informações sobre as razões das vendas.
10. **DimGeography**: Contém informações sobre a geografia.

### Relatórios e Dashboards

- **Análise de Vendas**: Total de vendas, quantidade de produtos vendidos, valor médio das vendas, etc.
- **Análise de Clientes**: Número de novos clientes, retenção de clientes, segmentação de clientes, etc.
- **Análise de Produtos**: Produtos mais vendidos, produtos com maior margem de lucro, etc.
- **Análise de Promoções**: Eficácia das promoções, impacto das promoções nas vendas, etc.
- **Análise Geográfica**: Desempenho de vendas por região, país, cidade, etc.

### Exemplo de Dashboard no Power BI

O dashboard deve incluir gráficos interativos, como gráficos de barras, gráficos de linhas e mapas, para fornecer uma visão clara e intuitiva do desempenho das vendas.

## Conclusão

Transformar dados de um banco OLTP para um Data Warehouse utilizando a arquitetura de Lakehouse com Databricks na Azure permite uma análise de dados mais eficiente e eficaz. Com a capacidade de processar e analisar grandes volumes de dados, a empresa pode obter insights valiosos para melhorar suas estratégias de vendas e operações, resultando em um melhor desempenho geral.

---

Este documento serve como um guia para entender o processo de transformação de dados de um banco OLTP para um Data Warehouse, utilizando ferramentas e serviços da Azure com Databricks. Se tiver alguma dúvida ou precisar de mais detalhes, sinta-se à vontade para perguntar!
