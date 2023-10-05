from student import Student

students_grades = {
    'Sharit':[40,22,89],
    'Gabriel': [59,70,90],
    "Sara":[57,22,78]
}
students = []
for name, grades in students_grades.items():
    student = Student(name, grades)
    students.append(student)
    
avg = students[0].calcular_promedio()
avg2 = students[1].calcular_promedio()
avg3 = students[2].calcular_promedio()

estado = students[0].determinar_estado(avg)
# print(estado)
estado1 = students[1].determinar_estado(avg2)
# print(estado1)
estado2 = students[2].determinar_estado(avg3)
# print(estado2)

print(f'''El estado de los estudiantes es:
      {estado} Con un promedio de {avg:.2f}.
      {estado1} Con un promedio de {avg2:.2f}.
      {estado2} Con un promedio de {avg3:.2f}.
      ''')
