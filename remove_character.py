#Write a Python program for removing i'th character from a string
def remove_char(str,i):
    if i < 0 or i >= len(str):
        print(f"Invalid index {i}. The string remains unchanged.")
        return str
    result_str = str[:i] + str[i+1:]
    return result_str

str = input("Enter a string:")
i = int(input("Enter index of character to remove:"))
print(remove_char(str,i))