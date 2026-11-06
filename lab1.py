name=input("Enter student name: ")
n=int(input("Enter number of subjects: "))
total=0
for i in range (1,n+1):
    mark=float(input(f"Enter mark for Subject {i}:"))
    total+=mark
    percentage=total/n
if percentage>=90:
    grade="A+"
    performace="Outstanding"
elif percentage>=80:
    grade="A"
    performace="Excellent"
elif percentage>=70:
    grade="B"
    performace="Very Good"
elif percentage>=60:
    grade="C"
    performace="Good"
elif percentage>=50:
    grade="D"
    performace="Average"
else:
    grade="F"
    performace="Needs Improvement"

print("\n--------ACADEMIC PERFORMANCE RECORD-------")
print("Student Name: ",name)
print("Total Marks: ",total)
print("Percentage: ",round(percentage,2),"%")
print("Grade: ",grade)
print("Performance: ",performace)


