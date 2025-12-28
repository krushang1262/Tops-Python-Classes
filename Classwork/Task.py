number = int(input("Enter a number: "))

for i in range(1,11):
    tab = number * i
    print(number, '*',i,'=', tab)
print("*****************table****************************")

for i in range(1,101):
    if i%2==0:
        print(i, "is Even")
    else:
        print(i,"is Odd")
print("****************odd/even*****************************")