# initial try for scraper and beautifulsoup
import requests
from bs4 import BeautifulSoup

def scrape_books(url):
    """
    Scrapes book titles and prices from a given URL.

    Args:
        url (str): The URL of the webpage to scrape.

    Returns:
        list: A list of dictionaries, where each dictionary contains
              'title' and 'price' for a book. Returns an empty list
              if no books are found or an error occurs.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        print("Successfully fetched web content!")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    print("Successfully parsed HTML!")

    book_containers = soup.find_all('article', class_='product_pod')

    if not book_containers:
        print("No book information found. Please check the page structure or URL.")
        return []

    print(f"Found {len(book_containers)} books.")
    books_data = []
    for book in book_containers:
        title_tag = book.find('h3').find('a')
        title = title_tag['title'] if title_tag and 'title' in title_tag.attrs else 'N/A'

        price_tag = book.find('p', class_='price_color')
        price = price_tag.text.strip() if price_tag else 'N/A'

        books_data.append({'title': title, 'price': price})
    return books_data

if __name__ == "__main__":
    target_url = 'http://books.toscrape.com/'
    scraped_books = scrape_books(target_url)

    if scraped_books:
        print("\n--- Scraped Book Information ---")
        for book in scraped_books:
            print(f"Title: {book['title']}, Price: {book['price']}")
    print("\n--- Scraping Complete ---")