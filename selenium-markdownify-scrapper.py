# %% Fucking imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import markdownify
from time import sleep
import os

# %% Setting up ChromeDriver

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=webdriver.chrome.service.Service(ChromeDriverManager().install()))


# %%

# Function to convert HTML to Markdown
def convert_html_to_markdown(html, title):
    md = markdownify.markdownify(html, heading_style="ATX")
    return f"# {title}\n\n" + md

# Function to expand all buttons and scrape content
def expand_and_scrape(url):
    driver.get(url)
    sleep(10)  # Wait for initial page load

    try:
        # Expanding all elements recursively
        while True:
            expandable_elements = driver.find_elements(By.CSS_SELECTOR, "div.pseudoSelection div[role='button']")
            if not expandable_elements:
                print("No expandable elements found. Exiting loop.")
                break  # Exit loop if no more expandable elements are found

            expanded = False
            for element in expandable_elements:
                aria_expanded = element.get_attribute("aria-expanded")
                if aria_expanded == 'false':
                    try:
                        driver.execute_script("arguments[0].click();", element)
                        sleep(0.5)  # Small delay to ensure DOM updates
                        print("Clicked an expandable element.")
                        expanded = True
                    except Exception as e:
                        print(f"Error clicking button: {e}")
                else:
                    print("Element already expanded, skipping.")

            if not expanded:
                print("No new elements expanded. Exiting loop.")
                break

        # Scraping content
        content = driver.page_source
        title = driver.title
        markdown_content = convert_html_to_markdown(content, title)

        # Save content to a markdown file
        filename = f"{title.replace('/', '-').replace(' ', '_')}.md"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(markdown_content)

        print(f"Scraped and saved content to {filename}")

    except TimeoutException as e:
        print(f"Timeout while processing {url}: {e}")

    finally:
        driver.quit()

# Notion public URL
notion_urls = [
    "https://crustdata.notion.site/Crustdata-Discovery-And-Enrichment-API-c66d5236e8ea40df8af114f6d447ab48"
    "https://crustdata.notion.site/Crustdata-Data-Dictionary-c265aa415fda41cb871090cbf7275922",
    "https://crustdata.notion.site/Crustdata-Dataset-API-Detailed-Examples-b83bd0f1ec09452bb0c2cac811bba88c",
    
]

for index, notion_url in enumerate(notion_urls):
    print(f"Processing {index + 1}/{len(notion_urls)}: {notion_url}")
    expand_and_scrape(notion_url)
    print(f"Finished processing {index + 1}/{len(notion_urls)}")



