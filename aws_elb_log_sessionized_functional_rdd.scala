import org.apache.spark.SparkConf
import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.rdd.RDD
import org.apache.spark.rdd.RDD._
import org.apache.spark.sql.functions._

// this is to get rid of winutils error (if you are running this test in Windows)
// read more at https://jaceklaskowski.gitbooks.io/mastering-apache-spark/spark-tips-and-tricks-running-spark-windows.html
System.setProperty("hadoop.home.dir", "C:\\hadoop\\")

val conf: SparkConf = new SparkConf().setMaster("local").setAppName("KhazretgaliSapenovElbLog")
val sc: SparkContext = new SparkContext(conf)

// some basic structure for our records
case class ElbLog(timestamp:String, elb:String, clientPort:String)

// path to sample log file
val dataFilePath = "C:\\test\\elb1.log"

// create RDD
val logRDD: RDD[ElbLog] = sc.textFile(dataFilePath)
  .map{ raw_line =>
  val columns = raw_line.split(" ")
  ElbLog(columns(0), columns(1), columns(2))
}.cache()

// create tuple of client ips and timestamps
val pairRdd = logRDD.map(rec => (rec.clientPort.split(":")(0), rec.timestamp))

// group by client ips and create a list of associated timestamps
val groupedbykey = pairRdd.groupByKey()

// materialize it
groupedbykey.collect().foreach(println)
