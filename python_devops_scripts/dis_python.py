# student_details = {
#     "name" : "arfath",
#     "age"  : "29",
#     "class" : "python"
# }
# print("====== print Name of student ==========")
# print(student_details["name"])
# print("====== print age of student ==========")
# print(student_details["age"])
# print("====== print Class of student ==========")
# print(student_details["class"])


''' below syntax is to show how to write list of dictioneris'''

ec2_instances_info = [
    {
        "id" : "instance-002",
        "type" : "t2.medium"
    },

    {
       "id" : "instance-002",
        "type" : "t2.medium" 
    },
    {
        "id" : "instance-003",
        "type" :"t2.Xlarge"
    }
]

print(ec2_instances_info[2]["id"],"\n",ec2_instances_info[2]["type"])