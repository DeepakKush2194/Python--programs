#Writing in file
# with open("practice.txt","w") as f:
#     f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java.")

#Replace all occurance of a word in file
# with open("practice.txt","r") as f:
#     data = f.read()
# new_data = data.replace("Java", "Python")
# #print(new_data)
# with open("practice.txt","w") as f:
#     f.write(new_data)

#Seaerch for a word in file
# def check_for_word(file_name, word):
#     with open(file_name,"r") as f:
#         data = f.read()
#         if word in data:
#             print("Found")
#         else:
#             print("Not Found")
# check_for_word("practice.txt","learning")

#First occurance of word in line
# def check_for_line(file_name,word):
#     with open(file_name,"r") as f:
#         line_num = 1
#         while True:
#             data = f.readline()
#             if not data: #End of file
#                 break
#             if word in data:
#                 print(f"Line {line_num}: {data.strip()}")
#                 return line_num
#             line_num += 1
#     return -1         
# check_for_line("practice.txt","learning")

#From a file containing numbers separated by comma, print the count of even numbers.
# with open("demo.txt","w") as f:
#     f.write("1,2,5,66,87,99,102")
# count = 0
# with open("demo.txt","r") as f:
#     data = f.read()
#     nums = data.split(",") #split the string in substrings
#     for val in nums:
#         if(int(val) % 2 == 0):
#             count += 1
# print(count)  