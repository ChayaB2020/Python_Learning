import unittest

def addition(val1,val2):
    return val1+val2

class Testcases(unittest.TestCase):
    def test1(self):
        val1='a'
        val2='c'
        res=addition(val1,val2)
        self.assertEqual(res,'ac')

    def test2(self):
        a=1
        b=3
        res=addition(a,b)
        self.assertEqual(res,4)

if __name__=='__main__':
    unittest.main()
