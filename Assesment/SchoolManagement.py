import json
forrecords = {}
data = {}
ch = 'yes'

while ch != 'no':
    choice = int(input("""
                1: New Admission
                2: View Students Details
                3: Update Student Info
                4: Remove Student Record
                """))


    if choice == 1:
        print("*** Enter the Student Details ***")
        
        studentId = 1
        studentNm = input("Enter Student Name: ")
        print("*** Enter the age between 5 to 18 ***")
        studentAge = int(input("Enter Student Age: "))
        print("*** Enter the class 1 to 12 ***")
        studentclass = int(input("Enter Student Class: "))
        print("*** Enter the mobile 10 digit ***")
        Mobile = input("Enter Student guardian's mobile number: ")
         
        if len(Mobile) != 10 or len(Mobile) > 10:
            print("Enter the Proper 10 digit Mobile Number. ")
            break
        
        if studentAge not in range(5,19):
            print(f"Invalid Age {studentAge}")
            break
        
        if studentclass in range(1,13):
            if studentclass > 12:
                print("Invalid Standard")
                break
            else:
                print("Admission Successfully")
                
            forrecords.update({"Id":studentId, "name":studentNm, "age":studentAge, "class":studentclass, "mobile":Mobile})
            
            try:
                with open('D:/Python Practice/Assesment/School.json', "r") as sr:
                    data = json.load(sr)
            except:
                forrecords = {}

            studentId = str(len(data) + 1)

            data[studentId] = {
                "name": studentNm,
                "age": studentAge,
                "class": studentclass,
                "mobile": Mobile
            }

            with open('D:/Python Practice/Assesment/School.json', "w") as sc:
                json.dump(data, sc, indent=4)
        else:
            print("Invalid class enter")            
        
    elif choice == 2:
        with open('D:/Python Practice/Assesment/School.json', "r") as reader:
            print(reader.readlines())
            
    elif choice == 3:
        print("")
                
    elif choice == 4:
        print("")
    
    ch = input("are you continue yes or no ? ")