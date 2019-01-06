
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

avg = 0.0;
count = 0;

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos = line.find(':');
    substring = line[pos+1:];
    snum = substring.strip();

    num = float(snum);
    avg += num;
    count = count + 1;

favg = avg/count;

print("Average spam confidence:" , favg)
