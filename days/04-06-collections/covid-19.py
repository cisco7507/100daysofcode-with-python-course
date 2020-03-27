import csv
from collections import defaultdict, namedtuple, Counter
import requests
from datetime import timedelta, datetime

now = datetime.now()
yesterday = timedelta(days=1)
report = now.strftime('%m-%d-%Y.csv')
report_yesterday = (now - yesterday).strftime('%m-%d-%Y.csv')
BASE_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/' + report
PREVIOUS_BASE_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/' + report_yesterday
TMP = '/tmp'

Covid = namedtuple('Covid', 'City Province Confirmed Deaths Recovered')

Covid_data = defaultdict(list)

r = requests.get(BASE_URL)
if not r:
    r = requests.get(PREVIOUS_BASE_URL)
    print(f'Using old file with date: {report_yesterday}')

with open('/tmp/' + report, 'wb') as f:
    f.write(r.content)


def create_dict():
    with open('/tmp/' + report, 'r') as f:
        for line in csv.DictReader(f):
            country = line['Country_Region']
            province = line['Province_State']
            city = line['Admin2']
            confirmed = line['Confirmed']
            deaths = line['Deaths']
            recovered = line['Recovered']
            Covid_data[country].append(
                Covid(Province=province, City=city, Confirmed=confirmed, Deaths=deaths, Recovered=recovered))
    return Covid_data


def data_by_country(country='*', **kwargs):
    if country == '*':
        return create_dict()
    _ = {}
    for c, d in kwargs.items():
        if c == country:
            _[country] = d
    return _


country_data = create_dict()
data = data_by_country('Canada', **country_data)

for k, v in data.items():
    s = sorted(v, key=lambda x: int(x.Confirmed), reverse=True)
    for p in s:
        print(
            f'Country: {k}, Province: {p.Province}, City: {p.City}, Confirmed: {p.Confirmed}, Deaths: {p.Deaths}, Recovered: {p.Recovered}')
