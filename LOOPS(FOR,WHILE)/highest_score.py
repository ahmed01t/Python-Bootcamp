students_score=[150,123,134,324,56,54,74,42,21,121,232,321]
for score in students_score:
    print(score)
total_score=sum(students_score)
print("\n")
print(total_score)
print(max(students_score))
#printing max score without using library function
print("\n")
max_score=0
for score in students_score:
    if score>max_score:
        max_score=score
print(max_score)