<?php
// set constants
define("PAUSED",'Settings::CAMPAIGN_STATUS_PAUSED'); 
define("RUNNING",'Settings::CAMPAIGN_STATUS_RUNNING'); 
define("COMPLETE",'Settings::CAMPAIGN_STATUS_COMPLETE'); 

include('coding-challenge-needls-2016-v2.php');

### Sort array ascending by timestamp

print "<h3>Test 1</h3>

<p>StartDate: null
<p>StopDate: null

<p>Expected Answer: 0
";

$d1 = new DateTime('2015-10-15 00:00:00');
$t1 = $d1->getTimestamp();

$statusLog = array(
array(

'date' => $t1,

'oldState' => null,

'newState' => PAUSED

)

);

$sorted =  insertionSort($statusLog,'date', $direction); //
var_dump($sorted);

$stats = getStats($sorted, RUNNING,null, null);
var_dump($stats);
if($stats['on']==0){
	print"<div style=\"background-color:green;color:white;padding:20px;\">Test 1 Passed</div>";
}
else{
	print"<div style=\"background-color:red;color:white;padding:20px;\">Test 1 Failed</div>";
}

##############################
print "<h3>Test 2</h3>

<p>StartDate: date(\"U\", strtotime(\"next week\"))
<p>StopDate: null
<p>Expected Answer: 0
";
$d1 = new DateTime('2015-10-15 00:00:00');
$t1 = $d1->getTimestamp();
$statusLog2 = array(

array('date' =>$t1 ,

'oldState' => null,

'newState' => PAUSED

)

);

$sorted2 =  insertionSort($statusLog2,'date', $direction); //
var_dump($sorted2);
$sdate=date("U", strtotime("next week"));
$stats = getStats($sorted2, RUNNING,$sdate, null);
var_dump($stats);

if($stats['on']==0){
	print"<div style=\"background-color:green;color:white;padding:20px;\">Test 2 Passed</div>";
}
else{
	print"<div style=\"background-color:red;color:white;padding:20px;\">Test 2 Failed</div>";
}
########################################
print "<h3>Test 3</h3>

<p>StartDate: null
<p>StopDate: null
<p>Expected Answer: Answer: time() ­ date(\"U\", strtotime(\"2015­10­16\"));
";

$d1 = new DateTime('2015-10-15 00:00:00');
$t1 = $d1->getTimestamp();

$d2 = new DateTime('2015-10-15 00:00:00');
$t2 = $d2->getTimestamp();
$statusLog3 = array(

array(

'date' => $t1,

'oldState' => null,

'newState' => PAUSED

),

array(

'date' => $t2,

'oldState' => PAUSED,

'newState' => RUNNING

)

);

$sorted3 =  insertionSort($statusLog3,'date', $direction); //
var_dump($sorted3);

$stats = getStats($sorted3, RUNNING,null, null);
var_dump($stats);

$a=time();
$b = new DateTime('2015-10-15 00:00:00');
$b2 = $b->getTimestamp();
$c=$a - $b2;
if($stats['on']==$c){
	print"<div style=\"background-color:green;color:white;padding:20px;\">Test 3 Passed</div>";
}
else{
	print"<div style=\"background-color:red;color:white;padding:20px;\">Test 3 Failed ($c)</div>";
}



###################################
print "<h3>Test 4</h3>

<p>StartDate: null
<p>StopDate: null
<p>Expected Answer: time() ­ date(\"U\", strtotime(\"2015­10­18\")) + (24 * 60 * 60);
";
$d1 = new DateTime('2015-10-15 00:00:00');
$t1 = $d1->getTimestamp();
$d2 = new DateTime('2015-10-16 00:00:00');
$t2 = $d2->getTimestamp();
$d3 = new DateTime('2015-10-17 00:00:00');
$t3 = $d3->getTimestamp();
$d4 = new DateTime('2015-10-18 00:00:00');
$t4 = $d4->getTimestamp();


$statusLog4 = array(

array(

'date' => $t1,

'oldState' => null,

'newState' => PAUSED

),

array(

'date' => $t2,

'oldState' => PAUSED,

'newState' =>RUNNING

),

array(

'date' => $t3,

'oldState' => RUNNING,

'newState' => PAUSED

),

array(

'date' => $t4,

'oldState' => PAUSED,

'newState' => RUNNING

),

);


$sorted4 =  insertionSort($statusLog4,'date', $direction); //
var_dump($sorted4);

$stats = getStats($sorted4, RUNNING,null, null);
var_dump($stats);

$a=time();
$b = new DateTime('2015-10-18 00:00:00');
$b1 = $b->getTimestamp() + (24 * 60 * 60);
$c=$a - $b1;

if($stats['on']==$c){
	print"<div style=\"background-color:green;color:white;padding:20px;\">Test 4 Passed</div>";
}
else{
	print"<div style=\"background-color:red;color:white;padding:20px;\">Test 4 Failed ($c)</div>";
}


#############################
print "<h3>Test 5</h3>

<p>StartDate: null
<p>StopDate: null
<p>Expected Answer: time() ­ date(\"U\", strtotime(\"2015­10­19\")) + (24 * 60 * 60 * 1.5);
";
$d1 = new DateTime('2015-10-15 00:00:00');
$t1 = $d1->getTimestamp();
$d2 = new DateTime('2015-10-16 00:00:00');
$t2 = $d2->getTimestamp();
$d3 = new DateTime('2015-10-17 00:00:00');
$t3 = $d3->getTimestamp();
$d4 = new DateTime('2015-10-18 00:00:00');
$t4 = $d4->getTimestamp();

$d5 = new DateTime('2015-10-18 12:00:00');
$t5 = $d5->getTimestamp();

$d6 = new DateTime('2015-10-19 00:00:00');
$t6 = $d6->getTimestamp();

$statusLog5 = array(

array(

'date' =>$t1,

'oldState' => null,

'newState' => PAUSED

),

array(

'date' => $t2,

'oldState' => PAUSED,

'newState' => RUNNING

),

array(

'date' => $t3,

'oldState' => RUNNING,

'newState' => PAUSED

),

array(

'date' => $t4,

'oldState' => PAUSED,

'newState' => RUNNING

),

array(

'date' => $t5,

'oldState' => RUNNING,

'newState' => PAUSED

),

array(

'date' => $t6,

'oldState' => PAUSED,

'newState' => RUNNING

),

);


$sorted5 =  insertionSort($statusLog5,'date', $direction); //
var_dump($sorted5);

$stats = getStats($sorted5, RUNNING,null, null);
var_dump($stats);

$a=time();
$b = new DateTime('2015-10-19 00:00:00');
$b1 = $b->getTimestamp()+ (24 * 60 * 60 * 1.5);

$c=$a - $b1;
if($stats['on']==$c){
	print"<div style=\"background-color:green;color:white;padding:20px;\">Test 5 Passed</div>";
}
else{
	print"<div style=\"background-color:red;color:white;padding:20px;\">Test 5 Failed ($c)</div>";
}


#############################
print "<h3>Test 6</h3>

<p>StartDate: null
<p>StopDate: null
<p>Expected Answer:  (24 * 60 * 60 * 2.5);
";

$d1 = new DateTime('2015-10-15 00:00:00');
$t1 = $d1->getTimestamp();
$d2 = new DateTime('2015-10-16 00:00:00');
$t2 = $d2->getTimestamp();
$d3 = new DateTime('2015-10-17 00:00:00');
$t3 = $d3->getTimestamp();
$d4 = new DateTime('2015-10-18 00:00:00');
$t4 = $d4->getTimestamp();

$d5 = new DateTime('2015-10-18 12:00:00');
$t5 = $d5->getTimestamp();

$d6 = new DateTime('2015-10-19 00:00:00');
$t6 = $d6->getTimestamp();
$d7 = new DateTime('2015-10-20 00:00:00');
$t7 = $d7->getTimestamp();

$statusLog6 = array(

array(

'date' => $t1,

'oldState' => null,

'newState' => PAUSED

),

array(

'date' => $t2,

'oldState' => PAUSED,

'newState' => RUNNING

),

array(

'date' => $t3,

'oldState' => RUNNING,

'newState' => PAUSED

),

array(

'date' => $t4,

'oldState' => PAUSED,

'newState' => RUNNING

),

array(

'date' => $t5,

'oldState' => RUNNING,

'newState' => PAUSED

),

array(

'date' => $t6,

'oldState' => PAUSED,

'newState' => RUNNING

),

array(

'date' => $t7,

'oldState' => RUNNING,

'newState' => PAUSED

)

);
//var_dump($statusLog6);

$sorted6 =  insertionSort($statusLog6,'date', $direction); //
var_dump($sorted6);

$stats = getStats($sorted6, RUNNING,null, null);
var_dump($stats);

$c=24 * 60 * 60 * 2.5;
if($stats['on']==$c){
	print"<div style=\"background-color:green;color:white;padding:20px;\">Test 6 Passed</div>";
}
else{
	print"<div style=\"background-color:red;color:white;padding:20px;\">Test 6 Failed ($c)</div>";
}

#############################
print "<h3>Test 7</h3>

<p>StartDate: null
<p>StopDate: date(\"U\", strtotime(\"2015­10­15\"))
<p>Expected Answer:  24 * 60 * 60;
";

$d1 = new DateTime('2015-10-13 00:00:00');
$t1 = $d1->getTimestamp();
$d2 = new DateTime('2015-10-14 00:00:00');
$t2 = $d2->getTimestamp();


$statusLog7 = array(

array(

'date' => $t1,

'oldState' => null,

'newState' => PAUSED

),

array(

'date' => $t2,

'oldState' => PAUSED,

'newState' => RUNNING

)

);


$d3 = new DateTime('2015-10-15 00:00:00');
$t3 = $d3->getTimestamp();

$sorted7 =  insertionSort($statusLog7,'date', $direction); //
var_dump($sorted7);

$stats = getStats($sorted7, RUNNING,null, $t3);
var_dump($stats);

$c=24 * 60 * 60;
if($stats['on']==$c){
	print"<div style=\"background-color:green;color:white;padding:20px;\">Test 7 Passed</div>";
}
else{
	print"<div style=\"background-color:red;color:white;padding:20px;\">Test 7 Failed ($c)</div>";
}
?>