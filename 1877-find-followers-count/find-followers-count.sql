# Write your MySQL query statement below
select f.user_id, count(f.follower_id ) as  followers_count from followers f group by f.user_id order by f.user_id;