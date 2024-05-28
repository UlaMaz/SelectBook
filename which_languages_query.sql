SELECT DISTINCT language, COUNT (language) AS 'number'
FROM catalogue_entries
GROUP BY language
ORDER BY number DESC