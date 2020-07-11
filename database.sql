// Monthly Customer Report
// Write a query to show the number of customer accounts created, number of orders placed, and total order amount per month.
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
