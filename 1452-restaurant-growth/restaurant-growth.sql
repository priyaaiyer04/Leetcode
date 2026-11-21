# Write your MySQL query statement below

#select c.visited_on,c1.visited_on, c1.customer_id from customer c join customer c1 on day(c.visited_on)>=7 and c1.visited_on<=c.visited_on and c1.visited_on>c.visited_on-7 order by c.visited_on;

select distinct c.visited_on,(select sum(amount) from customer c1 where c1.visited_on<=c.visited_on and datediff(c.visited_on,c1.visited_on)<=6) as amount, round((select sum(amount)/7 from customer c1 where c1.visited_on<=c.visited_on and datediff(c.visited_on,c1.visited_on)<=6 ),2) as average_amount from customer c where  datediff(c.visited_on,(select min(visited_on) from customer))>=6  order by c.visited_on;

#select visited_on, sum(amount), avg(amount) from customer where day(visited_on)>=7 group by visited_on;