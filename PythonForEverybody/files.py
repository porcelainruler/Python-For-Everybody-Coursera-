# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

for line in fh :
    trim = line.rstrip();
    string = trim.upper();
    print(string);
