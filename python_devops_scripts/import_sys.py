import sys
# In this is writen to show how to import sys module and write if, elif, and else 
type = sys.argv[1]

if type == "t2.micro":
    print("it will cost you zero dollers")
elif type == "t3.micro":
    print("it will cost you 2 dollers")
elif type == "t4.micro":
    print("it will cost you 4 dollers")

else:
    print("please enter valide name")
