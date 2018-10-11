class ConfigParserInterface:
    extension = None

    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename) as file:
            content = file.read()
            return self.parse(content)

    def parse(self, content):
        return NotImplementedError


class ConfigParserINI(ConfigParserInterface):
    extension = '.ini'

    def parse(self, content):
        print('Parsing INI file')
        return dict(...)

class ConfigParserCSV(ConfigParserInterface):
    extension = '.csv'

    def parse(self, content):
       print('Parsing CSV file')
       return dict()

class ConfigParserYAML(ConfigParserInterface):
    extension = '.yaml'

    def parse(self, content):
       print('Parsing YAML file')
       return dict()

class ConfigFileJSON(ConfigParserInterface):
    extension = '.json'

    def parse(self, content):
       print('Parsing JSON file')
       return dict()


class ConfigFileXML(ConfigParserInterface):
    extension = '.xml'

    def parse(self, content):
       print('Parsing XML file')
       return dict()


def config_parser_factory(filename):
    import os
    parsers = {p.extension: p for p in ConfigParserInterface.__subclasses__()}
    extension = os.path.splitext(filename)[1]

    try:
        return parsers[extension](filename)
    except KeyError:
        raise NotImplementedError


 # iris.csv or *.csv, *.json *.yaml...
filename = input('Type filename: ')

config_parser = config_parser_factory(filename)
config_parser.read()
