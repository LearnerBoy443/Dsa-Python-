# for non duplicate values

list1 = [56, 3, 2, 78, 6, 0]
print(list1)

for i in range(len(list1)):
    min_value = min(list1[i:])
    min_ind = list1.index(min_value)

    temp = list1[i]
    list1[i] = list1[min_ind]
    list1[min_ind] = temp

print(list1)

# for duplicate values also lets use maximum

list1 = [56, 3, 2, 3, 78, 0, 0]
print("unsorted list:", list1)

for i in range(len(list1)):
    max_value = max(list1[i:])
    max_ind = list1.index(max_value, i)
    if list1[i] != list1[max_ind]:
        temp = list1[i]
        list1[i] = list1[max_ind]
        list1[max_ind] = temp
    print(list1)


#without using min/max method OR Wwithout index method

#list1 = [56, 3, 2, 3, 78, 0, 0]
num=int(input("Enter the number of element"))
list1=[]
for i in range(num):
    elem=int(input(f"Enter the element for{i+1}"))
    list1.append(elem)

print("unsorted list:", list1)

for i in range(len(list1)):
    min_ind =i
    
    for j in range(i+1,len(list1)):
        if list1[j]<list1[min_ind]:
            min_ind=j
    #min_ind = list1.index(min_value, i)
    temp = list1[i]
    list1[i] = list1[min_ind]
    list1[min_ind] = temp
print(list1)

