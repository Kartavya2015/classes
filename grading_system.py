print("Enter the marks of the five subjects below")
math = int(input("Enter the marks: "))
spark = int(input("Enter the marks: "))
sst = int(input("Enter the marks: "))
hindi = int(input("Enter the marks: "))
lit = int(input("Enter the marks: "))
la = int(input("Enter the marks: "))

total = math+spark+sst+hindi+lit+la
avg = total/6


if avg >= 91 and  avg <= 100:
   print("Youe grade is A1")
elif avg >= 81 and  avg <= 91:
   print("Youe grade is A2")
elif avg >= 71 and  avg <= 81:
   print("Youe grade is B1")
elif avg >= 61 and  avg <= 71:
   print("Youe grade is B2")
elif avg >= 51 and  avg <= 61:
   print("Youe grade is C1")
elif avg >= 41 and  avg <= 51:
   print("Youe grade is C2")
elif avg >= 33 and  avg <= 41:
   print("Youe grade is D")
else:
   print("invalid input")