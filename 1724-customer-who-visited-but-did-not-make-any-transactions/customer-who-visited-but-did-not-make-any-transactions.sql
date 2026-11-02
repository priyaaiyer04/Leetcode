# Write your MySQL query statement below


select c.customer_id, count(c.visit_id ) as count_no_trans  from Visits c left join Transactions t on c.visit_id=t.visit_id where t.transaction_id is Null and  t.visit_id is Null and t.amount is Null group by  c.customer_id  ;