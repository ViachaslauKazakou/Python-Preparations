import httpx
from selenium import webdriver
from bs4 import BeautifulSoup
import asyncio

async def get_player_name(url: str) -> str:
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Adjust selector based on actual HTML structure
            player_element = soup.find_all('body div.outcomes-desktop-player')  
            print(player_element)
            name = soup.find_all('body')
            print(name)
            if player_element:
                return player_element.text.strip()
            return "Player name not found"
            
    except httpx.RequestError as e:
        return f"Request error: {e}"
    except Exception as e:
        return f"Error: {e}"

async def main():
    url = "https://pari.ru/quick-games/nard"
    player_name = await get_player_name(url)
    print(f"Player name: {player_name}")

if __name__ == "__main__":
    asyncio.run(main())