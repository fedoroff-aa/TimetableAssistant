import educational_objects
import reader


class Maker:

    def __init__(self, path_to_classrooms, path_to_edu_programs, path_to_quantity):
        self.classrooms = reader.Classrooms(path_to_classrooms).get_classrooms()
        self.educational_programs, self.lessons = reader.EducationalPrograms(path_to_edu_programs).get_programs()
        self.class_quantities = reader.ClassQuantities(path_to_quantity).get_quantities()
        


    def make(self):
        pass

