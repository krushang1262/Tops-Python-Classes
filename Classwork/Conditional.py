marks = int(input("Enter your Marks: "))

if marks >=91 and marks<=100:
    print("Grade A")
elif marks >= 71 and marks <=90:
    print("Grade B")
elif marks >=51 and marks <=70:
    print("Grade C")
elif marks >= 50 and marks <=35:
    print("Grade D")
elif marks <=34:
    print("Fail")
else:
    print("Invalid output")

# print("********************match catch********************************")

choice =  int(input("Enter your choice"))
match choice:
    case 1:
        print("gujarati")
    case 2:
        print("hindi")
    case 3:
        print("english")
    case 4:
        print("marathi")
    case _:
        print("Invalid choice")

# print("********************match catch*****calc***************************")

num1 = int(input("Enter number 1: "))
operation = input("Added a Calculation method ")
num2 = int(input("Enter number 2: "))

match operation:
    case "add":
        print("Added value is",num1+num2)
    case "min":
        print("minus value is",num1-num2)
    case "mult":
        print("multiply value is",num1*num2)
    case "div":
        print("division value is",num1/num2)
    case _:
        print("Invalid opeation your perform")