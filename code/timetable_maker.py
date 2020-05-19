import educational_objects
import reader


class Maker:

    def __init__(self, path_to_classrooms, path_to_edu_programs):
        self.classrooms = reader.Classrooms(path_to_classrooms).get_classrooms()
        self.educational_programs, self.lessons = reader.EducationalPrograms(path_to_edu_programs).get_programs()
        print(self.classrooms)
        print(*self.educational_programs, sep='\n')
        print()
        print(*self.lessons, sep=', ')


