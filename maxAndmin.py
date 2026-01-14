def maxAndmin():
    n = int(input("How many numbers??\n"))
    list = []
    for i in range(n):
        a = float(input(f"Enter the {i+1} no: "))
        list.append(a)
        
    
    print(f"The largest number is {max(list)}")
    print(f"The smallest number is {min(list)}")
    
maxAndmin()