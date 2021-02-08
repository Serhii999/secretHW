from models import *
if __name__ == '__main__':


    Ksusha = Recruiter('Kseniya', 'ksusha@gmail.com', 30)

    Serhii = Programmer('Serhii', 'serhii@gmail.com', 40)
    Radislav = Programmer('Radislav', 'radislavchik@gmail.com', 45)

    Dmitrii = Candidate('Dmitrii Vosruf', 'vosruf@gmail.com', '.Net, C#', 'Communication', 10)
    Ilya = Candidate('Khamza Ilya', 'khamza@gmail.com', 'FullStack', 'JS+html', 6)
    Artem = Candidate('Artem Pogorelov', 'pogorelov@gmail.com', 'FrontEnd', 'html+css', 7)

    NetJunior = Vacancy('.Net Junior', 'JS, C#, .Net', 6)
    Verstka = Vacancy('HTML+css Junior', 'html, css, js', 8)

    print(Ksusha.check_salary(20))
    print(Dmitrii)
    print(Verstka)
    print(Ilya)
    print(Serhii)
