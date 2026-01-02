num = 121
temp = num
rep = 0

while num !=0:
    rem = num%10
    rep+=(rem**3)
    num = num//10

if temp == rep:
    print("armstrong")
else:
    print("not armstrong")