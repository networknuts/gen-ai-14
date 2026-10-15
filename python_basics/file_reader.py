customer_file = input("Enter file name to read: ")

file_path = open(customer_file,"r")

for line in file_path.readlines():
    print(line.strip())

file_path.close()