import p1
import unittest

class TestMethods(unittest.TestCase):
    
    def test_range(self):
        ranges = [[["20", "10", "5"],["2","15","2"]], [["1000","1", "20"]]]
        self.assertEqual(p1.ConvertInput(11,0,ranges), 21)  #generic
        self.assertEqual(p1.ConvertInput(1,0,ranges), 1)   #not in range
        self.assertEqual(p1.ConvertInput(15,1,ranges), 1014) # 2nd range
        self.assertEqual(p1.ConvertInput(1,1,ranges), 1000) # matches start of a set
        self.assertEqual(p1.ConvertInput(16,0,ranges), 3) #matches end of the set
        self.assertEqual(p1.ConvertInput(17,0,ranges), 17) #checking off by 1


if __name__ == '__main__':
    unittest.main()
