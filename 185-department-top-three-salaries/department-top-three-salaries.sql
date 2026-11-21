# Write your MySQL query statement below


#select d.name as department, e.name as employeee, e.salary from employee e join department d on d.id=e.departmentId where e.salary in (select case when count(*)<=3 then salary
#end as salary from employee where departmentId =d.id order by departmentId, salary desc) order by e.departmentId, e.salary desc;

select department  ,  Employee, salary from (select d.name as department  , e.departmentId, e.name as Employee, e.salary as salary, dense_rank() over (partition by e.departmentId order by e.salary desc) as dn from employee e join department d on d.id=e.departmentId order by e.departmentId, e.salary desc) as t where dn<=3;