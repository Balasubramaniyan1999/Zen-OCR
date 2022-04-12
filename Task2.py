#Q2 : Identify Phone numbers and email id in the list


#Identify Phone numbers in the list

import json
import re

json_file = open('task_input_list.json')
data_parsing = json.load(json_file)
phone_finding = re.findall(r"\w{3}-\w{3}-\w{4}",str(data_parsing))
print(phone_finding)


#Identify  email id in the list
json_file = open('task_input_list.json')
data_parsing = json.load(json_file)
email_finding = re.fullmatch( r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",str(data_parsing))
print(email_finding)