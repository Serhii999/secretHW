class Employee(object):

    def __init__(self, name, mail, daily_pay):
        self.name = name
        self.mail = mail
        self.daily_pay = daily_pay

    def work(self):

        return "{} come to the office" .format(self.name)

    def check_salary(self, days):
        return "Zarabotok za {} dney = {}".format(days, days*self.daily_pay)


class Recruiter(Employee):
    def work(self):
        return "{} come to the office and start to hiring ".format(self.name)

    def __str__(self):
        return "{}: {}".format(self.name, self.__class__.__name__)


class Programmer(Employee):

    def work(self):
        return "{} come to the office and start coding".format(self.name)

    def __str__(self):
        return "{}: {}".format(self.name, self.__class__.__name__)


class Candidate:
    def __init__(self, full_name, email, technologies, main_skill, main_skill_grade):
        self.full_name = full_name
        self.email = email
        self.technologies = technologies
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    def __str__(self):
        return '{}:{}'.format(self.full_name, self.__class__.__name__)


class Vacancy:
    def __init__(self, title, main_skill, main_skill_level):
        self.title = title
        self.main_skill = main_skill
        self.main_skill_level = main_skill_level

    def __str__(self):
        return '{}:{}'.format(self.title, self.__class__.__name__)

