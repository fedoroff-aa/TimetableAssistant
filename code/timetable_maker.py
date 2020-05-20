import educational_objects
import reader


class Maker:

    def __init__(self, path_to_classrooms, path_to_edu_programs, path_to_quantity):
        self.classrooms = reader.Classrooms(path_to_classrooms).get_classrooms()
        educational_programs, self.lessons = reader.EducationalPrograms(path_to_edu_programs).get_programs()
        class_quantities = reader.ClassQuantities(path_to_quantity).get_quantities()

        self.classes = {}
        for class_of_students in educational_programs.keys():
            if class_of_students in ['9Ж', '9Ж2', '10Ж', '10З', '11Ж', '11Ж2']:
                pass
            else:
                self.classes[class_of_students + '-1'] = educational_objects.Class(
                    class_of_students + '-1',
                    class_quantities[class_of_students][0])
                self.classes[class_of_students + '-2'] = educational_objects.Class(
                    class_of_students + '-2',
                    class_quantities[class_of_students][1])
                for (lesson_name, together), study_hours in educational_programs[class_of_students].items():
                    if study_hours != 0:
                        self.classes[class_of_students + '-1'].add_lesson(lesson_name, together, study_hours)
                        self.classes[class_of_students + '-2'].add_lesson(lesson_name, together, study_hours)

    def make(self):
        classes_sorted_by_quantity = sorted(self.classes.values(), key=lambda x: x.get_students_quantity())
        for lesson in self.lessons:
            print(lesson)
            for class_of_students in classes_sorted_by_quantity:
                if lesson in class_of_students:
                    print(class_of_students[lesson], class_of_students.get_class_name())
                    if class_of_students[lesson]:  # Together
                        pass
                    else:  # apart
                        pass
            print()
