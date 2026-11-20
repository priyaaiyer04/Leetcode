# Write your MySQL query statement below

select name as results from users where user_id =(select  u.user_id from MovieRating m join users u on u.user_id=m.user_id  group by m.user_id order by count(m.movie_id) desc, u.name asc limit 1) 
union all
select * from (select m1.title from MovieRating m join movies m1 on m.movie_id=m1.movie_id where m.created_at >'2020-01-31' and m.created_at<'2020-03-01' group by m.movie_id order by avg(m.rating) desc,m1.title asc limit 1) as movies ;
