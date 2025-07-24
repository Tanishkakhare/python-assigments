with open("output.txt", "w") as file:
    data = input("Enter text to write to the file: ")
    file.write(data + "\n")
    print("Data successfully written to output.txt")

with open("output.txt", "a") as file:
    more_data = input("Enter more text to append to the file: ")
    file.write(more_data + "\n")
    print("Data successfully append to output.txt")


with open("output.txt", "r") as file:
    content = file.read()
    print("\nFinal content of output.txt:")
    print(content)