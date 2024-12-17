-- database: c:/Users/adrie/Documents/projectethon/predictive_maintenance.db

-- SQLite
SELECT device_id, COUNT(*) AS failure_count
FROM maintenance_data
WHERE failure_flag = 1
GROUP BY device_id
ORDER BY failure_count DESC;



SELECT name 
FROM sqlite_master 
WHERE type = 'table';



SELECT AVG(sensor_pressure) AS avg_pressure, AVG(vibration_spike) AS avg_vibration
FROM maintenance_data
WHERE failure_flag = 1;


SELECT DATE(date) AS failure_date, COUNT(*) AS failure_count
FROM maintenance_data
WHERE failure_flag = 1
GROUP BY DATE(date)
ORDER BY failure_date;

SELECT * FROM failed_devices_usage;

SELECT name 
FROM sqlite_master 
WHERE type = 'table';



