SELECT I.ANIMAL_ID, I.NAME
FROM ANIMAL_INS I
JOIN ANIMAL_OUTS O ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE O.DATETIME - I.DATETIME < 0
ORDER BY I.DATETIME