import json
import time
import logging
from datetime import datetime
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession
import os

class GoogleIndexingAPI:
    def __init__(self, service_account_file: str, urls_file: str, log_file: str = 'indexing.log'):
        self.service_account_file = service_account_file
        self.urls_file = urls_file
        
        
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format='[%(asctime)s] [%(levelname)s] %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        self.logger = logging.getLogger(__name__)
        
        
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def get_authenticated_session(self):
        try:
            credentials = service_account.Credentials.from_service_account_file(
                self.service_account_file,
                scopes=['https://www.googleapis.com/auth/indexing']
            )
            
            session = AuthorizedSession(credentials)
            self.logger.info(f"Successfully authenticated with service account")
            return session
            
        except Exception as e:
            self.logger.error(f"Authentication failed: {str(e)}")
            return None

    def submit_url(self, session, url: str):
        api_url = 'https://indexing.googleapis.com/v3/urlNotifications:publish'
        
        data = {
            'url': url,
            'type': 'URL_UPDATED'
        }
        
        try:
            self.logger.info(f"Submitting URL to index: {url}")
            response = session.post(api_url, json=data)
            
            if response.status_code == 200:
                response_data = response.json()
                if ('urlNotificationMetadata' in response_data and 
                    'url' in response_data['urlNotificationMetadata'] and 
                    response_data['urlNotificationMetadata']['url'] == url):
                    self.logger.info(f"Successfully submitted URL: {url}")
                    return True
                else:
                    self.logger.warning(f"URL mismatch in response for: {url}")
                    return False
            else:
                self.logger.error(f"Failed to submit URL {url}. Status code: {response.status_code}")
                self.logger.error(f"Response: {response.text}")
                return False
                
        except Exception as e:
            self.logger.error(f"Error submitting URL {url}: {str(e)}")
            return False

    def process_urls(self):
        if not os.path.exists(self.urls_file):
            self.logger.error(f"URLs file not found: {self.urls_file}")
            return
            
        session = self.get_authenticated_session()
        if not session:
            return
            
        try:
            with open(self.urls_file, 'r') as f:
                urls = [line.strip() for line in f if line.strip()]
                
            self.logger.info(f"Found {len(urls)} URLs to process")
            
            successful_urls = []
            failed_urls = []
            
            for url in urls:
                if self.submit_url(session, url):
                    successful_urls.append(url)
                else:
                    failed_urls.append(url)
                time.sleep(1)  
            
            
            if failed_urls:
                failed_file = 'failed_urls.txt'
                with open(failed_file, 'w') as f:
                    for url in failed_urls:
                        f.write(f"{url}\n")
                self.logger.info(f"Failed URLs written to {failed_file}")
            
            self.logger.info(f"Processing complete. Success: {len(successful_urls)}, Failed: {len(failed_urls)}")
            
        except Exception as e:
            self.logger.error(f"Error processing URLs: {str(e)}")

if __name__ == "__main__":
    # Configuration
    SERVICE_ACCOUNT_FILE = "service-account.json"  # путь к файлу джсон
    URLS_FILE = "urls.txt"  # файл с урлами страним
    LOG_FILE = "indexing.log"  # лог файл
    
    indexer = GoogleIndexingAPI(SERVICE_ACCOUNT_FILE, URLS_FILE, LOG_FILE)
    indexer.process_urls()