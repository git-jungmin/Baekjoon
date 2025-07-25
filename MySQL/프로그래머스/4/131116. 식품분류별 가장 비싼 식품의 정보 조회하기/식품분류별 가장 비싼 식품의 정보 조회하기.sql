SELECT T1.CATEGORY, T1.PRICE, T1.PRODUCT_NAME
FROM FOOD_PRODUCT T1
JOIN (
    SELECT CATEGORY, MAX(PRICE) AS MAX_PRICE
    FROM FOOD_PRODUCT
    WHERE CATEGORY IN ('과자', '국', '김치', '식용유')
    GROUP BY CATEGORY
) T2 ON T1.CATEGORY = T2.CATEGORY AND T1.PRICE = T2.MAX_PRICE
ORDER BY T1.PRICE DESC