import os
import requests

# Set your Google Custom Search Engine (CSE) API key and search engine ID
API_KEY = ''
SEARCH_ENGINE_ID = ''

def get_image_urls(query, num_images=3):
    base_url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': API_KEY,
        'cx': SEARCH_ENGINE_ID,
        'q': query,
        'searchType': 'image',
        'num': num_images
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    image_urls = [item['link'] for item in data.get('items', [])]
    return image_urls

def download_images(image_urls, folder_name):
    os.makedirs(folder_name, exist_ok=True)
    for i, url in enumerate(image_urls):
        try:
            response = requests.get(url)
            with open(os.path.join(folder_name, f"image_{i+1}.jpg"), 'wb') as f:
                f.write(response.content)
                print(f"Downloaded image {i+1}")
        except Exception as e:
            print(f"Error downloading image {i+1}: {e}")

if __name__ == "__main__":
    search_terms = ["Pav Bhaji", "Masala Dosa", "Chicken Tikk"]  # Add your desired search terms here
    num_images_per_term = 3

    for term in search_terms:
        print(f"Downloading images for '{term}'...")
        image_urls = get_image_urls(term, num_images=num_images_per_term)
        download_images(image_urls, term)
        print(f"Downloaded {len(image_urls)} images for '{term}'.")
