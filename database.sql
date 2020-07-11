// Monthly Customer Report
// Write a query to show the number of customer accounts created, number of orders placed, and total order amount per month.
// variant 1
WITH TABLE1 AS(
SELECT
		date_trunc(‘month’ , o. ord_date) AS month,  
COUNT(DISTINCT o.ord_id) AS num_orders,
		SUM(o.amount) AS total_amount	,
FROM orders o
GROUP BY date_trunc(‘month’ , o. ord_date) 
), table2 AS(
	SELECT date_trunc(‘month’, c.created_at) month, COUNT(DISTINCT c.id) AS num_customers
	From customers
	GROUP BY date_trunc(‘month’ , o. ord_created_at) 
) SELECT t1.month, COALESCE(t2.num_customers, 0) , t1.num_orders, t2.total_amount
FROM table1 t1 
LEFT JOIN table2 t2
ON t1.month = t2.month

// variant 2

select 
c.month, 
num_customers, 
num_orders, 
order_amt 
from (
	select 
	month(created_at) as month, 
	count(id) as num_customers 
	from customers group by month 
) c 
inner join ( 
	select 
	month(ord_date) as month, 
	count(distinct ord_id) as num_orders, 
	sum(amount) as order_amt 
	from orders group by month 
) o 
on c.month = o.month

// Conversations Distribution
/*
We have a table that represents the total number of messages sent between two users by date on messenger.

1. What are some insights that could be derived from this table?

2. What do you think the distribution of the number of conversations created by each user per day looks like?

3. Write a query to get the distribution of the number of conversations created by each user by day in the year 2020.
*/

SELECT num_conversations, COUNT(*) AS frequency
FROM (
    SELECT user1, DATE(created_at), COUNT(DISTINCT user2) AS num_conversations
    FROM messages
    WHERE YEAR(date) = '2020'
    GROUP BY 1
) AS t
GROUP BY 1

// Manager Team Sizes
// Write a query to identify managers with the biggest team size.
WITH t AS(
SELECT 
	m.id AS manager_id,
	m.name AS manager_name,
       COUNT(DISTINCT e.id)  AS total_employees
FROM
	Employees m
LEFT JOIN
	Managers m
ON 
	m.id = e.manager_id
AND
	m.id IS NOT NULL
GROUP BY m.id
) SELECT  manager_id, manager_name FROM t ORDER BY total_employees DESC LIMIT 5;

/* Customer Orders
Part 1) Write a query to identify customers who placed more than 3 orders each in 2016 and 2017.
Part 2) Write a query to identify customers who placed less than 3 orders or ordered less than $500 worth of product.
*/
select name from (
	select 
	name,
	year, 
	dense_rank() over (partition by year,customer_id order by ord_id) as rnk 
	from 
	orders o 
	inner join customers c 
	on o.customer_id = c.id
	where year(ord_date) in (2016, 2017)
) a 
where a.rnk > 3 
group by name 
having count(distinct year) > 1;

// variant 2

select foo.name 
from (
	select * 
	from customers 
	join orders on id=customer_id
)foo 
group by foo.name 
having count(distinct ord_id)>3
 
select foo.name 
from (
	select 
	* 
	from customers 
	join orders on id=customer_id
)foo 
group by foo.name 
having 
count(distinct ord_id)<3 or sum(amount)<500

// variant 3

//1) 
SELECT 
DISTINCT name 
FROM ( 
	SELECT 
	name, 
	YEAR(ord_date) year, 
	COUNT(order_id) 
	FROM customers c 
	INNER JOIN orders o 
	WHERE YEAR(ord_date) IN (2016, 2017) 
	GROUP BY name, YEAR(ord_date) 
	HAVING COUNT(order_id) > 3 )

// 2) 
SELECT 
name 
FROM customers c 
INNER JOIN orders o 
GROUP BY name 
HAVING COUNT(order_id) < 3 OR SUM(amount) < 500

