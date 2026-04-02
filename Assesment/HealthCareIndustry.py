time = [10,11,12,2,3]
db = {}

import json

ch = 'yes'
while ch != 'no':
    choice = int(input("""
                1: Booking appoinment
                2: Cancel appoinment
                3: View all appoinment   
                    """))

    if choice ==1:
        print("*** Booking appoinment ***")
        
        name = input("Enter Your Name: ")
        phone = input("Enter Your Phone: ")
        dr = input("Enter Your dr. name: ")
        slot = int(input(f"Enter Your slot:{time} "))
        
        k = []
        for s in db.values():
            k.append(s['slot'])
            
            if slot in k:
                print(f"appoinment already taken")
        else:
          db.update({phone: {"name":name,"dr":dr,"slot":slot}})
          
          with open('D:/Python Practice/Assesment/HealthCare.json',"r") as f:
              json.load(f)
          
          with open('D:/Python Practice/Assesment/HealthCare.json',"w") as f:
              json.dump(db,f)
        
    elif choice == 2:
        print("*** Cancel appoinment ***")
        phone = input("Enter Your Phone: ")
        if len(phone) == 10:
            db.pop(phone)
        else:
            print("enter 10 digit number")
    elif choice == 3:
        print("*** View all appoinment ***")
        print(db)
    else:
        print("Invalid Choice:")
    
    ch = input("do you want to continue yes or no ?")