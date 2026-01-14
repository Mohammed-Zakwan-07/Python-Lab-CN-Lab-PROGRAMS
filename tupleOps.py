def tupleOps():
    my_tuple = (10, 20, 30, 40, 50, 60, 70)
    print("Tuple created!")

    print("\na) Elements in the tuple are:", my_tuple)

    n = int(input("\nb) Enter the value to search: "))
    if n in my_tuple:
        print(f"{n} is in the tuple")
    else:
        print(f"{n} is not in the tuple")

    print(f"\nc) Length of the tuple is {len(my_tuple)}")

tupleOps()
