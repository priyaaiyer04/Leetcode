# Write your MySQL query statement below


select round(sum(case when d.order_date=d.customer_pref_delivery_date then 1 else 0 end)*100/(select count(distinct customer_id) from delivery),2) as immediate_percentage
from delivery d where (d.customer_id,d.order_date) in (select customer_id,min(order_date) from delivery group by customer_id );