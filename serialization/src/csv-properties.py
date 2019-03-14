import csv

"""
    sonar.host.url=https://sonarcloud.io
    sonar.language=py
    sonar.sourceEncoding=UTF-8
    sonar.verbose=true
    sonar.projectKey=habitatOS
    sonar.projectName=habitatOS
    sonar.projectDescription=Operating System for extraterrestrial habitats.
"""

with open(r'../data/sonar-project.properties') as file:

    data = csv.DictReader(
        file,
        fieldnames=['property', 'value'],
        delimiter='=',
        lineterminator='\n',
        quoting=csv.QUOTE_NONE)

    for line in data:
        print(dict(line))

# {'property': 'sonar.host.url', 'value': 'https://sonarcloud.io'}
# {'property': 'sonar.language', 'value': 'py'}
# {'property': 'sonar.sourceEncoding', 'value': 'UTF-8'}
# {'property': 'sonar.verbose', 'value': 'true'}
# {'property': 'sonar.projectKey', 'value': 'habitatOS'}
# {'property': 'sonar.projectName', 'value': 'habitatOS'}
# {'property': 'sonar.projectDescription', 'value': 'Operating System for analog extraterrestrial habitats.'}
