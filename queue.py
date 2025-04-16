queue = []
n = int(input("Enter the size of Queue: "))


def enqueue():
    if len(queue) == n:
        print("The Queue is full")
    else:
        element = input("Enter the element: ")
        queue.append(element)
        print("The entered element is:", element)


def dequeue():
    if len(queue) == 0:
        print("The Queue is Empty")
    else:
        e = queue.pop(0)
        print("The Element popped is:", e)


def isFull():
    if len(queue) == n:
        print("The Queue is full")
    else:
        print("The Queue is not full")


def isEmpty():
    if len(queue) == 0:
        print("The Queue is empty")
    else:
        print("The Queue is not empty")


def display_queue():
    print("Current Queue:", queue)


while True:
    print("\nEnter the Operation:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. isFull")
    print("4. isEmpty")
    print("5. Display Queue")
    print("6. Quit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        isFull()
    elif choice == 4:
        isEmpty()
    elif choice == 5:
        display_queue()
    elif choice == 6:
        print("Exiting program. Goodbye!")
        break
    else:
        print("Enter the correct operation")
