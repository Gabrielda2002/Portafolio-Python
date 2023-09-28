import ejercicios
import random

name_student=["Gabriel","Juan", "Sharit", "Saraic"]
grade_student = {student:random.randint(1,100) for student in name_student}
print(grade_student)
