%fs head dbfs:/mnt/training/sensor-data/accelerometer/time-series-stream.json/file-0.json

from pyspark.sql.functions import window, col

inputPath = "dbfs:/mnt/training/sensor-data/accelerometer/time-series-stream.json/"

jsonSchema = "time timestamp, action string"

inputDF = (spark
  .readStream                                 # Returns an instance of DataStreamReader
  .schema(jsonSchema)                         # Set the schema of the JSON data
  .option("maxFilesPerTrigger", 1)            # Treat a sequence of files as a stream, one file at a time
  .json(inputPath)                            # Specifies the format, path and returns a DataFrame
)

countsDF = (inputDF
  .groupBy(col("action"),                     # Aggregate by action...
           window(col("time"), "1 hour"))     # ...then by a 1 hour window
  .count()                                    # For the aggregate, produce a count
  .select(col("window.start").alias("start"), # Elevate field to column
          col("count"),                       # Include count
          col("action"))                      # Include action
  .orderBy(col("start"))                      # Sort by the start time
)

myStreamName = "lesson03_ps"
display(countsDF,  streamName = myStreamName)

untilStreamIsReady(myStreamName)

# for s in spark.streams.active: # Iterate over all active streams
#   s.stop()                     # Stop the stream

# As mentioned in lesson #2, we have provided additional methods for working with streams, and in  
# this case, for dealing with the rare exceptions that may arise as a result of terminating a stream.
# Listed above is the logical equivalent to this operation.
stopAllStreams()

# changed 200 partitions to default - 8 partitions
spark.conf.set("spark.sql.shuffle.partitions", sc.defaultParallelism)

# see the effect of change
display(countsDF,  streamName = myStreamName)

untilStreamIsReady(myStreamName)
stopAllStreams()


# optimized code


watermarkedDF = (inputDF
  .withWatermark("time", "2 hours")             # Specify a 2-hour watermark
  .groupBy(col("action"),                       # Aggregate by action...
           window(col("time"), "1 hour"))       # ...then by a 1 hour window
  .count()                                      # For each aggregate, produce a count
  .select(col("window.start").alias("start"),   # Elevate field to column
          col("count"),                         # Include count
          col("action"))                        # Include action
  .orderBy(col("start"))                        # Sort by the start time
)

display(watermarkedDF, streamName = myStreamName) # Start the stream and display it

untilStreamIsReady(myStreamName)
stopAllStreams()
