num_of_strings = int(input("enter the count of strings : \n"))
string_list= []
for _ in range(num_of_strings):
    string_list.append(input("enter the string :  \n"))

string_tuple = tuple(string_list)
print( "<======= print the strign list ===========>")
print(string_list)
print( "<======= print the type of list ===========>")
print(type(string_tuple))