import json


class Student:
    def __init__(self, name, group, gpa):
        # Инкапсуляция: приватные атрибуты
        self.__name = name
        self.__group = group
        self.__gpa = gpa

    # Геттеры и сеттеры для атрибутов
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_group(self):
        return self.__group

    def set_group(self, group):
        self.__group = group

    def get_gpa(self):
        return self.__gpa

    def set_gpa(self, gpa):
        if 0 <= gpa <= 5:  # Проверка корректности GPA
            self.__gpa = gpa
        else:
            print(f"Ошибка: GPA должен быть в пределах от 0 до 5.")

    def display_info(self):
        print(f"Имя: {self.__name}, Группа: {self.__group}, Средний балл: {self.__gpa}")

    def update_gpa(self, new_gpa):
        self.set_gpa(new_gpa)


class Group:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)
        else:
            print("Ошибка: добавляемый объект не является студентом.")

    def remove_student(self, name):
        for student in self.students:
            if student.get_name() == name:
                self.students.remove(student)
                print(f"Студент {name} удалён.")
                return
        print(f"Студент с именем {name} не найден.")

    def show_all(self):
        if not self.students:
            print("Нет студентов в группе.")
        else:
            for student in self.students:
                student.display_info()

    def get_top_students(self, threshold):
        print(f"Студенты с GPA выше {threshold}:")
        top_students = [student for student in self.students if student.get_gpa() > threshold]
        if not top_students:
            print(f"Нет студентов с GPA выше {threshold}.")
        for student in top_students:
            student.display_info()

    def save_to_file(self, filename):
        # Сохраняем данные о студентах в JSON
        students_data = [{"name": student.get_name(), "group": student.get_group(), "gpa": student.get_gpa()} for
                         student in self.students]
        with open(filename, 'w') as file:
            json.dump(students_data, file, indent=4)


# Пример работы программы

# Создание студентов
student1 = Student("Смирнов Алексей", "Группа ИС-24", 4.5)
student2 = Student("Кузнецова Анна", "Группа ИС-25", 3.8)
student3 = Student("Морозов Дмитрий", "Группа ИС-26", 5.0)


# Создание группы
group = Group()

# Добавление студентов в группу
group.add_student(student1)
group.add_student(student2)
group.add_student(student3)

# Вывод всех студентов
group.show_all()

# Обновление GPA
student1.update_gpa(4.9)

# Вывод студентов с GPA выше 4.0
group.get_top_students(4.0)

# Удаление студента по имени
group.remove_student("Петрова Мария")

# Сохранение данных в файл
group.save_to_file("students.json")
