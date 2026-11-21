# Write your MySQL query statement below


select department  ,  Employee, salary from (select d.name as department  , e.departmentId, e.name as Employee, e.salary as salary, dense_rank() over (partition by e.departmentId order by e.salary desc) as dn from employee e join department d on d.id=e.departmentId order by e.departmentId, e.salary desc) as t where dn<=3;