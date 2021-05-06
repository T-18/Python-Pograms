#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      TANU
#
# Created:     06/02/2021
# Copyright:   (c) TANU 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import math
# If 'X' is perfectly quare
def isPerfectSquare(x):
   s = int(math.sqrt(x))
   return s*s == x
# If 'n' is a Fibonacci Number
def isFibonacci(n):
   return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)
for i in range(1,11):
   if (isFibonacci(i) == True):
      print (i,"is a Fibonacci Number")
   else:
      print (i,"is a not Fibonacci Number")
