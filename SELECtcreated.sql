SELECT MIN(Created)
FROM catalogue_entries
WHERE Created NOT IN ('0000-00-00', 'None')