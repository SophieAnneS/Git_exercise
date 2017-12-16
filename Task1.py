class Module(object):

    module_count = 0

    def __init__(self, ects, title, semester, grade=None):
        self.ects = ects
        self.title = title
        self.semester = semester
        self.grade = grade
        self.dates = []
        self.elements = []

        Module.module_count += 1

    def get_important_dates_overview(self):

        print("Important dates for {0:s}:".format(self.title))

        for kind,date in self.dates:
            print("\t{0:s} on {1:s}".format(kind,date))

    def set_grade(self, new_grade):
        self.grade = new_grade

    def add_module_element(self, a_class, date):

        new_object = a_class(self)
        new_object.add_important_date(date)
        self.elements.append(new_object)

    def get_title(self):
        return self.title

    def get_grade(self):
        return self.grade


class ModuleElement(object):

    def __init__(self, module):
        self.module = module

    def add_important_date(self, kind, date):
        self.module.dates.append((kind, date))

class Lesson(ModuleElement):

    def __init__(self, module):
        ModuleElement.__init__(self, module)

        self.module = module

    def add_important_date(self, date):

        ModuleElement.add_important_date(self, "Lesson", date)


class Lab(ModuleElement):

    def __init__(self, module):
        ModuleElement.__init__(self, module)

        self.module = module

    def add_important_date(self, date):

        ModuleElement.add_important_date(self, "Lab Session", date)

class Midterm(ModuleElement):

    def __init__(self, module):
        ModuleElement.__init__(self, module)

        self.module = module

    def add_important_date(self, date):

        ModuleElement.add_important_date(self, "Midterm", date)



class FinalExam(ModuleElement):

    def __init__(self, module):
        ModuleElement.__init__(self, module)

        self.module = module

    def add_important_date(self, date):

        ModuleElement.add_important_date(self, "Final Exam", date)

#info1 = Module(6,"Info 1",1)
#info1.add_module_element(Midterm,"31.10.2017")
#info1.add_module_element(FinalExam,"20.12.2017")
#info1.get_important_dates_overview()

class Course(Module):

    def __str__(self):

        return "Course:" + str(self.title)

class Seminar(Module):

    def __init__(self, ects, title, semester, topic, grade = None):
        Module.__init__(self, ects, title, semester, grade = None)

        self.ects = ects
        self.title = title
        self.semester = semester
        self.topic = topic
        self.grade = grade

    def get_topic(self):
        return self.topic

    def __str__(self):

        return  str(self.get_title()) + " under the topic: "+ str(self.get_topic())

class Thesis(Module):

    def __init__(self, ects, title, semester, topic, research_group, grade = None):
        Module.__init__(self, ects, title, semester, grade = None)

        self.ects = ects
        self.title = title
        self.semester = semester
        self.topic = topic
        self.grade = grade
        self.research_group = research_group

    def get_topic(self):
        return self.topic

    def get_research_group(self):
        return self.research_group

    def __str__(self):

        return self.get_title() + " on the topic: "+ str(self.get_topic()) + " in the Research Group " + str(self.get_research_group())


info1 = Course(6,"Info 1",1)
info1.add_module_element(Midterm,"31.10.2017")
info1.add_module_element(FinalExam,"20.12.2017")
#info1.get_important_dates_overview()
#print(info1)
# expected output:
# Course: Info 1

math1 = Course(6, "Mathematik I", 1)
math1.add_module_element(Midterm,"18.12.2017")
#math1.get_important_dates_overview()
# expected output:
# Important dates for Info 1:
#	Midterm on 31.10.2017
#	Final Exam on 20.12.2017
# Important dates for Mathematik I:
#	Midterm on 18.12.2017


#print(Module.module_count)
# expected output: 2

if __name__ == '__main__':
    print(info1)
    info1.get_important_dates_overview()
    math1.get_important_dates_overview()
    print(Module.module_count)



thesis = Thesis(18,"Bachelor Thesis",6,"A promising research topic on Software Engineering","SEAL")
#print(thesis)
# expected output:
# Bachelor Thesis on the topic: A promising research topic on Software Engineering in the Research Group SEAL


sem = Seminar(3,"Seminar in Software Engineering",4,"A Seminar topic")
#print(sem)
# print(thesis)
# expected output:
# Seminar in Software Engineering under the topic: A Seminar topic

info1.set_grade(6)

if __name__ == '__main__':
    print(thesis)
    print(sem)

class Student(object):

    def __init__(self, name):

        self.name = name
        self.modules = []
        self.grades = {}

    def add_module(self, module):
        self.modules.append(module.get_title())

        self.grades[module.get_title()] = module.get_grade()

    def get_list_modules(self):
        for each in self.modules:
            print(each)

    def get_grades(self):
        for module, grade in self.grades.items():
            print(str(module) + ": " + str(grade))


me = Student("FirstName LastName")
me.add_module(info1)
me.get_list_modules()
# expected output:
# Modules of Student FirstName LastName:
#	Info 1

me.get_grades()
# expected output:
# Grades of Student FirstName LastName:
#	Info 1: 6



