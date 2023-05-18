-- lists the numberj of records with the same score in the table 
SELECT score, COUNT(`score`) AS number
FROM second_table 
ORDER BY number DESC
GROUP BY score;
