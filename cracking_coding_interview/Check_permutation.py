#Given two strings, write a method to decide if one is a permutation of the other.
def sorting(s):
    return sorted(s)

def permutation(s1,s2):
    if len(s1) != len(s2):
        return False
    elif sorting(s1) == sorting(s2):
        return True
    else:
        return False

print(permutation("jdjsadio","adiojdjs"))