# Write your MySQL query statement below
#select distinct c.customer_id from customer c  having count(c.customer_id)=(select distinct count(product_key) from product) ;

select c.customer_id from customer c group by c.customer_id having count(distinct c.customer_id,c.product_key) =(select distinct count(product_key) from product) ;