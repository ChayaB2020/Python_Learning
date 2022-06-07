def has_33(lst):
    for i,elem in enumerate(lst):
        if elem==3 and lst[i+1]==3:
            return True
        else:
            pass
    return False

def has_33_range(lst):
    for i in range(0,len(lst)-1):
        if lst[i]==3 and lst[i+1]==3:
            return True
        else:
            pass
    return False
def paper_doll(my_str):
    new_string=''
    for i in my_str:
        new_string+=i*3
    return new_string
def summer_69(lst):
    if 6 in lst:
        first=lst.index(6)
        last=lst.index(9)+1
        my_sub=lst[first:last]
    print(my_sub)
    #lst.remove(my_sub)
    for i in my_sub:
        lst.remove(i)
    print(lst)
    sum=0
    for i in lst:
        sum+=i
    return sum

def spy_game(lst):
    first=second=last=False
    for i in lst:
        if i==0 and not first:
            first=True
            continue
        if first and i==0:
            second=True
        if second and i==7:
            last=True
    if first and second and last:
        return True
    else:
        return False

res=spy_game([1,7,2,0,4,5,0])
print(res)
