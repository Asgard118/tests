import unittest

def get_unique_sorted_names(mentors: list):
    # Добавьте в список всех преподавателей со всех курсов
    all_list = []
    for m in mentors:
        all_list.extend(m)

    # Сделайте список all_names_list, состоящий только из имён, и заполните его
    all_names_list = []
    for men in all_list:
        names = men.split(' ')
        for name in names:
            all_names_list.append(name)

    # Сделайте так, чтобы остались только уникальные имена (без повторений)
    unique_names = set(all_names_list)

    # Теперь необходимо отсортировать имена в алфавитном порядке
    unique_names = list(unique_names)
    all_names_sorted = sorted(unique_names)

    return all_names_sorted

def test_get_unique_sorted_names():
    mentors = [
        ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко"],
        ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев"],
        ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко"],
        ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов"]
    ]

    expected_result = ['Адилет', 'Александр', 'Алена', 'Анатолий', 'Анна', 'Антон', 'Асканжоев', 'Бардин', 'Батицкая', 'Беспоясов', 'Бибиков', 'Бочаров', 'Булыгин', 'Вадим', 'Валерий', 'Владимир', 'Воронов', 'Гордиенко', 'Демидов', 'Дмитрий', 'Евгений', 'Ерошевичев', 'Иван', 'Иванов', 'Илья', 'Кирилл', 'Корсаков', 'Максим', 'Маркитан', 'Нуруллин', 'Олег', 'Пеньков', 'Ринат', 'Роман', 'Сейсембаев', 'Солонилин', 'Сухачев', 'Табельский', 'Татьяна', 'Тен', 'Тимур', 'Ульянцев', 'Филипенко', 'Филипп', 'Фитискин', 'Хаслер', 'Чебукин', 'Шек', 'Шлейко', 'Шмаргунов', 'Эдгар', 'Юрий', 'Юшина']

    result = get_unique_sorted_names(mentors)

    assert result == expected_result, f"Ожидаемый результат: {expected_result}, Фактический результат: {result}"

def get_top_3_names(mentors: list):
    all_list = []
    for m in mentors:
        all_list.extend(m)

    all_names_list = []
    for men in all_list:
        name = (men.split(' ')[0])
        all_names_list.append(name)

    popular = []
    for name in all_names_list:
        popular.append((name, all_names_list.count(name)))

    popular.sort(key=lambda x: x[1], reverse=True)
    pop = sorted(set(popular), key=lambda x: x[1], reverse=True)

    top_3 = pop[:3]

    return top_3

def test_get_top_3_names():
    mentors = [
        ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко"],
        ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев"],
        ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко"],
        ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов"]
    ]

    expected_result = [('Александр', 10), ('Евгений', 3), ('Иван', 2)]

    result = get_top_3_names(mentors)

    assert result == expected_result, f"Ожидаемый результат: {expected_result}, Фактический результат: {result}"

def check_course_order(courses_list: list):
    duration_index = []
    mcount_index = []
    
    for index, course in enumerate(courses_list):
        duration_index.append([course['duration'], index])
        mcount_index.append([len(course['mentors']), index])
    
    duration_index.sort()
    mcount_index.sort()
    
    indexes_d = [i[1] for i in duration_index]
    indexes_m = [i[1] for i in mcount_index]
    
    if indexes_d == indexes_m:
        return "Связь есть"
    else:
        return "Связи нет", indexes_d, indexes_m

courses = [
    {"title": "Java-разработчик с нуля", "mentors": ["Филипп Воронов", "Анна Юшина", "Иван Бочаров"], "duration": 14},
    {"title": "Fullstack-разработчик на Python", "mentors": ["Евгений Шмаргунов", "Олег Булыгин"], "duration": 20},
    {"title": "Python-разработчик с нуля", "mentors": ["Евгений Шмаргунов", "Олег Булыгин"], "duration": 12},
    {"title": "Frontend-разработчик с нуля", "mentors": ["Владимир Чебукин", "Эдгар Нуруллин"], "duration": 20}
]

class TestCourseOrder(unittest.TestCase):
    def check_course_order(courses_list):
        duration_index = []
        mcount_index = []
    
        for index, course in enumerate(courses_list):
            duration_index.append([course['duration'], index])
            mcount_index.append([len(course['mentors']), index])
    
        duration_index.sort()
        mcount_index.sort()
    
        indexes_d = [i[1] for i in duration_index]
        indexes_m = [i[1] for i in mcount_index]
    
        if indexes_d == indexes_m:
            return "Связь есть"
        else:
            return "Связь есть" 

if __name__ == '__main__':
    unittest.main()
    test_get_top_3_names()
    test_get_unique_sorted_names()