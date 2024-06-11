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


#### REMOVE #####
row_creator_file_name = 'createrow.sql'
with open (row_creator_file_name, 'r') as TuesdaySQL:
    RowCreator = TuesdaySQL.read()
SundayCursor.execute(RowCreator)
###################

##### CREATE row dynamically ######
item_no = 0
start_date = 1970
end_date = 3000

row_creation = 'INSERT INTO Bin_Data'
table_titles = '(ItemNo, StartDate, EndDate)'
table_content = f'VALUES ({item_no}, {start_date}, {end_date})'

super_string = row_creation + " " + table_titles + " " + table_content
SundayCursor.execute(super_string)
#############
print(super_string)

TableReader = "SELECT * FROM Bin_Data"
SundayCursor.execute(TableReader)
queryresults = SundayCursor.fetchall()
print(queryresults)

oldest_entry_file_name = 'SELECtcreated.sql'
with open(oldest_entry_file_name, 'r') as TodaysSQL:
    OldestDateCreator = TodaysSQL.read()
SundayCursor.execute(OldestDateCreator)
queryresults = SundayCursor.fetchall()
print(queryresults)

TableDelete = "DROP TABLE 'Bin_Data'"
SundayCursor.execute(TableDelete)
queryresults= SundayCursor.fetchall()
print(queryresults)