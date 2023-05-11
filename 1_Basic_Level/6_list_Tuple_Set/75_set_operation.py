
student_a_courses = {'history', 'english', 'biology', 'theatre'}
student_b_courses = {'biology', 'english', 'mathematics', 'computer science'}

print(student_a_courses.intersection(student_b_courses))
print(student_a_courses & student_b_courses)

print(student_a_courses.union(student_b_courses))
print(student_a_courses | student_b_courses)


print(student_a_courses.difference(student_b_courses))
print(student_a_courses - student_b_courses)

print(student_b_courses.difference(student_a_courses))
print(student_b_courses - student_a_courses)

print(student_a_courses.symmetric_difference(student_b_courses))