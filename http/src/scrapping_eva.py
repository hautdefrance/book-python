import csv
from datetime import datetime
from bs4 import BeautifulSoup
import requests


URL = 'https://www.worldspaceflight.com/bios/eva/eva.php'
FILENAME_HTML = 'eva.html'
FILENAME_CSV = 'eva.csv'


# When you dump page for the first time, you can test parsing on local file
# It saves bandwidth, and speeds you development
# Then comment following ``with`` context manager

with open(FILENAME_HTML, mode='w', encoding='utf-8') as file:
    response = requests.get(URL)
    file.write(response.text)


# Parser content below

with open(FILENAME_HTML, mode='r', encoding='utf-8') as file:
    content = file.read()

html = BeautifulSoup(content, 'html.parser')
table = html.find_all('table')[1]


def parse_date(text):
    try:
        return datetime.strptime(text, '%d %B %Y')
    except ValueError:
        return text


def parse_str(text):
    if text == '\xa0':
        return ''
    return text


records = []

for row in table.find_all('tr')[1:]:
    td = row.find_all('td')
    participants = ','.join(x.string for x in td[3].find_all('a'))

    records.append({
        'Number': parse_str(td[0].string),
        'ISS': parse_str(td[1].string),
        'Mission': parse_str(td[2].string),
        'Participants': participants,
        'Duration': parse_str(td[4].string),
        'Date': parse_date(td[5].string),
        'Notes': parse_str(td[6].string),
    })


with open(FILENAME_CSV, mode='w', encoding='utf-8') as file:
    writer = csv.DictWriter(
        file,
        fieldnames=records[0].keys(),
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL,
        lineterminator='\n')

    writer.writeheader()

    for row in records:
        writer.writerow(row)
