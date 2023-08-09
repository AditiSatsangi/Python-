#class and object

class Human:
    def __init__(self,name,age):
        self.name= name
        self.age= age
        
    def methods(self): 
        print("Hi, I am " + self.name+".")
        
           
h1= Human("Sherlock", 6) 
h2= Human("Raja",9)
print(h1.name)  
print(h1.age) 
h1.methods()
h2.methods()

class kk:
    pass