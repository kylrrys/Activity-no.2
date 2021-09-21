print("EXAM AVERAGE CALCULATOR")
pg = int(input("Prelim    Exam  :  "))
mg = int(input("Midterm   Exam  :  "))
sg = int(input("SemiFinal Exam  :  "))
fg = int(input("Final     Exam  :  "))
av = float((pg + mg + sg + fg)/4)
print("")
print("Average Grade is =",str(av))
print("")
print("")

if (av>=75):
	print(" PASSED! ")
else:
	print(" FAILED! ")

