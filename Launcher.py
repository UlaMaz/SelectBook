import sqlite3
newname = 'which_languages_query.sql'
with open(newname, 'r')as newSQLfile:
	Query519 = newSQLfile.read()

#print(Query519)

database_file_name = "../SQL_data_copy/converted_catalogue.db"
SundayDatabase   =  sqlite3.connect(database_file_name)
SundayCursor = SundayDatabase.cursor()

SundayCursor.execute(Query519)
queryresults=SundayCursor.fetchall()

totalrows = len(queryresults)
#print(totalrows)

languagefreq = []
#for each row number in the range 0 to 10
for row_number in range(totalrows):
    # print the row number
    print(row_number)
    row = queryresults[row_number]
    languagefreq.append(row[1])
    print(row)


twenty_most_cmn_lnggs = (queryresults[0:20])
print("The 20 most common languages are")
print(twenty_most_cmn_lnggs)


# Aim is to create a dictionary with the 20 most common languages
language_dictionary = {"en":"English",
						}

table_creator_file_name = 'bin_table.sql'
with open(table_creator_file_name, 'r') as TuesdaySQL:
    TableCreator = TuesdaySQL.read()

SundayCursor.execute(TableCreator)

row_creator_file_name = 'createrow.sql'
with open (row_creator_file_name, 'r') as TuesdaySQL:
    RowCreator = TuesdaySQL.read()
SundayCursor.execute(RowCreator)

TableReader = "SELECT * FROM Bin_Data"
SundayCursor.execute(TableReader)
queryresults = SundayCursor.fetchall()
print(queryresults)