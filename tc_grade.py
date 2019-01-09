import unittest

def avg(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test_average(self):
        self.assertEqual(avg(3), 4)
    def test1_average(self):
        self.assertEqual(avg(3), 3)

def total(a,b):
    return a + b

class MyTest1(unittest.TestCase):
    def test_get_average(self):
        self.assertEqual(total(5,7), 12)
                    

if __name__ == '__main__':
    unittest.main()
