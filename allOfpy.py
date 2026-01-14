"""
===========================================================
      COMPLETE PYTHON MASTER FILE (ALL TOPICS INCLUDED)
===========================================================
"""

# ---------------------------------------------------------
# 1. DATA TYPES
# ---------------------------------------------------------
def demo_datatypes():
    print("\n--- DATA TYPES ---")
    a = 10
    b = 3.14
    c = "Hello"
    d = True
    e = [1, 2, 3]
    f = (4, 5, 6)
    g = {1, 2, 3}
    h = {"name": "Alice", "age": 25}

    print(type(a), type(b), type(c))
    print(type(e), type(f), type(g), type(h))


# ---------------------------------------------------------
# 2. BUILT-IN FUNCTIONS
# ---------------------------------------------------------
def demo_builtins():
    print("\n--- BUILT-IN FUNCTIONS ---")
    nums = [1, 2, 3, 4]
    print("Length:", len(nums))
    print("Sum:", sum(nums))
    print("Max:", max(nums))
    print("Min:", min(nums))


# ---------------------------------------------------------
# 3. CONTROL STATEMENTS
# ---------------------------------------------------------
def demo_control():
    print("\n--- CONTROL STATEMENTS ---")

    for i in range(5):
        if i == 2:
            continue
        if i == 4:
            break
        print("For i =", i)

    count = 3
    while count > 0:
        print("While count =", count)
        count -= 1


# ---------------------------------------------------------
# 4. FUNCTIONS
# ---------------------------------------------------------
def add(a, b=5):
    return a + b

def demo_functions():
    print("\n--- FUNCTIONS ---")

    print(add(10))
    print(add(10, 20))

    def show_all(*args, **kwargs):
        print("ARGS:", args)
        print("KWARGS:", kwargs)

    show_all(1, 2, 3, name="Alice")

    square = lambda x: x * x
    print("Lambda:", square(6))


# ---------------------------------------------------------
# 5. EXCEPTION HANDLING
# ---------------------------------------------------------
def demo_exceptions():
    print("\n--- EXCEPTION HANDLING ---")
    try:
        print(10 / 0)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    finally:
        print("Finally block executed")


# ---------------------------------------------------------
# 6. OOP — ENCAPSULATION
# ---------------------------------------------------------
class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amt):
        self.__balance += amt

    def get_balance(self):
        return self.__balance

def demo_encapsulation():
    print("\n--- ENCAPSULATION ---")
    acc = BankAccount()
    acc.deposit(500)
    print("Balance:", acc.get_balance())


# ---------------------------------------------------------
# 7. OOP — INHERITANCE & POLYMORPHISM
# ---------------------------------------------------------
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Bark"

def demo_inheritance_polymorphism():
    print("\n--- INHERITANCE & POLYMORPHISM ---")
    d = Dog()
    print("Dog says:", d.speak())


# ---------------------------------------------------------
# 8. OOP — ABSTRACTION
# ---------------------------------------------------------
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

def demo_abstraction():
    print("\n--- ABSTRACTION ---")
    c = Circle(5)
    print("Circle area:", c.area())


# ---------------------------------------------------------
# 9. OOP — CLASS & STATIC METHODS
# ---------------------------------------------------------
class Student:
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

    @classmethod
    def total_students(cls):
        return cls.count

    @staticmethod
    def greet():
        return "Hello Student!"

def demo_class_static():
    print("\n--- CLASS & STATIC METHODS ---")
    s1 = Student("Alice")
    s2 = Student("Bob")
    print("Total students:", Student.total_students())
    print(Student.greet())


# ---------------------------------------------------------
# 10. DATA STRUCTURES — LIST, TUPLE, SET, DICT
# ---------------------------------------------------------
def demo_collections():
    print("\n--- COLLECTIONS ---")
    lst = [1, 2, 3]
    tpl = (4, 5, 6)
    st = {1, 2, 2, 3}
    dct = {"a": 1, "b": 2}

    print(lst)
    print(tpl)
    print(st)
    print(dct)


# ---------------------------------------------------------
# 11. STACK
# ---------------------------------------------------------
def demo_stack():
    print("\n--- STACK (LIFO) ---")
    stack = []
    stack.append(10)
    stack.append(20)
    print("Popped:", stack.pop())


# ---------------------------------------------------------
# 12. QUEUE
# ---------------------------------------------------------
from collections import deque

def demo_queue():
    print("\n--- QUEUE (FIFO) ---")
    q = deque()
    q.append(10)
    q.append(20)
    print("Dequeued:", q.popleft())


# ---------------------------------------------------------
# 13. LINKED LIST
# ---------------------------------------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

def demo_linked_list():
    print("\n--- LINKED LIST ---")
    ll = LinkedList()
    ll.insert(10)
    ll.insert(20)
    ll.insert(30)
    ll.display()


# ---------------------------------------------------------
# 14. SEARCHING — LINEAR & BINARY
# ---------------------------------------------------------
def linear_search(arr, key):
    for i, v in enumerate(arr):
        if v == key:
            return i
    return -1

def binary_search(arr, key):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def demo_searching():
    print("\n--- SEARCHING ---")
    print("Linear Search:", linear_search([5, 10, 15], 10))
    print("Binary Search:", binary_search([10, 20, 30, 40], 30))


# ---------------------------------------------------------
# 15. SORTING — BUBBLE SORT
# ---------------------------------------------------------
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def demo_sorting():
    print("\n--- SORTING ---")
    print("Bubble Sort:", bubble_sort([5, 3, 8, 2, 1]))


# ---------------------------------------------------------
# 16. RECURSION
# ---------------------------------------------------------
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def demo_recursion():
    print("\n--- RECURSION ---")
    print("Factorial 5:", factorial(5))


# ---------------------------------------------------------
# 17. FILE HANDLING
# ---------------------------------------------------------
def demo_file_handling():
    print("\n--- FILE HANDLING ---")
    with open("sample.txt", "w") as f:
        f.write("Hello file!")

    with open("sample.txt", "r") as f:
        print("File content:", f.read())


# ---------------------------------------------------------
# 18. MULTITHREADING
# ---------------------------------------------------------
import threading
def worker():
    print("Thread is running")

def demo_threading():
    print("\n--- MULTITHREADING ---")
    t = threading.Thread(target=worker)
    t.start()
    t.join()


# ---------------------------------------------------------
# 19. MULTIPROCESSING
# ---------------------------------------------------------
import multiprocessing
def process_worker():
    print("Process running")

def demo_multiprocessing():
    print("\n--- MULTIPROCESSING ---")
    p = multiprocessing.Process(target=process_worker)
    p.start()
    p.join()

# ---------------------------------------------------------
# RUN EVERYTHING
# ---------------------------------------------------------
if __name__ == "__main__":
    demo_datatypes()
    demo_builtins()
    demo_control()
    demo_functions()
    demo_exceptions()

    demo_encapsulation()
    demo_inheritance_polymorphism()
    demo_abstraction()
    demo_class_static()

    demo_collections()
    demo_stack()
    demo_queue()
    demo_linked_list()

    demo_searching()
    demo_sorting()
    demo_recursion()

    demo_file_handling()
    demo_threading()
    demo_multiprocessing()

    print("\n=== END OF PROGRAM ===")
