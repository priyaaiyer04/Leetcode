# Write your MySQL query statement below
select round(count(distinct a.player_id)/(select count(distinct a2.player_id) from activity a2),2) as fraction from activity a where datediff(a.event_date,(select a1.event_date from Activity a1 where a1.player_id=a.player_id ORDER BY event_date
LIMIT 1))=1;