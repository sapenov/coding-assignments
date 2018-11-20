val s = "aaabbdcccccf"
val t = "a3b2d1c5f1"

// create frequency map in order
val s2 = s.distinct.toCharArray.map(x=>(x,s.count(_==x)))

// transform array of tuples into string
val s3 = s2.flatMap { t => t.productIterator.mkString("")}.mkString("")

// really simple test
if(t == s3) println("OK. Test 1 is successful.")
else {println("FAIL. Test 1 failed.")}
