from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Define the path to ChromeDriver and proxy details
chrome_driver_path = "path/to/chromedriver.exe"  # Replace with the actual path to your ChromeDriver
proxy = "http://your_proxy_ip:port"  # Example: "http://123.45.67.89:8080"

# Configure ChromeOptions to use the proxy
options = Options()
options.add_argument(f"--proxy-server={proxy}")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")  # Mimic a real user

# Initialize ChromeDriver with the specified path and options
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# Define your query and target URL
query = "Laptop"
url = f'https://www.amazon.in/s?k={query}'

# Open the URL using ChromeDriver
driver.get(url)

# Locate elements by class name
elements = driver.find_elements(By.CLASS_NAME, "puis-card-container")

# Print the text of each element found
if elements:
    print(f"Number of elements found: {len(elements)}")
    for elem in elements:
        print(elem.text)
else:
    print("No elements found!")

# Allow some time before closing the browser
time.sleep(2)
driver.quit()
