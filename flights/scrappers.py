import requests
from bs4 import BeautifulSoup
from .models import City

def populate_countries():
    URL = "https://www.scrapethissite.com/pages/simple/"
    response = requests.get(URL)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    country_names = [h3.get_text(strip=True) for h3 in soup.select("h3")]

    for name in country_names:
        City.objects.get_or_create(name=name)