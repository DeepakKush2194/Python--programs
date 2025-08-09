#Write a Python program to find words which are greater than given length k
word_list = ["apple", "banana", "cherry", "date", "elderberry", "dragon-fruit"]
def find_words(word_list,k):
    words = [el for el in word_list if len(el) > k]
    return words
k = int(input("Enter number of word-lenght:"))
print(f"Words greater than {k} length: ",find_words(word_list,k))