def recur_factorial(n):
   if n ==1:
      return n
   else:
      return n*recur_factorial(n-1)
num = input("Enter the number: ")
if num<0:
   print "Factorial does not exist for negative numbers"
elif num == 0:
   print"Factorail of 0 is 1"
else:
   print"The factorial of",num,"is",recur_factorial(num)
