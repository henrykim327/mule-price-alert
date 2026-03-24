import requests
from bs4 import BeautifulSoup

WEBHOOK_URL = "디스코드 웹훅 URL"

URL = "https://www.mule.co.kr/bbs/market/guitar"

def send_discord(message):
    requests.post(WEBHOOK_URL, json={"content": message})

def check_mule():
    res = requests.get(URL)
    soup = BeautifulSoup(res.text, "html.parser")

    posts = soup.select(".list_item")

    for post in posts:
        title = post.select_one(".title").text
        price = post.select_one(".price").text

        price_num = int(price.replace(",", "").replace("원", ""))

        if "THR10II" in title and price_num <= 350000:
            send_discord(f"THR10II 매물: {title} / {price}")

        if "THR10" in title and price_num <= 250000:
            send_discord(f"THR10 매물: {title} / {price}")

if __name__ == "__main__":
    check_mule()
