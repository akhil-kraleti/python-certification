student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

#finding sum of all scores in the list
sum_of_scores = 0
for score in student_scores:
    sum_of_scores += score
print(sum_of_scores)
#OR
total_score = sum(student_scores)
print(total_score)

#finding max score in the list
max_score = 0
for score in student_scores:
    if score>max_score:
        max_score=score
print(max_score)
#OR
maximum_score = max(student_scores)
print(maximum_score)
