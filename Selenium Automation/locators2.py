from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome WebDriver
service_obj = Service("C:\\WebDrivers\\chromedriver.exe")  # Update with the correct path
driver = webdriver.Chrome(service=service_obj)

try:
    # 1️⃣ Open the login page
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.maximize_window()

    # 2️ Type username into Username field
    driver.find_element(By.NAME, "username").send_keys("student")

    # 3️ Type password into Password field
    driver.find_element(By.ID, "password").send_keys("Password123")

    # 4️ Click the Submit button
    driver.find_element(By.ID, "submit").click()

    # 5 Verify new page URL contains 'logged-in-successfully'
    WebDriverWait(driver, 10).until(EC.url_contains("logged-in-successfully"))
    current_url = driver.current_url
    assert "logged-in-successfully" in current_url, f"❌ Unexpected URL: {current_url}"
    print("✅ URL verification passed!")

    # 6️⃣ Verify page contains expected text ('Congratulations' or 'successfully logged in')
    success_message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, "h1"))  # Update if needed
    )
    success_message = success_message_element.text.strip()

    # Print actual success message for debugging
    print(f"🔍 Actual success_message: '{success_message}'")

finally:
    driver.quit()
