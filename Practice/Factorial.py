# fact = 1
# for i in range(1,6):
#    fact = fact * i
# print(fact)
print("============================================================================================")

for i in range(1,11):
    num = i
    fact = 1
    while num != 0:
        fact*=num
        num-=1
    print(fact)