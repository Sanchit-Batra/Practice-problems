num = int(input("enter your no."))
if num <= 1:
    print("not a prime no.")
else:
    for i in range(2, num):
        if num % i == 0:
            print("not prime")
            break
    else:
        print("prime")
