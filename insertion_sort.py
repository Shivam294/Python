#Insertion Sort
def insertion_sort(input_list):
    for i in range(1, len(input_list)):
        j=i-1
        nxt_element=input_list[i]
        while(input_list[j]>nxt_element) and (j>=0):
            input_list[j+1]=input_list[j]
            j=j-1
        input_list[j+1] = nxt_element
    return input_list

n=int(input("Enter n:"))
unsorted_list=[]
for i in range (n):
    unsorted_list.append(int(input("Enter element: ")))
print("Unsorted List: ",unsorted_list)
print("Sorted List: ", insertion_sort(unsorted_list))
