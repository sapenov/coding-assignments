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
// and format values to get rid of microseconds
val pairRdd = logRDD.map(rec => (rec.clientPort.split(":")(0), rec.timestamp.split('.')(0)))

// group by client ips and create a list of associated timestamps
val groupedbykey = pairRdd.groupByKey()

// materialize it
groupedbykey.collect().foreach(println)

/*
The results should look like this

(176.43.114.180,CompactBuffer(2015-11-07T18:45:35))
(188.3.115.162,CompactBuffer(2015-11-07T18:45:33, 2015-11-07T18:45:33, 2015-11-07T18:45:35, 2015-11-07T18:45:35, 2015-11-07T18:45:35))
(95.13.166.72,CompactBuffer(2015-11-07T18:45:33, 2015-11-07T18:45:33, 2015-11-07T18:45:33, 2015-11-07T18:45:34))
(88.232.134.216,CompactBuffer(2015-11-07T18:45:35))
(95.15.104.165,CompactBuffer(2015-11-07T18:45:36))
(212.252.57.107,CompactBuffer(2015-11-07T18:45:35, 2015-11-07T18:45:36, 2015-11-07T18:45:37))
(176.219.169.34,CompactBuffer(2015-11-07T18:45:37))
(88.228.23.45,CompactBuffer(2015-11-07T18:45:33, 2015-11-07T18:45:34))
(85.97.200.138,CompactBuffer(2015-11-07T18:45:34))
(88.252.222.143,CompactBuffer(2015-11-07T18:45:37))
(78.172.82.113,CompactBuffer(2015-11-07T18:45:36))
(159.146.55.94,CompactBuffer(2015-11-07T18:45:36))
*/
