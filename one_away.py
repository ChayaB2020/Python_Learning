#Given two strings,write a function to check if they are one edit away.
#This is having time complexity of O(N) because of for loop and some contacts because of if conditions

def one_away(s1,s2):
    if len(s1)==len(s2) and s1==s2:
        return True
    elif len(s1)==len(s2)+1 or len(s2)==len(s1)+1 or len(s1)==len(s2):
        flag=0
        if len(s1)>len(s2):
            for i in s1:
                if i not in s2:
                    flag+=1
        else:
            for i in s2:
                if i not in s1:
                    flag+=1
        if flag>1:
            return False
        else:
            return True
    else:
        return False

print(one_away("pale","bake"))
