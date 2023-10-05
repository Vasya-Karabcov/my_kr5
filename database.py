import psycopg2


class DataBase:

    def __init__(self):
        conn = psycopg2.connect(host='localhost',
                                database='postgres',
                                user='postgres',
                                password='658311')
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute('CREATE DATABASE employers_vacancies')

        self.conn = psycopg2.connect(host='localhost',
                                     database='employers_vacancies',
                                     user='postgres',
                                     password='658311')
        self.cur = self.conn.cursor()

    def create_table_employers(self):
        self.cur.execute('CREATE TABLE employers'
                         '(id_employer int,'
                         'name_employer varchar(500),'
                         'discription_employer text,'
                         'open_vacancies int,'
                         'site_url varchar(500));')

    def create_table_vacancies(self):
        self.cur.execute('CREATE TABLE vacancies'
                         '(id_employer int, '
                         'id_vacancy int, '
                         'name_vacancy varchar(500), '
                         'requirement text, '
                         'salary_from int, '
                         'salary_to int, '
                         'url_vacancy varchar(500));')

    def writing_data_to_table_employers(self, company):
        self.cur.execute(
            f"INSERT INTO employers VALUES"
            f"({company['id']}, "
            f"'{company['name']}', "
            f"'{company['alternate_url']}', "
            f"'{company['open_vacancies']}', "
            f"'{company['site_url']}')"
        )

    def validation_salary(self, salary):
        if salary is None:
            salary_from, salary_to = 0, 0
        elif salary['from'] is None:
            salary_from = 0
            salary_to = salary['to']
        elif salary['to'] is None:
            salary_to = 0
            salary_from = salary['from']
        else:
            salary_to = salary['to']
            salary_from = salary['from']
        return salary_from, salary_to

    def writing_data_to_table_vacancies(self, vacancy):
        salary_from, salary_to = self.validation_salary(vacancy['salary'])

        self.cur.execute(
            f"INSERT INTO vacancies VALUES"
            f"({vacancy['employer']['id']},"
            f"{vacancy['id']},"
            f"'{vacancy['name']}',"
            f"'{vacancy['snippet']['requirement']}',"
            f"{salary_from},"
            f"{salary_to},"
            f"'{vacancy['alternate_url']}')"
        )