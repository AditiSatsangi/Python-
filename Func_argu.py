list= ['car','bus', 'scooyter','truvk']
def loop(x):
    print(x*3)
    
    
def map_simple(c, list):
    for items in list:
        c(items)
        
map_simple(loop,list)        
