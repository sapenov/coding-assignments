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
