from data_base.database import sql_command_insert
import requests
from bs4 import BeautifulSoup

URL = "https://rezka.ag/films/"
HEADERS = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,"
             "image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",

    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}


def get_html(url):
    response = requests.get(url=url, headers=HEADERS)
    return response


async def get_data_from_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_="b-content__inline_item")
    films = []
    for item in items:
        film = {
            "id": item.get("data_id"),
            "title": item.find("div", class_="b-content__inline_item-link").find('a').getText(),
            "link": item.find("div", class_="b-content__inline_item-link").find("a").get("href"),
        }
        await sql_command_insert(film)
        films.append(film)
    return films


async def parser():
    html = get_html(URL)
    if html.status_code == 200:
        films = []
        for i in range(1, 2):
            html = get_html(f"{URL}page/{i}/")
            current_page = await get_data_from_page(html.text)
            films.extend(current_page)
            return films
    else:
        raise Exception("Error in parser")
