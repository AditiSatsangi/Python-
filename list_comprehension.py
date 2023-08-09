fruits= ["apples","bananas","kiwi","mango"]

newfruits= [x for x in fruits if x!= "bananas"]
print(newfruits)

food= [x for x in range(10)]
print(food)

upper_fruit= [x.upper() for x in fruits]
print(upper_fruit)

fru= [ x if x== "apples" else "kiwi" for x in fruits]
print(fru)