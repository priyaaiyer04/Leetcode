# Write your MySQL query statement below
#select p.product_id, coalesce(round(sum(p.price*u.units)/sum(u.units),2),0) as average_price from prices p left join unitsSold u on p.product_id=u.product_id where u.purchase_date>=p.start_date and u.purchase_date<=p.end_date  group by p.product_id ;

select p.product_id,
coalesce(round(sum(case when  u.purchase_date>=p.start_date and u.purchase_date<=p.end_date 
then (p.price*u.units)
else 0 
end)
/
sum(case when  u.purchase_date>=p.start_date and u.purchase_date<=p.end_date 
then u.units
else 0 
end),2),0) as average_price 
from prices p left join unitsSold u on p.product_id=u.product_id group by p.product_id  ;