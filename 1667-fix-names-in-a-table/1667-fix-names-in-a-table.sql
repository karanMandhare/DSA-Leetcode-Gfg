-- SELECT 
--     CONCAT(
--         UPPER(LEFT(name, 1)), 
--         LOWER(SUBSTRING(name, 2, LENGTH(name)))
--     ) AS capitalized_name
-- FROM users;


SELECT
USER_ID, 
CONCAT(
    UPPER(LEFT(NAME,1)),
    LOWER(SUBSTRING(NAME,2,LENGTH(NAME))) 
) AS NAME 
    FROM USERS
    ORDER BY USER_ID;