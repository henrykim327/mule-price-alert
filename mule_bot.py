import requests
from bs4 import BeautifulSoup

WEBHOOK_URL = "디스코드 웹훅 URL"

URL = "https://www.mule.co.kr/bbs/market/guitar"

def send_discord(message):
    requests.post(WEBHOOK_URL, json={"content": message})

def check_mule():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    res = requests.get(URL, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    posts = soup.select("table tr")

    for post in posts:
        text = post.get_text()

        if "THR10II" in text:
            if "350,000" in text or "340,000" in text or "330,000" in text:
                send_discord("THR10II 매물 발견\n" + text)

        if "THR10" in text and "THR10II" not in text:
            if "250,000" in text or "240,000" in text or "230,000" in text:
                send_discord("THR10 매물 발견\n" + text)

if __name__ == "__main__":
    check_mule()
