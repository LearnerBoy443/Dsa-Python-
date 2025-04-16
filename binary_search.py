def binary_search(list1,key):
    low=0
    high=len(list1)-1
    mid=(low+high)//2
    Found=False
    while low<=high and not Found:
        mid=(low+high)//2
        if key==list1[mid]:
            Found=True
        elif key<list1[mid]:
            high=high-1
        elif key>list1[mid]:
            low=mid+1
    if Found==True:
        print(f"Element {key} is found at index {mid}, value = {list1[mid]}")
    else:
        print("Element not found")
        
num = int(input("Enter the number of element"))
list1 = []
for i in range(num):
    list1.append(int(input()))
print(f"Unsorted List:{list1}")
list1.sort()        #here we can use other sorting method instead of direct "sort()""
print(f"Sorted List:{list1}")
key=int(input("Enter a Key: "))
binary_search(list1,key)
