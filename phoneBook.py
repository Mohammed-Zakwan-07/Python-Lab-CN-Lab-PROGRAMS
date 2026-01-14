def phoneBook():
    phone_book = {}
    
    while True:
        print("----------- Phone Book -----------")
        print("1. Add a contact")
        print("2. Search a contact")
        print("3. Delete a contact")
        print("4. View all contacts")
        print("5. Exit")
        
        ch = input("Choose the operation you want to perform: ")
        
        if ch == '1':
            name = input("Enter the name: ")
            no = input("Enter the phone: ")
            phone_book[name] = no
            print("Contact added!\n")
        
        elif ch == '2':
            search = input("Enter the name: ")
            result = phone_book.get(search, "Not found")
            print(f"Number: {result}\n")
        
        elif ch == '3':
            name_to_delete = input("Enter the name you want to delete: ")
            if name_to_delete in phone_book:
                phone_book.pop(name_to_delete)
                print("Deleted successfully!\n")
            else:
                print("Contact not found!\n")
        
        elif ch == '4':
            print("\n------ Phone Book ------")
            if not phone_book:
                print("No contacts saved.\n")
            else:
                for name, number in phone_book.items():
                    print(f"{name}: {number}")
                print()
        
        elif ch == '5':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice! Please try again.\n")

phoneBook()
