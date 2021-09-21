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
    print("Grade Rating is F")
elif (av>=61 and av<=70):
    print("Grade Rating is E")
elif (av>=71 and av<=79):
    print("Grade Rating is D")
elif (av>=80 and av<=89):
    print("Grade Rating is C")
elif (av>=90 and av<=98):
    print("Grade Rating is B")
else:
    print("Grade Rating is A")

