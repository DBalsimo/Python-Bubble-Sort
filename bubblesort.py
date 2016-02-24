#Bubble Sort

changed = True
passes = 0
list = [9,4,6,8,1,3,2,5,7,0]

print("Before: ",list)

while changed == True:

    changed = False
    passes += 1
    
    for i in range( len(list) - 1 ):
        if list[i] > list[i+1]:
            changed = True
            list[i], list[i+1] = list[i+1], list[i]
	
print("After: ",list,"\ntook",passes,"passes")
