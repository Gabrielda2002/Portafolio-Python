class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
        
    def calcular_promedio(self):
        total = 0
        for nota in self.grades:
            total += nota
        total /= len(self.grades)
        return total
    
    def determinar_estado(self, total):
        
        if (total > 70):
            return f"El alumno {self.name} a aprobado."
        else:
            return f"El alumno {self.name} a reprobado."
    