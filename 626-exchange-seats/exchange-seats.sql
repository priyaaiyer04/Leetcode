# Write your MySQL query statement below

select case when id%2=0 then id-1 
 when id=(select count(student) from seat)  and id%2!=0 then id
 when id%2!=0 then id+1
 else 1000 
 end as id, student from seat order by id;