import requests
from bs4 import BeautifulSoup
import json
import csv
from pathlib import Path
import time

BASE_URL = "https://books.toscrape.com/"

def convert_rating(rating_text):
    mapping = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    return mapping.get(rating_text, 0)

def scrape_books():
    headers = {
        "User-Agent": "TraineeCrawlerChallenge/1.0"
    }

    response = requests.get(BASE_URL, headers=headers, timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    books = []

    for book in soup.select("article.product_pod"):
        title = book.select_one("h3 a")["title"]
        price = book.select_one(".price_color").get_text(strip=True)
        availability = book.select_one(".availability").get_text(strip=True)

        rating_classes = book.select_one(".star-rating")["class"]
        rating_text = next(
            (cls for cls in rating_classes if cls != "star-rating"),
            "Zero"
        )

        books.append({
            "title": title,
            "price": price,
            "availability": availability,
            "rating": convert_rating(rating_text)
        })

    return books

def save_json(data):
    Path("data").mkdir(exist_ok=True)

    with open("data/books.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def save_csv(data):
    Path("data").mkdir(exist_ok=True)

    with open("data/books.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["title", "price", "availability", "rating"]
        )
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    books = scrape_books()
    save_json(books)
    save_csv(books)

    print(f"{len(books)} books extracted successfully.")
