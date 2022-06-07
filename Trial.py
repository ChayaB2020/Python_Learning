import re
print("This is the start of code")

with open("Check_docu.txt",'r',encoding='utf-8') as f:
    for line in f.readlines():
        print(line)
        my_value=re.search(r'\w+\d+',line)
        if(my_value):
            print(my_value.group(0))
    print("Inside with method")

print("This is the end of code")
