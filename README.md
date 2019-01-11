
How to sessionize ELB log file in Spark and Scala

I can see three approaches to sessionize ELB logs file :

1) Using purely functional operations on RDD
2) Using relational operations on DataFrame (which is really a Dataset)
3) Using relational operations on DataSets

Typically AWS ELB file has following fields, separated by whitespace:
// timestamp elb client:port backend:port request_processing_time backend_processing_time
// response_processing_time elb_status_code backend_status_code received_bytes
// sent_bytes "request" "user_agent" ssl_cipher ssl_protocol

I'll put a sample file called elb1.log in the repo for your review.

