queue = []

def enqueue():
    item = input("Enter element to insert: ")
    queue.append(item)   # insert at rear
    print("Element inserted")

def dequeue():
    if len(queue) == 0:
        print("Queue is empty. Cannot delete.")
    else:
        print("Deleted element:", queue.pop(0))  # remove from front

def peek():
    if len(queue) == 0:
        print("Queue is empty.")
    else:
        print("Front element:", queue[0])

def is_empty():
    if len(queue) == 0:
        print("Queue is empty.")
    else:
        print("Queue is not empty.")

def display():
    if len(queue) == 0:
        print("Queue is empty.")
    else:
        print("Queue elements:")
        for i in queue:
            print(i)

# Menu-driven program
while True:
    print("\nQUEUE OPERATIONS")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Check if Empty")
    print("5. Display Queue")
    print("6. Exit")

    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        peek()
    elif choice == 4:
        is_empty()
    elif choice == 5:
        display()
    elif choice == 6:
        print("Exiting program.")
        break
    else:
        print("Invalid choice.")
