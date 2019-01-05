text = "X-DSPAM-Confidence:    0.8475";

pos = text.find(':');
substring = text[pos+1:];
snum = substring.strip();

num = float(snum);

print(snum);
