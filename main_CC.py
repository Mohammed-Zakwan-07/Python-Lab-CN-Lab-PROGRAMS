import Currency_converter as cc


while True:
    print("----Currency Converter-------")
    print("1. USD to INR.")
    print("2. INR to USD.")
    print("3. USD to EUR.")
    print("4. EUR to USD.")
    print("5. EUR to INR.")
    print("6. INR to EUR.")
    
    ch = input("Enter your choice. \n")
    
    amount = float(input("Enter the amount. \n"))
    
    if ch == "1":
        print(f"${amount} = ₹{cc.usd_to_inr(amount):.2f}.")
        
    
    elif ch == "2":
        print(f"₹{amount} = ${cc.inr_to_usd(amount):.2f}.")
        
    
    elif ch == "3":
        print(f"${amount} = €{cc.usd_to_eur(amount):.2f}.")
        
    
    elif ch == "4":
        print(f"€{amount} = ${cc.eur_to_usd(amount):.2f}.")
        
    
    elif ch == "5":
        print(f"€{amount} = ₹{cc.eur_to_inr(amount):.2f}.")
        
    
    elif ch == "6":
        print(f"₹{amount} = €{cc.inr_to_eur(amount):.2f}.")
        
    elif ch == "7":
        print("Exiting....")
        break
    
    else:
        print("Invalid choice")