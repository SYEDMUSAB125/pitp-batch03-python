import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    # Send a GET request to the URL
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
     
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract the title of the webpage
        title = soup.title.text if soup.title else 'No title found'
        print(f"Page Title: {title}\n")
        
        # Extract all paragraphs of the webpage
        paragraphs = soup.find_all('p')
        if paragraphs:
            print("All Paragraphs:")
            for para in paragraphs:
                print(para.text.strip())
                print("\n")
        else:
            print("No paragraphs found.")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

# Example usage
url = "https://en.wikipedia.org/wiki/Artificial_intelligence"  # Replace with the URL you want to scrape
scrape_website(url)