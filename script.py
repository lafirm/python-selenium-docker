from selenium import webdriver
from datetime import datetime
import pytz


def app() -> None:
    chrome_options = webdriver.chrome.options.Options()
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Remote(command_executor='http://chrome:4444/wd/hub', options=chrome_options)
    print('Driver Initiated!')
    driver.get('https://www.google.com')
    ist_tz = pytz.timezone('Asia/Kolkata')
    print(f'Current Time: {datetime.now(tz=ist_tz).strftime("%d-%B-%Y %H:%S %Z")}')
    print(f'Current URL: {driver.current_url}')
    driver.close()
    driver.quit()
    return None

if __name__ == '__main__':
    app()
