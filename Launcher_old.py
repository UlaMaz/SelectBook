# Importing libraries we will need to use
import time
import sqlite3
#####################################


# Reading in an example query that we will use on the database
file_name = 'example_query.sql'
print('my name is '+file_name)
# opening a context
# with some_function() as some_variable:
with open(file_name, 'r') as query_file:
	# inside the context
	query_text = query_file.read()
	# still inside the context
# outside the context
print (query_text)
#########################################


# Opening a connection to the database
database_file_name = 'converted_catalogue.db'
ThursdayDatabase = sqlite3.connect(database_file_name)
ThursdayCursor = ThursdayDatabase.cursor()
#########################################


# Generating an example database
may12database = 'May12work.sql'
with open(may12database, 'r') as current_file:
	file_text = current_file.readlines()

first_statement = file_text[:6]
empty_string = ''
first_statement_joined = empty_string.join(first_statement)

second_statement = file_text[6:]
print(second_statement)
second_statement_joined = empty_string.join(second_statement)


ThursdayCursor.execute(first_statement_joined)
ThursdayCursor.execute(second_statement_joined)

# Querying the database
ThursdayCursor.execute(query_text)
rows = ThursdayCursor.fetchall()
print(type(rows))
print(f"The number of rows in this database is {len(rows)}")

my_dog_names = ['Fido', 'Peter', 'Oscar', 'Maramduke']
print(my_dog_names[0][2])
number_of_dog_names = len(my_dog_names)
print(number_of_dog_names)
#number_of_rows = len(rows)
#print(number_of_rows)
#print(rows[100])
###############################################