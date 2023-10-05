import requests


class ApiHH:

    def __init__(self, api_server):
        self.api_server = api_server
        print(self.api_server)

    def get_company(self, id_company):
        params = {'area': 113,
                  'locale': 'RU',
                  'only_with_vacancies': True, }
        response = requests.get(f'{self.api_server}{id_company}', params=params)
        if response.status_code == 200:
            return response
        return quit(f'Ошибка {response.status_code}')

    def get_vacancies(self, vacancies_url, page=0):
        params = {
            'page': page,
            'per_page': 100
        }
        response = requests.get(vacancies_url, params=params)
        if response.status_code == 200:
            return response
        return quit(f'Ошибка {response.status_code}')
