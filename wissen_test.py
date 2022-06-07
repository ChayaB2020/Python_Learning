def find_index(my_list):
    sum=0
    for i in my_list:
        sum+=i
    return sum

A = [15, 45, 8, 7]
temp=-1
for i in range(0,len(A)-1):
    if find_index(A[0:i])==find_index(A[i+1:]):
        temp=i
#print(temp)
left_sum=0
right_sum=0
for i in range(0,len(A)): 
    right_sum+=A[i]
for i in range(0,len(A)-1):
    right_sum-=A[i]
    if(left_sum==right_sum):
        print(i)
    left_sum+=A[i]