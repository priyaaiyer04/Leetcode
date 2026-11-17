# Write your MySQL query statement below

select person_name from (select person_name, sum(weight) over (order by turn) as cumsum from queue order by turn) as  person_name where cumsum<=1000 order by cumsum desc limit 1 ;

