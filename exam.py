#Take input from student that he can attend exam or not
medical_cause = str(input("Do you have a medical cause? Y or N: "))
#Take input of the attendence
attend = int(input("Enter the attendence of the student: "))

if medical_cause == 'y':
    print("You are allowed")
else:
    if attend >= 75:
        print("allowed")
    else:
        print("not allowed")