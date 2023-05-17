-- Write a script that displays the max temperature of each state (ordered by State name
SELECT city, AVG(value) AS avg_temp FROM temperatures
WHERE month BETWEEN 7 AND 8
GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
