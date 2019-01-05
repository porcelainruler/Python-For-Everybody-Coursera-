str = "The graet wall of china is such a piece of shit";
lst = [];
print(lst)

wrds = str.split();
print(wrds);
for wrd in wrds :
    if not wrd in lst :
        print(wrd)
        lst.append(wrd);

print(lst)
