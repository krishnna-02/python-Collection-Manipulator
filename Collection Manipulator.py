print("Welcome To The Student Data Organizer")
L = []
while True:
    print("Select The Option ->")
    print("1.Add Student")
    print("2.Display All Student")
    print("3.Update Student Information")
    print("4.Delete Student")
    print("5.Display Subjects Offered")
    print("6.Exit")

    choice = int(input("\nEnter The Option"))
    print("Your Option", choice)

    if choice == 1:
        print("Enter Student Detail")
        id =int(input("Student ID : "))
        Name =str(input("Name :"))
        Age =int(input("Age :"))
        Grade=str(input("Grade :"))
        Dob=input("Date Of Birth(YYYY-MM-DD) :")
        Sub=str(input("Subjects (Comma-separated) :"))
        Subject=[i.strip() for i in Sub.strip().split(',')]
        for i in subject:
            a.add(i)
        print("\nStudent Added Successfully")
        stu = {
            "id": sid,
            "Name": name,
            "Age": age,
            "Grade":grade,
            "Dob":dob,
            "Sub":sub
        }
        L.append(stu)
    elif choice == 2:
        for i in L:
            print("Student Id",i['id'],"| Name ",i['Name'],"| Age ",i['Age'],"| Grade ",i['Grade'],"| Date Of Birth",i['Dob'],"| Subject",i['Sub'])

    elif choice==3:
        print("Update Student Information\n")
        s=int(input("Enter Student Id To Update"))
        for i in L:
            if i["id"]==s:
                print("Enter Your Choice")
                print("1.Update Name")
                print("2.Update Age")
                print("3.Update Grade")
                print("4.Update DOB")
                print("5.Update Subject")
                choice=int(input("Enter Youe Choice -->"))
                if choice==1:
                    i['Name']=input("Enter the Name :")
                elif choice==2:
                    i['Age']=input("Enter The Age :")
                elif choice==3:
                    i['Grade']=input("Enter The Grade :")
                elif choice==4:
                    i['Dob']=input("Enter The DOB :")
                elif choice==5:
                    i['Sub']=input("Enter The Subject :")
                    subject = [i.strip() for i in Sub.strip().split(',')]
                    for i in subject:
                        a.add(i)
                else:
                    print("Invalid Choice")

                print("Update Details Successfully!")
            else:
                print("User Not Found")
    elif choice==4:
        print("Delete Student")
        s=int(input("Enter Student Id"))
        for i in range(len(L)):
            if L[i]['id']==s:
                del L[i]
                print("Student Detail Is Deleted Successfully")
            else:
                print("User Not Found")

    elif choice==5:
        print("Display Subjects Offered")
        for i in a:
            print(i,end=" ")
    elif choice==6:
        print("Thank You!")
        break

    else:
        print("Invalid Option,Try Again!")