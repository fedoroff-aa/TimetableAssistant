class Timetable:

    def __init__(self, educational_object):
        if isinstance(educational_object, Class):
            self.timetable = [[[[['', None, None, None], ['', None, None, None]]
                                for k in range(4)] for j in range(5 + i)] for i in range(2)]
        else:
            self.timetable = [[[[['', None, None, None], ['', None, None, None]]
                                for k in range(4)] for j in range(5 + i)] for i in range(2)]
        self.educational_object = educational_object

    def set_lesson(self,
                   week: int,
                   day: int,
                   lesson_number: int,
                   lesson_name: str,
                   lesson_class,
                   lesson_classroom,
                   lesson_teacher,
                   group=0):
        """
        :param lesson_name: name of the lesson ('english')
        :param week: number of the week (0 or 1)
        :param day: number of the day in the week (0 to 4 if week == 0 or 0 to 5 if week == 1)
        :param lesson_number: number of the lesson in the day (0 to 3)
        :param lesson_classroom: the classroom where the lesson is planned (409)
        :param lesson_teacher: the teacher of the lesson ('Ольга Сергеевна')
        :param lesson_class: the name of the class which lesson is planned
        :param group: number of the group
        (by default is 0, used only if educational_object == Class)
        """
        if isinstance(self.educational_object, Class):
            self.timetable[week][day][lesson_number][group] =\
                [lesson_class,
                 lesson_name,
                 lesson_classroom,
                 lesson_teacher]
        else:
            for i in range(2):
                self.timetable[week][day][lesson_number][i] = \
                    [lesson_class,
                     lesson_name,
                     lesson_classroom,
                     lesson_teacher]

    def get_timetable(self):
        return self.timetable


class Class:

    def __init__(self, class_name, students_quantity_group_1, students_quantity_group_2):
        self.class_name = class_name
        self.students_quantity_group_1 = students_quantity_group_1
        self.students_quantity_group_2 = students_quantity_group_2
        self.lessons = []
        self.timetable = Timetable(self)

    def add_lesson(self, lesson_name: str, study_hours: int, together=False):
        self.lessons.append([lesson_name, study_hours, together])

    def get_class_timetable(self):
        return self.timetable

    def get_class_name(self):
        return self.class_name

    def get_lessons(self):
        return self.lessons

    def get_students_quantity_group_1(self):
        return self.students_quantity_group_1

    def get_students_quantity_group_2(self):
        return self.students_quantity_group_2


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
    def __init__(self):
        self.timetable = Timetable(self)

