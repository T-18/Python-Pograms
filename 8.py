#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      TANU
#
# Created:     08/02/2021
# Copyright:   (c) TANU 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
str1=input("Enter first String with space :: ")
print(str1.split())
str2=input("Enter second String with (,) :: ")
print(str2.split(','))
str3=input("Enter third String with (:) :: ")
print(str3.split(':'))
str4=input("Enter fourth String with (;) :: ")
print(str4.split(';'))
str5=input("Enter fifth String without space :: ")
print([str5[i:i+2]for i in range(0,len(str5),2)])