def computepay(h, r) :
    pay = 0;
    if h <= 40.0 :
        pay = h*r;
    else :
        pay = h*r + (h-40.0)*r*0.5;
    
    return pay;

hrs = input("Enter the number of hours");
h = float(hrs);

rate = input("Enter the rate");
r = float(rate);

pay = computepay(h, r);

print(pay);

