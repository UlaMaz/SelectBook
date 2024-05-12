CREATE TABLE IF NOT EXISTS May12Table (
	id INTEGER PRIMARY KEY,
	genre TEXT,
	publication DATE,
	avg_rating FLOAT, 
	in_stock BOOLEAN) ;

INSERT INTO May12Table (genre, publication, avg_rating, in_stock)
VALUES ('Fiction','2022-09-07',5.6,1);