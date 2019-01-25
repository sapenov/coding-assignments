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

/* 3a. Get youngest customer who bought at least 1 product;  */

select concat(c.first_name, c.last_name) as name,nc.birthdate as bd, sum(s.units_sold) as bought
from sales as s
join customers as c on s.customer_id = c.customer_id
group by name, bd
having bought > 0
order by bd desc
limit 1

/* 3b. Get oldest customer who bought at least 1 product;  */

select concat(c.first_name, c.last_name) as name,nc.birthdate as bd, sum(s.units_sold) as bought
from sales as s
join customers as c on s.customer_id = c.customer_id
group by name, bd
having bought > 0
order by bd asc
limit 1

/* 4a. find earliest born and last born customers, by gender, who bought at least 1 product */

select concat(c.first_name, c.last_name) as name,
c.gender,
c.birthdate as bd, sum(s.units_sold) as bought
from sales as s
join customers as c on s.customer_id = c.customer_id
group by name, gender, bd
having bought > 0 and gender = 'M'
order by bd desc
limit 1

/* 4b. find latest born customers, by gender, who bought at least 1 product */

select concat(c.first_name, c.last_name) as name,
c.gender,
c.birthdate as bd, sum(s.units_sold) as bought
from sales as s
join customers as c on s.customer_id = c.customer_id
group by name, gender, bd
having bought > 0 and gender = 'F'
order by bd asc
limit 1

/* 5. Get the areas from which we have the products sold */
select  st.state as area,
sum(s.units_sold) as units
from sales as s
join stores as st
on s.store_id = st.store_id
group by area
having units >= 1
order by units desc;

/* number of unique products per customer */
SELECT concat(c.first_name,' ', c.last_name) as name, 
COUNT(DISTINCT product_id) as products_count 
FROM customers as c
INNER JOIN sales as s
ON c.customer_id = s.customer_id
GROUP BY c.customer_id, name
HAVING COUNT(DISTINCT product_id) between 1 and 2;

SELECT concat(c.first_name,' ', c.last_name) as name, 
COUNT(DISTINCT product_id) as products_count 
FROM customers as c
INNER JOIN sales as s
ON c.customer_id = s.customer_id
GROUP BY c.customer_id
HAVING COUNT(DISTINCT product_id) = 2;

/* 11.The names of people that have 2 or more orders. When was the earliest and latest order made ? cumulative sum */
select 
concat(c.first_name, ' ', c.last_name) as name,
count(s.store_sales) as orders, 
min(transaction_date) as earliest, 
max(transaction_date) as latest,
sum(s.store_sales) as cumulative_sum
from sales as s
join customers as c
on s.customer_id = c.customer_id
group by name 
having orders =12
order by orders desc
limit 10;

/* 8. Percentage increase in revenue compared to promoted and non-promoted products. */

SELECT 
  p1.store_id, ROUND(((p2.gross - p1.gross)/p2.gross * 100),0) AS 'Growth, %'
FROM 
    (SELECT store_id, sum(store_sales) AS gross FROM sales WHERE promotion_id = 0 group by store_id) AS p1,
    (SELECT store_id, sum(store_sales) AS gross FROM sales WHERE promotion_id > 0 group by store_id) AS p2
order by 2 desc;

/* orders whose total values are greater than 60,000 */

SELECT 
    orderNumber, 
    customerNumber, 
    status, 
    shippedDate
FROM
    orders
WHERE
    orderNumber IN (
        SELECT 
            orderNumber
        FROM
            orderDetails
        GROUP BY orderNumber
        HAVING SUM(quantityOrdered * priceEach) > 60000
       );

