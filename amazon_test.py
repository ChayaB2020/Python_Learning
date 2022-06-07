num=str(4596)
first=int(num[0])
for i in num:
    if int(i)>first:
        first=int(i)
lst=list(num)
if int(lst[0])==first:
    print("no need to swap")
else:
    temp=lst[0]
    ind=lst.index(str(first))
    lst[0]=lst[ind]
    lst[ind]=temp

num=''.join(lst)
print(num)
