"""
In this code chat gpt improve my code by handling the errors 
and refactoring it as a functions making it easy to maintain 
chat gpt also documented the code so that it's easy to understand.
"""
from bs4 import BeautifulSoup
import requests


def fetch_html_content(url):
    """
    Fetches HTML content from the specified URL.

    Parameters:
    - url (str): The URL to fetch HTML from.

    Returns:
    - bytes: The HTML content.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def extract_book_info(book):
    """
    Extracts title, rating, and price information from a book element.

    Parameters:
    - book (Tag): Beautiful Soup Tag representing a book.

    Returns:
    - str: Formatted string with book information.
    """
    title_element = book.h3.a
    title = title_element.get("title", "N/A") if title_element else "N/A"

    rate_element = book.p
    rate = (
        rate_element["class"][1]
        if rate_element and len(rate_element["class"]) > 1
        else "N/A"
    )

    price_element = book.find("p", class_="price_color")
    price = price_element.text if price_element else "N/A"

    return f"The title is {title}\nRate: {rate} stars out of five\nPrice: {price}"


def main():
    """
    Main function to scrape book information from the specified URL.
    """
    url = "https://books.toscrape.com"
    html_content = fetch_html_content(url)

    if html_content:
        soup = BeautifulSoup(html_content, "html.parser")
        books = soup.findAll("article")

        for book in books:
            print(extract_book_info(book))


if __name__ == "__main__":
    main()
