try:
    
    input_file = input("Enter the name of the input file: ")
    
    with open("findings.txt", "w") as f:
        data = f.write("This is a very interesting topic.\nI am enjoying it.")
        print("File written successfully.")
    

    with open("findings.txt", "r") as f:
        modified_content = f.read().upper()
    

    with open("findings1.txt", "w") as f1:
        f1.write(modified_content)
        print("File modified successfully.")

except FileNotFoundError:
    print("The file was not found.")
except IOError:
    print("An error occurred while writing to the file.")


