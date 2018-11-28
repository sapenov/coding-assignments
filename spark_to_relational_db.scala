// Spark 2.0 and up
val dbStr = "jdbc:mysql://[host1][:port1][,[host2][:port2]]...[/[database]]"

spark
  .read
    .format("csv")
    .option("header", "true")
    .load("some/path/to/file.csv")
  .write
    .mode("overwrite")
    .jdbc(dbStr, tablename, props)
    
 
// more realistically files will be in HDFS, so one line has to be changed

val dbStr = "jdbc:mysql://[host1][:port1][,[host2][:port2]]...[/[database]]"

spark
  .read
    .format("csv")
    .option("header", "true")
    .load("hdsf://some/path/to/file.csv")
  .write
    .mode("overwrite")
    .jdbc(dbStr, tablename, props)
   
