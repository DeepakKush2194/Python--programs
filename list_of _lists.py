#Write a Python program to Remove empty List from List.
list_of_lists = [[1, 2, 3], [], [4, 5], [], [6, 7, 8], []]

# # Create an empty list to store non-empty sublists
# filtered_list = []
# # Loop through each sublist
# for sublist in list_of_lists:
#     # Check if the sublist is not empty
#     if len(sublist) > 0:
#         # Add it to the filtered list
#         filtered_list.append(sublist)
#print("List after removing empty lists:", filtered_list)

def lists(list_of_lists):
    filtered_list = [i for i in list_of_lists if i]
    return filtered_list
# Print the result
print("List after removing empty lists:", lists(list_of_lists))