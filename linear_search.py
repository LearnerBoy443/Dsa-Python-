#for non duplicate values
def linear_search(list1,key):
    for i in range(len(list1)):
        if key==list1[i]:
            print(f"Element is found at index:{i}")
            break
    else:
        print("Element is not found")   
num = int(input("Enter the number of element"))
list1 = []
for i in range(num):
    list1.append(int(input()))
print(list1)
key=int(input("Enter the element to be searched:"))
linear_search(list1,key)

#for duplicate values


def linear_search(list1, key):
    list2=[]
    flag=False
    for i in range(len(list1)):
        if key == list1[i]:
            flag=True
            list2.append(i)
    if flag==True:
        print("the element is found at")
        for i in list2:
            print(i)
    else:
        print("Element is not found")


num = int(input("Enter the number of element"))
list1 = []
for i in range(num):
    list1.append(int(input()))
print(list1)
key = int(input("Enter the element to be searched:"))
linear_search(list1, key)
