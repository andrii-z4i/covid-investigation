import requests


urls = {
    'all': 'https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/osoby.csv',
    'recovered': 'https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/vyleceni.csv',
    'death': 'https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/umrti.csv',
    'hosptial': 'https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/hospitalizace.csv'
} 

for url in urls:
    print(f'Downloading data for {url} by next url={urls[url]}')
    response = requests.get(urls[url])
    file = open(f'data/{url}.csv', "wb")
    file.write(response.content)
    file.close()