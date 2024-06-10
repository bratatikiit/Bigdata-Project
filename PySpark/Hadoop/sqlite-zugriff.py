from pyspark.sql import SparkSession

# Erstellen einer SparkSession mit JDBC-Treiberpfad
spark = SparkSession.builder \
    .appName("SQLite Access with PySpark") \
    .config("spark.jars", "/opt/spark/jars/sqlite-jdbc-3.45.1.0.jar") \
    .getOrCreate()

# Verbindung zur SQLite-Datenbank
db_path = "/home/alfa/Dokumente/sqlite.db"
table_name = "customers"

jdbc_url = f"jdbc:sqlite:{db_path}"

# Lesen einer Tabelle aus der SQLite-Datenbank
df = spark.read.format("jdbc") \
    .option("url", jdbc_url) \
    .option("dbtable", table_name) \
    .load()

# Zeige die ersten Zeilen der DataFrame
df.show()

# Schließe die SparkSession
spark.stop()
