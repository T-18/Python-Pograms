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
list = ['xtanu', 'xloves', 'pizza', 'xit', 'is', 'best']
print("The original list : " + str(list))
pref = 'x'
for word in list[:]:
    if word.startswith(pref):
        list.remove(word)
print("List after removal of Kth character of each string : " + str(list))