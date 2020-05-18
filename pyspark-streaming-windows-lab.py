myStreamName = "lab03_ps"
path = "dbfs:/mnt/training/asa/flights/2007-01-stream.parquet/part-00000-tid-9167815511861375854-22d81a30-d5b4-43d0-9216-0c20d14c3f54-178-c000.snappy.parquet"
df = spark.read.parquet(path)
display(df)
