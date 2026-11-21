# Write your MySQL query statement below

select r.requester_id as  id,(select  count(accepter_id ) over (partition by  requester_id) from RequestAccepted where requester_id=r.requester_id limit 1)+
coalesce((select  count(requester_id ) over (partition by  accepter_id) from RequestAccepted where accepter_id=r.requester_id limit 1),0) as num
from RequestAccepted r group by  r.requester_id
union 
select r.accepter_id  as  id,(select  count(requester_id ) over (partition by  accepter_id ) from RequestAccepted where accepter_id =r.accepter_id  limit 1)+
coalesce((select  count(accepter_id ) over (partition by  requester_id) from RequestAccepted where requester_id=r.accepter_id  limit 1),0) as num
from RequestAccepted r group by  r.accepter_id 

 order by num desc limit 1 ;