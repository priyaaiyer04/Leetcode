# Write your MySQL query statement below

select (select distinct coalesce(salary,null) as SecondHighestSalary from employee order by salary desc limit 1,1) as  SecondHighestSalary;

