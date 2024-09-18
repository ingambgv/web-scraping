import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Scrape Data from Amazon Best Sellers (Example URL)
url = 'https://www.amazon.com/Best-Sellers/zgbs'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
response = requests.get(url, headers=headers)

# Check if request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Step 2: Extract product details (name, price, rating)
    products = []
    
    # Amazon's Best Seller product containers have a class 'zg-item-immersion'
    product_items = soup.select('div.zg-grid-general-faceout')

    for item in product_items:
        # Extract product name
        name = item.select_one('div.p13n-sc-truncated').get_text(strip=True) if item.select_one('div.p13n-sc-truncated') else None
        
        # Extract price (may not be present for some items)
        price_tag = item.select_one('span.p13n-sc-price')
        price = price_tag.get_text(strip=True) if price_tag else 'N/A'
        
        # Extract rating
        rating_tag = item.select_one('span.a-icon-alt')
        rating = rating_tag.get_text(strip=True) if rating_tag else 'N/A'
        
        # Extract the number of reviews (optional)
        review_count_tag = item.select_one('a.a-size-small')
        review_count = review_count_tag.get_text(strip=True) if review_count_tag else 'N/A'
        
        products.append({
            'Product Name': name,
            'Price': price,
            'Rating': rating,
            'Reviews': review_count
        })
else:
    print(f"Failed to fetch page, status code: {response.status_code}")

# Step 3: Data Cleaning and Formatting
df = pd.DataFrame(products)

# Step 4: Analysis

# Step 5 (Optional): Visualization
