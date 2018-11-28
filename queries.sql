/* create schema*/
create table recipes (
recipe_id int, 
recipe_name varchar(100), 
description varchar(100), 
ingredient varchar(100), 
active boolean, 
updated_date datetime, 
created_date datetime);

/*populate sample schema with data */
insert into recipes(recipe_id, recipe_name, description, ingredient, active, updated_date, created_date) values (1, 'pasta', 'Italian pasta', 'tomato sauce', true, '2018-01-09 10:00:57',  '2018-01-10 13:00:57'),
(1, 'pasta', null, 'cheese', true, '2018-01-09 10:10:57',  '2018-01-10 13:00:57'),
(2, 'lasagna', 'layered lasagna', 'cheese', true, '2018-01-09 10:00:57',  '2018-01-10 13:00:57'),
(2, 'lasagna', 'layered lasagna', 'blue cheese', false, '2018-01-09 10:00:57',  '2018-01-10 13:00:57');

/* average number of recipes which are updated per hour*/
SELECT 
  recipe_name,
  HOUR(updated_date),
  COUNT(*) AS cnt 
FROM recipes
GROUP BY HOUR(updated_date), recipe_name

/* number of recipes which got updated at 10:00 o'clock in the entire year*/

SELECT 
  recipe_name,
  YEAR(updated_date),
  COUNT(*) AS cnt 
FROM recipes
WHERE HOUR(updated_date)=10 AND MINUTE(updated_date)=00
GROUP BY YEAR(updated_date), recipe_name
