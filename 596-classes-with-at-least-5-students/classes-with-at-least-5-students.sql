# Write your MySQL query statement below
select DISTINCT m.class from courses m where m.class in (select s.class from courses s group by s.class having count(s.student) >=5 );