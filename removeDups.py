def remove_dups(input_list):
    unique_list = []
    
    for item in input_list:
        is_present = False
        
        for unique_item in unique_list:
            if item == unique_item:
                is_present = True
                break
        
        if not is_present:   # ← this must be outside the inner loop
            unique_list.append(item)
    
    return unique_list


my_list = ["apple", "banana", "mango", "apple", "banana", "grape"]
clean_list = remove_dups(my_list)
print(f"Original values: {my_list}")
print(f"clean_list :  {clean_list}")
