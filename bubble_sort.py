num = int(input("Enter the number of element"))
list1 = []
for i in range(num):
    list1.append(int(input()))
    
for i in range(len(list1)-1):
    for j in range(len(list1)-1):
        if list1[j]>list1[j+1]:
            temp=list1[j]
            list1[j]=list1[j+1]
            list1[j+1]=temp
            print(list1)
        else:
            print(list1)
        print()    
print(f"Sorted list{list1}")