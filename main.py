#importing the module
import sys

#this function will be the first to run as soon as the main function executes
def initial_phonebook():
    rows, cols = int (input("please enter initial number of contacts: ")), 5
#we are collecting the initial number of contacts the user wants to have in the 
#phone book already.                  user may add 0 if he/she doesn't wish to enter any.
    phone_book = []
    print(phone_book)
    for i in range(rows):
        print("\nEnter contact %d details in the following order(ONLY):" % (i + 1))
        print("Note * indicates mandatory field")
        print("***********************************************************")
        temp = []
        for j in range(cols):
            #we have taken the conditions for values of j only for the personalized fields
            #such as name, e-mail id, dob, category etc
            if j == 0:
                temp.append(str(input("Enter Name")))
                #We need to check if the user has left the name empty as its mentioned that
                                     #name and number are mandatory fields
                                     #So implement a condition to check as bellow
    if temp[j] == '' or temp[j] == '':
     sys.exit(
        "name is a mandatory field.Process exiting due to blank feild.....")
     #this will exit the process if a blank field is encountered
    if j == 1:
       temp.append(int(input("Enter number")))
       #we do not need to check if user has entered the number because int auto matically
       #takes care of it.Int value canot accept a blank as that counts as a string.
       #so prcees auto ma tically shuts down without us using the sys pakage
       if j==2:
          temp.append(str(input("enter date of birth(dd/mm/yyyy)")))
          #What ever format the user enters dob in, it won't make a diffrence to the compiler
          #only while searching the user will have to enter query exactly the same way as
          #he entered during the input so as to ensure accurate searches
          if temp[j] == '' or temp[j] == ' ':
             #even if this field is left blank, none will take the blank's place
             if temp[j] == '' or temp[j] == ' ':
                temp[j] = None
                phone_book.append(temp)
                return phone_book
             
             def menu():
                #we created this simple menu function for
                #code reusability and also for an interactive console
                #Menu func will only execute when called

                print("************************************************************")
                print("\t\t\tSMARTPHONE DIRECTORY", fulsh=False)
                print("************************************************************")
                print("\tYou can now perform the following operations on this phone book\n")
                print("1. Add a new contact")
                print("2. Remove an existing contact")
                print("3. Delete all contacts")
                print("4. Scearch for a contact")
                print("5. Display all contacts")
                print("6. Exit phonebook")
                #Out of the provided 6 options, the user can choose any 1 choice
                choice = int(input("Enter your choice: "))

                return choice
             
             def add_contact(pb):
                dip = []
                for i in range(len(pb[0])):
                   if i == 0:
                      dip.append(str(input("enter name")))
                   if i == 1:
                      dip.append(int(input("enter number")))
                   if i == 2:
                      dip.append(str(input("enter date of birth(dd/mm/yyyy)")))
                   if i == 3:
                      dip.append(str(input("enter email id")))
                   if i == 4:
                      dip.append(str(input("enter category(Family/Friends/Work/Others)")))
                pb.append(dip)
                return pb
             def remove_existing(pb):
                query = str(input("Enter the name of the contact you want to remove: "))
                temp = 0
                for i in range(len(pb)):
                   if query == pb[i][0]:
                      temp += 1
                      print(pb.pop(i))
                      return pb
                   if temp == 0:
                      print("Sorry, you have entered a invaled qurey." \
                      "\nPlease try again")
                      return pb
                def delete_all(pb):
                   return pb.clear()
                def search_exsisting(pb):
                 choice = int(input("Enter scearch criteria\n\n\n 1. Name\n2.Number\n3.email id\n4.DOB\n5.category(family/Friends/Work/Others)\\nPlease enter:"))
                 temp = [
                 check = -1
                 if choice = -1
                 ]