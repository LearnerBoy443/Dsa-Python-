stack=[]

def push():
    element=input("Enter the element")
    stack.append(element)
    print(stack)
    
def pop():
    if len(stack)==0:
        print("Stack is empty")
    else:
        e=stack.pop()
        print("Removed Element",e)
        print(stack)
        
def peek():
    if len(stack)==0:
        print("Stack is empty")
    else:
        top=stack[-1]
        print("The topmost element:",top)

def isEmpty():
    if len(stack)==0:
        print("Stack is empty")
    else:
        print("Stack is not empty")

while True:
    print("Enter the Operation:\n1.Push \n 2.Pop \n 3.Peek \n 4.isEmpty\n 5.Quit") 
    choice=int(input("Enter your choice"))
    if choice==1:
        push()
    elif choice==2: 
        pop()
    elif choice==3: 
        peek()
    elif choice==4:
        isEmpty()
    elif choice==5:
        break
    else:
        print("Enter the correct operation")      