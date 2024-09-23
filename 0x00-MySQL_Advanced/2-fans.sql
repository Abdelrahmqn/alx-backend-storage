-- fans

SELECT origin, SUM(fans) AS np_fans
FROM metal_bands
GROUP BY origin
ORDER BY np_fans DESC;