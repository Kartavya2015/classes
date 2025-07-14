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
          temp.append(str(input("Enter some thing about your friend")))
          #Even if this place is blank,None will take the blank's place
          if temp[j] == ''or temp[j] == ' ':
             temp[j] = None

             if j ==3:
                temp.append(str(input("Enter date of birth (dd/mm/yyyy)")))

                if temp[j] == ''or temp[j] == ' ':
                    #Even if this place is blank,None will take the blank's place
                    temp[j] = None
                if j == 4:
                    temp.append(str(input("Enter category of contact (family/friend/colleague)")))
                    #even if this place is blank,None will take the blank's place
                    if temp[j] == '' or temp[j] == ' ':
                        temp[j] = None
    phone_book.append(temp)
    #by this step we are appending a list temp into a list phone_book

    print(phone_book)
    return phone_book

def menu():
    print("************************************************************")
    print("\t\t\tSMARTPHONE DIRECTERORY", flush=False)
    print("************************************************************")
    print("1. Add a new contact")
    print("6.exit")

def add_contact(pb):
   #Adding a contact is the easiest beacuse all you need to do is :
   #append another list of details into the already existing list
   dip = []
   for i in range(len(pb[0])):
      if i == 0:
            dip.append(str(input("Enter Name: ")))
            if i == 1:
             dip.append(str(input("Enter number: ")))
            if i == 2:
             dip.append(str(input("Enter date of birth(dd/mm/yyyy): ")))
            if i == 3:
             dip.append(str(input("Enter email address: ")))
            if i == 4:
             dip.append(str(input("Enter enter category(family/friends/work/others): ")))
             pb.append(dip)
             return pb
            
            def thanks():
               print("*************************************************************")
               print("thank you for using the phone book")
               sys.exit("goodby,Have a nice day ahead!")
               #Main function code
               print("*************************************************************")
               print("welcome to our phone book")

               ch = 1
               pb = initial_phonebook()
            while ch in (1, 2, 3, 4, 5):
               ch = menu()
               pb = add_contact(pb)
            else:
               thanks()