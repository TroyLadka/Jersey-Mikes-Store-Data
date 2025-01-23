

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
import time
import pandas as pd

# Set up the Edge WebDriver service
service = Service("C:/Users/troyl/Downloads/edgedriver_win64/msedgedriver.exe")
driver = webdriver.Edge(service=service)

# Base URL of Jersey Mike's store locations
base_url = "https://www.jerseymikes.com/locations/usa"

# Open the base URL in the browser
driver.get(base_url)
time.sleep(5)

# Find all state links on the main page
state_links = driver.find_elements(By.CSS_SELECTOR, "a.state-link")
state_urls = [link.get_attribute("href") for link in state_links]

store_data = []

# Function to extract store information from the current page
def extract_store_info():
    # Locate all store elements on the page
    store_elements = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='storecard-address']")
    for store in store_elements:
        try:
            # Extract the title, address, city, state, and ZIP code of each store
            title = store.find_element(By.CSS_SELECTOR, "p[data-testid='storecard-title']").text
            address = store.find_element(By.CSS_SELECTOR, "p[class='text-base']").text
            city = store.find_element(By.CSS_SELECTOR, "span[itemprop='addressLocality']").text
            state = store.find_element(By.CSS_SELECTOR, "span[itemprop='addressRegion']").text
            zip_ = store.find_element(By.CSS_SELECTOR, "span[itemprop='postalCode']").text
            
            # Add the store information to the list as a dictionary
            store_data.append({
                "Title": title,
                "Address": address,
                "City": city,
                "State":state,
                "Zip": zip_
                })
        except Exception as e:
            # Handle and log any errors during extraction
            print(f"Error extracting store info: {e}")

# Function to handle pagination for each state's store listings
def handle_pagination(state_url):
    driver.get(state_url)
    time.sleep(5)
    
    while True:
        # Extract store information from the current page
        extract_store_info()
        
        try:
            # Locate the "Next" button for pagination
            next_button = driver.find_element(By.CSS_SELECTOR, "li[data-testid='pagination-next']")
            
            # Check if the "Next" button has a valid link
            next_link = next_button.find_element(By.TAG_NAME, "a")
            href = next_link.get_attribute("href")

            if href: 
                # Click the "Next" button and wait for the next page to load
                next_button.click()
                time.sleep(5)
            else:
                break
            
        except Exception as e:
            # Handle cases where there are no more pages or other errors
            print(f"No more pages or error: {e}")
            break

# Loop through all state URLs and scrape store data
for state_url in state_urls:
    print(f"Scraping stores from: {state_url}")
    handle_pagination(state_url)

# Create a DataFrame from the scraped data
store_df = pd.DataFrame(store_data)

# Save the DataFrame to a CSV file
store_df.to_csv('jersey_mikes_all_stores.csv', index=False, encoding='utf-8')

driver.quit()





