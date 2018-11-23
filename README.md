Data Load Process Outline:

1) Estimate the total size of the data, and determine the optimal number of regions in HBase.

2) Create an empty table, pre-split on the region boundaries - here we salt our keys in a predictable manner to achieve this.

3) Use a simple custom partitioner in Spark to split the RDD to match the destination region splits.

4) Generate the HFiles using Spark and standard Hadoop libraries.

5) Load the data into HBase using the standard HBase command line bulk load tools.
