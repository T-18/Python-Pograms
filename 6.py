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
def Fibonacci(n):
    if n<0:
        print("Incorrect input")
    # First Fibonacci number = 0
    elif n==1:
        return 0
    # Second Fibonacci number = 1
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
print(Fibonacci(9))