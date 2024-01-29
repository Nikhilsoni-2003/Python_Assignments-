# "E:\f1.txt"
# def reverse_file_content(input_filename, output_filename):
#     with open(input_filename, 'r') as file:
#         content = file.read()

#     reversed_content = content[::-1]

#     with open(output_filename, 'w') as file:
#         file.write(reversed_content)

# input_filename = r'E:\f1.txt'  
# output_filename = r'E:\f1_reversed.txt'
# reverse_file_content(input_filename, output_filename)


# to store content in same file 

def reverse_file_content_inplace(filename):
    with open(filename, 'r') as file:
        content = file.read()

    reversed_content = content[::-1]

    with open(filename, 'w') as file:
        file.write(reversed_content)

file_to_reverse = r'E:\f1.txt'  
reverse_file_content_inplace(file_to_reverse)
