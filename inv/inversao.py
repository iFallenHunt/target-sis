# Step 1: Input the string
input_string = input("Enter a string: ")

# Step 2: Reverse the string
reversed_string = ""
for char in input_string:
    reversed_string = char + reversed_string

# Step 3: Output
print("Reversed string:", reversed_string)
