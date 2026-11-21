# Write your MySQL query statement below


select round(sum(tiv_2016),2) as tiv_2016 from Insurance where pid in (select pid from Insurance where tiv_2015 in (select tiv_2015 from Insurance group by tiv_2015 having count(tiv_2015)>1 )) and pid in (select pid from (select pid,concat(convert(lat,char)," ",convert(lon,char)) as count1 from Insurance) as count2 group by count1 having count(*)=1);