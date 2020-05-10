
-- Department Top Three Salaries

/* 203 ms */
SELECT
    d.Name AS 'Department', 
    e1.Name AS 'Employee', 
    e1.Salary
FROM
    Employee e1
JOIN
    Department d 
ON 
    e1.DepartmentId = d.Id
WHERE
    3 > (SELECT
            COUNT(DISTINCT e2.Salary)
        FROM
            Employee e2
        WHERE
            e2.Salary > e1.Salary
                AND e1.DepartmentId = e2.DepartmentId
        );

/* 190 ms */
select 
  d.Name as Department, 
  a. Name as Employee, 
  a. Salary 
from (
  select 
    e.*, 
    dense_rank() over (partition by DepartmentId order by Salary desc) as DeptPayRank 
  from Employee e 
) a 
join Department d
on a. DepartmentId = d. Id 
where DeptPayRank <=3; 


/* 270 ms */
select 
  tD.Name as 'Department', 
  tE1.Name as 'Employee', 
  tE1.Salary 
from Employee as tE1
Inner join Department as tD 
  on tE1.DepartmentId = tD.Id
Left join Employee as tE2 
  on tE1.DepartmentId = tE2.DepartmentId and tE1.Salary <= tE2.Salary
group by tE1.Id
having count(distinct tE2.Salary) <= 3
order by tE1.DepartmentId, tE1.Salary desc


-- Average Salary: Departments VS Company
-- Given two tables below, write a query to display the comparison result (higher/lower/same) of the average salary of employees 
-- in a department to the company's average salary.

select 
department_salary.pay_month, 
department_id,
case
  when department_avg>company_avg then 'higher'
  when department_avg<company_avg then 'lower'
  else 'same'
end as comparison
from
(
  select 
    department_id, 
    avg(amount) as department_avg, 
    date_format(pay_date, '%Y-%m') as pay_month
  from 
  salary 
  join employee 
  on salary.employee_id = employee.employee_id
  group by 
  department_id, 
  pay_month
) as department_salary
join
(
  select 
    avg(amount) as company_avg,  
    date_format(pay_date, '%Y-%m') as pay_month 
    from salary 
    group by date_format(pay_date, '%Y-%m')
) as company_salary
on department_salary.pay_month = company_salary.pay_month
;

-- Human Traffic of Stadium
/*
X city built a new stadium, each day many people visit it and the stats are saved as these columns: id, visit_date, people.
Please write a query to display the records which have 3 or more consecutive rows and the amount of people more than 100(inclusive).
Each day only have one row record, and the dates are increasing with id increasing.
*/
-- solution 1 (148 ms)
select distinct t1.*
from stadium t1, stadium t2, stadium t3
where 
t1.people >= 100 
and 
t2.people >= 100 
and 
t3.people >= 100
and
(
	(t1.id - t2.id = 1 and t1.id - t3.id = 2 and t2.id - t3.id =1)  -- t1, t2, t3
    or
    (t2.id - t1.id = 1 and t2.id - t3.id = 2 and t1.id - t3.id =1) -- t2, t1, t3
    or
    (t3.id - t2.id = 1 and t2.id - t1.id =1 and t3.id - t1.id = 2) -- t3, t2, t1
)
order by t1.id;

-- Solution 2 (144 ms)
SELECT DISTINCT S1.*
FROM stadium S1
JOIN stadium S2
JOIN stadium S3
ON 
  ((S1.id = S2.id - 1 AND S1.id = S3.id -2)
  OR (S3.id = S1.id - 1 AND S3.id = S2.id -2)
  OR (S3.id = S2.id - 1 AND S3.id = S1.id -2))
WHERE 
  S1.people >= 100
  AND S2.people >= 100
  AND S3.people >= 100
ORDER BY S1.id;*/


-- Solution 3 203 ms

SELECT 
    id, visit_date, people
FROM 
    stadium
WHERE 
    3 <= (
        SELECT COUNT(s.people) 
        FROM stadium AS s
        WHERE 
            s.people >= 100
            AND s.id >= stadium.id
            AND s.id <= stadium.id+2
    ) 
    OR
    3 <= (
        SELECT COUNT(s.people) 
        FROM stadium AS s
        WHERE 
            s.people >= 100
            AND s.id >= stadium.id-1
            AND s.id <= stadium.id+1
    ) 
    OR
    3 <= (
        SELECT COUNT(s.people) 
        FROM stadium AS s
        WHERE 
            s.people >= 100
            AND s.id >= stadium.id-2
            AND s.id <= stadium.id
    ) 

