import random
def Generaterandom(upper):
    r= random.randint(1,upper)
    return r

def main():
    program= True
    num1= Generaterandom(10)
    num2= Generaterandom(10)
    result= num1*num2
    while program:
        ans= input("What is "+ str(num1) +"x" + str(num2)+ "=")
        
        if ans.isdigit():
            if int(ans)== result:
                print("Correct")
                program= False
                
            else:
                print("Inaccurate")
        else:
            print("Anser must be posuitive.")            

x=10
for x in range(x):
    main()