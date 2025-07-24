try:
    file1 = open('sample.txt',"r")
    read = file1.readline()
    read1 = file1.readline()
    print("Reading file contents:")
    print("line 1:",read)
    print("line 2:",read1)
except FileNotFoundError:
    print("The file 'sample.txt' was not found")