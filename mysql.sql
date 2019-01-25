/* Top 3 Products by sale */
select p.product_name,  sum(s.store_sales) as gross 
from sales as s 
join products as p on p.product_id = s.product_id
group by product_name
order by gross DESC
limit 3;

/* Count the number of products which sold more than 10 units */
select p.product_name, 
sum(s.units_sold) as units,
sum(p.price * s.units_sold) as total
from sales as s
join products as p 
on p.product_id = s.product_id
group by product_name
having units >= 10 AND total > 20
order by units desc;

/* Sales per brand which sold more than 10 units */
select p.brand_name, 
sum(s.units_sold) as units,
sum(p.price * s.units_sold) as total
from sales as s
join products as p 
on p.product_id = s.product_id
group by brand_name
having units >= 10 AND total > 20
order by units desc;

/* 5) For each store show % difference in sales between 2014 and 2015 */
SELECT 
  p1.store_id, ROUND(((p2.gross - p1.gross)/p2.gross * 100),0) AS 'Growth, %'
FROM 
    (SELECT store_id, sum(store_sales) AS gross FROM sales WHERE YEAR(transaction_date) = 2014 group by store_id) AS p1,
    (SELECT store_id, sum(store_sales) AS gross FROM sales WHERE YEAR(transaction_date) = 2015 group by store_id) AS p2;
