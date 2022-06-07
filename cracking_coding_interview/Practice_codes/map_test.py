def square(num):
    return num**2


my_list=[1,2,3,4]
for i in map(square,my_list):
    print(i, end=" ")
