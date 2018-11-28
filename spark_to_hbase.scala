//su - hdfs
hadoop fs -put /home/hadoop/hourly.csv /user/hadoop/khazret_dir/

import org.apache.spark.sql.types.{DateType, IntegerType, TimestampType}
import org.apache.hadoop.hbase.HBaseConfiguration
import org.apache.hadoop.hbase.client.HBaseAdmin
import org.apache.hadoop.hbase.mapreduce.TableInputFormat

import org.apache.hadoop.fs.Path
import org.apache.hadoop.hbase.HBaseConfiguration
import org.apache.hadoop.hbase.client.HBaseAdmin
import org.apache.hadoop.hbase.mapreduce.TableInputFormat
import org.apache.spark._

object HBaseLoaderEMR {
  def main(args: Array[String]) {

    val spark = org.apache.spark.sql.SparkSession.builder.master("local").appName("Spark CSV Reader").getOrCreate
    val csv = spark.read.format("csv").option("header", "true").option("mode", "DROPMALFORMED").load("hdfs:///user/hadoop/khazret_dir/hourly.csv")
    case class Recipe(recipe_id: Integer, recipe_name: String, description: String, ingredient: String, active: Boolean, updated_date: TimestampType, created_date: TimestampType )
    
    val sparkConf = new SparkConf().setAppName("HBaseTest").setMaster("local[4]")
    val sc = new SparkContext(sparkConf)

    val conf = HBaseConfiguration.create()

    val table_name="recipes"
    conf.addResource(new Path("/etc/spark/walmart/hbase/conf/hbase-site.xml"))
    conf.set(TableInputFormat.INPUT_TABLE, table_name)

    println("-------------1")
    val admin = new HBaseAdmin(conf)
    //println(admin.listTables())
    println("-------------2")
    if (admin.isTableAvailable(table_name))  println("exists")
    else println("not exists")
    println("-------------3")

    // salt a key using a modulus based approach
    def salt(key: String, modulus: Int) : String = {
      val saltAsInt = Math.abs(key.hashCode) % modulus

      // left pad with 0's (for readability of keys)
      val charsInSalt = digitsRequired(modulus)
      ("%0" + charsInSalt + "d").format(saltAsInt) + ":" + key
    }

    // number of characters required to encode the modulus in chars (01,02.. etc)
    def digitsRequired(modulus: Int) : Int = {
      (Math.log10(modulus-1)+1).asInstanceOf[Int]
    }

    // A partitioner that puts data destined for the same HBase region together
    class SaltPrefixPartitioner[K,V](modulus: Int) extends Partitioner {
      val charsInSalt = digitsRequired(modulus)

      def getPartition(key: Any): Int = {
        key.substring(0,charsInSalt).toInt
      }

      override def numPartitions: Int = modulus
    }

    // salt the keys
    val saltedRDD = sourceRDD.map(r => {
      (salt(r._1, 45), r._2)
    })

    // repartition and sort the data - HFiles want sorted data
    val partitionedRDD = saltedRDD.repartitionAndSortWithinPartitions(new SaltPrefixPartitioner(modulus))

    // cells of data for HBase
    val cells = partitionedRDD.map(r => {
      val saltedRowKey = Bytes.toBytes(r._1)
      val cellData = r._2

      // create a cell of data for HBase
      val cell = new KeyValue(
        saltedRowKey,
        Bytes.toBytes("recipe"),  // column familily
        "ingredient", // column qualifier (i.e. cell name)
        cellData)

      (new ImmutableBytesWritable(saltedRowKey), cell)
    }

    // setup the HBase configuration
    val baseConf = HBaseConfiguration.create()
    conf.set("hbase.zookeeper.quorum", "<your ZK cluster here>");

    // NOTE: job creates a copy of the conf
    val job = new Job(baseConf, "map data")
    val table = new HTable(conf, "map_data")
    // Major gotcha(!) - see comments that follow
    PatchedHFileOutputFormat2.configureIncrementalLoad(job, table);

    val conf = job.getConfiguration // important(!)

    // write HFiles onto HDFS
    cells.saveAsNewAPIHadoopFile(
      "/tmp/map_data/hfiles",
      classOf[ImmutableBytesWritable],
      classOf[KeyValue],
      classOf[PatchedHFileOutputFormat2],
      "map_data",
      conf)
  })


    sc.stop()

  }
}

/*
* val rddToSave = sc.parallelize(Seq(("1111123", "456456", "Name1"), ("22222234", "8987987", "Name2")))
*/
val columnName = ("ACCT_ID", "ACCT_NAME")
val columnFamily = ("CF", "PP")

val rdd = rddToSave.map(x => {
val key = x._1
val acct_id = x._2
val acct_name = x._3
val colNameAcctId = columnName._1
val colNameAcctName = columnName._2

val rdd = rddToSave.flatMap(x => {
  val key = x._1
  val acct_id = x._2
  val acct_name = x._3
  val colNameAcctId = columnName._1
  val colNameAcctName = columnName._2
  val colFamily = columnFamily._1

  // return a sequence of updates
  List(
    new ImmutableBytesWritable(Bytes.toBytes(key)), new KeyValue(Bytes.toBytes(key), colFamily.getBytes(), colNameAcctId.getBytes(), acct_id.getBytes())),
    new ImmutableBytesWritable(Bytes.toBytes(key)), new KeyValue(Bytes.toBytes(key), colFamily.getBytes(), colNameAcctName.getBytes(), acct_name.getBytes()))
  )

  // call repartitionAndSortWithinPartitions afterwards
})

val colFamily = columnFamily._1

val kv = new KeyValue(Bytes.toBytes(key), colFamily.getBytes(), colNameAcctId.getBytes(), acct_id.getBytes())

(new ImmutableBytesWritable(Bytes.toBytes(key)), kv)
})

rdd.saveAsNewAPIHadoopFile(pathToHFile, classOf[ImmutableBytesWritable], classOf[KeyValue],
classOf[HFileOutputFormat], conf)

val loadFfiles = new LoadIncrementalHFiles(conf)
loadFfiles.doBulkLoad(new Path(pathToHFile), hTable)
* */
