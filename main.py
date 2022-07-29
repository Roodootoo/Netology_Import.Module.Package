import application.salary as app_salary
import application.db.people as app_db_people
import datetime

if __name__ == '__main__':
    app_salary.calculate_salary()
    app_db_people.get_employees()
    print(datetime.datetime.now().strftime('%d/%m/%Y'))
