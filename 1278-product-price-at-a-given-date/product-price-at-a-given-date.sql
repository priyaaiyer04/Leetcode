# Write your MySQL query statement below


select product_id, new_price as price from products where (product_id,change_date) in (select distinct product_id, max(change_date) over (partition by product_id order by change_date desc) from products where change_date<='2019-08-16')
union
select product_id, case when min(change_date)>'2019-08-16' then 10
end as price from products group by product_id having price is not null;

