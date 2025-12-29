# number = int(input("Enter a number: "))

# for i in range(1,11):
#     tab = number * i
#     print(number, '*',i,'=', tab)
# print("*****************table****************************")

# for i in range(1,101):
#     if i%2==0:
#         print(i, "is Even")
#     else:
#         print(i,"is Odd")
# print("****************odd/even*****************************")

for i in range(1,101):
    rem =0
    for j in range(2,i):
        if i%j==0:
            rem=1
            break
    
    if rem ==0:
        print(i,"is prime no.")
    else:
        print(i,"is not prime no.")

print("****************prime number *****************************")