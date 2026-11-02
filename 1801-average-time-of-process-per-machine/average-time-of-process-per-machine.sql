# Write your MySQL query statement below

select m.machine_id, round(avg(m1.timestamp-m.timestamp),3) as processing_time from Activity m join Activity m1 on ( m.machine_id=m1.machine_id) where m.activity_type='start' and m1.activity_type='end' and m.process_id=m1.process_id group by m.machine_id; 