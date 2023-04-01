import requests as r
from dotenv import dotenv_values, load_dotenv
import os

load_dotenv()
config = dotenv_values('.env')

api_key = os.getenv("API_KEY")

site = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/111.0.0.0 Safari/537.36"}


def get_api_data():
    res = r.get(site, headers=headers).json()
    copywriter = res["copyright"]
    date = res["date"]
    explanation = res["explanation"]
    url = res["url"]
    title = res["title"].split(":")[1].strip()

    return {"title": title, "date": date,
            "explanation": explanation,
            "copywriter": copywriter,
            "url": url}


def get_image():
    img_site = get_api_data()
    img_url = img_site["url"]
    res = r.get(img_url, headers)
    with open("assets/images/image.jpg", "wb") as file:
        file.write(res.content)


if __name__ == "__main__":
    data = get_api_data()
    print(data["title"])
    get_image()


