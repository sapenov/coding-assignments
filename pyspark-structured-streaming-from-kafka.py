myStreamName = "lab04a_ps"

spark.conf.set("spark.sql.shuffle.partitions", sc.defaultParallelism)

kafkaServer = "server1.databricks.training:9092" # Specify "kafka" bootstrap server

# Create our initial DataFrame
initialDF = (spark.readStream
 .format("kafka")              # Specify "kafka" as the type of the stream
 .option("kafka.bootstrap.servers", kafkaServer)              # Set the location of the kafka server
 .option("subscribe","logdata")              # Indicate which topics to listen to
 .option("startingOffsets","earliest")              # Rewind stream to beginning when we restart notebook
 .option("maxOffsetsPerTrigger", 1000)              # Throttle Kafka's processing of the streams
 .load()              # Load the input data stream in as a DataFrame
)

# TEST - Run this cell to test your solution.
initSchemaStr = str(initialDF.schema)

dbTest("SS-04-key",       True, "(key,BinaryType,true)" in initSchemaStr)
dbTest("SS-04-value",     True, "(value,BinaryType,true)" in initSchemaStr)
dbTest("SS-04-topic",     True, "(topic,StringType,true)" in initSchemaStr)
dbTest("SS-04-partition", True, "(partition,IntegerType,true)" in initSchemaStr)
dbTest("SS-04-offset",    True, "(offset,LongType,true)" in initSchemaStr)
dbTest("SS-04-timestamp", True, "(timestamp,TimestampType,true)" in initSchemaStr)
dbTest("SS-04-timestampType", True, "(timestampType,IntegerType,true)" in initSchemaStr)

print("Tests passed!")

# do some ETL stuff
from pyspark.sql.functions import col, unix_timestamp, regexp_extract

cleanDF = (initialDF
 .withColumn("value", col("value").cast("string"))  # Select the "value" column, cast "value" column to STRING
 .withColumn("ts_string", col("value").substr(14,24))  # Select the "value" column, pull substring(14, 24) from it and rename to "ts_string"
 .withColumn("epoc", unix_timestamp("ts_string",  "yyyy/MM/dd HH:mm:ss.SSS"))  # Select the "ts_string" column, apply unix_timestamp to it and rename to "epoc"
 .withColumn("capturedAt", col("epoc").cast("timestamp"))  # Select the "epoc" column and cast to a timestamp and rename it to "capturedAt"
 .withColumn("logData", regexp_extract("value", """^.*\]\s+(.*)$""", 1))  # Select the "logData" column and apply the regexp `"""^.*\]\s+(.*)$"""`
)

# TEST - Run this cell to test your solution.
schemaStr = str(cleanDF.schema)

dbTest("SS-04-schema-value",     True, "(value,StringType,true)" in schemaStr)
dbTest("SS-04-schema-ts_string",  True, "(ts_string,StringType,true)" in schemaStr)
dbTest("SS-04-schema-epoc",   True, "(epoc,LongType,true)" in schemaStr)
dbTest("SS-04-schema-capturedAt", True, "(capturedAt,TimestampType,true)" in schemaStr)
dbTest("SS-04-schema-logData",  True, "(logData,StringType,true)" in schemaStr)

print("Tests passed!")

from pyspark.sql.functions import col,length, window, when

#This is the regular expression pattern that we will use 
IP_REG_EX = """^.*\s+(\d{1,3})\.\d{1,3}\.\d{1,3}\.\d{1,3}.*$"""

ipDF = (cleanDF
 .withColumn("ip", regexp_extract(col("logData"), IP_REG_EX, 1))                                # apply regexp_extract on IP_REG_EX with value of 1 to "logData" and rename it "ip"
 .filter(length(col("ip")) > 0)                                            # keep only "ip" that have non-zero length
 .withColumn("ipClass", 
     when(col("ip")< 127, "Class A")                # figure out class of IP address based on first two octets
    .when(col("ip")== 127, "Loopback")                                        # add rest of when/otherwise clauses
    .when((col("ip") <=128) & (col("ip")>=191), "Class B")
    .when((col("ip") <=192) & (col("ip")>=223), "Class C")
    .when((col("ip") <=224) & (col("ip")>=239), "Class D")
    .when((col("ip") <= 240) & (col("ip")>=256), "Class E")
    .otherwise("Invalid"))
 .groupBy(window("capturedAt", "10 seconds").alias("time"), col("ipClass"))                  # gather in 10 second windows of "capturedAt", call them "time" and "ipClass" 
 .count()                                            # add up total
 .orderBy("ipClass")                                            # sort by IP class
       )
      
      # TEST - Run this cell to test your solution.
schemaStr = str(ipDF.schema)

dbTest("SS-04-schema-ipClass", True, "(ipClass,StringType,false)" in schemaStr)
dbTest("SS-04-schema-count",   True, "(count,LongType,false)" in schemaStr)
dbTest("SS-04-schema-start",   True, "(start,TimestampType,true)" in schemaStr)
dbTest("SS-04-schema-end",     True, "(end,TimestampType,true)" in schemaStr)

print("Tests passed!")

# TODO
display(ipDF, streamName = myStreamName)

# TEST - Run this cell to test your solution.
dbTest("SS-04-numActiveStreams", True, len(spark.streams.active) > 0)

print("Tests passed!")

for s in spark.streams.active:  # Iterate over all the active streams
  s.stop() # Stop the stream
  
 dbTest("SS-04-numActiveStreams", 0, len(spark.streams.active))

print("Tests passed!")
