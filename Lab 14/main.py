import logging

# Настройка логирования
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def calculate_average(grades):
    """Вычисляет средний балл"""
    if not grades:
        logging.error("Список оценок пуст")
        raise ValueError("Список оценок не может быть пустым")

    if not all(isinstance(x, (int, float)) for x in grades):
        logging.error("Некорректный тип данных в списке")
        raise TypeError("Все оценки должны быть числами")

    avg = sum(grades) / len(grades)
    logging.info(f"Средний балл рассчитан: {avg}")
    return round(avg, 2)


def determine_grade_letter(avg):
    """Определяет буквенную оценку"""
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


def student_report(name, grades):
    """Формирует итоговый отчёт"""
    avg = calculate_average(grades)
    letter = determine_grade_letter(avg)
    result = f"Студент: {name}\nСредний балл: {avg}\nОценка: {letter}"
    logging.info(f"Создан отчёт для студента {name}")
    return result


if __name__ == "__main__":
    try:
        name = input("Введите имя студента: ")
        grades_input = input("Введите оценки через пробел: ")
        grades = [float(x) for x in grades_input.split()]
        print(student_report(name, grades))
    except Exception as e:
        print("Ошибка:", e)
        logging.exception("Произошло исключение")
