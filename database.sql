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

