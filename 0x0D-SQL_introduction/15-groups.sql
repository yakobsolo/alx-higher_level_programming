-- number by score
-- selects and group by score
SELECT score, COUNT(*) AS "number" FROM second_table GROUP BY score ORDER BY "number";
