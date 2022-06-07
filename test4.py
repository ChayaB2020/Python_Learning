class My_test():
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def addition(self):
        print(self.num1+self.num2)
    def multi(self):
        print(self.num1*self.num2)
        
#a=My_test(1,3)
#a.addition()
#a.multi()

def multiplication(my):
    mul=1
    temp=list(my.values())
    for i in temp:
        if isinstance(i,int):
            mul*=i
        else:
            continue
    return mul
    

my_dict={'a':1,'b':5,'c':6,'d':7,'e':8}
a=multiplication(my_dict)
print(a)