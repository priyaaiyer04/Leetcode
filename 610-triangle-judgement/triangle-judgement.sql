# Write your MySQL query statement below
select x,y,z, case
when x>=y and x>=z and z+y>x  and x>0 and y>0 and z>0 then "Yes"
when y>=x and y>=z and z+x>y  and x>0 and y>0 and z>0 then "Yes"
when z>=y and z>=x and x+y>z  and x>0 and y>0 and z>0 then "Yes"
else "No"
end as triangle
from Triangle;