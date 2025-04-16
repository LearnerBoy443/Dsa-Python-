def insertion_sort(list1):
    for i in range(1,len(list1)):
        current_element=list1[i]
        pos=i
        while current_element<list1[pos-1] and pos>0:
            list1[pos]=list1[pos-1]
            pos=pos-1
        list1[pos]=current_element
        

num = int(input("Enter the no of element you want to add:"))
list1 = []
for i in range(num):
    list1.append(int(input()))
insertion_sort(list1)
print(list1)
