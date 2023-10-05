from api_hh import ApiHH
from database import DataBase

api_server = f'https://api.hh.ru/employers/'

companies = {'Тинькофф': '78638',
             'Яндекс': '1122462',
             'Сбербанк-Сервис': '1473866',
             'Skyeng ': '1122462',
             'Сбер': '3529',
             'Eqvanta': '3785152',
             'Яндекс Практикум': '5008932',
             'РУТ КОД': '8642172',
             'ScanFactory': '5580158',
             'АЛЬФАБАНК': '80'}


api_hh = ApiHH(api_server)
database = DataBase()

try:
    with database.conn:
        database.create_table_vacancies()
        database.create_table_employers()
        for id_company in companies:
            company = api_hh.get_company(id_company=companies[id_company]).json()
            write_to_basedate_emp = database.writing_data_to_table_employers(company)

            vacancies_url = company['vacancies_url']
            pages = api_hh.get_vacancies(vacancies_url, 0).json()['pages']
            for page in range(pages):
                vacancies = api_hh.get_vacancies(vacancies_url, page).json()
                for vacancy in vacancies['items']:
                    write_to_basedate_vac = database.writing_data_to_table_vacancies(vacancy)

finally:
    database.conn.close()
