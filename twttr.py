
# Ask the user to input text
user_input = input("input: ")

# Print the same text but with all vowels omitted
print("Output: ", end="")
for l in user_input:
    if l not in "aAeEiIoOuU":
        print(c, end="")
print()

