class Timetable:

    def __init__(self, educational_object):
        self.timetable = [[['', None, None, None] for k in range(4)] for i in range(11)]
        self.educational_object = educational_object

    def set_lesson(self,
                   day: int,
                   lesson_number: int,
                   lesson_name: str,
                   lesson_class,
                   lesson_classroom,
                   lesson_teacher):
        """
        :param lesson_name: name of the lesson ('english')
        :param day: number of the day in 2 weeks (0 to 11)
        :param lesson_number: number of the lesson in the day (0 to 3)
        :param lesson_classroom: the classroom where the lesson is planned (409)
        :param lesson_teacher: the teacher of the lesson ('Ольга Сергеевна')
        :param lesson_class: the name of the class which lesson is planned
        """
        self.timetable[day][lesson_number] = \
            [lesson_class,
             lesson_name,
             lesson_classroom,
             lesson_teacher]

    def get_timetable(self):
        return self.timetable


class Class:

    def __init__(self, class_name, students_quantity):
        self.class_name = class_name
        self.students_quantity = students_quantity
        self.lessons = {}
        self.timetable = Timetable(self)

    def add_lesson(self, lesson_name: str, study_hours: int, together=False):
        self.lessons[lesson_name] = [study_hours, together]

    def get_class_timetable(self):
        return self.timetable

    def get_class_name(self):
        return self.class_name

    def get_lessons(self):
        return self.lessons

    def get_students_quantity(self):
        return self.students_quantity

    def __str__(self):
        return str(self.lessons)

    def __contains__(self, item):
        return item in self.lessons

    def __getitem__(self, item):
        return self.lessons[item]



class Classroom:

    def __init__(self, classroom_number: str, classroom_capacity: int):
        self.classroom_number = classroom_number
        self.classroom_capacity = classroom_capacity
        self.timetable = Timetable(self)

    def get_classroom_timetable(self):
        return self.timetable

    def get_classroom_number(self):
        return self.classroom_number

    def get_classroom_capacity(self):
        return self.classroom_capacity


class Teacher:

    def __init__(self, name):
        self.name = name
        self.timetable = Timetable(self)
