-- List all the records from second_table and don't show the rows where name doesn't contain any value
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
