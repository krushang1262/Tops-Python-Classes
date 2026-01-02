number = 120
tmp = number
sum = 0 

while number !=0:
    rem = number %10
    sum = (sum*10)+rem
    number = number//10
    
    if tmp == sum:
        print("Armstrong")
    else:
        pass
        # print("not armstrong")