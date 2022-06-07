#Given a string, write a function to check if it is a permutation of a palindrome.
def palindrome(s):
    my_set=set(s.lower())
    if " " in my_set:
        my_set.remove(" ")
    dict={}
    for i in my_set:
        dict[i]=s.lower().count(i)
    length=sum(tuple(dict.values()))
    for i in my_set:
        flag=0
        if length%2==0 and dict[i]%2!=0:
            return False
        elif length%2!=0 and dict[i]%2!=0:
            flag+=1
            
    if flag>1:
        return False
    else:
        return True

print(palindrome("Tact Coa"))
            
            