/* Rolling Bank Transactions
We're given a table bank transactions with three columns, user_id, a deposit or withdrawal value, and created_at time for each transaction.
Write a query to get the total three day rolling average for deposits by day.
*/
SELECT 
curr.dt, 
avg(prev.total_deposits) 
FROM ( 
	SELECT 
	created_at AS dt , 
	SUM(transaction_value) AS total_deposits 
	FROM bank_transactions AS bt 
	WHERE transaction_value > 0 
	GROUP BY 1 ) AS curr 
INNER JOIN ( 
	SELECT 
	created_at AS dt , 
	SUM(transaction_value) AS total_deposits 
	FROM bank_transactions AS bt 
	WHERE transaction_value > 0 
	GROUP BY 1 ) AS prev 
ON prev.dt BETWEEN DATE_ADD(curr.dt, INTERVAL -2 DAY) AND curr.dt 
GROUP BY curr.dt;

// variant 2

WITH valid_transactions AS (
    SELECT DATE_TRUNC('day', created_at) AS dt
        , SUM(transaction_value) AS total_deposits
    FROM bank_transactions AS bt
    WHERE transaction_value > 0
    GROUP BY 1
)

SELECT vt1.dt
    AVERAGE(vt2.total_deposits) AS rolling_three_day
FROM valid_transactions AS vt1
INNER JOIN valid_transactions AS vt2
    -- set conditions for greater than three days 
    ON vt1.dt > DATE_ADD('DAY', -3, vt2.dt)
    -- set conditions for max date threshold
        AND vt1.dt <= vt2.dt
GROUP BY 1

/* Closest SAT Scores
Given a table of students and their SAT test scores, write a query to return the two students with the closest test scores with the score difference.
Assume a random pick if there are multiple students with the same score difference.
*/ 

// v1

select 
s1.student as one_student, 
s2.student as other_student, 
abs(s1.score - s2.score) as score_diff 
from scores s1 
join scores s2 
on s1.score > s2.score 
order by score_diff 
limit 1;

// v2

SELECT 
stud1, 
stud2, 
sc_1, 
sc_2, 
diff 
FROM ( 
	SELECT 
	s1.score as sc_1, 
	s2.score as sc_2, 
	s1.student as stud1, 
	s2.student as stud2, 
	abs(s1.score - s2.score) as diff 
	FROM scores s1 
	CROSS JOIN scores s2 
	WHERE s1.id != s2.id 
	) 
ORDER BY diff 
LIMIT 1;

// v3

SELECT 
	a.student AS one_student, 
	b.student AS other_student, 
	MIN(ABS(a.score-b.score)) AS score_diff 
FROM 
	student a, 
	student b 
WHERE a.id <> b.id 
GROUP BY a.student,b.student 
ORDER BY score_diff 
LIMIT 1;
	
// v4
select 
	a.student as student, 
	b.student as other_student, 
	abs(a.score - b.score) as score_diff 
from scores a 
inner join scores b 
on a.student != b.student and a.id > b.id 
order by 3 
limit 1

/* Swipe Precision
There are two tables. One table is called `swipes` that holds a row for every Tinder swipe and contains a boolean column that determines if the swipe was a right or left swipe called `is_right_swipe`. The second is a table named `variants` that determines which user has which variant of an AB test.

Write a SQL query to output the average number of right swipes for two different variants of a feed ranking algorithm by comparing users that have swiped the first 10, 50, and 100 swipes on their feed.

Tip: Users have to have swiped at least 10 times to be included in the subset of users to analyze the mean number of right swipes.

Example Input:

`variants`

id	experiment	variant	user_id
1	feed_change	control	123
2	feed_change	test	567
3	feed_change	control	996
`swipes`

id	user_id	swiped_user_id	created_at	is_right_swipe
1	123	893	2018-01-01	0
2	123	825	2018-01-02	1
3	567	946	2018-01-04	0
4	123	823	2018-01-05	0
5	567	952	2018-01-05	1
6	567	234	2018-01-06	1
7	996	333	2018-01-06	1
8	996	563	2018-01-07	0
Note: created_at doesn't show timestamps but assume it is a datetime column.

Output:

mean_right_swipes	variant	swipe_threshold	num_users
5.3	control	10	9560
5.6	test	10	9450
20.1	control	50	2001
22.0	test	50	2019
33.0	control	100	590
34.0	test	100	568
		
		*/
