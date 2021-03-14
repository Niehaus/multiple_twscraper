import datetime
import json
import os

from rich import print
from rich.panel import Panel


from query_handler import Scraper


class Handler:
    def __init__(self, answers):
        self.action = answers['action'],
        self.which = answers['which']
        self.scraper = Scraper()
        # self.chosen = {
        #     'Buscar por termo': AGb(),
        # }
        self.chosen = {}
        self.queries = []

        self.action = ''.join(self.action)
        self.which = ''.join(self.which)

    @staticmethod
    def confirm_date_format(date_str):
        regex = datetime.datetime.strptime
        date = '2021-01-01'
        date_format = False
        while not date_format:
            try:
                date = input(date_str)
                regex(date, '%Y-%m-%d')
                date_format = True
            except ValueError:
                print('Formato errado. Insira novamente a data \n')

        return date

    @staticmethod
    def confirm_max_tweets():
        num = 1
        input_integer = False

        while not input_integer:
            try:
                num = int(input('Quantos tweets deseja buscar? '))
                input_integer = True
            except ValueError:
                print("Apenas números inteiros serão aceitos.")

        return num

    @staticmethod
    def nice_print(keyword, since_date, til_date, max_tweets):
        print(
            Panel.fit(
                f'Palavra Chave: {keyword} \n'
                f'De {since_date} até {til_date}\n'
                f'Tweets Buscados: {max_tweets}',
                title="[bold blue] Parâmetros da Busca[/bold blue]",
                border_style='magenta'
            )
        )

        # f'f6(x): [bold red]{inf_limit}[/bold red] <= xi <= [bold red]{sup_limit}[/bold red]\n'
        # f'The global minimum is located at origin[bold red] x* = (0,. . .,0), f(x*) = 0[/bold red]\n'
        # f'Number of particles: [bold red]{cloud_size}[/bold red]\n'
        # f'Dimension(s): [bold red]{dimension}[/bold red]\n'
        # f'Global Best founded: [bold green]{best_fitness}[/bold green]',

    @staticmethod
    def write_json_file(json_content, keyword, data):
        os.chdir('resultados_busca')
        directory = f"{keyword}/coleta/"
        filename = f"{data}.json"

        if not os.path.exists(directory):
            os.makedirs(directory)
        os.chdir(directory)

        json_file = open(filename, "w")
        json_string = json.dumps(json_content)
        json_file.write(json_string)
        json_file.close()

        print(f'Arquivo de coleta escrito com sucesso.\n'
              f'Verifique {directory + filename}')

    def handle_which(self):
        keyword = input('Digite o que deseja buscar: ')
        if self.which == 'Buscar por hashtag':
            keyword = "#" + keyword
        print(f'\nInforme a data de coleta. '
              f'Insira no formato yyyy-mm-dd.\n'
              f'Por exemplo 2021-01-01 é data válida. \n')

        since_date = self.confirm_date_format('Desde a data: ')
        til_date = self.confirm_date_format('Até a data: ')
        max_tweets = self.confirm_max_tweets()

        query = {
            keyword: keyword,
            since_date: since_date,
            til_date: til_date,
            max_tweets: max_tweets
        }
        self.queries.append(query)
        self.nice_print(*query)
        print('...\n')
        scraped_tweets = self.scraper.cli_scrape_tweets_by_content(
            since_date,
            til_date,
            keyword,
            max_tweets
        )
        print('Coleta Realizada.\n')  # Pesquisar em como fazer isso ser legal

        self.write_json_file(scraped_tweets, keyword, til_date)
