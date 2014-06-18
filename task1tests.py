import task1 as t1
import unittest

class TestSequenceFunctions(unittest.TestCase):
    def setup(self):
        t1.rates =[1,2,3,4]
        
    def test1(self):
        assert (t1.rates[0]==1))#test 1 fails gbp rate not 1
    
    def test2(self):
        assert(t1.conv(10,0,2) ==30)#test 2 fails gbp to usd failure
        assert(t1.conv(10,0,1)==20)#test2 fails gbp to eur fail
    
    def test3(self):
        assert(t1.conv(9,2,0)==3)#test 3 conversion fail from usd
        assert(t1.conv(20,1,0)==10)#test3 conversion fail from EUR
    
   
if __name__ == '__main__':
    unittest.main()
