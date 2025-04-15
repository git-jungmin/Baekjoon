SELECT A.CATEGORY, SUM(B.SALES) AS TOTAL_SALES
FROM BOOK A
RIGHT JOIN BOOK_SALES B ON A.BOOK_ID = B.BOOK_ID
WHERE DATE_FORMAT(B.SALES_DATE,'%Y-%m') = '2022-01'
GROUP BY A.CATEGORY
ORDER BY A.CATEGORY