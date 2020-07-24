# Libraries Included:
# Numpy, Scipy, Scikit, Pandas

""" 
I’m going to present a challenge in 3 parts, each part will get more difficult than the last. 
Getting through all 3 parts is actually pretty rare, so don’t worry if we don’t finish. 

At lark we have users who engage with our application every day. 
But sometimes they miss a day here or there. The goal here is to build a set of features representing the number of consecutive days of user-engagement. 
We’ll concentrate on the “cold-start” problem first, where we need to account for the user’s entire history. 

Part 1
To start off, we just want to know the maximum number of consecutive days a user has ever been active.

To make this easier, we’ll say that we have a set of boolean list of days representing all of time for each user. 
Every True means the user was active that day, and every False means the user was not active that day. For brevity I’ll use ‘1’ for true, and ‘0’ for false. 
E.g. [1,0,1,0,1,1,1,1,0,1] etc. Assume that the length of this vector is arbitrary. 

Write a function that takes a list of boolean values, and will calculate the longest number of consecutive days the user has been active. 
(e.g. maxConsecutiveDays(days: List[Boolean]): Int) 
"""


from typing import List
import numpy as np

def max_consecutive_days(days: List[bool]) -> int:
    is_cons = np.concatenate([0], np.equal(days, 1).view(np.int8),[0])
    d = np.abs(np.diff(is_cons))
    periods = np.where(d == 1)[0].reshape(-1,2)
    print(f"periods is {periods}")
    return periods

def max_consecutive_days_v2(days: List[bool]) -> int:
    temp_max = 0
    max_list = list()
    l = len(days) -1
    for i in range(l):
        cur = days[i]
        nxt = days[i+1]
        if nxt == cur and cur==1: # we still see consecutive occurence
            temp_max +=1
        else:
            max_list.append(temp_max+1)
            temp_max = 0   
            
        if len(max_list) == 0 and temp_max > 0:
            max_list.append(temp_max+1)            
            
    return max(max_list)   
    
print(max_consecutive_days_v2([1,1,1,0,0,0,1,1])) 
print(max_consecutive_days_v2([1,1,1,0,0,0,1,1])) 
print(max_consecutive_days_v2([1,1,1])) 
