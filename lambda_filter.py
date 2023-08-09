
#lamda
x= lambda a,b: a+b
print(x(5,30))

def f1(n):
    return lambda a: a*n

doub= f1(2)
print(doub(11))

#filter usage
def prime(x):
    for n in range(2,x):
        if x%n==0:
            return False
        else:
            return True
            
filtered= filter(prime,range(10))
print("Prime No. are: ", list(filtered))

#map function
def square(x):
    return x*x

numbers=[ 1 ,2,3,4,5]
listsquares= map(square, numbers)
print(list(listsquares))

