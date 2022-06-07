#program to check if a string has all unique characters without using additional data structures.
#method1
def unique(s):
    #converting list/string to set will have time complexity of O(N) and space O(1)
    if len(set(s))==len(s):
        print("Unique")
    else:
        print("not unique")
    

#unique("aabbccd")

#method 2,having time complexity O(N) and space O(1)
def unique_2(s):
    # considering ASI characters which is having total of 128 characters
    if len(s)>128:
        return False
    res=[False]*128
    for i in s:
        val=ord(i)
        if res[val]==True:
            return False
        res[val]=True
    return True

#print(unique_2("aabbccd"))

#method 3 when chars are Unicode chars, and there is total 1,44,697 unicode chars present
#having time complexity O(N) and space O(1)
def unique_3(s):
    my_dict={}
    for i in s:
        if i in list(my_dict.keys()):
            return False
        my_dict[i]=0
    return True


print(unique_3("abcd"))