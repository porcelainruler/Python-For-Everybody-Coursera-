fname = input("Enter file name: ")
fh = open(fname)

lst = list()
for line in fh:
    line = line.rstrip();
    wrds = line.split();
    for wrd in wrds :
        if not wrd in lst :
            lst.append(wrd);

lst.sort();            
print(lst)
