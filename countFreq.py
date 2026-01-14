def count_frequency(user_input):
    frequency = {}
    
    for char in user_input:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
        
    return frequency


user_input = input("Enter a string")

result = count_frequency(user_input)

print("The character freqenuecy")
for char, count in result.items():
    print(f"{char} : {count}")