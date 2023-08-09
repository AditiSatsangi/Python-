#unordered, changeable, don't alow duplicates\
    
dictt= { 
        "name":"Raj",
        "age":26,
        "DOB": "12-2-45",
        "fruits":["Orange","pineapple"]
        }
print(dictt)

dictt["name"]= "Bike"
dictt.update({"age":90})
dictt.pop("age")
print(dictt)