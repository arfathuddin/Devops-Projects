# names = tuple(input("Enter the names seprated by space :  \n"))
# print(names)

# Taking an arbitrary number of input strings
num_strings = int(input("Enter the number of strings: "))

string_list = []
for _ in range(num_strings):
    string_list.append(input("Enter a string: "))

# Creating a tuple from the input strings
string_tuple = tuple(string_list)

# Displaying the tuple
print("Tuple of strings:", string_tuple)
