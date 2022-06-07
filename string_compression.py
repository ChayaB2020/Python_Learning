#Implement a method to perform basic string compression using the counts of repeated 
# characters.ex: the string aabcccccaaa would become a2b1c5a3.If compressed string would 
# not become smaller than the original one method will return original string.

def comp(s):
    res=[]
    count=0
    for i in range(len(s)):
        if i!=0 and s[i]!=s[i-1]:
            res.append(str(s[i-1])+str(count))
            count=0
        count+=1
    res.append(str(s[-1])+str(count))

    return min(s, ''.join(res),key=len)

print(comp("aabcccccaaa"))