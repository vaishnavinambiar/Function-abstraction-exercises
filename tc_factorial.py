import unittest

def recur_factorial(n):
   if n ==1:
      return n
   else:
      return n*recur_factorial(n-1)

class MyTest(unittest.TestCase):
    def test1_fact(self):
        self.assertEqual(recur_factorial(5), 120)
    def test2_fact(self):
        self.assertEqual(recur_factorial(2), 3)
        

if __name__ == '__main__':
    unittest.main()
