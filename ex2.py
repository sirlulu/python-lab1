
string = input("Insert a string: \n")
length = len(string)
if length < 2:
    print(" \n");

else:
   # print("%s%s%s%s" %(string[0],string[1],string[length-2],string[length-1]))
    print( string[0:2] + string[-2:])
