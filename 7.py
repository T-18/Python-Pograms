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
def Remove(string, i):
    a = string[ : i]
    b = string[i + 1: ]
    return a + b
if __name__ == '__main__':
    string = "Tanu18"
    i = 5
    print(Remove(string, i))