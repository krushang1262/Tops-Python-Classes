number = int(input("Enter a number: "))

for i in range(1,11):
    tab = number * i
    print(f"{number} * {i} = {tab}")
print("*****************table****************************")

for i in range(1,101):
    if i%2==0:
        print(i,"is Even")
    else:
        print(i,"is Odd")
print("****************odd/even*****************************")

for i in range(2,101):
    for j in range(2,i):
        if i%j==0:
            print(i,"is prime")
            break

    else:
        print(i,"is not prime")
                
print("****************prime number*****************************")