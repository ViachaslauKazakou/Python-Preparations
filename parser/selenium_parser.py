from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def fetch_data(url):
    chrome_service = Service("/Users/Viachaslau_Kazakou/Work/Python-Preparations/parser/chromedriver-mac-x64/chromedriver")  # Update this path
    driver = webdriver.Chrome(service=chrome_service)
    driver.get(url)

    try:
        # Wait until the iframe is present
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "iframe"))
        )

        # Switch to the iframe
        iframe = driver.find_element(By.TAG_NAME, "iframe")
        driver.switch_to.frame(iframe)

        # Wait until the element with class 'outcomes-desktop-player' is present within the iframe
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "outcomes-desktop-player"))
        )

        # Get the page source after the JavaScript has rendered the content
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')

        # Adjust the selector based on the actual HTML structure
        player_name_element = soup.select_one('.outcomes-desktop-player')
        if player_name_element:
            player_name = player_name_element.text.strip()
            print(f"Player name: {player_name}")
        else:
            print("Player name element not found")
    except Exception as e:
        print(f"Error fetching player name: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    url = "https://pari.ru/quick-games/nard"
    fetch_data(url)