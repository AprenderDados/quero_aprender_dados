# Adventure Works Data Project

**Created by:** Bernardo Cambruzzi
**Last updated:** 3 days ago

## Objetivo

Criar um projeto de Data Analytics para uma empresa de retail.

## O que vamos fazer

- [X] Construir uma arquitetura de dados na Azure
- [X] Construir um Lakehouse
- [X] Desenvolver um projeto similar ao de grandes empresas de comércio/retail
- [X] Implementar um projeto de Analytics para BI e Machine Learning

## Ferramentas

- [ ] Databricks
- [ ] Azure Data Lake Storage (ADLS)
- [ ] Azure Data Factory (ADF)
- [ ] Microsoft PowerBI
- [ ] CI/CD
- [ ] Processos e cultura de engenharia de dados

## Fases do Projeto

- [ ] **V1** - Ingestão simples, full load, projeto de ponta a ponta
- [ ] **V2** - Ingestão incremental, Workflows
- [ ] **V3** - Unity Catalog, Delta Live Tables
- [ ] **V4** - CI/CD
- [ ] **V5** - Custos, Governança e Produto (visualização)

## Setup

- [ ] Criar Subscription na Azure
- [ ] Integrar recursos da Azure
  - [ ] Grupo de Recursos
  - [ ] Databricks
  - [ ] ADLS
  - [ ] Azure Data Factory (ADF)
  - [ ] ADF + ADLS
  - [ ] ADF + Databricks
  - [ ] ADF + Fonte de Dados (BASE SQL da Aprender Dados)
  - [ ] Extrair dados com ADF

## Base de Dados

- [ ] Base de dados Adventure Works no Azure SQL
- [ ] Configurar Linked Services, Datasets e Pipelines
- [ ] Implementar Ingestão com Metadados
  - [ ] Criar Tabela de controle
  - [ ] Loop nos metadados
  - [ ] Abordagem com pipeline para customização

## Configurações e Permissões

- [ ] Montar o Data Lake
- [ ] Criar App Registration
- [ ] Configurar Permissões e Planejamento dos Diretórios
- [ ] Configurar Key Vault
  - [ ] Criar recursos na Azure
  - [ ] Definir permissões de usuário e políticas de acesso
  - [ ] Criar segredos/senhas
- [ ] Configurar Databricks Secrets
  - [ ] Criar um escopo de Segredos do Databricks
  - [ ] Integrar com o Azure Key Vault
  - [ ] Armazenar e testar segredos

## Camada Bronze

- [ ] Criar Databases do Databricks (formato delta)
  - [ ] Managed -> Controlado pelo Databricks
  - [ ] External -> Lê um caminho do data lake
- [ ] Fazer ingestão de arquivos
  - [ ] Ler e transformar dados (se necessário)
  - [ ] Salvar como Delta
  - [ ] Orquestrar Extração + Ingestão
- [ ] Integrar Atividades do ADF + ADB
- [ ] Refatorar notebooks e pipelines para uso com parâmetros

## Camada Prata

- [ ] Criar Database no Hive Metastore (managed)
- [ ] Contextualização dos projetos e exemplos em SQL e PySpark
- [ ] Definir Regras de Qualidade de Dados e Framework
  - [ ] Módulos de reaproveitamento
  - [ ] Adicionar pasta de git
- [ ] Priorização das tabelas
  - [ ] Definir tabelas de vendas e produtos
  - [ ] Criar cadernos de configuração e transformação
  - [ ] Aplicar lógica com PySpark (Where/filter, Quality Checks, Deduplicate)
- [ ] Salvar tabelas com opções de Upsert e Full Load

## Camada Ouro

- [X] Abordagem de ETL em SQL e PySpark
- [X] Criar ETL para Analytics e Machine Learning
- [X] Implementar camada Ouro
- [X] Entender e aplicar conceitos importantes

  - [X] Conhecimento básico de GitHub
  - [X] Aplicação de frameworks (Read, Transform, Write)
- [X] Qualidade, Análise de Dados e debugar no Databricks
- [ ] Orquestração com ADF e Databricks Workflows
- [ ] Governança e acesso pelo PowerBI

## Governança e Automação

- [ ] ADF Pipelines e ADB Workflows para automação
- [ ] Implementar SQL Serverless e compartilhamento de dados
- [ ] Monitoramento de Pipelines e Data Quality no Databricks
- [ ] Configurar Unity Catalog para governança

## Avançado

- [ ] Planejamento e Gerenciamento de Custos
- [ ] Configurar Azure DevOps para CI/CD
- [ ] Implementar Delta Live Tables
