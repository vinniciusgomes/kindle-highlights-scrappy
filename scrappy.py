from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import re
import uuid
import os

# Function to set up and access the Amazon Notebook page
def setup_webdriver():
    # Set up Chrome WebDriver. Selenium Manager will automatically download ChromeDriver.
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # Remove this line to see the browser opening
    driver = webdriver.Chrome(options=options)

    # Access the Amazon Notebook website
    driver.get("https://read.amazon.com/notebook")

    # Give time for the user to log in manually
    print("Please log in to your Amazon account.")
    input("Press Enter after logging in...")

    return driver

# Function to extract highlights from a book after the user clicks on it
def extract_highlights_from_html_content(driver):
    # Reload the current page HTML to ensure we're reading updated content
    page_source = driver.page_source

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # List to store the highlights
    highlights_data = []

    # Find all divs that have the structure we want
    highlight_blocks = soup.find_all('div', class_='a-row a-spacing-base')

    for block in highlight_blocks:
        # Search for the correct header with page/location information
        highlight_header = block.find(id="annotationHighlightHeader")
        if highlight_header:
            highlight_header_text = highlight_header.get_text(strip=True)
            location_match = re.search(r'Local:\s*([\d,]+)', highlight_header_text)
            page_match = re.search(r'Página:\s*([\d,]+)', highlight_header_text)

            if location_match:
                header_type = 'location'
                header_value = location_match.group(1).replace(',', '')
            elif page_match:
                header_type = 'page'
                header_value = page_match.group(1).replace(',', '')
            else:
                continue
        else:
            continue

        # Search for the highlight content
        highlight = block.find(id="highlight")
        if highlight:
            highlight_text = highlight.get_text(strip=True)
        else:
            continue

        highlight_id = str(uuid.uuid4())

        highlights_data.append({
            "id": highlight_id,
            header_type: header_value,
            "content": highlight_text
        })

    return highlights_data

# Function to collect manual information and generate the JSON file
def collect_manual_info_and_generate_json(highlights):
    # Request user to enter book data manually
    title = input("Enter the book title: ")
    author = input("Enter the book author: ")
    cover = input("Enter the book cover URL: ")
    description = input("Enter the book description: ")

    # Generate a UUID for the book
    book_id = str(uuid.uuid4())

    # Build the dictionary with book information and its highlights
    book_data = {
        "id": book_id,
        "book": {
            "name": title,
            "author": author,
            "cover": cover,
            "description": description
        },
        "highlights": highlights
    }

    # Save the data to a JSON file with the book name
    save_book_data_as_json(title, book_data)

# Function to save the JSON with the book name
def save_book_data_as_json(book_title, book_data):
    # Create the /exported folder if it doesn't exist
    os.makedirs('exported', exist_ok=True)

    # Remove characters not allowed in file names and convert to lowercase
    safe_title = re.sub(r'[^\w\s-]', '', book_title).strip().replace(' ', '_').lower()
    file_name = f"exported/{safe_title}.json"

    # Save the JSON to the file
    with open(file_name, 'w', encoding='utf-8') as json_file:
        json.dump(book_data, json_file, indent=2, ensure_ascii=False)

    print(f"JSON for the book '{book_title}' generated successfully! File: {file_name}")

def main():
    # Set up the browser and log in
    driver = setup_webdriver()

    # Leave the browser open for you to click on books
    print("Click on the book you want to export highlights from and press Enter to continue...")
    
    while True:
        input("Press Enter after selecting a book...")
        highlights = extract_highlights_from_html_content(driver)
        collect_manual_info_and_generate_json(highlights)
        
        choice = input("Do you want to export another book? (Y/n): ").strip().lower()
        # Set 'y' as default if the input is empty
        if choice == '':
            choice = 'y'
        
        if choice != 'y':
            break

if __name__ == "__main__":
    main()
