import sqlite3

######## Languages in the catalogue_entries database ###############

# read in query
newname = 'which_languages_query.sql'
with open(newname, 'r')as newSQLfile:
	Query519 = newSQLfile.read()

# opened a connection to the SQL database
database_file_name = "../SQL_data_copy/converted_catalogue.db"
SundayDatabase   =  sqlite3.connect(database_file_name)
SundayCursor = SundayDatabase.cursor()

# run the query and get results
SundayCursor.execute(Query519)
queryresults=SundayCursor.fetchall()


# print some resuts
totalrows = len(queryresults)
languagefreq = []
#for each row number in the range 0 to 10
for row_number in range(10):
#for row_number in range(totalrows):
    # print the row number
    print(row_number)
    row = queryresults[row_number]
    languagefreq.append(row[1])
    print(row)

want_to_print_more = False

if want_to_print_more:
    twenty_most_cmn_lnggs = (queryresults[0:20])
    print("The 20 most common languages are")
    print(twenty_most_cmn_lnggs)


# Aim is to create a dictionary with the 20 most common languages
language_dictionary = {"en":"English",
						}

###################################################################

###### Creating a table for histogam bins #########################

# reading in instructions for table creation
table_creator_file_name = 'bin_table.sql'
with open(table_creator_file_name, 'r') as TuesdaySQL:
    TableCreator = TuesdaySQL.read()

# create the new table
SundayCursor.execute(TableCreator)


# Find oldest published book
oldest_entry_file_name = 'SELECtcreated.sql'
with open(oldest_entry_file_name, 'r') as TodaysSQL:
    OldestDateCreator = TodaysSQL.read()
SundayCursor.execute(OldestDateCreator)
queryresults = SundayCursor.fetchall()
print(queryresults)

##### CREATE row dynamically ######
item_no = 0
start_date = 1970
end_date = 3000

# Now apply that here
# Put all the lines below up to and including the 'execute' call inside a for loop
# it should create a set of rows,
# each one with different item_no, start_date and end_date

row_creation = 'INSERT INTO Bin_Data'
table_titles = '(ItemNo, StartDate, EndDate)'

for row_number in range(1970, 3001):
    start_date = row_number
    end_date= start_date+1
    item_no= row_number - 1969
    table_content = f'VALUES ({item_no}, {start_date}, {end_date})'
    super_string = row_creation + " " + table_titles + " " + table_content
    SundayCursor.execute(super_string)

#############


# Reading what we put into the histogram bin table
TableReader = "SELECT * FROM Bin_Data"
SundayCursor.execute(TableReader)
queryresults = SundayCursor.fetchall()
print(queryresults)


# Delete the hitogram bin table, so we can start afresh next time
TableDelete = "DROP TABLE 'Bin_Data'"
SundayCursor.execute(TableDelete)
queryresults= SundayCursor.fetchall()
print(queryresults)

###################################################################




  