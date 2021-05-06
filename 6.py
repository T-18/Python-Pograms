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
text = 'Text with special character (0#$%^*UIJKNHJCH^)'
from string import printable
if set(text).difference(printable):
    print('Text has special characters.')
else:
    print("Text does not have special characters.")