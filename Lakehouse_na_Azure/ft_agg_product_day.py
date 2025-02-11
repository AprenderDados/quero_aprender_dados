# Databricks notebook source
# MAGIC %run "/Workspace/AdventureWorks_Lakehouse/AdventureWorks/src/utils/common_functions"

# COMMAND ----------

from pyspark.sql import DataFrame, Window
from pyspark.sql import functions as F
from pyspark.sql.types import (
    IntegerType, StringType, DateType, DecimalType, StructType, StructField
)

# COMMAND ----------

# Informações da Tabela Destino (target)
target_table_name = "ft_agg_product_day"
target_database = "adventure_works_ouro"
target_table = f"{target_database}.{target_table_name}"

# Informações das Tabelas Fonte
sales_order_header_df = spark.read.table("adventure_works_prata.sales_salesorderheader")
sales_order_detail_df = spark.read.table("adventure_works_prata.sales_salesorderdetail")
product_df = spark.read.table("adventure_works_prata.production_product")
product_subcategory_df = spark.read.table("adventure_works_prata.production_productsubcategory")
product_category_df = spark.read.table("adventure_works_prata.production_productcategory")

# COMMAND ----------

expected_schema = StructType([
    StructField("ProductID", IntegerType(), False),
    StructField("OrderDate", DateType(), False),
    StructField("TotalOrderQty", IntegerType(), False),
    StructField("TotalLineTotal", DecimalType(19, 4), False),
    StructField("ProductName", StringType(), False),
    StructField("ProductCategoryName", StringType(), False),
    StructField("ProductSubcategoryName", StringType(), False)
])

# COMMAND ----------

def transform_ft_agg_product_day(
    fact_internet_sales_df: DataFrame,
    dim_product_df: DataFrame
) -> DataFrame:
    '''
    Transformação da tabela: ft_agg_product_day
    '''

    # Join das tabelas de fatos e produtos
    join_df = (
        fact_internet_sales_df.alias("fis")
        .join(dim_product_df.alias("dp"), F.col("fis.ProductKey") == F.col("dp.ProductKey"), "left")
    )

    # Seleção inicial para garantir propagação correta do alias
    selected_df = join_df.select(
        F.col("fis.ProductKey").alias("ProductKey"),
        F.to_date("fis.OrderDateKey").alias("OrderDate"),
        F.col("fis.OrderQty"),
        F.col("fis.LineTotal"),
        F.col("dp.ProductName"),
        F.col("dp.CategoryName").alias("ProductCategoryName"),
        F.col("dp.SubcategoryName").alias("ProductSubcategoryName")
    )

    # Agregação por dia e produto
    agg_df = (selected_df
        .groupBy("ProductKey", "OrderDate", "ProductName", "ProductCategoryName", "ProductSubcategoryName")
        .agg(
            F.sum("OrderQty").alias("TotalOrderQty"),
            F.sum("LineTotal").alias("TotalLineTotal")
        )
    )

    return agg_df

# Executar a transformação
transformed_df = transform_ft_agg_product_day(
    fact_internet_sales_df=spark.read.table("adventure_works_ouro.factinternetsales"),
    dim_product_df=spark.read.table("adventure_works_ouro.dimproduct")
)

# Mostrar o DataFrame final
display(transformed_df)

# Escrever a tabela agregada no Delta Lake
transformed_df.write.format('delta').mode('overwrite').option('overwriteSchema', 'true').saveAsTable("adventure_works_ouro.ft_agg_product_day")


# COMMAND ----------

# Executar a transformação
transformed_df = transform_ft_agg_product_day(
    sales_order_header_df=sales_order_header_df,
    sales_order_detail_df=sales_order_detail_df,
    product_df=product_df,
    product_subcategory_df=product_subcategory_df,
    product_category_df=product_category_df
)

display(transformed_df)

# COMMAND ----------

# Validação do schema usando a função _validate_schema
from utils.common_functions import _validate_schema

if _validate_schema(transformed_df, expected_schema):
    print("Schema validado com sucesso.")
else:
    raise Exception("Falha na validação do schema.")

# COMMAND ----------

# Escreve a tabela agregada no banco de dados como uma tabela Delta
transformed_df.write.format('delta').mode('overwrite').option('overwriteSchema', 'true').saveAsTable(target_table)

# COMMAND ----------

print(f"Tabela agregada '{target_table}' criada com sucesso!")

