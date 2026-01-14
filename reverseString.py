def reverse_with_slicing(s):
    return s[::-1]


def reverse_with_loop(s):
    reversed_string = ""
    for char in s:
        reversed_string = char + reversed_string
    return reversed_string


text = input("Enter a string : ")

print("Original string:", text)
print("Reversed using slicing:", reverse_with_slicing(text))
print("Reversed using loop:", reverse_with_loop(text))
