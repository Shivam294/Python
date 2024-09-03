my_list=[10,1,8,3,5]
#sortList=my_list.sort()
#print("Sorted List: ",sortList)
for i in range(0,len(my_list)-1):
    my_list[i], my_list[len(my_list)-1-i]=my_list[len(my_list)-1-i], my_list[i]
    if i==len(my_list)-1-i:
        break
print("Swapped List/Reversed:",my_list)