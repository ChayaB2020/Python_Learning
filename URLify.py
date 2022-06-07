#Write a method to replace all the spaces in a string with %20.
#time complexity is O(n)
def urlify(s,length):
    ans=''
    for i in range(length):
        if s[i]==' ':
            ans+='%20'
        else:
            ans+=s[i]
    return ans

# here split function has time complexity of O(n) and space complexity is O(n)
def urlify1(s,length):
    lst=s.split(' ')
    return '%20'.join(lst)

print(urlify1("Mr John Smith ",14))