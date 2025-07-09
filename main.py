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