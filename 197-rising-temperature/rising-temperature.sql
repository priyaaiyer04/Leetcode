# Write your MySQL query statement below
select w1.id from Weather w join Weather w1 on w1.recordDate- INTERVAL 1 DAY=w.recordDate where w.temperature <w1.temperature;