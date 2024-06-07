/* Write your PL/SQL query statement below */
select w2.id from weather w1,weather w2 where w1.temperature<w2.temperature and w2.recordDate
-w1.recordDate=1