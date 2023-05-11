numberStudents = int(input("Insert the number of the students: "))
average = 0
for i in range (1,numberStudents+1):
    score = float(input(f"student number {i}'s score was "))
    average +=score
average = average /numberStudents
print("\n\t\t\tAVERAGE\n____________________________\n")
print(f"Average of the class is:  {average} ")