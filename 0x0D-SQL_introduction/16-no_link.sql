-- list all records 
-- select score name order by score descending
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
