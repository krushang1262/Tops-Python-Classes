num = 153
temp = num
sum =0

while num !=0:
    rem = num%10
    sum+=(rem**3)
    num = num//10
    
if temp == sum:
    print("armstrong")
else:
    print("not armstrong")