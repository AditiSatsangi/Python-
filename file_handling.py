"""f =  open("Adi.txt", "r")
print(f.read(0))#Peinr firrst letter to

print(f.read())  #print whole file
print(f.readline())# print first  line
for x in f:#Loop for printing each line
    print(x)
f.close() 

"""

import os
#f= open("Aditi.txt", "w")
#os.remove("Aditi.txt")
import os
if os.path.exists("Newfileeee.txt"):
   os.remove("Newfileeee.txt")
else:
    print("File is not present.")   

