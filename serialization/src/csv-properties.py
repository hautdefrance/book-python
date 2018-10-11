import csv

FILENAME = r'sonar-project.properties'
"""
    sonar.host.url=https://sonarcloud.io
    sonar.language=py
    sonar.sourceEncoding=UTF-8
    sonar.verbose=true
    sonar.projectKey=habitatOS
    sonar.projectName=habitatOS
    sonar.projectDescription=Operating System for analog extraterrestrial habitats.
"""

with open(FILENAME) as file:
    config = csv.DictReader(
        file,
        fieldnames=['property', 'value'],
        delimiter='=',
        lineterminator='\n',
        quoting=csv.QUOTE_NONE)

    for line in config:
        property = line['property']
        value = line['value']
        print(f'{property} -> {value}')
