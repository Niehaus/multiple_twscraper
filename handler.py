
# from query_handler import Scraper

class Handler:
    def __init__(self, answers):
        self.action = answers['action'],
        self.which = answers['which']
        # self.scraper = Scraper()
        # self.chosen = {
        #     'Buscar por termo': AGb(),
        # }
        self.chosen = {}

        self.action = ''.join(self.action)
        self.which = ''.join(self.which)

    def handle_which(self):
        keyword = input('Digite o que deseja buscar: ')
        if self.which == 'Buscar por hashtag':
            print('Adicionar #')
            keyword = "#" + keyword
        print(keyword)