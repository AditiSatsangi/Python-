tuple= ("car",1,2,"bus")
print(len(tuple))
print(tuple[0])
print(tuple)
#Ordered , unchangeable,allow duplicates
y= list(tuple)
y[1]="Orange"
print(y)


x= tuple(y)