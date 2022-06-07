import re
def check_palindrome(num):
    val_palindrome=False
    rev=0
    temp=num
    while temp>0:
        dig=temp%10
        rev=rev*10+dig
        temp=temp//10
    if rev==temp:
        val_palindrome=True
    return val_palindrome

def getSumOfDoubleBasePalindromes(maximum):
    # Write your code here
    val_sum=0
    for i in list(range(1,maximum+1)):
        num_binary=bin(i)
        num_binary_val=re.search(r'^0b(.*)',num_binary).group(1)
        num_binary_val=int(num_binary_val)
        result_bin=check_palindrome(num_binary_val)
        result_dec=check_palindrome(i)
        if result_bin and result_dec:
            val_sum+=i
        else:
            continue

    return val_sum

a=getSumOfDoubleBasePalindromes(5)
print(a)