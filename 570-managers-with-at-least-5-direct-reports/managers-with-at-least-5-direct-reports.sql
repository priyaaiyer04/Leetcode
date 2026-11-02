# Write your MySQL query statement below
select e.name from employee e LEFT join employee e1 on e.id=e1.managerId group by e.id having count(e1.managerId)>=5;