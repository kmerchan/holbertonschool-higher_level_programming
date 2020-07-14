-- lists score and name records from second_table ordered by score (top first), doesn't list row without name value
SELECT `score`, `name` FROM second_table WHERE `name` IS NOT NULL ORDER BY `score` DESC;
