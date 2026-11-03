# Write your MySQL query statement below

select substring(t.trans_date,1,7) as month,t.country, count(t.id) as trans_count,
sum(case when t.state='approved' then 1 else 0 end)   as approved_count,
sum(t.amount )   as  trans_total_amount,
sum(case when t.state='approved' then t.amount else 0 end)   as approved_total_amount
from  transactions t join transactions t1 on t.id=t1.id group by substring(t.trans_date,1,7),t.country;