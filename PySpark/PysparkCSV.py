#Imports
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit

from pyspark.sql.types import StructType,StructField 
from pyspark.sql.types import StringType, IntegerType, ArrayType

# Create SparkSession 
spark = SparkSession.builder \
      .master("local[1]") \
      .appName("meinSparkCSV") \
      .getOrCreate() 

df = spark.read.csv("/axel/all_us_zipcodes.csv")
print(df.printSchema())
print(df.show())
