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

if (av<=60):
	print(" STUDENT RATING F ")
	print(" FAILED!!! ")
elif (av>=61 and av<=70):
	print(" STUDENT RATING E ")
	print(" FAILED!!! ")
elif (av>=71 and av<=79):
	if av>=75:
	    print(" STUDENT RATING D ")
	    print(" PASSED!! ")
	else:
	    print(" STUDENT RATING D ")
	    print(" FAILED!! ")
elif (av>=81 and av<=89):
	print(" STUDENT RATING C")
	print(" PASSED!!! ")
elif (av>=90 and av<=98):
	print(" STUDENT RATING B ")
	print(" PASSED!!! ")
elif (av>=99 and av<=100):
	print(" STUDENT RATING A ")
	print(" PASSED!!! ")