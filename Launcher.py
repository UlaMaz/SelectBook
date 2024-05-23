import sqlite3
newname = 'which_languages_query.sql'
with open(newname, 'r')as newSQLfile:
	Query519 = newSQLfile.read()

print(Query519)

database_file_name = "../SQL_data/converted_catalogue.db"
SundayDatabase   =  sqlite3.connect(database_file_name)
SundayCursor = SundayDatabase.cursor()
SundayCursor.execute(Query519)
rows=SundayCursor.fetchall()

totalrows = len(rows)
print(totalrows)

languagefreq = []
#for each row number in the range 0 to 10
for row_number in range(totalrows):
    # print the row number
    #print(row_number)
    row = rows[row_number]
    languagefreq.append(row[1])
print(languagefreq)


new_list = sorted(languagefreq)
print (new_list)
# Aim is to create a dictionary with the 20 most common languages
language_dictionary = {"en":"English",
						}


