class CourseFactory:
    def iCourseFactory(self):
        kimi = Teacher("Kimi", "Python for beginners")
        karen = Teacher("Karen", "C++")
        print(kimi.Iteacher())
        print(karen.Iteacher())
        python = LocalCourse("Python for beginners", "Kimi", ["array", "loops"], "local")
        c_plus_plus = OffsiteCourse("C++", "Karen", ["array", "loops"], "Warsaw")
        print(python.IlocalCourse())
        print((c_plus_plus.IlocalCourse()))


class Teacher:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name

    def Iteacher(self):
        return self.name, self.course_name


class LocalCourse:
    def __init__(self, course_name, teacher, program, typ):
        self.course_name = course_name
        self.teacher = teacher
        self.program = program
        self.type = typ

    def IlocalCourse(self):
        return self.course_name, self.teacher, self.program, self.type


class OffsiteCourse(LocalCourse):
    def __init__(self, course_name, teacher, program, typ):
        super().__init__(course_name, teacher, program, typ)


CourseFactory().iCourseFactory()