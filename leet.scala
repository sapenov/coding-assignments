
val d = Map(
  'a' -> '4',
  'A' -> '4',
  'e' -> '3',
  'E' -> '3',
  'i' -> '1',
  'I' -> '1',
  'o' -> '0',
  'O' -> '0',
  's' -> '5',
  'S' -> '5',
  't' -> '7',
  'T' -> '7',
  'b' -> '5',
  'D' -> '5'
)

val n = "Let's have some fun."
val n2 = "L37'5 h4v3 50m3 fun."
val t1 = n.map(c => d.getOrElse(c,c))

val m = "C is for cookie, that’s good enough for me"
val m2 = "C 15 f0r c00k13, 7h47’5 g00d 3n0ugh f0r m3"
val t2 = m.map(c => d.getOrElse(c,c))

val p = "By the power of Grayskull!"
val p2 = "By 7h3 p0w3r 0f Gr4y5kull!"
val t3 = p.map(c => d.getOrElse(c,c))

/* Micro Test Suite */
if(n2 == t1) println("OK. Test 1 succeeded!")
else  println("FAIL. Test 1 failed!")

if(m2 == t2) println("OK. Test 2 succeeded!")
else  println("FAIL. Test 2 failed!")

if(p2 == t3) println("OK. Test 3 succeeded!")
else  println("FAIL. Test 3 failed!")
