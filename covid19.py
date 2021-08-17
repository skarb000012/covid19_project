from bs4.element import ResultSet
import requests
from bs4 import BeautifulSoup

def get_corona_summary():
    url = "http://ncov.mohw.go.kr/"

    res =  requests.get(url)

    soup = BeautifulSoup(res.text, 'lxml')
    patients = soup.select("ul.liveNum span.num")

    results={
        '확진환자' : int(patients[0].text.replace(',','').replace('(누적)','')),
        '완치' : int(patients[1].text.replace(',','')),
        '치료중' : int(patients[2].text.replace(',','')),
        '사망' : int(patients[3].text.replace(',','')),
    }

    return results
print(get_corona_summary())