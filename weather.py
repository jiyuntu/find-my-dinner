from bs4 import BeautifulSoup as bs
import requests

def get_weather_data():
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    URL = "https://www.google.com/search?lr=lang_en&ie=UTF-8&q=weather"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html = session.get(URL)
    soup = bs(html.text, "html.parser")

    result = {}
    result['temp'] = soup.find("span", attrs={"id": "wob_tm"}).text
    result['weather'] = soup.find("span", attrs={"id": "wob_dc"}).text
    result['precent'] = soup.find("span", attrs={"id": "wob_pp"}).text

    return result


if __name__ == "__main__":
    data = get_weather_data()

    print(f"氣溫: {data['temp']}°C")
    print("天氣:", data['weather'])
    print("降雨機率:", data["precent"])