# Write your MySQL query statement below

select distinct c.num as ConsecutiveNums  from logs c join logs l on c.id=l.id+1 and c.num=l.num join logs l1 on c.id=l1.id+2 and c.num=l1.num;