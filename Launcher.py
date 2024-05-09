# Importing libraries we will need to use
import time
import sqlite3
#####################################


# Reading in an example query that we will use on the database
file_name = 'example_query.sql'

print('my name is '+file_name)
with open(file_name, 'r') as query_file:
	content = query_file.read()
print (content)
#########################################


# Opening a connection to the database
database_file_name = 'converted_catalogue.db'
ThursdayDatabase = sqlite3.connect(database_file_name)
ThursdayCursor = ThursdayDatabase.cursor()
#########################################

# Querying the database
ThursdayCursor.execute(content)
rows = ThursdayCursor.fetchall()
print(type(rows))

my_dog_names = ['Fido', 'Peter', 'Oscar', 'Maramduke']
number_of_dog_names = len(my_dog_names)
print(number_of_dog_names)
number_of_rows = len(rows)
print(number_of_rows)
print(rows[100])
###############################################