import requests
from bs4 import BeautifulSoup

def scrape_product_info(url):
    headers = {'User-Agent': 'Mozilla/5.0'}  # Some websites require a user-agent header
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # These selectors need to be customized for the site you're targeting
    product_name = soup.select_one('selector_for_product_name').get_text(strip=True)
    product_price = soup.select_one('selector_for_product_price').get_text(strip=True)
    product_description = soup.select_one('selector_for_product_description').get_text(strip=True)
    
    return product_name, product_price, product_description
