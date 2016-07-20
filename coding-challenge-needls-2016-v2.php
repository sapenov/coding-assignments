<?php
// set constants
define("PAUSED",'Settings::CAMPAIGN_STATUS_PAUSED'); 
define("RUNNING",'Settings::CAMPAIGN_STATUS_RUNNING'); 
define("COMPLETE",'Settings::CAMPAIGN_STATUS_COMPLETE'); 



/**
* Description:
*
*@param1 int
*@param2 string
*@param3 boolean
*@return object with 
*/
function getStats($arr,$metric, $StartDate, $EndDate)
{
	### Define time boundaries
	$track = [];
	$track['on']=0;
	$track['off']=0;
	$track['on_count']=0;
	$track['off_count']=0;

	### Loop through the log, testing invariants
	
	foreach ($arr as $k=>$v) 
	{
		$prev=$arr[$k-1];
		$cur = $v;
		$next =$arr[$k+1];
		
		
		if($prev==null) //first element
		{		
			if(isset($StartDate) && $StartDate > $cur['date']) // lower boundary cutoff
			{
				$lower_boundary =$StartDate;		
			}		
			else 
			{
				$lower_boundary = $cur['date'];	
			}

			$ptime = $next['date'] - $lower_boundary;
		}
		elseif( $next ==null)// last item
		{
			if(isset($EndDate) && $EndDate > $cur['date']) // lower boundary cutoff
			{
				$upper_boundary = $EndDate;
				//$upper_boundary = $cur['date'];		
				print 1; print "\$EndDate=$EndDate";
			}	
			elseif(isset($EndDate) && $EndDate < $cur['date'])
			{
				$upper_boundary = $cur['date'];		
			}
			elseif($cur['newState']==RUNNING)
			{
				$upper_boundary =time(); 
			}
		  $ptime = $upper_boundary - $cur['date'];
		}
		else{
			$ptime = $next['date'] - $cur['date']; 
		}

	

		if($cur['newState']==PAUSED && $next['newState']==RUNNING)
		{
			$track['off'] += $ptime;
			$track['off_count']++;	
		}
		elseif($cur['newState']==PAUSED && $next['newState']==null)
		{
			$track['off'] += $ptime;
			$track['off_count']++;	
		}
		elseif($cur['newState']==PAUSED && $next['newState']==PAUSED)
		{
			$track['off'] += $ptime;
			$track['off_count']++;	
		}
		elseif($cur['newState']==RUNNING && $next['newState']==PAUSED)
		{
			$track['on'] += $ptime;		
			$track['on_count']++;
		}
		elseif($cur['newState']==RUNNING && $next['newState']==RUNNING)
		{
			$track['on'] += $ptime;		
			$track['on_count']++;
		}
		elseif($cur['newState']==RUNNING && $next['newState']==null)
		{
			$track['on'] += $ptime;		
			$track['on_count']++;	
		}
		elseif($cur['newState']==null && $next['newState']==PAUSED)
		{
			$track['off'] += $ptime;
			$track['off_count']++;	
		}
		elseif($cur['newState']==null && $next['newState']==RUNNING)
		{
			$track['off'] += $ptime;
			$track['off_count']++;	
		}
		elseif($cur['newState']==null && $next['newState']==null)
		{
			$track['off'] += $ptime;
			$track['off_count']++;	
		}
		else 
		{
			$track['missed'] +=1;
		}

	}

	return $track;
	
}//end func



/**
* Description:
*
*@arr - multidimensional array
*@key_name - the field to sort on (has to be integer)
*@direction - ASC or DESC (TODO)
*@return array sorted 
*/
function insertionSort($arr,$key_name, $direction)
{
	$length=count($arr);
	if($length>1)
	{
		for ($i = 1; $i < $length;$i++)
	{
		$x =$arr[$i][$key_name];
		$j = $i - 1;
		$element= $arr[$i];	
		while( $j >= 0 && $arr[$j][$key_name] > $x)
			{
				$arr[$j+1] = $arr[$j];
				$j = $j - 1;		
			}
		 $arr[$j+1] = $element;
	}
		
	}
		
	return $arr;
}//end func

?>