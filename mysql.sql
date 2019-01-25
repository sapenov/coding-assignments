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
order by units desc
