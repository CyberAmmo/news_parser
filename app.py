import requests
import json
from bs4 import BeautifulSoup


def get_article():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    url = 'https://seoprofy.ua/blog'
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    article_card = soup.find_all("article", class_="article")

    art_dict = {}
    for article in article_card:
        art_title = article.find("h2", class_="title__h2").text.strip()
        art_link = article.find("a").attrs["href"]
        art_descript = article.find("p", class_="get-more").text.strip()
        art_pubdate = article.find("time").text.strip()
        
        art_id = art_link.split('/')[-1]

        art_dict[art_id] = {
            "article_date_timestamp": art_pubdate,
            "article_title": art_title,
            "article_description": art_descript,
            "article_link": art_link
        }

        with open("news_dict.json", "w", encoding="utf-8") as f:
            json.dump(art_dict, f, indent=4, ensure_ascii=False)


def check_update_news():
    with open("news_dict.json", encoding="utf-8") as f:
        art_dict = json.load(f)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    url = 'https://seoprofy.ua/blog'
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    article_card = soup.find_all("article", class_="article")

    fresh_news = {}
    for article in article_card:
        art_link = article.find("a").attrs["href"]
        art_id = art_link.split('/')[-1]

        if art_id in art_dict:
            continue
        else:
            art_title = article.find("h2", class_="title__h2").text.strip()
            art_descript = article.find("p", class_="get-more").text.strip()
            art_pubdate = article.find("time").text.strip()


            art_dict[art_id] = {
                "article_date_timestamp": art_pubdate,
                "article_title": art_title,
                "article_description": art_descript,
                "article_link": art_link
            }

            fresh_news[art_id] = {
                "article_date_timestamp": art_pubdate,
                "article_title": art_title,
                "article_description": art_descript,
                "article_link": art_link
            }

    with open("news_dict.json", "w", encoding="utf-8") as f:
        json.dump(art_dict, f, indent=4, ensure_ascii=False)

    return fresh_news


def main():
    # get_article()
    print(check_update_news())


if __name__ == "__main__":
    main()