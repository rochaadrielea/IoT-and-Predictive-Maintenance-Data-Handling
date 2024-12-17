-- database: c:/Users/adrie/Documents/projectethon/iot_cleaned_data.db


SELECT name 
FROM sqlite_master 
WHERE type = 'table';


SELECT * FROM cleaned_iot_data;

PRAGMA table_info(cleaned_iot_data);
