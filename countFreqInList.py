def countFreqInList():
    user_input = input("Enter numbers separated by commas: ")
    num_list = [int(x) for x in user_input.split(",")]

    target = int(input("Enter the number you want to find the frequency of: "))

    print(f"The number {target} appears {num_list.count(target)} times.")

countFreqInList()
