file_name = 'example_query.sql'

print('my name is'+file_name)


query_file = open('example_query.sql', 'r')
content = query_file.read()

print (query_file)
print (content)

query_file.close()