"""File content difference"""
first_file = open("file_1.txt")
second_file = open("file_2.txt")

first_list = first_file.readlines()
second_list = second_file.readlines()

for i in first_list:
    if i not in second_list:
        print(i)

first_file.close()
second_file.close()

