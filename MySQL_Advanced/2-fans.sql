-- Task: Rank country origins of bands by number of fans
-- Selects origin and sums fans, ordered by total fans descending
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
