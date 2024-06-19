def write_to_file():
    
    user = input("Enter the text you want to write to the file: ")

    
    file_name = "python.txt"

    
    with open(file_name, "w") as file:
        file.write(user)

    print(f"The text has been written to {file_name}")


write_to_file()