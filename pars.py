import requests
from bs4 import BeautifulSoup
import csv


# url = "https://masterzoo.ua/ua/catalog/sobaki/korm-dlya-sobak/"
#
headers = {
    "user-agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 105.0.0.0 Safari / 537.36"
}

all_urls = []


for i in range(1, 2, 1):
    url = f'https://masterzoo.ua/ua/catalog/sobaki/korm-dlya-sobak/filter/page={i}/'
    req = requests.get(url,headers)
    html = req.text

    soup = BeautifulSoup(html, "lxml")
    cards = soup.find_all("li", class_="catalog-grid__item")

    cards_urls = []
    for card in cards:
        card_url = "https://masterzoo.ua/" + card.find("div", class_="catalogCard-view").find("a").get("href")
        cards_urls.append(card_url)

    for card_url in cards_urls[1:17]:
        req = requests.get(card_url, headers)
        rere = req.text
        soup = BeautifulSoup(rere, "lxml")
        card_data = soup.find("div", class_="product__grid")

        card_img = "https://masterzoo.ua" + card_data.find("span",class_="gallery__link j-gallery-zoom j-gallery-link").find("img").get("src")
        card_title = card_data.find("div", class_="product-header__block product-header__block--wide").find("h1").text
        card_price = card_data.find("div", class_="product-price__item").text.strip()
        card_text = card_data.find("div", class_="product-description j-product-description").find("p").text
        articul = card_data.find("div", class_="product-header__code").text.split()[1:]

        
        
        
        #####Табличные значения
         
         
        table_data = card_data.find(class_="product-features__table").find_all("tr")


        for item in table_data:
            table_tds = item.find_all("td")

            print(table_tds)











        # with open(f"main_sec.csv", "a", newline="", encoding="utf-8") as file:
        #     writer = csv.writer(file)
        #     writer.writerow(
        #         [
        #             articul[0],
        #             card_img,
        #             card_title,
        #             card_price,
        #             card_text
        #         ]
        #     )





