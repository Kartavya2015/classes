#Take marks from user
math = int(input("Enter your marks for math: "))
science = int(input("Enter your marks for science: "))
sst = int(input("Enter your marks for social studies: "))
english = int(input("Enter your marks for english: "))
lit = int(input("Enter your marks for liturature: "))
hindi = int(input("Enter your marks for hindi: "))
marathi = int(input("Enter your marks for marathi: "))

#lets caculate the percantage of marks
sum = math+science+sst+english+lit+hindi+marathi
print("Sum of all the subject's marks is", sum)

perc = (sum/700)*100

print("Percentage of marks is", perc)