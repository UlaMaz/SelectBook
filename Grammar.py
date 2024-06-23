### Iteration oer lists  ###################


# list_a = ["A", "quite", "naughty", "cat", "."]
# list_b = list(range(5, 10))


# length_of_a = len(list_a)

# print("The number of items in list_a is")
# print(length_of_a)

# loop_number = 0

# print("Starting the loop;")
# for loop_number in range(length_of_a):
# 	print("Going round the loop")
# 	item_from_a = list_a[loop_number]
# 	print(item_from_a)
# print("Loop is done")

# for item_from_a in list_a:
# 	print("Going round the second loop.")
# 	print(item_from_a)

# length_of_b = len(list_b)

# print("Starting the loop")
# for loop_number in range(length_of_b):
# 	print("Going round the loop")
# 	item_from_b = list_b[loop_number]
# 	print(item_from_b)
# print("Loop is done")

# for item_from_b in list_b:
# 	print("Going round the second loop.")
# 	print(item_from_b)


########## String formatting  #######

# print("Some text to print to the screen.")

# number_of_books = 100

# my_string = f"The number of books is {number_of_books}. Isn't that nice."
# #print(my_string)

# most_common_title = "Best book title"

# my_other_string = f"The most common title in the database is {most_common_title}"

# my_longer_string = my_string + "\n" +  my_other_string
# print(my_longer_string)
# pi = 3.141592653589793

# #print(f"The number pi = {pi:.3}")

# # how many words in there title
# length_of_title = [1, 2, 1, 4, 6, 1, 10]
# mean_length_of_title = sum(length_of_title)/len(length_of_title)

# #print(f"The mean length of the title is {mean_length_of_title}")
# #print(f"The mean length of the title is {mean_length_of_title:.4}")

# empty = ""

# if len(most_common_title) < 100:
# 	print("Title isn't too long")

# # print a message if the mean_length_of_title is greater than 6

# if (mean_length_of_title) > 6:
# 	print("Not too bad")
# else:
# 	print("Titles are a bit short...")

# # change this variable from mean_length_of_title to a few others in the file and see of they evaluate as True or False

# if empty:
# 	print(f"{empty} evaluated to True")
# else:
# 	print(f"{empty} evaluated to False")

# if 2 in length_of_title:
# 	print("Some titles only have 2 letters")
# else:
# 	print("2 letter titles don't exist")

# # if statement to check if "book" is in my_other_string
# if "book" in my_other_string:
# 	print("I like book")
# else:
# 	print("Wher buk :(")

my_int = 4
my_string = f"My number is {my_int}"
print(my_string)

print(f"The type of my int is {type(my_int)}")

my_string = "-22"
my_int = int(my_string)
my_string = str(my_int)
print(my_int)

my_string = "3.14"
my_float = float(my_string)
print(my_float)


my_list = list(my_string)
print(my_list)