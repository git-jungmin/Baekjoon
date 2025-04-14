SELECT COUNT(ID) AS FISH_COUNT, EXTRACT(MONTH FROM TIME) AS MONTH
FROM FISH_INFO
GROUP BY MONTH
ORDER BY MONTH;