import unittest
'''Just a module to check try and except block functions'''

def addition(val1,val2):
    '''This function will add two variables'''
    temp=1
    while temp:
        try:
            #val1,val2=map(int,input().split())
            temp=val1+val2
        except Exception as err:
            print(type(err))
            #continue
        else:
            return temp
        finally:
            print("Completed addition function")


#print(addition())

class test_addition(unittest.TestCase):
    def test_one(self):
        val1,val2=1,2
        res=addition(val1,val2)
        self.assertEqual(res,3)

    def test_two(self):
        val1,val2=2,3
        res=addition(val1,val2)
        self.assertEqual(res,5)

unittest.main()
