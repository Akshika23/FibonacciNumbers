Noterms = int(input("Enter number of terms"));
n1,n2=0,1;
count =0;
if Noterms<0:
    print("Please enter positive integer");
elif Noterms == 1:
    print (n1);
else:
    while count < Noterms:
        print(n1);
        n = n1 +n2;
        n1 = n2;
        n2 = n;
        count +=1;