//v1
WITH table AS(
	SELECT s.*, v.*,
 ROW_NUMBER() OVER(PARTITON BY user_id ORDER BY created_at ASC) AS feed_number
	FROM swipes s
	JOIN variants v
	USING user_id
	WHERE experiment = ‘feed_change’
), users_feeds AS(
	SELECT user_id, MAX(feed_number) AS max_feeds
	FROM table 
	GROUP BY user_id
	HAVING MAX(feed_number) > 10
), users_flagged AS(
	SELECT user_id,
	CASE
		WHEN max_feeds >= 100 THEN 100
		ELSE IF max_feeds >= 50 AND max_feeds < 100 THEN 50
		ELSE 10
	END AS swipe_threshold
) , users_with_buckets AS(
	SELECT * 
FROM table 
JOIN 
users_flagged 
USING user_id
WHERE feed_number <= swipe_threshold
) SELECT swipe_threshold, 
variant,  
	SUM(is_swipe_right)::FLOAT/COUNT(DISTINCT user_id) AS mean_right_swipes_per_user,
, COUNT(DISTINCT user_id)  AS num_users
FROM users_with_buckets;

//v2
with swiped_count_per_user as (
select user_id, count(distinct swiped_user_id) as swiped_user_count
from swipes
group by user_id
having count(distinct swiped_user_id) >= 10),
variants_filtered as (
select v.*, 
case when s.swiped_user_count >= 10 then 1 else 0 end as swipe_10,
case when s.swiped_user_count >= 50 then 1 else 0 end as swipe_50,
case when s.swiped_user_count >= 100 then 1 else 0 end as swipe_100
from variants as v,
join swiped_count_per_user as s
on v.user_id = s.user_id
),
variants_10_swipes as (
select variant, '10' as swipe_threshold, count(distinct swiped_user_id) as num_users,
cast(sum(is_right_swipe)/count(distinct swiped_user_id) as float) as mean_right_swipes
from variants_filtered
where swipe_10 = 1
group by 1, 2),
variants_50_swipes as (
select variant, '50' as swipe_threshold, count(distinct swiped_user_id) as num_users,
cast(sum(is_right_swipe)/count(distinct swiped_user_id) as float) as mean_right_swipes
from variants_filtered
where swipe_50 = 1
group by 1, 2),
variants_100_swipes as (
select variant, '100' as swipe_threshold, count(distinct swiped_user_id) as num_users,
cast(sum(is_right_swipe)/count(distinct swiped_user_id) as float) as mean_right_swipes
from variants_filtered
where swipe_100 = 1
group by 1, 2)
select mean_right_swipes, variant, swipe_threshold, num_users
from variants_10_swipes
union
variants_50_swipes
union
variants_100_swipes;
		
// v3
with swiper_data as (select user_id, 
variant,
is_right_swipe,
rank() over (partition by user_id order by created_at ASC) as rank
from variants
inner join swipes
where experiment = "feed-change"
)
select variant, 
sum(is_right_swipe)/count(distinct user_id) as mean_right_swipes,
"10" as swipe_threshold,
count(distinct user_id)
from swipes_data 
inner join on (
select user_id 
from swipe_data 
where rank>10
group by 1) as subset
on swipes_data.user_id = subset.user_id
where rank <=10
group by 1

UNION ALL

select variant, 
sum(is_right_swipe)/count(distinct user_id) as mean_right_swipes,
"10" as swipe_threshold,
count(distinct user_id)
from swipes_data 
inner join on (
select user_id 
from swipe_data 
where rank>50
group by 1) as subset
on swipes_data.user_id = subset.user_id
where rank <=50
group by 1

UNION ALL

select variant, 
sum(is_right_swipe)/count(distinct user_id) as mean_right_swipes,
"10" as swipe_threshold,
count(distinct user_id)
from swipes_data 
inner join on (
select user_id 
from swipe_data 
where rank>100
group by 1) as subset
on swipes_data.user_id = subset.user_id
where rank <=100
group by 1
