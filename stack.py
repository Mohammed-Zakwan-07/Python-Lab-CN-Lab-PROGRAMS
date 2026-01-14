stack = []

def push():
    item = input("Enter element to push: ")
    stack.append(item)   # built-in function
    print("Element pushed")

def pop():
    if len(stack) == 0:
        print("Stack is empty. Cannot pop.")
    else:
        print("Popped element:", stack.pop())  # built-in function

def peek():
    if len(stack) == 0:
        print("Stack is empty.")
    else:
        print("Top element:", stack[-1])

def is_empty():
    if len(stack) == 0:
        print("Stack is empty.")
    else:
        print("Stack is not empty.")

def display():
    if len(stack) == 0:
        print("Stack is empty.")
    else:
        print("Stack elements:")
        for i in range(len(stack) - 1, -1, -1):
            print(stack[i])

# Menu-driven program
while True:
    print("\nSTACK OPERATIONS")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Check if Empty")
    print("5. Display Stack")
    print("6. Exit")

    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        push()
    elif choice == 2:
        pop()
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
 