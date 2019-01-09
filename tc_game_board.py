import unittest


class Testingstring(unittest.TestCase):
    def test_horizontal(self):
        a = 'some'
        b = 'some'
        self.assertEqual(a, b)

    def test_vertical(self):
        a = True
        b = True
        self.assertEqual(a, b)

    def test1_horizontal(self):
        a= 'bat'
        b= 'cat'
        self.assertEqual(a,b)
        

if __name__ == '__main__':
    unittest.main()

    



 
